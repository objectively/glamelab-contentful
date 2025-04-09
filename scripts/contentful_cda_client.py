from contentful import Client
import os
from dotenv import load_dotenv

load_dotenv("./.env")
DELIVERY_API_TOKEN = os.getenv("GLAMELAB_DELIVERY_TOKEN")
CONTENTFUL_ENV = os.getenv("CONTENTFUL_ENV")
SPACE_ID = os.getenv("SPACE_ID")

client = Client(
  space_id= SPACE_ID,
  access_token=DELIVERY_API_TOKEN,
  environment=CONTENTFUL_ENV # Optional - it defaults to 'master'.
)