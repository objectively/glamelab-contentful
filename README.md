
Using the Contentful Management API to update GLAM-E-LAB data platforms

https://www.contentful.com/developers/docs/references/content-management-api


This repo uses a virtual environment using pip and venv: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/. It contains a csv of all the GLAM-E-LAB survey data platforms' necessary fields and an example script to update an entry's open data volume. The environment variables are stored in a `.env` file that is loaded with `python-dotenv`.

- create a virtual environment
  `python3 -m venv .venv`

- activate the virtual environment
  `source .venv/bin/activate`

- deactivate the virtual environment
  `deactivate`

- set your ENV variables
  - rename `.env.example` to `.env`
  - you can find the space id, delivery token, and management token in Contentful. I added an `api-test` environment so you can play around with the api, but when you are ready to make updates, change the environment to `master`

- Install 2 packages: 
  `python3 -m pip install python-dotenv contentful_management`

- run the script to update a data platform. Use the `entry_id` found in 'data/survey_data_platforms.csv' and replace it in the script.
  `python3 scripts/update_platform.py`

- you can also update multiple data platforms using a CSV and 'scripts/csv_update_platform.py` and the sample csv in 'data/sample_update'
