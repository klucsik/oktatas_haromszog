from flask import Flask, request, render_template, redirect, flash
import logging
from app.forms import HaromszogForm
from app.haromszog import calc_haromszog

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nemtalálszki'


@app.route("/<ver>", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index(ver=1):
    ver = int(ver)
    form = HaromszogForm()
    if form.is_submitted():
        a = form.a_oldal.data
        b = form.b_oldal.data
        c = form.c_oldal.data
        print("ver: "+ str(ver) + " a: " + str(a) +" b: " + str(b) +" c: " + str(c))
        result = calc_haromszog(ver,a,b,c)
        flash(result)
        print(result)
        return redirect('/'+str(ver))
    return render_template("index.html", form=form, id=ver)
