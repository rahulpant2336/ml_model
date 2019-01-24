# Import libraries
#flask_env
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
	
@app.route('/request',methods=['POST'])
def hello_world():
   import requests
   rahul = request.form['Name']
   rahul1 = json.loads(rahul)
   
   url = 'http://localhost:5000/api'
   exp = 1
   r = requests.post(url,json={'exp':rahul1,})
   return str(r.json())
   
@app.route('/rahul')
def hello_form():
   return render_template("rahul.html")
  
   
	
if __name__ == '__main__':
    app.run(port=5000, debug=True)