import re
from flask import Flask, render_template
from flask.wrappers import Request
from flask import request
from model import Model

app = Flask(__name__)


def Car_decider():
    pass


def petrol(fuel):
    if fuel == "Petrol":
        return 1
    else:
        return 0


def diesel(fuel):
    if fuel == "diesel":
        return 1
    else:
        return 0


def owner_decider(owner):
    if owner == "Yes":
        return 1
    else:
        return 0


def seller_type(seller):
    if seller == "Yes":
        return 1
    else:
        return 0


def Car_Name_Activa3g(car):
    if car == "Activa 3g":
        return 1
    else:
        return 0


def Car_Name_Activa4g(car):
    if car == "Activa 4g":
        return 1
    else:
        return 0


def Car_Name_BajajAvenger150(car):
    if car == "Bajaj Avenger 150":
        return 1
    else:
        return 0


def Car_Name_scross(car):
    if car == "s cross":
        return 1
    else:
        return 0


def Car_Name_swift(car):
    if car == "swift":
        return 1
    else:
        return 0


def Car_Name_sx4(car):
    if car == "sx4":
        return 1
    else:
        return 0


def Car_Name_verna(car):
    if car == "verna":
        return 1
    else:
        return 0


def Car_Name_vitarabrezza(car):
    if car == "vitara brezza":
        return 1
    else:
        return 0


def Car_Name_wagonr(car):
    if car == "wagon r":
        return 1
    else:
        return 0


def Car_Name_xcent(car):
    if car == "xcent":
        return 1
    else:
        return 0


@app.route("/", methods=["POST", "GET"])
def intial_func():
    prediction = 0
    if request.method == "POST":

        car = request.form["car"]
        fuel = request.form["fuel"]

        kms = request.form["kms"]
        year = request.form["year"]
        owner = request.form["owner"]
        price = request.form["price"]
        seller = request.form["seller"]
        prediction = Model(year, price, kms, owner_decider(owner), Car_Name_Activa3g(car), Car_Name_Activa4g(car), Car_Name_BajajAvenger150(car),	Car_Name_scross(car), Car_Name_swift(car),
                           Car_Name_sx4(car), Car_Name_verna(car), Car_Name_vitarabrezza(car), Car_Name_wagonr(car), Car_Name_xcent(car)	, diesel(fuel), petrol(fuel), seller_type(seller))

    return render_template("index.html", predict=prediction)


if __name__ == "__main__":
    app.run(debug=True)
