import csv
import json
import os

import django
from django.contrib.auth.hashers import make_password

from Homework_31_PD12.settings import BASE_DIR

# ----------------------------------------------------------------------------------------------------------------------
# Setup env settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Homework_30_PD12.settings')
django.setup()


# ----------------------------------------------------------------------------------------------------------------------
# Convert csv file to json file
def csv_2_json(csv_file, json_file, model):
    """
    Convert csv file to json file
    """
    data_list: list = []

    with open(csv_file, encoding="utf-8") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            if "location_id" in row:
                row["locations"] = [int(row["location_id"])]
                del row["location_id"]
            if row.get("is_published") is not None:
                if row["is_published"] == "TRUE":
                    row["is_published"] = True
                else:
                    row["is_published"] = False
            if "password" in row:
                row["password"] = make_password(row["password"])

            data_dict: dict = {"model": model, "pk": row["id"], "fields": row}
            data_list.append(data_dict)
    with open(json_file, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(data_list, indent=4, ensure_ascii=False))


# ----------------------------------------------------------------
# call function to convert datasets to fixtures
csv_2_json(os.path.join(BASE_DIR, "data", "raw_data", "location.csv"), os.path.join(BASE_DIR, "data", "location.json"),
           "locations.location")
csv_2_json(os.path.join(BASE_DIR, "data", "raw_data", "user.csv"), os.path.join(BASE_DIR, "data", "user.json"),
           "authentication.user")
csv_2_json(os.path.join(BASE_DIR, "data", "raw_data", "ad.csv"), os.path.join(BASE_DIR, "data", "ad.json"),
           "ads.advertisement")
csv_2_json(os.path.join(BASE_DIR, "data", "raw_data", "category.csv"), os.path.join(BASE_DIR, "data", "category.json"),
           "ads.category")
