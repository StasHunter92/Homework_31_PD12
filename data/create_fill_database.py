import os
import time

from Homework_31_PD12.settings import BASE_DIR

# ----------------------------------------------------------------------------------------------------------------------
# Create and run container
os.system("docker run --name homework_31_postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres")

time.sleep(3)

# ----------------------------------------------------------------------------------------------------------------------
# Migrate database
os.system(f"cd {BASE_DIR} && python manage.py makemigrations authentication")
time.sleep(1)
os.system(f"cd {BASE_DIR} && python manage.py makemigrations locations")
time.sleep(1)
os.system(f"cd {BASE_DIR} && python manage.py makemigrations ads")
time.sleep(1)
os.system(f"cd {BASE_DIR} && python manage.py makemigrations selections")
time.sleep(1)
os.system(f"cd {BASE_DIR} && python manage.py migrate")

time.sleep(3)

# ----------------------------------------------------------------------------------------------------------------------
# Fill database
os.system(
    f"cd {BASE_DIR} "
    f"&& python manage.py loaddata data/category.json "
    f"&& python manage.py loaddata data/location.json "
    f"&& python manage.py loaddata data/user.json "
    f"&& python manage.py loaddata data/ad.json")

print("Finished")
