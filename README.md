# test_grpc project

* GetMeterDataChart - this is directory for Helm Chart
* docker - this is directiry with 2 docker files: webserver and gRPC server
* grpc - These are the sources that perform the main functionality of the project.
* kubernetes - this is directory with YAML files for kubernetes
* meter_data - here is the csv file for the gRPC server
* proto - here is protocol description file

# Pure docker scripts:

* 1_create_grpc_interface.sh - this script generate python classes from gRPC proto description
* 2_make_pure_dockerS.sh - generate 2 docker images (webserver and gRPC server) from 2 docker files
* 3_start_grpc_pure_docker.sh - run gRPC server process in pure docker
* 4_start_web_pure_docker.sh - run web server process in pure docker
* 5_STOP_grpc_pure_docker.sh - stop gRPC server. now there are some problems in it - it doesn’t exit by CTRL+C.

# Kubernetes script(not need to run Pure docker scripts)

* 6_kubernetes.sh - start kubernetes from ./kubernetes/*.YAML
* 7_kubernetes_stop.sh - stop all kubernetes from privious step

# Additional scripts

* docker_clean.sh - clear all docker images
* helm_clear.sh - clear all helm
* push_docker.sh - upload docker inages to Docker Hub
* start_minikube.sh - start kubernetes|minicube (don't forget that ingress addons is default off)
