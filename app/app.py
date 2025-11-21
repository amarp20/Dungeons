from flask import Flask, render_template, Blueprint

# Definir blueprint
main = Blueprint('main', __name__)

# Página de inicio (usa index.html que hereda de base.html)
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ficha')
def ficha():
    return render_template('ficha.html')

@main.route('/hechizos')
def hechizos():
    return render_template('hechizos.html')

# Crear la app principal
def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app

# Ejecutar app en modo debug
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
