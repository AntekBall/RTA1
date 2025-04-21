# TWOJ KOD 
from flask import Flask, request, jsonify
# from flask import 
# Create a flask
app = Flask(__name__)

@app.route('/api/v1.0/predict',methods=["GET"])
def rule():
    number1 = float(request.args.get("number1", 0))
    number2 = float(request.args.get("number2", 0))

    
    if number1 + number2 > 5.8:
        prediction = 1
    else:
        prediction = 0

    prediction_dict = {"prediction":prediction, "features":[number1,number2]}
    return jsonify(prediction_dict)

if __name__ == '__main__':
    app.run(port=5005)
    
