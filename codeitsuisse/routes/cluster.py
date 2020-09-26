import logging
import json
import random

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/cluster', methods=['POST'])
def evaluateCluster():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    rows = len(data)
    cols = len(data[0])
    i = 0
    j = 0
    arr = [["0"]*cols]*rows
    logging.info("Rows :{}".format(rows))
    logging.info("Cols :{}".format(cols))
    result = 0
    for i in range(0,rows):
        for j in range(0,cols):
            if data[i][j] == "1" and arr[i][j]=="0":
                clusterarr(arr,data,i,j,rows,cols)
                result = result + 1
    logging.info("My result :{}".format(result))
    return json.dumps({"answer": result});

def clusterarr(arr,data,i,j,rows,cols):
    logging.info("i :{}".format(i))
    logging.info("j :{}".format(j))
    arr[i][j]="1"
    if i+1<rows  and data[i+1][j]=="0" and arr[i+1][j] == "0":
        clusterarr(arr,data,i+1,j,rows,cols)
    if i+1<rows  and data[i+1][j]=="1" and arr[i+1][j] == "0":
        clusterarr(arr,data,i+1,j,rows,cols)
    if i-1>=0 and j-1>=0 and data[i-1][j-1]=="0" and arr[i-1][j-1] == "0":
        clusterarr(arr,data,i-1,j-1,rows,cols)
    if i-1>=0 and j-1>=0 and data[i-1][j-1]=="1" and arr[i-1][j-1] == "0":
        clusterarr(arr,data,i-1,j-1,rows,cols)
    if i-1>=0  and data[i-1][j]=="0" and arr[i-1][j] == "0":
        clusterarr(arr,data,i-1,j,rows,cols)
    if i-1>=0  and data[i-1][j]=="1" and arr[i-1][j] == "0":
        clusterarr(arr,data,i-1,j,rows,cols)
    if i-1>=0 and j+1<cols and data[i-1][j+1]=="0" and arr[i-1][j+1] == "0":
        clusterarr(arr,data,i-1,j+1,rows,cols)
    if i-1>=0 and j+1<cols and data[i-1][j+1]=="1" and arr[i-1][j+1] == "0":
        clusterarr(arr,data,i-1,j+1,rows,cols)
    if j-1>=0  and data[i][j-1]=="0" and arr[i][j-1] == "0":
        clusterarr(arr,data,i,j-1,rows,cols)
    if j-1>=0  and data[i][j-1]=="1" and arr[i][j-1] == "0":
        clusterarr(arr,data,i,j-1,rows,cols)
    if j+1<cols  and data[i][j+1]=="0" and arr[i][j+1] == "0":
        clusterarr(arr,data,i,j+1,rows,cols)
    if j+1<cols  and data[i][j+1]=="1" and arr[i][j+1] == "0":
        clusterarr(arr,data,i,j+1,rows,cols)
    if i+1<rows and j-1>=0 and data[i+1][j-1]=="0" and arr[i+1][j-1] == "0":
        clusterarr(arr,data,i+1,j-1,rows,cols)
    if i+1<rows and j-1>=0 and data[i+1][j-1]=="1" and arr[i+1][j-1] == "0":
        clusterarr(arr,data,i+1,j-1,rows,cols)
    if i+1<rows and j+1<cols and data[i+1][j+1]=="0" and arr[i+1][j+1] == "0":
        clusterarr(arr,data,i+1,j+1,rows,cols)
    if i+1<rows and j+1<cols and data[i+1][j+1]=="1" and arr[i+1][j+1] == "0":
        clusterarr(arr,data,i+1,j+1,rows,cols)
    


