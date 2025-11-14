from flask import Flask, jsonify, render_template, render_template_string
import json

werehouse=[ 
    { "id": 1, "quantify": 4},
    { "id": 2, "quantify": 10}
]

app = Flask(__name__)

@app.route('/service/<int:id>', methods=['GET'])
def Get_Service(id):
    stan = 0
    for s in werehouse:
        if s["id"] == id:
            stan = s
    if stan == 0:
        return render_template_string('PageNotFound {{errorCode}}', errorCode='404'), 404
    return jsonify("stan:",werehouse)

if __name__ == "__main__":
    app.run(debug = True)