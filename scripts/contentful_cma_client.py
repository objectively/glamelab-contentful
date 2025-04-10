# https://www.contentful.com/developers/docs/references/content-management-api/

import os
from dotenv import load_dotenv #python-dotenv
import contentful_management

load_dotenv("./.env")

MANAGEMENT_API_TOKEN = os.getenv("GLAMELAB_MANAGEMENT_TOKEN")
CONTENTFUL_ENV = os.getenv("CONTENTFUL_ENV") #'api-test' or 'master'
SPACE_ID = os.getenv("SPACE_ID")

# create contentful client 
client = contentful_management.Client(MANAGEMENT_API_TOKEN)