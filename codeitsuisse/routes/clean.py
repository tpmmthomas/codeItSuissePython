import logging
import json
import random
import operator as op
from functools import reduce


from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/supermarket', methods=['POST'])
def evaluateClean():
    data = request.get_json();
    result={}
    logging.info("data sent for evaluation {}".format(data))
    i =  0
    for case in data["tests"]:
        maze = data["tests"][case]["maze"]
        start = data["tests"][case]["start"]
        end = data["tests"][case]["end"]
        st=solveMaze(maze,start,end)
        result[case]= st
        i = i + 1
    fr = { "answers": result }
    logging.info("My result :{}".format(fr))
    return json.dumps(fr);

  

  
