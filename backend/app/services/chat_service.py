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


def load_database():
    query = "SELECT * FROM users"  # Replace with your actual table name
    with engine.connect() as connection:
        df = pd.read_sql(text(query), con=connection)
    # Convert DataFrame to string with no truncation
    return df.to_dict(orient='records')
    


# def querring(df,question: str) -> str:
#     try:
#             llm = ChatGroq(
#             groq_api_key=GROQ_API , model_name="llama3-70b-8192",
#             temperature=0.7)
#             pandas_ai = SmartDataframe(df, config={"llm": llm})
#             result = pandas_ai.chat(question)
#             print(result)
#             return result

#     except Exception as e:
#         return f"Error: {str(e)}"

# def querring(df, question: str) -> str:
#     try:
#         llm = ChatGroq(
#             groq_api_key=GROQ_API, model_name="llama3-70b-8192", temperature=0.7
#         )
#         pandas_ai = SmartDataframe(df, config={"llm": llm})
#         result = pandas_ai.chat(question)
#         print(result)
#         return result
#     except Exception as e:
#         return f"Error: {str(e)}"

def querring(df, question: str):
    try:
        llm = ChatGroq(
            groq_api_key=GROQ_API, model_name="llama3-70b-8192", temperature=0.7
        )
        pandas_ai = SmartDataframe(df, config={"llm": llm})
        result = pandas_ai.chat(question)

        # Check if the result is a DataFrame or a string
        if isinstance(result, pd.DataFrame):
            return {"type": "dataframe", "value": result.to_dict(orient="records")}  # Convert DataFrame to JSON

        return {"type": "string", "value": str(result)}  # Return a normal string

    except Exception as e:
        return {"type": "error", "value": str(e)}



def asking_question(question:str):
    
    data_json = load_database()
    user_question = f"{question}"
    return querring(data_json,user_question)

