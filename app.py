from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')



@app.route('/departures/<departure>/')
def departure(departure):
    return render_template('departure.html',departure='1')


@app.route('/tours/<id>/')
def tour(id):
    return render_template('tour.html',id='1')



app.run()