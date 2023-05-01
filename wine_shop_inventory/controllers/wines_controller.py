from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.wine import Wine
from models.producer import Producer
import repositories.wine_repository as wine_repo
import repositories.producer_repository as producer_repo

wines_blueprint = Blueprint("wines", __name__)
producer_blueprint = Blueprint("producers", __name__)


@wines_blueprint.route("/wines")
def wines():
    wines = wine_repo.select_all()
    return render_template("wines/index.jinja", all_wines = wines)



@wines_blueprint.route("/wines/<id>", methods = ['GET'])
def wine(id):
    wines = wine_repo.select(id)
    return render_template("/wines/show.jinja", wines = wines)


@wines_blueprint.route("/wines/add", methods=['GET'])
def new_wine():
    producers = producer_repo.select_all()
    return render_template("wines/new.jinja", all_producers=producers)  #hadnt rendered template with wines/new - (hours worth of pain)!!!

@wines_blueprint.route("/wines/new", methods =['POST'])
def add_wine():
    name = request.form['name']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    producer_id = int(request.form['producer_id'])
    producer = producer_repo.select(producer_id)
    if not producer:
        error_message = f"Producer with ID {producer_id} does not exist."
        return render_template('error.html', message=error_message)
    wine = Wine(name, description, stock_quantity, buying_cost, selling_price, producer_id)
    wine_repo.save(wine)
    return redirect (url_for('wines.wines'))


@wines_blueprint.route("/wines/<id>/delete", methods=['POST'])
def delete_wine(id):
    wine_repo.delete(id)
    return redirect('/wines')




