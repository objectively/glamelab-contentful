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

def update_open_data_volume(entry_id, count):
    # get entry 
    entry = client.entries(SPACE_ID, CONTENTFUL_ENV).find(entry_id)
    # update the Entry:
    entry.open_data_volume = str(count) #field is a string
    # save the entry 
    entry.save()
    # publish entry 
    # entry.publish()

# update_open_data_volume('6jH9t5XT78xKj1A8xalHNS', 0)