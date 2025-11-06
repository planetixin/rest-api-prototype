from flask import Flask, jsonify
import json

products=[ 
    { "id": 1, "name": "Laptop", "price": 4500.00 },
    { "id": 2, "name": "gra", "price": 100.00 }
]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Get_product():
    product = 0
    for p in products:
        if p["id"] == id:
            product = p
    return jsonify("products:",products)

if __name__ == "__main__":
    app.run(debug = True)
    