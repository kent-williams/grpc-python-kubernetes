from __future__ import print_function
import grpc
import sys
import getid_pb2
import getid_pb2_grpc


def run(argv):
    creds = grpc.ssl_channel_credentials(open('tls.pem', 'rb').read())
    channel = grpc.secure_channel(str(argv[1]), creds)
    stub = getid_pb2_grpc.InformationStub(channel)
    response = stub.RequestID(getid_pb2.IDRequest())
    print(response.message)


if __name__ == '__main__':
  while True:
     run(sys.argv)
