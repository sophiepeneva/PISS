from time import sleep
from json import dumps
from kafka import KafkaConsumer


def do_smth_with_the_message(message):
    print(message)


def main():
    consumer = KafkaConsumer(
        'quickstart-events',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: x.decode('utf-8'))
    
    for message in consumer:
        do_smth_with_the_message(message.value)


if __name__ == "__main__":
    main()