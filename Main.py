#!/usr/bin/env python
# coding: utf-8

# In[5]:


#pip install fastapi
#pip install uvicorn

import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
from ProfilePrediction import PPrediction


# In[ ]:


from pydantic import BaseModel

#Class which describes Profile Prediction measurements

class PPrediction(BaseModel):
    Gender: str
    Age: float
    openness: float
    neuroticism: float
    conscientiousness: float
    agreeableness: float
    extraversion: float


# In[6]:


#Create the app object

app = FastAPI()
pickle_in = open("mul_lr.pkl","rb")
mul_lr = pickle.load(pickle_in)


# In[7]:


#Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return{'message': 'Hello, Stranger'}


# In[8]:


#Loacated at: http://127.0.0.1:8000/AnyNameHere

@app.get('/{name}')
def get_name(name: str):
    return{'Welcome': f'{name}'}


# In[9]:


#Expose the prediction functionality, make a prediction from the JSON data
#and return the predicted Profile with the confidence

@app.post('/predict')
def predict_profile(data:PPrediction):
    data=data.dict()
    Gender=data['Gender']
    Age=data['Age']
    openness=data['openness']
    neuroticism=data['neuroticism']
    conscientiousness=data['conscientiousness']
    agreeableness=data['agreeableness']
    extraversion=data['extraversion']
    
    print(mul_lr.predict([[Gender,Age,openness,neuroticism,conscientiousness,agreeableness,extraversion]]))
    print("Hello")
    
    prediction = mul_lr.predict([[Gender,Age,openness,neuroticism,conscientiousness,agreeableness,extraversion]])
    if(prediction==dependable):
        return{'Your personality type is dependable'}
    elif(prediction=extraverted):
        return{'Your personality type is extraverted'}
    elif(prediction=lively):
        return{'Your personality type is lively'}
    elif(prediction=responsible):
        return{'Your personality type is responsible'}
    else:
        return{'Your personality type is serious'}
        
        


# In[11]:


#Run the API with uvicorn

if __name__ == '__main__':
    uvicorn.run(app)


# In[ ]:




