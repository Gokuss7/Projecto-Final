from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/provincias')
def provincias():
    response=requests.get("http://127.0.0.1:5000/api/provincias")
    return render_template('provincias.html', data=response.json())

@app.route('/cantones')
def cantones():
    response=requests.get("http://127.0.0.1:5000/api/cantones")
    return render_template('cantones.html', data=response.json())

@app.route('/distritos')
def distritos():
    response=requests.get("http://127.0.0.1:5000/api/distritos")
    return render_template('distritos.html', data=response.json())

@app.route('/SAN JOSE')
def sanjose():
    response=requests.get("http://127.0.0.1:5000/api/cantones")
    return render_template('sanjose.html', data=response.json())

@app.route('/ALAJUELA')
def alajuela():
    response=requests.get("http://127.0.0.1:5000/api/cantones")
    return render_template('alajuela.html', data=response.json())

@app.route('/CARTAGO')
def cartago():
    response=requests.get("http://127.0.0.1:5000/api/cantones")
    return render_template('cartago.html', data=response.json())

@app.route('/HEREDIA')
def heredia():
    response=requests.get("http://127.0.0.1:5000/api/cantones")
    return render_template('heredia.html', data=response.json())

@app.route('/GUANACASTE')
def guanacaste():
    response=requests.get("http://127.0.0.1:5000/api/cantones")
    return render_template('guanacaste.html', data=response.json())

@app.route('/PUNTARENAS')
def puntarenas():
    response=requests.get("http://127.0.0.1:5000/api/cantones")
    return render_template('puntarenas.html', data=response.json())

@app.route('/LIMON')
def limon():
    response=requests.get("http://127.0.0.1:5000/api/cantones")
    return render_template('limon.html', data=response.json())

@app.route('/CONSULADO')
def consulado():
    response=requests.get("http://127.0.0.1:5000/api/cantones")
    return render_template('consulado.html', data=response.json())

@app.route('/CENTRAL')
def central():
    response=requests.get("http://127.0.0.1:5000/api/distritos")
    return render_template('central.html', data=response.json())

if __name__ == '__main__':
    app.debug = True
    app.run(port=2000)