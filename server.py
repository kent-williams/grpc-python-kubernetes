from concurrent import futures
import time
import grpc
import getid_pb2
import getid_pb2_grpc
import uuid

id = uuid.uuid4()

class Information(getid_pb2_grpc.InformationServicer):
    def RequestID(self, request, context):
        return getid_pb2.IDReply(message='ID: %s' % id)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    getid_pb2_grpc.add_InformationServicer_to_server(Information(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
