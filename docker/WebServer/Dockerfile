FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV PORT_EXTERNAL=80 PORT_GRPC=50002 HOST_GRPC=grpc_server1

RUN pip install grpcio ujson protobuf

COPY GetMeterData_pb2.py GetMeterData_pb2_grpc.py main.py index.html /app/
