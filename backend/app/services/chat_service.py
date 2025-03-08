from groq import Groq
from dotenv import load_dotenv
import pandas as pd
from pandasai import SmartDataframe
from langchain_groq import ChatGroq
import os
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
GROQ_API = os.getenv("GORQ_API")

client = Groq(api_key=GROQ_API)

CATEGORY_MAP = {"Present": "1", "Leave": "2", "Transor": "3", "VOP": "4"}
CATEGORY_MAP_REVERSE = {v: k for k, v in CATEGORY_MAP.items()}

async def load_database():
    mongo_client = AsyncIOMotorClient(DB_URL)
    db = mongo_client["users"]
    try:
        users = await db["users"].find().to_list(length=None)
        for user in users:
            user["_id"] = str(user["_id"])
            if "category_id" in user:
                user["category_id"] = str(user["category_id"])
        return users
    finally:
        mongo_client.close()

def modify_question(question: str):
    question_lower = question.lower()
    for category_name, category_id in CATEGORY_MAP.items():
        if category_name.lower() in question_lower:
            question = question.replace(category_name, str(category_id))
            question = question.replace(category_name.lower(), str(category_id))
    return question

async def querring(data_json, question: str):
    try:
        modified_question = modify_question(question)
        df = pd.DataFrame(data_json)
        llm = ChatGroq(groq_api_key=GROQ_API, model_name="llama3-70b-8192", temperature=0.1)
        pandas_ai = SmartDataframe(df, config={"llm": llm})
        result = pandas_ai.chat(modified_question)

        if isinstance(result, pd.DataFrame):
            if "category_id" in result.columns:
                result["category_name"] = result["category_id"].map(CATEGORY_MAP_REVERSE)
            if result.empty:
                return {"type": "dataframe", "value": pd.DataFrame(columns=result.columns).to_dict(orient="records")}
            return {"type": "dataframe", "value": result.to_dict(orient="records")}
        elif isinstance(result, str):
            return {"type": "string", "value": result}
        else:
            return {"type": "string", "value": str(result)}
    except Exception as e:
        return {"type": "error", "value": f"Error: {str(e)}"}

async def asking_question(question: str):
    data_json = await load_database()
    return await querring(data_json, question)