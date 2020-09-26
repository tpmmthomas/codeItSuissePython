import logging
import json
import random

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/social_distancing', methods=['POST'])
def evaluateSOCIAL():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    cases = data["tests"]
    for x in cases:
        logging.info("My result :{}".format(x))
    logging.info("My result :{}".format(data))
    return jsonify(data);

