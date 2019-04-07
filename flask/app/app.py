from flask import Flask
from flask import request
import decimal

import corr_calves.corr as cr
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/corr/')
def corrParam():
    #print(request.args.get("target"))
    #print(request.args.get("src"))

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

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')