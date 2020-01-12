import cv2
import numpy as np
import scipy.interpolate

def get_upper_eyelids(landmarks):
    if landmarks is None:
            return None
    liner = ""
    for point in landmarks[36:40]:
        liner += str(point).replace('[', '').replace(']', '') + '\n'
    liner += '\n'
    for point in landmarks[42:46]:
        liner += str(point).replace('[', '').replace(']', '') + '\n'
    return liner

def apply_liner(im, liner, imc , eyeliner_color):
    global image
    global im_copy , red_e, green_e, blue_e
    im_copy=imc
    image=im
    h=eyeliner_color
    red_e, green_e, blue_e = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    liner = list([point.split() for point in liner.split('\n')])
    eyes_points= [item for sublist in liner for item in sublist]
    d, v=__create_eye_liner(eyes_points)
    __draw_liner(d, 'left')
    __draw_liner(v, 'right')
    im_copy = cv2.cvtColor(im_copy, cv2.COLOR_BGR2RGB)
    return im_copy

def __draw_liner(eye, kind):
    global red_e
    global green_e
    global blue_e
    eye_x = []
    eye_y = []
    x_points = []
    y_points = []
    for point in eye:
        x_points.append(int(point[0]))
        y_points.append(int(point[1]))
    curve = scipy.interpolate.interp1d(x_points, y_points, 'quadratic')
    for point in np.arange(x_points[0], x_points[len(x_points) - 1] + 1, 1):
        eye_x.append(point)
        eye_y.append(int(curve(point)))
    if kind == 'left':
        y_points[0] -= 1
        y_points[1] -= 1
        y_points[2] -= 1
        x_points[0] -= 5
        x_points[1] -= 1
        x_points[2] -= 1
        curve = scipy.interpolate.interp1d(x_points, y_points, 'quadratic')
        count = 0
        for point in np.arange(x_points[len(x_points) - 1], x_points[0], -1):
            count += 1
            eye_x.append(point)
            if count < (len(x_points) / 2):
                eye_y.append(int(curve(point)))
            elif count < (2 * len(x_points) / 3):
                 eye_y.append(int(curve(point)) - 1)
            elif count < (4 * len(x_points) / 5):
                eye_y.append(int(curve(point)) - 2)
            else:
                eye_y.append(int(curve(point)) - 3)
    elif kind == 'right':
        x_points[3] += 5
        x_points[2] += 1
        x_points[1] += 1
        y_points[3] -= 1
        y_points[2] -= 1
        y_points[1] -= 1
        curve = scipy.interpolate.interp1d(x_points, y_points, 'quadratic')
        count = 0
        for point in np.arange(x_points[len(x_points) - 1], x_points[0], -1):
            count += 1
            eye_x.append(point)
            if count < (len(x_points) / 2):
                eye_y.append(int(curve(point)))
            elif count < (2 * len(x_points) / 3):
                eye_y.append(int(curve(point)) - 1)
            elif count < (4 * len(x_points) / 5):
                eye_y.append(int(curve(point)) - 2)
            elif count:
                eye_y.append(int(curve(point)) - 3)
    curve = zip(eye_x, eye_y)
    points = []
    for point in curve:
        points.append(np.array(point, dtype=np.int32))
    points = np.array(points, dtype=np.int32)
    cv2.fillPoly(im_copy, [points], (red_e, green_e, blue_e))
    return

def __create_eye_liner(eyes_points):
    left_eye=[]
    right_eye=[]
    for i in range (0, 8, 2):
        left_eye.append([int(eyes_points[i]), int(eyes_points[i + 1])])
    for i in range (8, 16, 2):
        right_eye.append([int(eyes_points[i]), int(eyes_points[i + 1])])
    return left_eye,right_eye
