from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('breast_cancer_aix360_model.pkl', 'explainer'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    #Fuel_Type_Diesel=0
    if request.method == 'POST':
        mean_radius = float(request.form['mean radius'])
        mean_texture=float(request.form['mean texture'])
        mean_perimeter=float(request.form['mean perimeter'])
        mean_area=float(request.form['mean area'])
        mean_smoothness=float(request.form['mean smoothness'])
        mean_compactness=float(request.form['mean compactness'])
        mean_concavity=float(request.form['mean concavity'])
        mean_concave_points=float(request.form['mean concave points'])
        mean_symmetry=float(request.form['mean symmetry'])
        mean_fractal_dimenstion=float(request.form['mean fractal dimenstion'])
        radius_error=float(request.form['radius error'])
        texture_error=float(request.form['texture error'])
        perimeter_error=float(request.form['perimeter error'])
        area_error=float(request.form['area error'])
        smoothness_error=float(request.form['smoothness error'])
        compactness_error=float(request.form['compactness error'])
        concavity_error=float(request.form['concavity error'])
        concave_points_error=float(request.form['concave points error'])
        symmetry_error=float(request.form['symmetry error'])
        fractal_dimension_error=float(request.form['fractal dimension error'])
        worst_radius=float(request.form['worst radius'])
        worst_texture=float(request.form['worst texture'])
        worst_perimeter=float(request.form['worst perimeter'])
        worst_area=float(request.form['worst area'])
        worst_smoothness=float(request.form['worst smoothness'])
        worst_compactness=float(request.form['worst compactness'])
        worst_concavity=float(request.form['worst concavity'])
        worst_concave_points=float(request.form['worst concave points'])
        worst_symmetry=float(request.form['worst symmetry'])
        worst_fractal_dimension=float(request.form['worst fractal dimension'])



        prediction=model.predict([['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst radius', 'worst texture', 'worst perimeter', 'worst area',
       'worst smoothness', 'worst compactness', 'worst concavity',
       'worst concave points', 'worst symmetry', 'worst fractal dimension']]])
        output=round(prediction[0],2)
        if output=0:
            return render_template('index.html',prediction_texts="BENIGN")
        elif output=1:
            return render_template('index.html',prediction_text="MELIGNANT")
        else:
            return render_temlate('index.html',prediction_text="error")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
