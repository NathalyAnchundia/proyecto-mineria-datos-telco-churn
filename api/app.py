from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "mensaje": "API de Predicción de Churn funcionando correctamente",
        "proyecto": "Minería de Datos - Telco Customer Churn",
        "estado": "activo"
    })


@app.route("/api/estado", methods=["GET"])
def estado():
    return jsonify({
        "api": "activa",
        "modelo": "pendiente de conexión"
    })


@app.route("/api/predict", methods=["POST"])
def predecir():

    datos = request.get_json()

    if not datos:
        return jsonify({
            "error": "No se recibieron datos."
        }), 400

    campos_requeridos = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "TotalServices"
    ]

    faltantes = [
        campo for campo in campos_requeridos
        if campo not in datos
    ]

    if faltantes:
        return jsonify({
            "error": "Faltan campos.",
            "campos_faltantes": faltantes
        }), 400

    return jsonify({
        "mensaje": "Datos recibidos correctamente.",
        "datos_recibidos": datos,
        "estado": "pendiente de conexión con el modelo"
    })


if __name__ == "__main__":
    app.run(debug=True)