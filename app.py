import os
import cv2
import numpy as np
from flask import Flask,request
app = Flask(__name__)

port=5000

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def send_file():
    img = cv2.imread('./uploaded_file.jpg')
    _, img_encoded = cv2.imencode('.jpg', img)
    """f=open('uploaded_file.jpg','rb')
    img=f.read()
    f.close()"""
    data=img_encoded.tostring()
    return data

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print ('post request')
        f = request.files['the_file']
        f.save('./uploaded_file.jpg')
        return send_file()



