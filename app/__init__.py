from flask import Flask, request, render_template, redirect, flash
import logging
from app.forms import HaromszogForm
from app.haromszog import calc_haromszog

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nemtalálszki'

@app.route("/", methods=['GET', 'POST'])
def root():
    return redirect ("/1")


@app.route("/<ver>", methods=['GET', 'POST'])
def index(ver):

    if ver == "666":
        return render_template("666.html")
    if ver == "500":
        return render_template("500.html")

    form = HaromszogForm()
    if form.is_submitted():
        a = form.a_oldal.data
        b = form.b_oldal.data
        c = form.c_oldal.data

        result = calc_haromszog(ver,a,b,c)
        flash(result)

        print("api call: ver: "+ str(ver) + " a: " + str(a) +" b: " + str(b) +" c: " + str(c) +" -> "+ result)

        return redirect('/'+str(ver))
    return render_template("index.html", form=form, id=ver)

@app.route("/api/tipizalj", methods=['POST'])
def api():
    ver = request.args.get('ver',"1")

    if ver == "666":
        return "rip and tear!"
    try:
        a = request.json['a_oldal']
        b = request.json['b_oldal']
        c = request.json['c_oldal']
    except:
        return "hibás kérés formátum!\n elvárt formátum: \n{\n\"a_oldal\": 1,\n\"b_oldal\": 2,\n\"c_oldal\": 1\n}"

    result = calc_haromszog(ver,a,b,c)

    print("api call: ver: "+ str(ver) + " a: " + str(a) +" b: " + str(b) +" c: " + str(c) +" -> "+ result)
    return result
        
    


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500