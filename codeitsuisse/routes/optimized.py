import logging
import json
import random
import operator as op
from functools import reduce


from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/optimizedportfolio', methods=['POST'])
def evaluatePort():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    out = []
    for case in data["inputs"]:
        todt= []
        for future in case["IndexFutures"]:
            OHR = ohrcal(future["CoRelationCoefficient"],case["Portfolio"]["SpotPrcVol"],future["FuturePrcVol"])
            futvol = future["FuturePrcVol"]
            NumCon = concal(OHR,case["Portfolio"]["Value"],future["IndexFuturePrice"],future["Notional"])
            todt.append([future["Name"],OHR,futvol,Numcon])
        sorted(todt, key=lambda x: (x[1],x[2],x[3]))
        out.append({"HedgePositionName": todt[0],"OptimalHedgeRatio": todt[1],"NumFuturesContract": todt[3]}) 
    fr = { "outputs": out }
    logging.info("My result :{}".format(out))
    return json.dumps(out);

def ohrcal(p,os,op):
    return round(p*os/op,3)

def NumCon(ohr,pv,fp,nvp):
    return round(ohr*pv/(fp*nvp),0)