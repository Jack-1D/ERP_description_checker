from flask import Flask, render_template, request
from flask_cors import CORS
from search import main_checker
import json

app = Flask(__name__)
CORS(app)
@app.route("/",methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        # print(json.loads(list(request.form.keys())[0])["BOM"])
        erp = json.loads(list(request.form.keys())[0])["erp"].replace('plus','+')
        factory = json.loads(list(request.form.keys())[0])["factory"]
        content = main_checker(erp, factory)
        return json.dumps({"error_msg": content})
    return json.dumps({"status": "ok"})

if __name__ == "__main__":
    app.run(ssl_context='adhoc', host='0.0.0.0')