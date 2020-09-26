import logging
import json
import random

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/intelligent-farming', methods=['POST'])
def evaluateFarming():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
   # for seq in data["list"]:
    #    seq["geneSequence"] = sortdri(seq["geneSequence"])
    logging.info("My result :{}".format(data))
    return json.dumps(data);

def sortdri(seq):
    result = ""
    a=0
    c=0
    g=0
    t=0
    for ch in seq:
        if ch == "A":
            a = a + 1
        elif ch == "C":
            c = c + 1
        elif ch == "G":
            g = g + 1 
        else:
            t = t + 1
    while a>0 and c>0 and g>0 and t>0 :
        result = result + "ACGT"
        a = a - 1 
        c=c-1
        g=g-1
        t=t-1
    if c % 2 == 1 and len(result)>=4 :
        result = result[:-4]
        a=a+1
        c=c+1
        g=g+1
        t=t+1 
    while c >= 2 :
        c = c - 2
        result = result + "CC"
    while a+c+g+t>0:
        if a > 1:
            a=a-1
            result = result + "A"
        if a > 1:
            a=a-1
            result = result + "A"
        if c > 1:
            c=c-1
            result = result + "C"
        elif g > 1:
            g = g-1
            result = result + "G"
        elif t > 1:
            t = t-1
            result = result + "T"
    return result
