"""
A stock portfolio generator application using Flask that helps users explore
different portfolio options based on their inputs.

This file extracts information from users, such as: 
    Age → age (int)
    Capital available → capital (int)
    Lock-up period → time (int)
    Risk tolerance → risk (int)
    Specific sectors → sectors (list)
    Number of stocks preferred → stocksnum (int)
    Market cap preference → marketcap (string)
    Beta preference → betapref (string)
"""

from flask import Flask
from flask import request
from flask import render_template
import project

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
        sectors = request.form.get("sectors")
        stocksnum = request.form.get("stocksnum")
        marketcap = request.form.get("marketcap")
        betapref = request.form.get("betapref")
        # a list of stocks, ETFs, Treasury bills from project.py
        # station_name, wheelchair_accessibility = mbta_helper.find_stop_near(place_name, radius,route_type)
        return render_template("results.html")
        # return the list of stocks, ETFs, Treasury bills in results.html template
        # return render_template("results.html", station_name=station_name,
                            #    wheelchair_accessibility=wheelchair_accessibility, radius = radius, route_type = route_type, place_name = place_name)
    return render_template("welcome.html")



if __name__ == "__main__":
    app.run(debug=True)