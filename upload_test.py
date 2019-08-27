# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 10:44:43 2019

@author: u71288
"""
import requests
import json

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        #f.save(f.filename)
        
        # URL for the web service
        scoring_uri = 'http://fd2feb61-69c2-4e00-bff2-b0db15b037cd.southeastasia.azurecontainer.io/score'
        # If the service is authenticated, set the key
        key = 'ustfpismsdev8855765643'


        #with open(f.read()) as image_stream:
            #data=image_stream.read()
            # Convert to JSON string
        input_data = f.read()
        #jsObject = json.loads(data)

        # Set the content type
        headers = { 'Content-Type':'application/json' }
        # If authentication is enabled, set the authorization header
        headers['Authorization']='Bearer{'+key+'}'
        # Make the request and display the response
        resp = requests.post(scoring_uri, input_data, headers = headers)
        output_str = Markup(resp.text)  
        return render_template("success.html",output=output_str);
if __name__ == '__main__':  
    app.run(debug = False)  
