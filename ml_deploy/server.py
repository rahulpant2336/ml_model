# Import libraries
import numpy as np
import requests
from flask import Flask, request, jsonify, render_template
import pickle
import json

app = Flask(__name__)
# Load the model
model = pickle.load(open('model.pkl','rb'))
@app.route('/api',methods=['POST'])
def predict():
    #projectpath = request.form['Name']
	
    #y = json.loads(projectpath)
	
    #return jsonify(y)
    #return request.json['name']
	# Get the data from the POST request.
    data = request.get_json(force=True)
    #return data
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])
    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)
	
    #print(y.json())
	
@app.route('/request')
def hello_world():
   import requests
   url = 'http://localhost:5000/api'
   r = requests.post(url,json={'exp':6,})
   return str(r.json())
	
if __name__ == '__main__':
    app.run(port=5000, debug=True)