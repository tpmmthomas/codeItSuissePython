import logging
import json
import random
import operator as op
from functools import reduce


from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/clean_floor', methods=['POST'])
def evaluateClean():
    data = request.get_json();
    result={}
    logging.info("data sent for evaluation {}".format(data))
    for case in data["tests"]:
        step = clean(data["tests"][case]["floor"],0,0)
        result[case] = step
    fr = { "answers": result }
    logging.info("My result :{}".format(fr))
    return json.dumps(fr);

def checkleft(floor,pos): 
    for i in range (0,pos):
        if floor[i] > 0:
            return False
    return True

def checkright(floor,pos): 
    for i in range (pos+1,len(floor)):
        if floor[i] > 0:
            return False
    return True

def clean(floor, pos,steps):
    logging.info("Floor {}".format(floor))
    logging.info("Pos {}".format(pos))
    logging.info("Steps {}".format(steps))
    if steps!=0 or pos != 0 :
        if floor[pos]>0:
            floor[pos] = floor[pos]- 1  
        else:
            floor[pos] = 1
        steps = steps + 1
    left = checkleft(floor,pos)
    right = checkright(floor,pos)
    if left and right:
        if floor[pos]== 0:
            return steps
        else:
            if pos + 1 < len(floor):
                return clean(floor,pos+1,steps)
            else:
                return clean(floor,pos-1,steps)
    elif left:
        return clean(floor,pos+1,steps)
    elif right:
        return clean(floor,pos-1,steps)
    else:
        floor1 = floor
        floor2 = floor
        return min(clean(floor1,pos+1,steps),clean(floor2,pos-1,steps))
            
