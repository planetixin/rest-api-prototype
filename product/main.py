from flask import Flask, jsonify, render_template, render_template_string
import json

products=[ 
    { "id": 1, "name": "Laptop", "price": 4500.00 },
    { "id": 2, "name": "gra", "price": 100.00 }
]

app = Flask(__name__)

@app.route('/products/<int:id>', methods=['GET'])
def Get_product(id):
    product = 0
    for p in products:
        if p["id"] == id:
            product = p
    if product == 0:
        return render_template_string('PageNotFound {{errorCode}}', errorCode='404'), 404
    return jsonify("products:",product)

@app.route('/products', methods=['GET'])
def Get_products():
    return jsonify("products:",products)

if __name__ == "__main__":
    app.run(debug = True)
    