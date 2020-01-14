import cv2
import dlib
import numpy as np
import scipy.interpolate
from itertools import zip_longest
from skimage import color

eye_x=[]
eye_y=[]
lip_x = []
lip_y = []

lower_left_end = 5
upper_left_end = 9
lower_right_end = 14
upper_right_end = 18

def get_eyebrow_eyelids(landmarks):
    if landmarks is None:
            return None
    liner = ""
    for point in landmarks[17:22]:
        liner += str(point).replace('[', '').replace(']', '') + '\n'
    for point in landmarks[36:40]:
        liner += str(point).replace('[', '').replace(']', '') + '\n'
    liner += '\n'
    for point in landmarks[22:27]:
        liner += str(point).replace('[', '').replace(']', '') + '\n'
    for point in landmarks[42:46]:
        liner += str(point).replace('[', '').replace(']', '') + '\n'
    return liner

def apply_eyeshadow(img, liner, im_c, wt, ht, im, eyeshadow_color):
    global im_copy
    global image
    global imm
    global width    
    global height , red_e, green_e, blue_e
    imm = im
    im_copy = im_c
    width = wt
    height = ht
    image = img
    h = eyeshadow_color
    red_e, green_e, blue_e = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    liner = list([point.split() for point in liner.split('\n')])
    eyes_points= [item for sublist in liner for item in sublist]
    pebl,pel,pebr,per =__get_points_eyes(eyes_points)
    pebl = np.array(pebl)
    pel = np.array(pel)
    pebr = np.array(pebr)
    per = np.array(per)
    pebl_x,pebl_y, pel_x,pel_y, pebr_x,pebr_y, per_x,per_y=__get_curves_eyeshadow(pebl,pel,pebr,per)
    pebl_y_min=min(pebl_y)
    pel_y_max= max(pel_y)
    offset_left = pel_y_max - pebl_y_min
    pebl_y[0] += offset_left*0.4
    pebl_y[1] += offset_left*0.4
    pebl_y[2] += offset_left*0.4
    pebl_y[3] += offset_left*0.3
    pebl_y[4] += offset_left*0.8
    pel_y[0] += offset_left*0.0
    pebr_y_min = min(pebr_y)
    per_y_max = max(per_y)
    offset_right = per_y_max - pebr_y_min
    pebr_y[-1] += offset_right*0.4
    pebr_y[0] += offset_right*0.8
    pebr_y[1] += offset_right*0.3
    pebr_y[2] += offset_right*0.4
    pebr_y[3] += offset_right*0.4
    per_y[-1] += offset_right*0.0
    l_l=__draw_curve(pel_x[:],pel_y[:], 'cubic' )
    u_l = __draw_curve(pebl_x[:],pebl_y[:],'cubic')
    l_r = __draw_curve(pebr_x[:],pebr_y[:],'cubic')
    u_r = __draw_curve(per_x[:],per_y[:],'cubic')
    __fill_color(l_l, u_l, l_r, u_r)
    im_copy = cv2.cvtColor(im_copy, cv2.COLOR_BGR2RGB)
    return im_copy

def __get_points_eyes(lips_points):
    point_eyebrow_xy = []
    point_eye_xy = []
    point_eyebrow_xy_right = []
    point_eye_xy_right = []
    for i in range(0, 10, 2):
        point_eyebrow_xy.append([float(lips_points[i]), float(lips_points[i + 1])])
    for i in range(10, 18, 2):
        point_eye_xy.append([float(lips_points[i]), float(lips_points[i + 1])])
    for i in range(18, 28, 2):
        point_eyebrow_xy_right.append([float(lips_points[i]), float(lips_points[i + 1])])
    for i in range(28, 36, 2):
        point_eye_xy_right.append([float(lips_points[i]), float(lips_points[i + 1])])
    return point_eyebrow_xy, point_eye_xy, point_eyebrow_xy_right, point_eye_xy_right
 
def __get_curves_eyeshadow(pebl,pel,pebr,per): 
    pebl_curve_x = np.array((pebl[:5][:,0]))
    pebl_curve_y = np.array(pebl[:5][:,1])
    pel_curve_x = np.array(pel[:6][:,0])
    pel_curve_y = np.array(pel[:6][:,1])
    pebr_curve_x = np.array((pebr[:5][:,0]))
    pebr_curve_y = np.array(pebr[:5][:,1])
    per_curve_x = np.array((per[:6][:,0]))
    per_curve_y = np.array(per[:6][:,1])
    return pebl_curve_x, pebl_curve_y, pel_curve_x, pel_curve_y, pebr_curve_x, pebr_curve_y, per_curve_x, per_curve_y

  
