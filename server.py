from flask import Flask, render_template, redirect
app = Flask(__name__)
app.secret_key = 'playplace'


@app.route('/')
def starter_boxes():
    return render_template('boxes.html')


if __name__ == "__main__":
    app.run(debug=True)
