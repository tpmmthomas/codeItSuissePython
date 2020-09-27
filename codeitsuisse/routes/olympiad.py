import logging
import json
import random
import operator as op
from functools import reduce


from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/olympiad-of-babylon', methods=['POST'])
def evaluateOlym():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    numdays = data["numberOfDays"]
    numbooks = data["numberOfBooks"]
    books = data["books"]
    days = data["days"]
    orgbooks = len(books)
    days.sort(reverse=True)
    for day in days:
        if len(books) == 0:
            break
        num, re = dpPick(books,day)
        logging.info("num {}".format(num))
        logging.info("re {}".format(re))
        for book in re:
            books.remove(book)
    result = orgbooks - len(books)
    logging.info("My result :{}".format(result))
    return json.dumps({"optimalNumberOfBooks": result});

def dpPick(books, target):
    n = len(books)
    dp = [[0 for i in range(target+1)] for j in range(n+1)]
    result = [[ [] for i in range(target+1)] for j in range(n+1)]
    for i in range(0,target+1):
        dp[n][i]=i
    i = n-1
    while i >=0:
        j = target
        while j>=0:
            pick = 0
            if j+books[i]<=target:
                pick = dp[i+1][j+books[i]]
            leave = dp[i+1][j]
            dp[i][j] = max(pick,leave)
            if dp[i][j] == pick:
                result[i][j] = result[i+1][j+books[i]].copy()
                result[i][j].append(books[i])
            else:
                result[i][j] = result[i+1][j].copy()
            j = j - 1 
        i = i - 1
    return dp[0][0], result[0][0]
