'''
Created on 15 окт. 2019 г.

@author: maxx
'''

import ujson
import grpc
import os
port_external = os.environ['PORT_EXTERNAL'] #2777
port_GRPC = os.environ['PORT_GRPC'] #localhost
host_GRPC = os.environ['HOST_GRPC'] #50002

import GetMeterData_pb2
import GetMeterData_pb2_grpc

from flask import Flask, request
app = Flask(__name__, static_folder='')


@app.route("/")
def hello():
    return app.send_static_file("index.html")


@app.route("/get_data", methods=['GET', 'POST'])
def GetData():
    ret = []
    with grpc.insecure_channel(host_GRPC + ':' + port_GRPC) as channel:
        stub = GetMeterData_pb2_grpc.GetMeterDataStub(channel)
        response = stub.GetData(GetMeterData_pb2.DataRequest(fromDateTime=int(request.values.get("dtFrom", "0")), toDateTime=int(request.values.get("dtTo", "0"))))
        for item in response.items:
            ret.append({'actEnIN': item.actEnIN, 'reactEnIN': item.reactEnIN, 'actEnOUT': item.actEnOUT, 'reactEnOUT': item.actEnOUT, 'datetime': item.datetime})
    return app.response_class(
        response=ujson.dumps(ret),
        status=200,
        mimetype='application/json'
    )
        

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=port_external)
