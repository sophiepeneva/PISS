import grpc
import Dyonysus.grpc.messages.Bus_pb2 as Bus_pb2
import Dyonysus.grpc.messages.Bus_pb2_grpc as Bus_pb2_grpc
from datetime import datetime
from influxdb import client as influxdb

class BusClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = Bus_pb2_grpc.ApolloStub(self.channel)

    def get_url(self, bus):
        """
        Client function to call the rpc for GetBusDetails
        """
        request = Bus_pb2.BusDetailsRequest(id=bus['number'], number=bus['number'])
        return self.stub.GetBusDetails(request)

client = BusClient()

influx = influxdb.InfluxDBClient("localhost", 8086, "root", "root", "wadus")

def get_bus_info_from_apollo(id, number):
    bus = {
        'id' : id,
        'number' : number
    }
    result = client.get_url(bus=bus)
    return result


if __name__ == '__main__':
    
    bus = {
        'id' : 1,
        'number' : 280
    }
    result = client.get_url(bus=bus)
    print(result.people_capacity)

    json_body = [
        {
            "measurement": "bus_data",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "fields": {
                "number": result.number,
                "id": result.id,
                "people_capacity": result.people_capacity,
                "average_people_count": result.average_people_count
            }
        }
    ]

    influx.write_points(json_body)