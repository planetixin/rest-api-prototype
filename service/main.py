from flask import Flask, jsonify
import json

werehouse=[ 
    { "id": 1, "quantify": 4},
    { "id": 2, "quantify": 10}
]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Get_Service():
    stan = 0
    for p in werehouse:
        if s["id"] == id:
            stan = s
    return jsonify("stan:",werehouse)

if __name__ == "__main__":
    app.run(debug = True)