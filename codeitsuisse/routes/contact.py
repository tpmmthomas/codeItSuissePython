import logging
import json
import random

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/contact_trace', methods=['POST'])
def evaluateContact():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result = 20000
    #weights = []
    #for x in data:
    #    y = random.randint(1,10)
    #    result = result + y*x[0]
    #    weights.append(y)
    #checking = weights
    #checking.append(result)
    #logging.info("My result :{}".format(checking))
    return json.dumps(result);


