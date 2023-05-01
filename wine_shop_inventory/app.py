from flask import Flask, render_template

from controllers.wines_controller import wines_blueprint
from controllers.producers_controller import producer_blueprint
app = Flask(__name__)

app.register_blueprint(wines_blueprint)
app.register_blueprint(producer_blueprint)


@app.route('/home')
def home():
    return render_template('home.jinja')

if __name__ == '__main__':
    app.run(debug=True)
