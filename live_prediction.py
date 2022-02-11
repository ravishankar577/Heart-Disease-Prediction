import pandas as pd
import os
import sys
import pickle

model = pickle.load(open("naive_bayes_model.pkl", "rb"))
# df = pd.DataFrame(columns=["Day-Part", "Start Time", "End Time"])

try:

    age = int(input("Enter Age of Participant as a number"))
    gender = int(input("Enter gender of the Participant : (1 = male; 0 = female)"))
    thal = int(input("Enter the type of thalassemia :3 = normal, 6 = fixed defect,7 = reversable defect"))
    cp = int(input("Enter the chest pain type : 1 = typical angina, 2 = atypical angina ,3 = non - anginal pain, 4 = asymptotic"))
    trestbps = int(input("Enter the resting blood pressure (in mm Hg )"))
    chol = int(input("Enter the serum cholestorl reading in mg/dl"))
    fbs = int(input("I the fasting blood sugar > 120 mg/dl (1 = true; 0 = false)"))
    restecg = int(input("Enter the Resting ECG type : 0 = normal , 1 = having ST-T wave abnormality, 2 = left ventricular hyperthrophy"))
    thalach = int(input("Enter the maximum heart rate achieved"))
    exang = int(input("Does the participant have exercise induced angina (1 = yes; 0 = no)"))
    oldpeak = float(input("Value of ST depression induced by exercise relative to rest - (decimal value)"))
    slope = int(input(" Value of the slope of the peak exercise ST segment :1 = upsloping, 2 = flat , 3 = downsloping"))
    ca = int(input("number of major vessels (0-3) colored by flourosopy"))
    
    
    cp_1 = 0
    cp_2 = 0
    cp_3 = 0
    cp_4 = 0
    
    thal_3 = 0
    thal_6 = 0
    thal_7 = 0
    
    slope_1 = 0
    slope_2 = 0
    slope_3 = 0
    
    
    if cp == 1:
        cp_1 = 1
    elif cp ==2:
        cp_2 =1
    elif cp == 3:
        cp_3 = 1
    elif cp ==4:
        cp_4 =1
        
    if thal == 3:
        thal_3 = 1
    elif thal == 6:
        thal_6 =1
    elif thal == 7:
        thal_7 =1
        
    if slope == 1:
        slope_1 = 1
    elif slope == 2:
        slope_2 =1
    elif slope ==3:
        slope_3 = 1




    df1 = pd.DataFrame(data=[[age,gender,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,ca,cp_1,cp_2,cp_3,cp_4,thal_3,thal_6,thal_7,
                          slope_1,slope_2,slope_3]],columns=['age', 'sex','trestbps', 'chol','fbs', 'restecg', 'thalach', 'exang', 
              'oldpeak', 'ca', 'cp_1','cp_2','cp_3','cp_4','thal_3.0','thal_6.0','thal_7.0','slope_1','slope_2','slope_3' ])

 


    prediction = model.predict(df1)[0]
    if prediction == 1:
        pred = "participant has heart disease"

    elif prediction == 0:
        pred = "participant does not have heart disease"

    print("prediction:",pred)
    
except Exception as e:
    
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print(str(exc_type), exc_tb.tb_lineno)
    print("error in live_prediction", e.args[0])


