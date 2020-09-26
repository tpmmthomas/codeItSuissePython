import logging
import json
import random
import operator as op
from functools import reduce


from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/inventory-management', methods=['POST'])
def evaluateInven():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    searchname = data[0]["searchItemName"]
    resultlist=[]
    for item in data[0]["items"]:
        lcsstr = lcs(searchname.lower(),item.lower(),len(searchname),len(item))
        changearr = [[] for y in range(len(lcsstr)+1)]
        ptrlcs = 0
        ptrbase = 0
        ptritem = 0
        while ptrbase < len(searchname):
            if ptrlcs == len(lcsstr):
                changestr = "-"+searchname[ptrbase]
                changearr[ptrlcs].append(changestr)
                ptrbase = ptrbase+1
                continue
            if lcsstr.lower()[ptrlcs] == searchname.lower()[ptrbase]:
                ptrlcs = ptrlcs+1
                ptrbase=ptrbase+1
            else:
                changestr = "-"+searchname[ptrbase]
                changearr[ptrlcs].append(changestr)
                ptrbase=ptrbase+1
        ptrlcs = 0
        nummin = len(changearr[0])
        while ptritem < len(item):
            if ptrlcs == len(lcsstr):
                changestr = "+"+item[ptritem]
                if nummin > 0:
                    changearr[ptrlcs][len(changearr[ptrlcs])-nummin] = changestr[1:]
                    nummin = nummin - 1
                else:
                    changearr[ptrlcs].append(changestr)
                ptritem = ptritem+1
                continue
            if lcsstr.lower()[ptrlcs] == item.lower()[ptritem]:
                ptrlcs = ptrlcs+1
                nummin = len(changearr[ptrlcs])
                ptritem = ptritem + 1
            else:
                changestr = "+"+item[ptritem]
                if nummin > 0:
                    changearr[ptrlcs][len(changearr[ptrlcs])-nummin] = changestr
                    nummin = nummin - 1
                else:
                    changearr[ptrlcs].append(changestr)
                ptritem=ptritem+1 
        noop = 0
        result = ""
        for i in range(0,len(lcsstr)):
            for op in changearr[i]:
                noop = noop + 1
                result = result + op
            result = result + lcsstr[i]
        for op in changearr[len(lcsstr)]:
            noop = noop + 1
            result = result + op
        resultlist.append([item,result,noop]) ##
    finalresult = sorted(resultlist, key=lambda param: (param[2],param[0]))
    rl = []
    for r in finalresult:
        if len(rl)>=10:
            break
        rl.append(r[1])
    returnset = {}
    returnset["searchItemName"] = searchname
    returnset["searchResult"] = rl
    logging.info("My result :{}".format(returnset))
    return json.dumps([returnset]);


def lcs(X, Y, m, n): 
    L = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Following steps build L[m+1][n+1] in bottom up fashion. Note 
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # Following code is used to print LCS 
    index = L[m][n] 
  
    # Create a character array to store the lcs string 
    lcs = [""] * (index+1) 
    lcs[index] = "" 
  
    # Start from the right-most-bottom-most corner and 
    # one by one store characters in lcs[] 
    i = m 
    j = n 
    while i > 0 and j > 0: 
  
        # If current character in X[] and Y are same, then 
        # current character is part of LCS 
        if X[i-1] == Y[j-1]: 
            lcs[index-1] = X[i-1] 
            i-=1
            j-=1
            index-=1
  
        # If not same, then find the larger of two and 
        # go in the direction of larger value 
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
    return "".join(lcs)