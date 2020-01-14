import cv2
import numpy as np
from itertools import zip_longest
import scipy.interpolate
from skimage import color

debug=0
lip_x = []
lip_y = []

#get lips landmark points
def get_lips(landmarks):
   if landmarks is None:
       return None
   lips = ""
   for point in landmarks[48:]:
       lips += str(point).replace('[', '').replace(']', '') + '\n'
   return lips

#apply lipstick
def apply_lipstick(im, lips, imc, ht, wt, lipstick_color):
    global image, width, height
    global im_copy , red_l, green_l, blue_l
    im_copy=imc
    image=im
    height=ht
    width=wt
    h=lipstick_color
    red_l, green_l, blue_l = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    lips = list([point.split() for point in lips.split('\n')])
    lips_points = [item for sublist in lips for item in sublist]
    a, e, f, c =__get_points_lips(lips_points)
    dd, ds, df, dh=__get_curves_lips(a, e, f, c)
    __fill_color(dd, ds, df, dh)
    im_copy = cv2.cvtColor(im_copy, cv2.COLOR_BGR2RGB)
    return im_copy
  
def __get_points_lips(lips_points):
    uol = []
    uil = []
    lol = []
    lil = []
    for i in range(0, 14, 2):
        uol.append([int(lips_points[i]), int(lips_points[i + 1])])
    for i in range(12, 24, 2):
        lol.append([int(lips_points[i]), int(lips_points[i + 1])])
    lol.append([int(lips_points[0]), int(lips_points[1])])
    for i in range(24, 34, 2):
        uil.append([int(lips_points[i]), int(lips_points[i + 1])])
    for i in range(32, 40, 2):
        lil.append([int(lips_points[i]), int(lips_points[i + 1])])
    lil.append([int(lips_points[24]), int(lips_points[25])])
    return uol, uil, lol, lil

def __get_curves_lips(uol, uil, lol, lil):
    uol_curve = __draw_curve(uol)
    uil_curve = __draw_curve(uil)
    lol_curve = __draw_curve(lol)
    lil_curve = __draw_curve(lil)
    return uol_curve, uil_curve, lol_curve, lil_curve

def __draw_curve(points):
    global debug
    x_pts = []
    y_pts = []
    curvex = []
    curvey = []    
    debug += 1
    for point in points:
        x_pts.append(point[0])
        y_pts.append(point[1])
    curve = scipy.interpolate.interp1d(x_pts, y_pts, 'cubic')
    if debug == 1 or debug == 2:
        for i in np.arange(x_pts[0], x_pts[len(x_pts) - 1] + 1, 1):
            curvex.append(i)
            curvey.append(int(curve(i)))
    else:
        for i in np.arange(x_pts[len(x_pts) - 1] + 1, x_pts[0], 1):
            curvex.append(i)
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
        lip_x.extend(xpoints)
        lip_y.extend([int(point) for point in line(xpoints)])
    return
 
def __add_color(intensity):
    val = color.rgb2lab(
            (image[lip_y, lip_x] / 255.)
            .reshape(len(lip_y), 1, 3)
        ).reshape(len(lip_y), 3)
    l_val, a_val, b_val = np.mean(val[:, 0]), np.mean(val[:, 1]), np.mean(val[:, 2])
    l1_val, a1_val, b1_val = color.rgb2lab(
            np.array(
                    (red_l / 255., green_l / 255., blue_l / 255.)
                    ).reshape(1, 1, 3)
            ).reshape(3,)
    l_final, a_final, b_final = (l1_val - l_val) * \
         intensity, (a1_val - a_val) * \
         intensity, (b1_val - b_val) * intensity
    val[:, 0] = np.clip(val[:, 0] + l_final, 0, 100)
    val[:, 1] = np.clip(val[:, 1] + a_final, -127, 128)
    val[:, 2] = np.clip(val[:, 2] + b_final, -127, 128)
    image[lip_y, lip_x] = color.lab2rgb(val.reshape(
            len(lip_y), 1, 3)).reshape(len(lip_y), 3) * 255

def __fill_lip_solid(outer, inner):
    global red_l 
    global green_l 
    global blue_l 
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
                    #apply colour 
    cv2.fillPoly(image, [points], (red_l, green_l, blue_l))


def __smoothen_color(outer, inner):
    global im_copy
    global height
    global width
    height, width = image.shape[:2]
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
    img_base = np.zeros((height, width))
    cv2.fillConvexPoly(img_base, np.array(np.c_[x_points, y_points], dtype='int32'), 1)
    img_mask = cv2.GaussianBlur(img_base, (81, 81), 0)
    img_blur_3d = np.ndarray([height, width, 3], dtype='float')
    img_blur_3d[:, :, 0] = img_mask
    img_blur_3d[:, :, 1] = img_mask
    img_blur_3d[:, :, 2] = img_mask
    im_copy = (img_blur_3d * image * 0.7 + (1 - img_blur_3d * 0.7) * im_copy).astype('uint8')
  
def __fill_color(uol_c, uil_c, lol_c, lil_c):
    __fill_lip_lines(uol_c, uil_c)
    __fill_lip_lines(lol_c, lil_c)
    __add_color(1)
    __fill_lip_solid(uol_c, uil_c)
    __fill_lip_solid(lol_c, lil_c)
    __smoothen_color(uol_c, uil_c)
    __smoothen_color(lol_c, lil_c)
    
