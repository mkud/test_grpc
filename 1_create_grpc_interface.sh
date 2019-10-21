docker run -v "$PWD":/tapp -it grpc/python:1.4 /bin/bash -c "python3 -m grpc_tools.protoc --python_out=/tapp/grpc --grpc_python_out=/tapp/grpc /tapp/proto/GetMeterData.proto -I/tapp/proto"
