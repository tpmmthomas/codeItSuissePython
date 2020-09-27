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
            todt.append([future["Name"],OHR,futvol,NumCon])
            logging.info("name {}".format(future["Name"]))
            logging.info("OHR {}".format(OHR))
            logging.info("OHR {}".format(futvol))
            logging.info("OHR {}".format(NumCon))
        logging.info("OHR {}".format(todt))
        sorted(todt, key=lambda x: (x[1],x[2],x[3]))
        logging.info("OHR {}".format(todt))
        out.append({"HedgePositionName": todt[0][0],"OptimalHedgeRatio": todt[0][1],"NumFuturesContract": todt[0][3]}) 
    fr = { "outputs": out }
    logging.info("My result :{}".format(fr))
    return json.dumps(fr);

def ohrcal(p,os,op):
    return round(p*os/op,3)

def concal(ohr,pv,fp,nvp):
    return round(ohr*pv/(fp*nvp))