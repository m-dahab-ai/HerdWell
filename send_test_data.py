from influxdb_client import InfluxDBClient, Point, WritePrecision
from datetime import datetime
from config import URL, TOKEN, ORG, BUCKET, ANIMAL_IDS
import random
import time

client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)
write_api = client.write_api()

def generate_test_data(animal_id):
    temperature = round(random.uniform(37.0, 39.0), 1)
    humidity = round(random.uniform(40.0, 60.0), 1)
    water_level = round(random.uniform(50.0, 100.0), 1)
    timestamp = datetime.utcnow()
    point = (
        Point("animal_data")
        .tag("animal_id", animal_id)
        .field("temperature", temperature)
        .field("humidity", humidity)
        .field("water_level", water_level)
        .time(timestamp, WritePrecision.NS)
    )
    return point

for animal_id in ANIMAL_IDS:
    point = generate_test_data(animal_id)
    write_api.write(bucket=BUCKET, org=ORG, record=point)
    print(f"تم إرسال البيانات للحيوان {animal_id} في {datetime.utcnow()}")

write_api.flush()
client.close()
print("تم إرسال جميع البيانات بنجاح!")
