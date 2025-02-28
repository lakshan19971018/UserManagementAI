from groq import Groq
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import pandas as pd
from pandasai import SmartDataframe
from langchain_groq import ChatGroq
import os

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
GROQ_API =  os.getenv("GORQ_API")


client = Groq(api_key=GROQ_API)
engine = create_engine(DB_URL)
# Category mapping matching the frontend
CATEGORY_MAP = {
    "Present": 1,
    "Leave": 2,
    "Transor": 3,
    "VOP": 4
}

# Reverse mapping for displaying category names in the response
CATEGORY_MAP_REVERSE = {v: k for k, v in CATEGORY_MAP.items()}

def load_database():
    query = "SELECT * FROM users"  # Replace with your actual table name
    with engine.connect() as connection:
        df = pd.read_sql(text(query), con=connection)
    return df.to_dict(orient='records')

def modify_question(question: str):
    """Replace category names in the question with their corresponding category IDs."""
    question_lower = question.lower()
    for category_name, category_id in CATEGORY_MAP.items():
        if category_name.lower() in question_lower:
            question = question.replace(category_name, str(category_id))
            question = question.replace(category_name.lower(), str(category_id))
    return question

def querring(df, question: str):
    try:
        # Modify the question to use category IDs
        modified_question = modify_question(question)

        llm = ChatGroq(
            groq_api_key=GROQ_API, model_name="llama3-70b-8192", temperature=0.1
        )
        pandas_ai = SmartDataframe(df, config={"llm": llm})
        result = pandas_ai.chat(modified_question)

        # Ensure the result is always a dictionary with 'type' and 'value'
        if isinstance(result, pd.DataFrame):
            if "category_id" in result.columns:
                # Add a category_name column for readability
                result["category_name"] = result["category_id"].map(CATEGORY_MAP_REVERSE)
            if result.empty:
                # Return an empty DataFrame with the same columns
                return {"type": "dataframe", "value": pd.DataFrame(columns=result.columns).to_dict(orient="records")}
            return {"type": "dataframe", "value": result.to_dict(orient="records")}
        elif isinstance(result, str):
            return {"type": "string", "value": result}
        else:
            # Handle unexpected result types
            return {"type": "string", "value": str(result)}

    except Exception as e:
        # Fallback for PandasAI errors
        if "InvalidOutputValueMismatch" in str(e):
            df_input = pd.DataFrame(df)
            # Manual filtering based on category names in the question
            category_ids = []
            question_lower = question.lower()
            for category_name, category_id in CATEGORY_MAP.items():
                if category_name.lower() in question_lower:
                    category_ids.append(category_id)
            
            if category_ids:
                result_df = df_input[df_input['category_id'].isin(category_ids)]
            else:
                result_df = df_input  # Default to all users if no specific category is matched

            if not result_df.empty:
                if "category_id" in result_df.columns:
                    result_df["category_name"] = result_df["category_id"].map(CATEGORY_MAP_REVERSE)
                return {"type": "dataframe", "value": result_df.to_dict(orient="records")}
            else:
                return {"type": "dataframe", "value": pd.DataFrame(columns=df_input.columns).to_dict(orient="records")}
        return {"type": "error", "value": f"Error: {str(e)}"}

def asking_question(question: str):
    data_json = load_database()
    return querring(data_json, question)

