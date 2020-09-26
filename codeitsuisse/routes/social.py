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
    ans = []
    for x in cases:
        y = calpos(cases[x]["seats"],cases[x]["people"],cases[x]["spaces"])
        ans.append(y)
    logging.info("My result :{}".format(data))
    return jsonify(ans);

def calpos(seat,ppl,space):
    return 1