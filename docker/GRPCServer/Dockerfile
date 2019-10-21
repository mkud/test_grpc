FROM grpc/python:1.4

ENV PORT_GRPC=50002 CSV_PATH=/data/meterusage.csv

COPY GetMeterData_pb2.py GetMeterData_pb2_grpc.py MeterDataServer.py /

VOLUME "/data"

ENTRYPOINT ["python3", "-u", "MeterDataServer.py"]

