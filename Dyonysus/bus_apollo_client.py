import grpc
import Dyonysus.grpc.messages.Bus_pb2 as Bus_pb2
import Dyonysus.grpc.messages.Bus_pb2_grpc as Bus_pb2_grpc
from datetime import datetime
from influxdb import client


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
        self.stub = Bus_pb2_grpc.DyonysusStub(self.channel)

    def get_url(self, bus):
        """
        Client function to call the rpc for GetServerResponse
        """
        request = Bus_pb2.BusRequest(id=bus['number'], number=bus['number'])
        return self.stub.GetServerResponse(request)


if __name__ == '__main__':
    client = BusClient()
    bus = {
        'id' : 1,
        'number' : 280
    }
    result = client.get_url(bus=bus)
    print(result.people_capacity)
    
    influx = client.InfluxDBClient("localhost", 8086, "root", "root", "PISS_DB")
    
    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2009-11-10T23:00:00Z",
            "fields": {
                "value": 0.64
            }
        }
    ]

    influx.write_points(json_body)