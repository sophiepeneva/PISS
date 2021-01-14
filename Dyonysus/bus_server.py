import grpc
from concurrent import futures
import time
import Dyonysus.grpc.messages.Bus_pb2 as Bus_pb2
import Dyonysus.grpc.messages.Bus_pb2_grpc as Bus_pb2_grpc
import random

class BusService(Bus_pb2_grpc.DyonysusServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        id = request.id
        number = request.number
        print('Received number')
        print(number)
        bus = {
            'id' : id,
            'number' : random.randint(0, 300),
            'people_capacity' : random.randint(0, 300),
            'average_people_count' : random.randint(0, 300)
        }
        return Bus_pb2.BusResponse(**bus)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Bus_pb2_grpc.add_DyonysusServicer_to_server(BusService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()