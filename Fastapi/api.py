from fastapi import FastAPI,Path
from Schema.userinput import UserInput,default_cols
from fastapi.responses import JSONResponse
import joblib
import pandas as pd 
app = FastAPI()

model = joblib.load(
    "/Users/bibekacharya/Documents/Documents/Machine_Learning/Machine_Learning_projects/Logistic_Regression/Model/employee_attrition_pipeline.pkl"
)

MODEL_VERSION= '1.0.0' #usually done with MLflow but here we suppose 


@app.get('/')
def home():
    return {'message':'Welcome to prediction'}


@app.get("/health") # machine readable cuz aws service hit at this endpoint, if this says ok then gests deployed esaily
def health_check():
    return {
        'status':'Ok', #status of API
        'Version': MODEL_VERSION
    }

@app.post('/predict') # use POST for Ml/dl
def predict(userinput:UserInput):

        # Merge user data with default values
    user_data = {

        'Age': userinput.Age,

        'Gender': userinput.Gender,

        'JobRole': userinput.JobRole,

        'Education': userinput.Education,

        'MonthlyIncome': userinput.MonthlyIncome,

        'JobSatisfaction': userinput.JobSatisfaction,

        'Department': userinput.Department,

        'OverTime': userinput.OverTime,

        'BusinessTravel': userinput.BusinessTravel,

        'TotalWorkingYears': userinput.TotalWorkingYears,

        'WorkLifeBalance': userinput.WorkLifeBalance,

        'MaritalStatus': userinput.MaritalStatus

    }
    
    final_data= final_data = {**user_data, **default_cols} #unpack

   #model was trained in dataframe so here also use dataframe for same input format 
    input_data=pd.DataFrame([final_data])

    prediction = int(model.predict(input_data)[0])

    # Probabilities

    probabilities = model.predict_proba(input_data)[0]
    prob_stayed = float(probabilities[0])
    prob_left = float(probabilities[1])


    # Confidence = probability of predicted class

    confidence = prob_left if prediction == 1 else prob_stayed

    status = "Left" if prediction == 1 else "Stayed"
    return JSONResponse(

        status_code=200,

        content={

            "model_version": MODEL_VERSION,

            "prediction": prediction,

            "status": status,

            "probability_left": round(prob_left, 4),

            "probability_stayed": round(prob_stayed, 4),

            "confidence": round(confidence, 4)

        }

    )


    # we seperated the code written in all this file to make it professional and Industry-grade. 
    #Like pydantic code sent to Schema folder, imported pydantic cls here from the file etc 