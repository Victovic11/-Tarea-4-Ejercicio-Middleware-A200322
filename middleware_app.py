from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Middleware que registra cada solicitud
@app.before_request
def registrar_solicitud():
    print(f"Solicitud recibida: {request.method} {request.path}")

# Ruta para servir la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar solicitudes
@app.route('/solicitudes', methods=['GET'])
def obtener_solicitudes():
    return jsonify({"mensaje": "Solicitud recibida y registrada"}), 200

if __name__ == "__main__":
    app.run(debug=True)
