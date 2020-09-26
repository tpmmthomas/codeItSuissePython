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
    Clusters = data["cluster"]
    Infected = data["infected"]
    Origin = data["origin"]
    result = []
    current_path = [Infected["name"]]
    RecurPath(Infected,Clusters,Origin,current_path,result)
    logging.info("My result :{}".format(result))
    return json.dumps(result);

def RecurPath(Infected,Clusters,Origin,current_path,result):
    IsPath, IsNonSi = genomeCompare(Infected["genome"],Origin["genome"])
    if IsPath:
        if IsNonSi: 
            current_path[-1] = current_path[-1] + "*"
        current_path.append(Origin["name"])
        AddToResult(current_path,result)
        current_path.pop(-1)
    for contact in Clusters:
        if contact["name"] in current_path:
            continue
        if contact["name"]+"*" in current_path:
            continue
        IsPath, IsNonSi =  genomeCompare(Infected["genome"],contact["genome"])
        if IsPath:
            if IsNonSi: 
                current_path[-1] = current_path[-1] + "*"
            current_path.append(contact["name"])
        RecurPath(contact,Clusters,Origin,current_path,result)
        current_path.pop(-1)



def AddToResult(current_path,result):
    thepath = ""
    for x in current_path:
        thepath = thepath + x + " -> "
    thepath = thepath[:-4]
    result.append(thepath)


def genomeCompare(x,y):
    i = 0
    numdiff = 0
    numfirst = 0 
    while i < len(x):
        if x[i] != y[i]:
            numdiff = numdiff + 1
            if i == 0 or x[i-1] == "-":
                numfirst = numfirst + 1
        i = i + 1
    if numdiff <= 2:
        if numfirst > 1:
            return True,True
        else:
            return True, False

    return False,False




