docker rm grpc_server1
docker run --name grpc_server1 -v $(pwd)/meter_data:/data mkud/grpc_grpctest:latest