"""
A stock portfolio generator application using Flask that helps users explore
different portfolio options based on their inputs.

This file extracts information from users, such as: 
    Age → age (int)
    Capital available → capital (int)
    Lock-up period → time (int)
    Risk tolerance → risk (int)
    Specific sectors → sectors (list)
    Market cap preference → marketcap (string)
"""

from flask import Flask
from flask import request
from flask import render_template
import model

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def welcome():
    return render_template("welcome.html")

@app.route("/input", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        age = request.form.get("age")
        capital = request.form.get("capital")
        time = request.form.get("time")
        risk = request.form.get("risk")
        sectors = request.form.getlist("sectors")
        marketcap = request.form.get("marketcap")
        message = model.message(age,time)
        model.generate_port(capital, risk, sectors, marketcap)
        return render_template("results.html", age=age, capital=capital, time=time, risk=risk, sectors=sectors, marketcap=marketcap, message=message)
    return render_template("welcome.html")

@app.route("/portfolio", methods=["GET", "POST"])
def results():
    return render_template("portfolio.html")


if __name__ == "__main__":
    app.run(debug=True)