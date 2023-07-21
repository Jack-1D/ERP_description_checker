from flask import Flask, render_template, request
from search import main_checker
import json

content = []

app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def hello():
    if request.method == "POST":
        input_string = request.form["name"]
        content = main_checker(input_string)
        return render_template('popup.html',content=content)
    return render_template('popup.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)