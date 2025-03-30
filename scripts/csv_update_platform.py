import csv
from update_platform import update_open_data_volume

with open('./data/sample_update.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        update_open_data_volume(row["entry_id"], row["open_data_volume"])