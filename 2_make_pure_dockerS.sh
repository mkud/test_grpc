cp ./grpc/{GetMeterData_pb2.py,GetMeterData_pb2_grpc.py,MeterDataClient.py,index.html} ./docker/WebServer
mv ./docker/WebServer/MeterDataClient.py ./docker/WebServer/main.py
docker build -t mkud/web_grpctest:latest ./docker/WebServer
cp ./grpc/{GetMeterData_pb2.py,GetMeterData_pb2_grpc.py,MeterDataServer.py} ./docker/GRPCServer
docker build -t mkud/grpc_grpctest:latest ./docker/GRPCServer
