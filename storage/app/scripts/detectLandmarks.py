import cv2
import numpy as np
import dlib
import os

PREDICTOR_PATH=os.path.dirname(os.path.abspath(__file__)) + "\\shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(PREDICTOR_PATH)
detector= dlib.get_frontal_face_detector()

class TooManyFaces(Exception):
    pass
class NoFcaes(Exception):
    pass

def get_landmarks(im):
    rects= detector(im, 1)
    if len(rects)>1:
        raise TooManyFaces
    if len(rects)==0:
        raise NoFcaes
    return np.matrix([[p.x,p.y]for p in predictor (im,rects[0]).parts()])

def annotate_landmarks(im,landmarks):
    for idx , point in enumerate(landmarks):
        pos=(point[0,0],point[0,1])
        cv2.putText(im,str(idx),pos,
                    fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                    fontScale=0.4,
                    color = (0,0,255))
        cv2.circle(im,pos,3,color=(0,255,255))
    return im
