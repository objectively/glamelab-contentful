
from contentful_cma_client import client, SPACE_ID, CONTENTFUL_ENV


def update_open_data_volume(entry_id, count):
    # get entry 
    entry = client.entries(SPACE_ID, CONTENTFUL_ENV).find(entry_id)
    # update the Entry:
    entry.open_data_volume = str(count) #field is a string
    # save the entry 
    entry.save()
    # publish entry 
    # entry.publish()

# update_open_data_volume('6jH9t5XT78xKj1A8xalHNS', 2000000000)