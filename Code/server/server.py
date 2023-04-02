from flask import Flask,request,jsonify
app = Flask(__name__)
import Util

@app.route('/get_location_name')
def get_location_name():
    response = jsonify({
        'locations': Util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price':Util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-control-Allow-origin','*')

    return response

if __name__ == "__main__":
    print("String python flask Server for Home price Prediction")
    Util.load_saved_artifacts()
    app.run()
