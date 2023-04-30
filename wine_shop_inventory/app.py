from flask import Flask, render_template

from controllers.wines_controller import wines_blueprint

app = Flask(__name__)

app.register_blueprint(wines_blueprint)


@app.route('/home')
def home():
    return render_template('index.jinja')


if __name__ == '__main__':
    app.run(debug=True)
