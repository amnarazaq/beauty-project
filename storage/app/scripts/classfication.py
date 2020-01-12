# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:32:38 2019

@author: DELL
"""
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from sklearn import svm
import numpy as np
import cv2
import os
from pylab import rcParams
from datetime import datetime


def training(dirc, img_size):
    training_data = []
    CATEGORIES=["white_tan/","extremely_fair/","fair_redspot/", "natural_redspot/","natural/","black_brown/","brown/","dark_brown/","fair/" ,"natural_white/" ]
    for category in CATEGORIES: 
        path=os.path.join(dirc,category)
        
        class_num=CATEGORIES.index(category)
        
        for img in os.listdir(path):
            try:
                img_array=cv2.imread(os.path.join(path , img) , cv2.IMREAD_GRAYSCALE)
                new_img=cv2.resize(img_array ,(img_size,img_size))
                training_data.append((new_img,class_num)) # strore this train data in database or file.
                
        
            except Exception as e:
                  print("exception", e,img)

    return training_data

def classification(dirc, myimage):
    print("Classification starts: ")
    print(datetime.now())
    np.printoptions(precision=4 ,suppress=True)
    #matplotlib inline
    rcParams['figure.figsize']=7,4
    test_data=r""+myimage;

    img_size=400
    training_data=training(dirc, img_size)

    print("training end ") 
    print(datetime.now())

    img=cv2.imread(test_data ,  cv2.IMREAD_GRAYSCALE)
    n_img=cv2.resize(img ,(img_size,img_size))
    #dimension=n_img.shape

    xs=[]
    yt=[]
    for i in range(len(training_data)):
        xs.append(training_data[i][0])
        yt.append(training_data[i][1])


    xs=np.array(xs)
    yt=np.array(yt)

    nsamples, nx, ny = xs.shape
    xs = xs.reshape((nsamples,nx*ny))

    y_train=n_img

    y_train = np.array(y_train)

    nx1, ny1 = y_train.shape
    y_train=y_train.reshape((1,nx1*ny1))

    y_train=np.expand_dims(y_train,axis=1)

    print("SVM Starts: ")
    print(datetime.now())
    clf=svm.SVC()
    clf.fit(xs,yt)
    y_pred = clf.predict(y_train[0])
    
    y_pred=np.array(y_pred)
    print("SVM End: ") 
    print( datetime.now())

    return y_pred