def __draw_curve(x_pts = [], y_pts = [], k1='cubic' ):
    global debug
    debug=0
    
    curvex = []
    curvey = []    
    debug += 1
    
    curve = scipy.interpolate.interp1d(x_pts, y_pts, k1)
    if debug == 1 or debug == 2:
        for i in np.arange(x_pts[0], x_pts[len(x_pts) - 1] + 1, 1):
            curvex.append(int(i))
            curvey.append(int(curve(i)))
    else:
        for i in np.arange(x_pts[len(x_pts) - 1] + 1, x_pts[0], 1):
            curvex.append(int(i))
            curvey.append(int(curve(i)))
    return curvex, curvey

def __fill_lip_lines(outer, inner):
    outer_curve = zip(outer[0], outer[1])
    inner_curve = zip(inner[0], inner[1])
    count = len(inner[0]) - 1
    last_inner = [inner[0][count], inner[1][count]]
    for o_point, i_point in zip_longest(
            outer_curve, inner_curve, fillvalue=last_inner
        ):
        line = scipy.interpolate.interp1d(
                [o_point[0], i_point[0]], [o_point[1], i_point[1]], 'linear')
        xpoints = list(np.arange(o_point[0], i_point[0], 1))
        eye_x.extend(xpoints)
        eye_y.extend([int(point) for point in line(xpoints)])
    return

def __add_color(intensity):
    
    val = color.rgb2lab(
            (image[eye_x, eye_y] / 255.)
            .reshape(len(eye_x), 1, 3)
        ).reshape(len(eye_x), 3)

    L, A, bB = np.mean(val[:, 0]), np.mean(val[:, 1]), np.mean(val[:, 2])
    rgbmean = (image[eye_x,eye_y])
    rmean = np.mean(rgbmean[:,0])
    gmean = np.mean(rgbmean[:,1])
    bmean = np.mean(rgbmean[:,2])
    
    L,A,bB = color.rgb2lab(np.array((rmean/255.,gmean/255.,bmean/255.)).reshape(1,1,3)).reshape(3,)
    
    L1, A1, B1 = color.rgb2lab(
            np.array(
                    (red_e / 255., green_e / 255., blue_e / 255.)
                    ).reshape(1, 1, 3)
            ).reshape(3,)
    
    val[:,0] += (L1-L)*intensity
    val[:,1] += (A1-A)*intensity
    val[:,2] += (B1-bB)*intensity
    
    image_blank = imm
    image_blank *= 0
    image_blank[eye_x,eye_y] = color.lab2rgb(val.reshape(len(eye_x),1,3)).reshape(len(eye_x),3)*255
    
    original = color.rgb2lab((image[eye_x,eye_y]*0/255.).reshape(len(eye_x),1,3)).reshape(len(eye_x),3)

    tobeadded = color.rgb2lab((image_blank[eye_x,eye_y]/255.).reshape(len(eye_x),1,3)).reshape(len(eye_x),3)
    original += tobeadded
    image[eye_x,eye_y] = color.lab2rgb(original.reshape(len(eye_x),1,3)).reshape(len(eye_x),3)*255


def __fill_lip_solid(outer, inner):
    global red_e 
    global green_e 
    global blue_e 
    inner[0].reverse()
    inner[1].reverse()
    outer_curve = zip(outer[0], outer[1])
    inner_curve = zip(inner[0], inner[1])
    points = []
    for point in outer_curve:
        points.append(np.array(point, dtype=np.int32))
    for point in inner_curve:
        points.append(np.array(point, dtype=np.int32))
    points = np.array(points, dtype=np.int32)
    #colour is filled here 
    cv2.fillPoly(image, [points], (red_e,green_e, blue_e))
    

def __smoothen_color(outer, inner):
    global im_copy
    outer_curve = zip(outer[0], outer[1])
    inner_curve = zip(inner[0], inner[1])
    x_points = []
    y_points = []
    for point in outer_curve:
        x_points.append(point[0])
        y_points.append(point[1])
    for point in inner_curve:
        x_points.append(point[0])
        y_points.append(point[1])
    
    filter = np.zeros((height,width))
    
    cv2.fillConvexPoly(filter,np.array(np.c_[x_points, y_points],dtype = 'int32'),1)
    
    cv2.fillConvexPoly(filter,np.array(np.c_[x_points, y_points],dtype = 'int32'),1)
    
    filter = cv2.GaussianBlur(filter,(31,31),0)
    kernel = np.ones((12,12),np.uint8)
    filter = cv2.erode(filter,kernel,iterations = 1)
    alpha=np.zeros([height,width,3],dtype='float64')
    alpha[:,:,0]=filter
    alpha[:,:,1]=filter
    alpha[:,:,2]=filter
    im_copy =(alpha*image+(1-alpha)*im_copy).astype('uint8')

def __fill_color(pebl, pel, pebr, per):
    __fill_lip_lines(pebl, pel)
    __fill_lip_lines(pebr, per)
    __add_color(1)
    __fill_lip_solid(pebl, pel)
    __fill_lip_solid(pebr, per)
    __smoothen_color(pebl, pel)
    __smoothen_color(pebr, per)
 


