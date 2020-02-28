from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class HaromszogForm(FlaskForm):
    a_oldal = IntegerField('"a" oldal', validators=[DataRequired()])
    b_oldal = IntegerField('"b" oldal', validators=[DataRequired()])
    c_oldal = IntegerField('"c" oldal')
    submit = SubmitField('Tipizálj!')