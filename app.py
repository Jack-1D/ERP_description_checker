from flask import Flask, request
from flask_cors import CORS
from search import main_checker
import json

app = Flask(__name__)
CORS(app)
@app.route("/",methods=["POST", "GET"])
def hello():
    content = {}
    if request.method == "POST":
        # print(json.loads(list(request.form.keys())[0])["BOM"])
        erp = json.loads(list(request.form.keys())[0])["erp"].replace('plus','+')
        factory = json.loads(list(request.form.keys())[0])["factory"]
        content = main_checker(erp, factory)
        with open('check_result.json', 'w') as jsonfile:
            json.dump(content, jsonfile, indent=4)
        return json.dumps(content)
    return json.dumps(content)

if __name__ == "__main__":
    app.run(ssl_context='adhoc', host='0.0.0.0')