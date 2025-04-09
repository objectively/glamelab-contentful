from contentful_cda_client import client
import csv

allowed_institution_fields = 'sys.id,fields.institutionName, fields.institutionDescription'


def get_institution_entries(entries=[], limit=100, skip=0, select=allowed_institution_fields):
    response = client.entries({'content_type': 'surveyInstitution', 'limit': limit, "skip": skip, "select": select})
    entries.extend(response.items)
    print(f'{response.skip} entries')
    if len(response.items) >= 100:
        return get_institution_entries(entries, limit = 100, skip = skip +  100)
    else:
        return entries

all_entries = get_institution_entries()

with open('./data/institutions.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'institution_name', 'institution_description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in all_entries:
        writer.writerow({"id":getattr(entry, 'id'), "institution_name": getattr(entry, 'institution_name'), "institution_description": getattr(entry, 'institution_description','')})
    
    