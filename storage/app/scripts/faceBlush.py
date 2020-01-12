import scipy.interpolate
from skimage import color
import cv2
import numpy as np

def get_blush_landmark(landmarks):
    if landmarks is None:
       return None
    blush = ""
        #Points of Left Cheek
    for point in landmarks[15:16]:
       blush += str(point).replace('[', '').replace(']', '') + '\n'
    for point in landmarks[35:36]:
       blush += str(point).replace('[', '').replace(']', '') + '\n'
        #Points of Right Cheek
    for point in landmarks[1:2]:
       blush += str(point).replace('[', '').replace(']', '') + '\n'  
    for point in landmarks[31:32]:
       blush += str(point).replace('[', '').replace(']', '') + '\n'
    return blush

def blush_points_list(lips):
    lips = list([point.split() for point in lips.split('\n')])
    lips_points = [item for sublist in lips for item in sublist]
    return lips_points

def blush_points_list_xy(lips_points):
    lc = []
    for i in range(0, 8, 2):
        lc.append([float(lips_points[i]), float(lips_points[i + 1])])
    lc.append([int(lips_points[0]), int(lips_points[1])])
    return lc

def get_xy_blush_points_separately(lcp):
    lcpx = []
    lcpy = []
    for point in lcp:
        lcpx.append(point[0])
        lcpy.append(point[1]) 
    return lcpx, lcpy

def get_blush_boundary_points(x, y):
    tck, u = scipy.interpolate.splprep([x, y], s=0, per=1)
    unew = np.linspace(u.min(), u.max(), 1000)
    xnew, ynew = scipy.interpolate.splev(unew, tck, der=0)
    tup = np.c_[xnew.astype(int), ynew.astype(int)].tolist()
    coord = list(set(tuple(map(tuple, tup))))
    coord = np.array([list(elem) for elem in coord])
    return np.array(coord[:, 0], dtype=np.int32), np.array(coord[:, 1], dtype=np.int32)

def add_blush_color(lx, ly, rx, ry, image, ht, wt, blush_color):
    global imOrg
    global height
    global width , Rg, Gg, Bg
    intensity = 0.3
    imOrg= image
    height= ht
    width= wt
    h=blush_color
    Rg, Gg, Bg = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    # Create blush shape
    mask = np.zeros((height, width))

    cv2.fillConvexPoly(mask, np.array(np.c_[lx, ly], dtype='int32'), 1)
    cv2.fillConvexPoly(mask, np.array(np.c_[rx, ry], dtype='int32'), 1)
    mask = cv2.GaussianBlur(mask, (51, 51), 0) * intensity

    # Add blush color to image
    val = cv2.cvtColor(imOrg, cv2.COLOR_RGB2LAB).astype(float)
    val[:, :, 0] = val[:, :, 0] / 255. * 100.
    val[:, :, 1] = val[:, :, 1] - 128.
    val[:, :, 2] = val[:, :, 2] - 128.
    LAB = color.rgb2lab(np.array((Rg / 255., Bg / 255., Gg / 255.)).reshape(1, 1, 3)).reshape(3,)

    mean_val = np.mean(np.mean(val, axis=0), axis = 0)
    mask = np.array([mask,mask,mask])
    mask = np.transpose(mask, (1,2,0))
    lab = np.multiply((LAB - mean_val), mask)

    val[:, :, 0] = np.clip(val[:, :, 0] + lab[:,:,0], 0, 100)
    val[:, :, 1] = np.clip(val[:, :, 1] + lab[:,:,1], -127, 128)
    val[:, :, 2] = np.clip(val[:, :, 2] + lab[:,:,2], -127, 128)

    imOrg = (color.lab2rgb(val) * 255).astype(np.uint8)
    imOrg = cv2.cvtColor(imOrg, cv2.COLOR_BGR2RGB)
    return imOrg

def apply_blush(lfx, lfy, flag):
    pointsx=[]
    pointsy=[]
        #For Left Cheek  
    if flag==0:
        lr= (lfx[0]-lfx[1] ) / 3.5 

        lcenter= (((lfx[0]+lfx[1] ) / 2.0), ((lfy[0]+lfy[1] ) / 2.0))
        #For Right Cheek 
    if flag==1:
        lr= (lfx[2]-lfx[3] ) / 3.5 

        lcenter= (((lfx[2]+lfx[3] ) / 2.0), ((lfy[2]+lfy[3] ) / 2.0))
        
    pointsx.append(lcenter[0] - lr)
    pointsy.append(lcenter[1])
    pointsx.append(lcenter[0])
    pointsy.append(lcenter[1] - lr)
    pointsx.append(lcenter[0] + lr)
    pointsy.append(lcenter[1])
    pointsx.append(lcenter[0])
    pointsy.append(lcenter[1] + lr)
    pointsx.append(lcenter[0] - lr)
    pointsy.append(lcenter[1])
    pointsx=np.array(pointsx)
    pointsy=np.array(pointsy)
    abx, aby =get_blush_boundary_points(pointsx, pointsy)
    return abx, aby