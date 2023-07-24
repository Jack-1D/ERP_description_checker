from flask import Flask, render_template, request
from search import main_checker
import json

content = []

app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def hello():
    if request.method == "POST":
        input_string = request.form["name"]
        factory = "TPMC" if len(request.form.getlist('factory')) != 0 else "SHMC"
        content = main_checker(input_string, factory)
        return render_template('popup.html',content=content, factory=factory)
    return render_template('popup.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)