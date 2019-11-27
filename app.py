from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, IntegerField, SelectField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://msa:zFcmVW!P5bBF2rmo97@37.77.193.36:3306/49winters'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Prodtest(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(50))
    product = db.Column(db.String(50))
    style = db.Column(db.String(50))
    stylecode = db.Column(db.String(50))

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(2))
    name = db.Column(db.String(50))

class Form(FlaskForm):
    state = SelectField('state', choices=[('CA', 'California'), ('NV', 'Nevada')]) 
    city = SelectField('city', choices=[])

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cities', methods=['GET', 'POST'])
def index():
    form = Form()
    form.city.choices = [(city.id, city.name) for city in City.query.filter_by(state='CA').all()]

    if request.method == 'POST':
        city = City.query.filter_by(id=form.city.data).first()
        return '<h1>State: {}, City: {}</h1>'.format(form.state.data, city.name)

    return render_template('index.html', form=form)

@app.route('/city/<state>')
def city(state):
    cities = City.query.filter_by(state=state).all()

    cityArray = []

    for city in cities:
        cityObj = {}
        cityObj['id'] = city.id
        cityObj['name'] = city.name
        cityArray.append(cityObj)

    return jsonify({'cities' : cityArray})

@app.route('/prod', methods=['GET', 'POST'])
def dispprod():
    # context=Prodtest.query.filter_by(stylecode="OXF")
    context = Prodtest.query.all()
    return render_template('products.html', context=context)

if __name__ == '__main__':
    app.run(debug=True)