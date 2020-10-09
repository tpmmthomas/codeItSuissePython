import logging
import json

from flask import request, jsonify;

from CfG import app;

logger = logging.getLogger(__name__)

@app.route('/sort', methods=['POST'])
def evaluateSort():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    data.sort()
    logging.info("My result :{}".format(data))
    return jsonify(data);


def qsort(inlist): 
    if inlist == []:  
        return [] 
    else: 
        pivot = inlist[0] 
        lesser = qsort([x for x in inlist[1:] if x < pivot]) 
        greater = qsort([x for x in inlist[1:] if x >= pivot]) 
        return lesser + [pivot] + greater 
