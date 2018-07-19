FROM python:3 

WORKDIR /root

RUN python -m pip install --upgrade pip
RUN python -m pip install grpcio protobuf 

EXPOSE 50051 

COPY . /root/
CMD ["python", "server.py"]
