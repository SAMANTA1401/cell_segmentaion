from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
import os
from cellSegmentaion.pipeline.prediction_pipeline import Prediction
from cellSegmentaion.pipeline.training_pipeline import TrainPipeline
from cellSegmentaion.utils.main_util import decodeImage




app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = Prediction()

@app.route('/')
@cross_origin()
def index():
    return render_template('app.html')

@app.route("/train",methods=['GET','POST'])
@cross_origin()
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "trainning done successfully!"

@app.route("/predict",methods=['POST', 'GET'])
@cross_origin()
def predictRoute():
    if request.method == "POST":
        image = request.files['image_input']
        imagedata = image.read()
        decodeImage(imagedata,clApp.filename)
        clApp.classifier.predict()
      
        return render_template("predict.html")
    

if __name__=='__main__':
    clApp = ClientApp()
    app.debug=True
    app.run(port=5000)