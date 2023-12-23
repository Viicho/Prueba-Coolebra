import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="",
        db="prueba"
    )

    if conexion.is_connected(): 
        print("conexion exitosa")
        cursor = conexion.cursor()
        
        app = Flask(__name__)
        
        CORS(app)

        @app.route("/")
        def index():
            cursor.execute("""
            SELECT product.id, product.name, product.ean, product.sku, market.name AS market_name, (SELECT price.normal_price FROM price WHERE price.product_id = product.id AND price.active = 1 ORDER BY price.create_date DESC, price.normal_price ASC LIMIT 1) AS price FROM product LEFT JOIN market ON market.id = product.market_id       
            """)
            registro = cursor.fetchall()
            productos = {}
            for producto in registro:
                if producto[2] in productos:
                    productos[producto[2]]["query"].append(producto)
                    if producto[4] not in productos[producto[2]]["markets"]:
                        productos[producto[2]]["markets"].append(producto[4])
                    if producto[-1] < productos[producto[2]]["min"]: 
                        productos[producto[2]]["min"] = producto[-1]
                    if producto[-1] > productos[producto[2]]["max"]: 
                        productos[producto[2]]["max"] = producto[-1]
                else:
                    productos[producto[2]] = {"name": producto[1], "query": [producto], "markets": [producto[4]], "min": producto[-1], "max": producto[-1]}
            resultados = []
            for key in productos:
                producto = productos[key]
                resultados.append({"Ean": {"nombre": producto["name"], "datos": producto["query"], "markets": len(producto["markets"]), "rango": str(producto["max"]) + " - " + str(producto["min"])}})
            return jsonify(resultados)

        if __name__ == "__main__":
            app.run(debug=True)


except Error as ex:
    print(f"Error durante la ejecucion {ex}")
finally:
    if conexion.is_connected():
        conexion.close()
        print('La conexion se a finalizado')