from contentful_cda_client import client
import csv

allowed_institution_data_platform_fields = 'sys.id,fields.institutionName, fields.institutionDescription, fields.dataPlatform'

def get_institution_data_platform_entries(entries=[], limit=100, skip=0, select=allowed_institution_data_platform_fields):
    response = client.entries({'content_type': 'surveyInstitution', 'limit': limit, "skip": skip, "select": select})
    
    for item in response.items:
        for data_platform in item.data_platform:
            entry = {
                "id": data_platform.id,
                "open_data_platform": data_platform.open_data_platform,
                "open_data_volume": data_platform.open_data_volume,
                "institution_id": item.id,
                "institution_name": item.institution_name
            }
            entries.append(entry)

    print(f'{response.skip} entries')
    if len(response.items) >= 100:
        return get_institution_data_platform_entries(entries, limit = 100, skip = skip +  100)
    else:
        return entries
    

all_entries = get_institution_data_platform_entries()

with open('./data/institution_data_platforms.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'open_data_platform', 'open_data_volume', 'institution_id', 'institution_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in all_entries: 
        writer.writerow(entry)
    
    