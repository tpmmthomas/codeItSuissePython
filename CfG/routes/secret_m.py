import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/sort', methods=['POST'])
def evaluateSfghrt():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for x in data :
        result.append(encrypt(x["n"],x["text"]))
    logging.info("My result :{}".format(data))
    return jsonify(result);


def encrypt(n, text):
    processed = ""
    