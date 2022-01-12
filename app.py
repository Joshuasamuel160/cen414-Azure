from flask import Flask, redirect, render_template
from pymongo import MongoClient

import pandas as pd
import os
import numpy as np
from plots import *

app =  Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    context = {2010:[], 2011:[], 2012:[], 2013:[], 2014:[], 2015:[], 2016:[], 2017:[], 2018:[], 2019:[]}
    df = pd.read_csv('AFRICANDATA.csv')
    
    
    #generate plots
    for i in range(2010,2019):    
        print(f"\nFOR {i}")
        print("Standard Deviation:") 
        standard_deviation = df[f'{i}'].std()
        print("VARIANCE:")
        variance = df[f'{i}'].var()
        print("RANGE:")
        rang = (df[f'{i}'].max())-(df[f'{i}'].min())
    
        context[i] = [standard_deviation, variance, rang]
    
    return render_template('index.html', context=context)


@app.route('/refresh_plots', methods=['GET'])
def refresh_plots():

    #connect to db

    
    #get and mutate dataframe 
    df = pd.read_csv('AFRICANDATA.csv')

    
    #generate plots
    for i in range(2010,2019):    
        print(f"\nFOR {i}")
        print("Standard Deviation:") 
        print(df[f'{i}'].std())
        print("VARIANCE:")
        print(df[f'{i}'].var())
        print("RANGE:")
        print((df[f'{i}'].max())-(df[f'{i}'].min()))

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)