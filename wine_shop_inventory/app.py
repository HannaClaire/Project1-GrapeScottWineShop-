from flask import Flask, render_template

from controllers.wines_controller import wines_blueprint

app = Flask(__name__)

app.register_blueprint(wines_blueprint)


@app.route('/wines')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
