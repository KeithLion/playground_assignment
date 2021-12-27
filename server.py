from flask import Flask, render_template, redirect
app = Flask(__name__)
app.secret_key = 'playplace'


@app.route('/')
def play():
    return redirect('/play')


@app.route('/play')
def starter_boxes():
    return render_template('boxes.html', box=3)


@app.route('/play/<int:num>')
def one_box(num):
    return render_template('boxes.html', box=num)


if __name__ == "__main__":
    app.run(debug=True)
