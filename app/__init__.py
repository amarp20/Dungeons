from flask import Flask, render_template, Blueprint, request
import json

# Definir blueprint
main = Blueprint('main', __name__)

# Rutas
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ficha')
def ficha():
    return render_template('ficha.html')

@main.route('/hechizos')
def hechizos():
    query = request.args.get('q', '').strip().lower()
    seleccion = request.args.get('seleccion', '')

    # Cargar hechizos desde el archivo JSON
    with open('hechizos.json', encoding='utf-8') as f:
        hechizos = json.load(f)

    resultados = []
    hechizo = None

    if seleccion:
        hechizo = next((h for h in hechizos if h['nombre'] == seleccion), None)
    elif query:
        resultados = [h for h in hechizos if query in h['nombre'].lower()]

    return render_template('hechizos.html', resultados=resultados, hechizo=hechizo)

# Crear la app principal
def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app

