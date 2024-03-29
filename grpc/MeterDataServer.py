'''
Created on 15 окт. 2019 г.

@author: maxx
'''

from concurrent import futures
import logging

import grpc

import GetMeterData_pb2
import GetMeterData_pb2_grpc
import csv
import os
from time import sleep
port_external = os.environ['PORT_GRPC'] #50002
csv_path = os.environ['CSV_PATH'] #'/data/meterusage.csv'

class GetMeterData(GetMeterData_pb2_grpc.GetMeterDataServicer):

    def GetData(self, request, context):
        ret = GetMeterData_pb2.MeterDataResponse()
        with open(csv_path) as csvfile:
            datareader = csv.reader(csvfile, delimiter=',')
            next(datareader)
            for row in datareader:
                if request.fromDateTime <= int(row[4]) <= request.toDateTime:
                    cur = ret.items.add()
                    cur.actEnIN = float(row[0])
                    cur.reactEnIN = float(row[1])
                    cur.actEnOUT = float(row[2])
                    cur.reactEnOUT = float(row[3])
                    cur.datetime = int(row[4])
        return ret

import signal
import sys
server = None
need_exit = False

def sigterm_handler(_signo, _stack_frame):
    if server is not None:
        server.stop(0)
    global need_exit
    need_exit = True

signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigterm_handler)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GetMeterData_pb2_grpc.add_GetMeterDataServicer_to_server(GetMeterData(), server)
    server.add_insecure_port('0.0.0.0:' + port_external)
    server.start()
    print('0.0.0.0:' + port_external)
    #server.wait_for_termination() #experimental IP
    try:
        while not need_exit:
            sleep(1)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    logging.basicConfig()
    serve()
