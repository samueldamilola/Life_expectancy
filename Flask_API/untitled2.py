# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:21:33 2021

@author: lenovo
"""


import requests
from data_input import data_in

URL =  'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL, json = data, headers = headers)

r.json()  