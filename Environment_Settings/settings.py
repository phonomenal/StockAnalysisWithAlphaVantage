import os
import dotenv
from dotenv import load_dotenv
load_dotenv(override=True)


API_KEY = os.getenv("API_KEY")

DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")
