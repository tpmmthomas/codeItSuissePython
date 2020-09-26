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

    logging.info("My result :{}".format(result))
    return json.dumps(result);


