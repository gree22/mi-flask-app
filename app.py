from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verificar')
def verificar():
    # Aquí agregaríamos la lógica para verificar las tarjetas o cualquier otra funcionalidad
    return jsonify({"status": "verificación exitosa"})

if __name__ == "__main__":
    app.run(debug=True)
