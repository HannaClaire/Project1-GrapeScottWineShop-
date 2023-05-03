from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.wine import Wine
from models.producer import Producer
import repositories.wine_repository as wine_repo
import repositories.producer_repository as producer_repo


producers_blueprint = Blueprint("producers", __name__)

# @producer_blueprint.route("/wines/new", methods=['GET'])
# def new_wine():
#     producers = producer_repo.select(id)
#     return render_template("wines/index.jinja", producers=producers)

@producers_blueprint.route("/producers", methods=['GET'])
def producers():
    all_producers = producer_repo.select_all()
    return render_template("producers/index.jinja", all_producers = all_producers)


@producers_blueprint.route("/producers/new", methods=['GET'])
def new_producer():
    return render_template("producers/new.jinja")

# add
@producers_blueprint.route("/producers", methods=['POST'])
def add_producer():
    name = request.form['name']
    producer = Producer(name)
    producer_repo.save(producer)
    return redirect('/producers')

# show
@producers_blueprint.route("/producers/<id>", methods=['GET'])
def show_producer(id):
    producer = producer_repo.select(id)
    wines = wine_repo.get_wines_for_producer(producer)
    return render_template("/producers/show.jinja", producer = producer, wines = wines)


# edit
@producers_blueprint.route("/producers/<id>/edit", methods=['GET'])
def edit_producer(id):
    producer = producer_repo.select(id)
    all_producers = producer_repo.select_all()
    return render_template('producers/edit.jinja', producer=producer, all_producers=all_producers)


#update
@producers_blueprint.route("/producers/<id>", methods=['POST'])
def update_producer(id):
    name = request.form['name']
    producer = Producer(name, id)
    producer_repo.update(producer)
    return redirect('/producers')
