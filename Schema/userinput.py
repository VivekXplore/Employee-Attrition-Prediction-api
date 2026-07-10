from pydantic import BaseModel, computed_field,Field
from typing import Dict, Literal,Annotated

default_cols ={
    'DailyRate': 802,
    'EnvironmentSatisfaction': 3,
    'HourlyRate': 66,
    'JobInvolvement': 3,
    'JobLevel': 2,
    'MonthlyRate': 14235,
    'NumCompaniesWorked': 2,
    'PercentSalaryHike': 14,
    'PerformanceRating': 3,
    'RelationshipSatisfaction': 3,
    'StockOptionLevel': 1,
    'TrainingTimesLastYear': 3 ,
    'YearsWithCurrManager': 3,
    'DistanceFromHome': 7,
    'YearsInCurrentRole': 3,
    'YearsSinceLastPromotion': 1,
    'YearsAtCompany': 5,
    'EducationField': 'Life Sciences'
}
class UserInput(BaseModel):
    # we will only take sensible input form user not all 
    Age:Annotated[int,Field(...,gt=18,strict=True,description='Age of the employee')]
    Gender:Annotated[Literal['Male','Female'],Field(...,description='Your sex M/F')]
    JobRole:Annotated[Literal['Sales Executive', 'Research Scientist', 'Laboratory Technician',
       'Manufacturing Director', 'Healthcare Representative', 'Manager',
       'Sales Representative', 'Research Director', 'Human Resources'],Field(...,description='What work you do in the compnay?')]
    Education:Annotated[Literal[1,2,3,4,5],Field(...,description=' 1: Below College, 2: College, 3: Bachelor, 4: Master, 5: Doctor')]
    MonthlyIncome:Annotated[int,Field(...,gt=1000, description='Enter your montly salary')]
    JobSatisfaction:Annotated[Literal[1,2,3,4],Field(...,description='How satisfied are you with job? 1 = Low, 2 = Medium, 3 = High, and 4 = Very High')]
    Department:Annotated[Literal['Sales', 'Research & Development', 'Human Resources'],Field(...,description='Enter the Deparatment you work in. ')]
    OverTime :Annotated[Literal['Yes','No'],Field(...,description='Do you do OverTime?')]
    BusinessTravel:Annotated[Literal['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'],Field(...,description='How ofteen do you travel for work?')]
    TotalWorkingYears:Annotated[int,Field(...,lt=60,description='How long have you been working in the company?')]
    WorkLifeBalance:Annotated[Literal[1,2,3,4],Field(...,description='Hows work-life balance? 1 = Bad, 2 = Good, 3 = Better, and 4 = Best')]
    MaritalStatus:Annotated[Literal['Single', 'Married', 'Divorced'],Field(...,description='Are you married?')]


    # above are input we will take from user 

   # we dont have field like Bmi or verdict or city tiers etc that we can compute from user input so we keep it default 


    # for others we will fill with the default/median values 


    ''' WE WILL USE OUR BIG BRAIN DO THIS IN OUR MODEL NOTEBOOK AND COPY THE OUPUT HERE 
    
    median_values = {
    'DailyRate': int(df['DailyRate'].median()),
    'EnvironmentSatisfaction': int(df['EnvironmentSatisfaction'].median()),
    'HourlyRate': int(df['HourlyRate'].median()),
    'JobInvolvement': int(df['JobInvolvement'].median()),
    'JobLevel': int(df['JobLevel'].median()),
    'MonthlyRate': int(df['MonthlyRate'].median()),
    'NumCompaniesWorked': int(df['NumCompaniesWorked'].median()),
    'PercentSalaryHike': int(df['PercentSalaryHike'].median()),
    'PerformanceRating': int(df['PerformanceRating'].median()),
    'RelationshipSatisfaction': int(df['RelationshipSatisfaction'].median()),
    'StockOptionLevel': int(df['StockOptionLevel'].median()),
    'TrainingTimesLastYear': int(df['TrainingTimesLastYear'].median()) .............
    }    ... there was error so we had to make it global dict '''

