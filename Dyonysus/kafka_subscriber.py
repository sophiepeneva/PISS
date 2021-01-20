from time import sleep
from json import dumps
from kafka import KafkaConsumer
import json
from Dyonysus.bus_apollo_client import get_bus_info_from_apollo
from datetime import datetime
from influxdb import client as influxdb

influx = influxdb.InfluxDBClient("localhost", 8086, "root", "root", "wadus")

def send_bus_info_to_influx(message):
    parsed_message = json.loads(message)
    additional_info = get_bus_info_from_apollo(parsed_message['id'])

    json_body = [
        {
            "measurement": "bus_data",
            "time" : parsed_message['timestamp'],
            "tags": {
                "number": str(additional_info.number),
                "current_station_id": str(parsed_message['stationId'])
            },
            "fields": {
                "number": additional_info.number,
                "id": additional_info.id,
                "standing_people_capacity": additional_info.standing_people_capacity,
                "sitting_people_capacity": additional_info.sitting_people_capacity,
                "disabled_people_capacity": additional_info.disabled_people_capacity,
                "average_people_count": additional_info.average_people_count,
                "station_id":int(parsed_message['stationId']),
                "current_people_count":parsed_message['peopleCountCurrent'],
                "people_out":parsed_message['peopleGettingOffTheBus'],
                "people_in":parsed_message['peopleGettingOnTheBus'],
                "timestamp":parsed_message['timestamp']
            }
        }
    ]
    influx.write_points(json_body, time_precision='ms')
    print('Sending bus info to influx: ', dumps(json_body))

def main():
    consumer = KafkaConsumer(
        'quickstart-events',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: x.decode('utf-8'))
    
    data = []
    for message in consumer:
        send_bus_info_to_influx(message.value)


if __name__ == "__main__":
    main()
    