'''
處理路由:flask主程式
'''
from search import main_checker
from get_ip import get_ipv4
from flask import Flask, request
from flask_cors import CORS
import json
from typing import Final

# 指定port，flask預設為5000
PORT: Final[int] = 5000

app = Flask(__name__)
CORS(app)
@app.route("/",methods=["POST", "GET"])
def hello():
    content = {"connected":True}
    if request.method == "POST":
        bom = json.loads(list(request.form.keys())[0])["BOM"]
        erp = json.loads(list(request.form.keys())[0])["erp"].replace('plus','+')
        factory = json.loads(list(request.form.keys())[0])["factory"]
        product_type = json.loads(list(request.form.keys())[0])["product_type"]
        content = main_checker(erp, factory, bom, product_type)
        return json.dumps(content)
    return json.dumps(content)

if __name__ == "__main__":
    get_ipv4(PORT)
    app.run(ssl_context='adhoc', host='0.0.0.0', port=PORT)