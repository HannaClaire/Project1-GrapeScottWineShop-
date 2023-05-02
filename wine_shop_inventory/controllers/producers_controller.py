from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.wine import Wine
from models.producer import Producer
import repositories.wine_repository as wine_repo
import repositories.producer_repository as producer_repo


wines_blueprint = Blueprint("wines", __name__)
producer_blueprint = Blueprint("producers", __name__)

# @producer_blueprint.route("/wines/new", methods=['GET'])
# def new_wine():
#     producers = producer_repo.select(id)
#     return render_template("wines/index.jinja", producers=producers)


# @wines_blueprint.route("/wines/new", methods=['GET'])
# def new_producer():
#     producers = producer_repo.select_all
#     return render_template("wines/new.jinja", all_producers = producers)


# @wines_blueprint.route("/wines/new", methods=['POST'])
# def add_producer():
#     name = request.form['name']
#     producer = Producer(name)
#     producer_repo.save(producer)
#     return redirect(url_for('wines.wines'))
