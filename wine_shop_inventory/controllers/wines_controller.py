from flask import Flask, render_template
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
    wines = wine_repo.select_all()
    return render_template("/wines/show.jinja", all_wines = wines)










