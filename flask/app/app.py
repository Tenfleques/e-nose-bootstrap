# -*- coding: utf-8 -*- 
from flask import Flask
from flask import request
import decimal
import pandas as pd
import numpy as np
import io
import ast

import corr_calves.corr as cr
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Correlation analysis server'

@app.route('/corr/')
def corrParam():
    b = request.args.get("target") or "fisiology"
    a = request.args.get("src") or "param-a"
    mintr = request.args.get("mincorr") or .65
    D = decimal.Decimal
    mintr = D(mintr)
    
    a = "./data/" + a + ".csv" 
    b = "./data/" + b + ".csv" 

    print((a,b))
    
    y = cr.readData(b)
    x = cr.readData(a)
    data = cr.corrsWithColumnsIn(
            x, 
            y, 
            mintr)
    return json.dumps(data.to_dict(), ensure_ascii=False)   
@app.route('/corr/plot/bar', methods = ['GET','POST'])
def corrParamImage():
    src = request.form['src'] or ""
    dict_in = ast.literal_eval(src)

    #return pd.DataFrame(dict_in).plot.bar()

@app.route('/corr/csv/', methods = ['GET','POST'])
def corrParamCSV():
    cols = request.form['target'] or ""
    cols = cols.split(",")
    data = request.form['src']
    mintr = request.form['mincorr']or .65

    D = decimal.Decimal
    mintr = D(mintr)

    data = cr.corrsWithColumnsCSV(
            data=data, 
            cols=cols, 
            corr_threshold=mintr)
    return json.dumps(data.to_dict(), ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')