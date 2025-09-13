import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import convert_to_messages
from langchain.chat_models import init_chat_model
from langchain_community.utilities import SQLDatabase

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

db = SQLDatabase.from_uri("sqlite:///database.sqlite")

print(f"Dialect: {db.dialect}")
print(f"Available tables: {db.get_usable_table_names()}")
print(f'Sample output: {db.run("SELECT * FROM Artist LIMIT 5;")}')

# llm = init_chat_model("openai:gpt-4.1")