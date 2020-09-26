import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluateSalad():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    numNeed = data["number_of_salads"]
    saladmap = data["salad_prices_street_map"]
    min_price = -1
    for street in saladmap:
        n = 0
        sumprice = 0 
        i = 0 
        for shop in street:
            if shop == "X":
                n = 0
                sumprice = 0
                i = i + 1
                continue
            else:
                n=n+1 
                sumprice= sumprice + int(shop)
            if n == numNeed:
                if  min_price == -1:
                    min_price = sumprice
                elif min_price > sumprice:
                    min_price = sumprice 
            if n > numNeed:
                sumprice = sumprice - int(street[i-numNeed])
                if min_price > sumprice:
                    min_price = sumprice
            i = i + 1
    if min_price == -1:
        min_price = 0
    logging.info("My result :{}".format(min_price))
    return json.dumps(min_price);


