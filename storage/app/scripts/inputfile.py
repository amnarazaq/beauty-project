# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:19:36 2019

@author: DELL
"""

import sys
import pymysql
import pymysql.cursors
import json
from classfication import classification
from casual  import casual
from party  import party
from bridal  import bridal
from applyMakeup import applyMakeup


data = []
data.append(sys.argv[1])
data.append(sys.argv[2])
data.append(sys.argv[3])
data.append(sys.argv[4])

print('Passed Arguments are: \n')
print('ImagePath: ' + data[0])
print('MakeupType: ' + data[1])
print('DressColorHex: ' + data[2])
print('path: ' + data[3])

#Database Connection
conn=pymysql.connect( host='127.0.0.1' , user='root' , password='', db='beauty')


#commented this for testing purpose.
y_pred = classification(data[3] ,data[0])
#y_pred = [0]

learnedColors = {}
if data[1] =="bridal":
   learnedColors = bridal(conn, y_pred, data[2])
if data[1] =="casual":
    learnedColors = casual(conn, y_pred, data[2])
if data[1] =="party":
   learnedColors = party(conn, y_pred, data[2])
applyMakeup(data[0], learnedColors)

print(json.dumps(learnedColors))
