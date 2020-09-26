import logging
import json
import random
import operator as op
from functools import reduce


from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/social_distancing', methods=['POST'])
def evaluateSOCIAL():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    cases = data["tests"]
    ans = {}
    for x in cases:
        y = calpos(cases[x]["seats"],cases[x]["people"],cases[x]["spaces"])
        ans[x] = y
    jsonans = {"answers": ans}
    logging.info("My result :{}".format(jsonans))
    return json.dumps(jsonans);


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  

def calpos(seat,ppl,space):
    numspace  = seat-ppl + 1
    total = ncr(numspace,ppl)
    i = 1
    while space > i:
        numspace = numspace - i + 1
        for j in range(1,ppl):
            total = total - ncr(numspace-j,ppl-j)
        i = i + 1
    return total
