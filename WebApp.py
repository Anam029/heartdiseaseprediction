# WebApp starts here
import pandas as pd
from pywebio.input import *
from pywebio.output import *
from pywebio.platform.flask import webio_view
from pywebio import start_server
from flask import Flask
import pickle
import argparse

# Load the trained model
model = pickle.load(open('logmod.pkl', 'rb'))
app = Flask(__name__)

def heart():
    put_text("Check your patient's heart health by filling out the form below.").style('font-size:20px')

    # Input form
    info = input_group("Heart disease form",
        [
         input("Age of patient:", name='Age', type=FLOAT, required=True),
         radio('Input your sex', options=['Male','Female'], name='Sex', required=True),
         radio('Input chest pain type', options=['Typical angina','Atypical angina','Non-anginal pain','Asymptomatic'], name='ChestPain', required=True),
         input("Resting blood pressure (mm Hg):", name='RestingBP', type=FLOAT, required=True),
         input("Serum cholesterol (mg/dl):", name='Cholesterol', type=FLOAT, required=True),
         radio("Fasting blood sugar > 120 mg/dl", options=['Yes','No'], name='FastingBS', required=True),
         radio('Resting electrocardiographic results', options=['Normal','ST-T wave abnormality','Left ventricular hypertrophy'], name='RestECG', required=True),
         input("Maximum heart rate achieved:", name='MaxHR', type=FLOAT, required=True),
         radio("Exercise induced angina", options=['Yes','No'], name='ExAng', required=True),
         input("ST depression induced by exercise:", name='STDepression', type=FLOAT, required=True),
         radio("Slope of peak exercise ST segment", options=['Upsloping','Flat','Downsloping'], name='Slope', required=True),
         radio("Number of major vessels (0-3) colored by fluoroscopy", options=['0','1','2','3'], name='NumVessels', required=True),
         radio("Thalassemia level", options=['Normal','Fixed defect','Reversable defect'], name='Thal', required=True)
        ])

    # Map categorical inputs to numeric values
    sex_map = {'Male':1, 'Female':0}
    cp_map = {'Typical angina':0, 'Atypical angina':1, 'Non-anginal pain':2, 'Asymptomatic':3}
    fbs_map = {'Yes':1, 'No':0}
    restecg_map = {'Normal':0, 'ST-T wave abnormality':1, 'Left ventricular hypertrophy':2}
    exang_map = {'Yes':1, 'No':0}
    slope_map = {'Upsloping':0, 'Flat':1, 'Downsloping':2}
    thal_map = {'Normal':0, 'Fixed defect':1, 'Reversable defect':2}

    # Prepare input for prediction in correct order
    input_data = [
        info['Age'],                     # age
        sex_map[info['Sex']],            # sex
        cp_map[info['ChestPain']],       # cp
        info['RestingBP'],               # trestbps
        info['Cholesterol'],             # chol
        fbs_map[info['FastingBS']],      # fbs
        restecg_map[info['RestECG']],    # restecg
        info['MaxHR'],                   # thalach
        exang_map[info['ExAng']],        # exang
        info['STDepression'],            # oldpeak
        slope_map[info['Slope']],        # slope
        int(info['NumVessels']),         # ca
        thal_map[info['Thal']]           # thal
    ]

    # Column order must match training data
    columns_order = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach',
                     'exang','oldpeak','slope','ca','thal']
    input_df = pd.DataFrame([input_data], columns=columns_order)

    # Predict
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        popup("You have a higher risk of heart disease (accuracy ~91%)")
    else:
        popup("You do not have heart disease (accuracy ~91%)")


# Run app locally
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(heart, port=args.port)

# Flask route (optional)
app.add_url_rule('/WebApp', 'webio_view', webio_view(heart), methods=['GET','POST','OPTIONS'])
