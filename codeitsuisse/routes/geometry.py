import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/revisitgeometry', methods=['POST'])
def evaluateGeo():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    shape = data["shapeCoordinates"]
    xco=[]
    yco=[]
    for coor in shape:
        xco.append(coor["x"])
        yco.append(coor["y"])
    lineeq_shape = []
    i=0
    while i < len(shape):
        slope = 0
        yintercept = 0
        if yco[(i+1)%len(shape)] == yco[i%len(shape)] :
            slope = 0
            yintercept = yco[i%len(shape)]
        elif xco[(i+1)%len(shape)] == xco[i%len(shape)] :
            slope = -1
            yintercept = xco[i%len(shape)]
        else:
            slope = (yco[(i+1)%len(shape)]-yco[i%len(shape)])/(xco[(i+1)%len(shape)]-xco[i%len(shape)])
            yintercept = yco[i%len(shape)]-slope * xco[i%len(shape)]
        line_shape.append([slope,yintercept])
        i = i + 1
    line = data["linecoordinates"]
    if line[0]["y"] == line[1]["y"] :
        slope = 0
        yintercept = line[0]["y"]
    elif  line[0]["x"] == line[1]["x"] :
        slope = -1
        yintercept = line[0]["x"]
    else:
        slope = (line[1]["y"]-line[0]["y"] )/(line[1]["x"]-line[0]["x"])
        yintercept = line[0]["y"]-slope * line[0]["x"]
    lineeq_line = [slope,yintercept]
    i = 0
    result = []
    for lineeq in lineq_shape:
        if lineeq[0] == 0:
            if lineeq_line[0] == -1 :
                xintercept =lineeq_line[1]
                yintercept = lineeq[1]
            elif lineeq_line[0] == 0:
                continue
            else:
                xintercept = (lineeq[1]-lineeq_line[1] )/lineeq_line[0]
                yintercept = lineeq[1]
        elif lineeq[0] == -1:
            if lineeq_line[0] == -1 :
                continue 
            elif lineeq_line[0] == 0:
                xintercept =lineeq[1]
                yintercept = lineeq_line[1]
            else:
                xintercept = lineeq[1]
                yintercept = lineeq_line[0]*lineeq[1]+lineeq_line[1]
        else:
            if lineeq_line[0] == -1 :
                xintercept = lineeq_line[1]
                yintercept = lineeq[0]*lineeq_line[1]+lineeq[1]
            elif lineeq_line[0] == 0:
                xintercept = (lineeq_line[1]-lineeq[1] )/lineeq[0]
                yintercept = lineeq_line[1]
            else:
                xintercept = (lineeq[1]-lineeq_line[1])/(lineeq_line[0]-lineeq[0])
                yintercept = lineeq_line[0]*xintercept+lineeq_line[1]
        if xintercept >= min(xco[i%len(shape)],xco[(i+1)%len(shape)]) and xintercept <= max(xco[i%len(shape)],xco[(i+1)%len(shape)]):
            if yintercept >= min(yco[i%len(shape)],yco[(i+1)%len(shape)]) and yintercept <= max(yco[i%len(shape)],yco[(i+1)%len(shape)]):
                result.append([xintercept,yintercept])
        i = i + 1
    output_json = []
    for c in result:
        output_json.append({"x": c[0], "y": c[1]})
    logging.info("My result :{}".format(putput_json))
    return json.dumps(output_json);


