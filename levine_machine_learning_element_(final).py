# -*- coding: utf-8 -*-
"""Levine Machine Learning Element (Final)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7nIH28CHC_aLdzrR9sMOR-W75MvEcR8

# Business 

Import: years(2)

We want: a linear regression model for number of miles and number of deaths

Why do we want it: cool to see how many deaths there will be, seeing the amount of predicted mielage can tell us where to put our highway funding

When do we want it: now
"""

import pandas as pd 
years=pd.read_csv("years (2)")
years

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

#For crashes 
X_train_c=years
y_train_c=years["Crashes"]

col_c=make_column_transformer(
    (StandardScaler(),["Deaths","Motor vehicles",	"Mileage (thousands)"]),
    remainder="drop"
)
pipeline = make_pipeline(
    col_c,
    LinearRegression()
)
pipeline.fit(X_train_c,y_train_c)
y_preds = pipeline.predict(X_train_c)
y_preds

#For deaths 
X_train_d=years
y_train_d=years["Deaths"]

col_d=make_column_transformer(
    (StandardScaler(),["Crashes","Motor vehicles",	"Mileage (thousands)"]),
    remainder="drop"
)
pipeline = make_pipeline(
    col_d,
    LinearRegression()
)
pipeline.fit(X_train_d,y_train_d)
y_preds = pipeline.predict(X_train_d)
y_preds

#For number of motor vehicles  
X_train_v=years
y_train_v=years["Motor vehicles"]

col_v=make_column_transformer(
    (StandardScaler(),["Crashes","Mileage (thousands)"]),
    remainder="drop"
)
pipeline = make_pipeline(
    col_v,
    LinearRegression()
)
pipeline.fit(X_train_v,y_train_v)
y_preds = pipeline.predict(X_train_v)
y_preds

#For mileage  
X_train_m=years
y_train_m=years["Motor vehicles"]

col_m=make_column_transformer(
    (StandardScaler(),["Crashes","Motor vehicles"]),
    remainder="drop"
)
pipeline = make_pipeline(
    col_m,
    LinearRegression()
)
pipeline.fit(X_train_m, y_train_m)
y_preds = pipeline.predict(X_train_m)
y_preds