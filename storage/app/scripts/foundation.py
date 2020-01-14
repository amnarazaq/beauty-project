
import cv2
import numpy as np
import scipy.interpolate
from skimage import color
from scipy.interpolate import InterpolatedUnivariateSpline
from numpy.linalg import eig, inv

up_left_end = 3
up_right_end = 5

inten=0.2

def get_Face_Points(landmarks):
   if landmarks is None:
       return None
   face = ""
   for point in landmarks[0:17]:
       face += str(point).replace('[', '').replace(']', '') + '\n'
   return face

def get_eyebrow_eyelids(landmarks):
    if landmarks is None:
            return None
    liner = ""
    # Points of  Right Eyebrow and Eyelid
    for point in landmarks[17:22]:
        liner += str(point).replace('[', '').replace(']', '') + '\n'
    for point in landmarks[36:42]:
        liner += str(point).replace('[', '').replace(']', '') + '\n'
    liner += '\n'
    # Points of  Right Eyebrow and Eyelid
    for point in landmarks[22:27]:
        liner += str(point).replace('[', '').replace(']', '') + '\n'
    for point in landmarks[42:48]:
        liner += str(point).replace('[', '').replace(']', '') + '\n'
    return liner

def get_lips(landmarks):
   if landmarks is None:
       return None
   lips = ""
   for point in landmarks[48:60]:
       lips += str(point).replace('[', '').replace(']', '') + '\n'
   return lips


def get_list_face_points(face):
    face = list([point.split() for point in face.split('\n')])
    face_points= [item for sublist in face for item in sublist]
    return face_points

def get_list_eye_points(eye):
    eye = list([point.split() for point in eye.split('\n')])
    eyes_points= [item for sublist in eye for item in sublist]
    return eyes_points

def get_list_lips_points(lip):
    lip = list([point.split() for point in lip.split('\n')])
    lip_points = [item for sublist in lip for item in sublist]
    return lip_points

def get_f_points(f_p):
    fp=[]
    for i in range(0, 34, 2):
        fp.append([float(f_p[i]), float(f_p[i + 1])])
    return fp

def get_e_points(e_p):
    pebl=[]
    pel=[]
    pebr=[]
    per=[]
    for i in range(0, 10, 2):
        pebl.append([float(e_p[i]), float(e_p[i + 1])])
    for i in range(10, 22, 2):
        pel.append([float(e_p[i]), float(e_p[i + 1])])
    for i in range(22, 32, 2):
        pebr.append([float(e_p[i]), float(e_p[i + 1])])
    for i in range(32, 44, 2):
        per.append([float(e_p[i]), float(e_p[i + 1])])
    return pebl,pel, pebr, per

def get_l_points(l_p):
    uol=[]
    uil=[]
    for i in range(0, 14, 2):
        uol.append([float(l_p[i]), float(l_p[i + 1])])
    for i in range(14, 24, 2):
        uil.append([float(l_p[i]), float(l_p[i + 1])])
    return uol,uil

def get_xy_face_points_separately(points):
    x_pts = []
    y_pts = []
    for point in points:
        x_pts.append(point[0])
        y_pts.append(point[1])
    return x_pts, y_pts      

def get_xy_eyes_points_separately(pebl, pel, pebr, per):
    peblx_pts = []
    pebly_pts = []
    pelx_pts = []
    pely_pts = []
    pebrx_pts = []
    pebry_pts = []
    perx_pts = []
    pery_pts = []
    for point in pebl:
        peblx_pts.append(point[0])
        pebly_pts.append(point[1])
    for point in pel:
        pelx_pts.append(point[0])
        pely_pts.append(point[1])
    for point in pebr:
        pebrx_pts.append(point[0])
        pebry_pts.append(point[1])
    for point in per:
        perx_pts.append(point[0])
        pery_pts.append(point[1])
    
    return peblx_pts, pebly_pts, pelx_pts, pely_pts, pebrx_pts, pebry_pts, perx_pts, pery_pts 

def get_xy_lips_points_separately(points):
    x_pts = []
    y_pts = []
    for point in points:
        x_pts.append(point[0])
        y_pts.append(point[1])
    return x_pts, y_pts    
  
####FACE FUNCTIONS####
def univariate_plot(lx=[],ly=[]):
    unew = np.arange(lx[0], lx[-1]+1, 1)
    f2 = InterpolatedUnivariateSpline(lx, ly)
    return unew,f2(unew)

def fitEllipse(x,y):
    x = x[:,np.newaxis]
    y = y[:,np.newaxis]
    D =  np.hstack((x*x, x*y, y*y, x, y, np.ones_like(x)))
    S = np.dot(D.T,D)
    C = np.zeros([6,6])
    C[0,2] = C[2,0] = 2; C[1,1] = -1
    E, V =  eig(np.dot(inv(S), C))
    n = np.argmax(np.abs(E))
    a = V[:,n]
    return a

def ellipse_center(a):
    b,c,d,f,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[0]
    num = b*b-a*c
    x0=(c*d-b*f)/num
    y0=(a*f-b*d)/num
    return np.array([x0,y0])

def ellipse_angle_of_rotation( a ):
    b,c,a = a[1]/2, a[2],  a[0]
    return 0.5*np.arctan(2*b/(a-c))

def ellipse_axis_length( a ):
    b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
    up = 2*(a*f*f+c*d*d+g*b*b-2*b*d*f-a*c*g)
    down1=(b*b-a*c)*( (c-a)*np.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
    down2=(b*b-a*c)*( (a-c)*np.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
    res1=np.sqrt(up/down1)
    res2=np.sqrt(up/down2)
    return np.array([res1, res2])

def getEllipse(x,y):
    arc = 0.8
    R = np.arange(0,arc*np.pi, 0.01)
    a = fitEllipse(x,y)
    center = ellipse_center(a)
    phi = ellipse_angle_of_rotation(a)
    axes = ellipse_axis_length(a)
    return (center[0],center[1]),(axes[0],axes[1]/1.3),phi

def getBoundaryPoints(x , y):
    tck,u = scipy.interpolate.splprep([x, y], s=0, per=1)
    unew = np.linspace(u.min(), u.max(), 10000)
    xnew,ynew = scipy.interpolate.splev(unew, tck, der=0)
    tup = np.c_[xnew.astype(int),ynew.astype(int)].tolist()
    coord = list(set(tuple(map(tuple, tup))))
    coord = np.array([list(elem) for elem in coord])
    return coord[:,0],coord[:,1]

def getInteriorPoints(x , y):
    intx = []
    inty = []
    def ext(a, b, i):
     a, b=round(a), round(b)
     intx.extend(list(np.arange(a, b, 1)))
     a=int(a)
     b=int(b)
     inty.extend(list(np.ones(b-a)*i))
    x, y = np.array(x), np.array(y)
    xmin, xmax = np.amin(x), np.amax(x)
    xrang = np.arange(xmin, xmax+1, 1)
    for i in xrang:
     ylist = y[np.where(x==i)]
     ext(np.amin(ylist), np.amax(ylist), i)
    return intx, inty


#####LIPS FUNCTIONS######
def inter_plot(lx=[],ly=[],k1='quadratic'):
    unew = np.arange(lx[0], lx[-1]+1, 1)
    f2 = scipy.interpolate.interp1d(lx, ly, kind=k1)
    return unew,f2(unew)


#####colur fill FUNCTIONS####

def checkForSkin(IMG10):
    high,widt=IMG10.shape[:2]

    B1=np.reshape(np.float32(IMG10[:,:,0]),high*widt)#B
    G1=np.reshape(np.float32(IMG10[:,:,1]),high*widt)#G
    R1=np.reshape(np.float32(IMG10[:,:,2]),high*widt)#Rs

    h3=np.zeros((high,widt,3),np.uint8)

    tem=np.logical_and(np.logical_and(np.logical_and(np.logical_and(R1 > 95, G1 > 40),np.logical_and(B1 > 20, (np.maximum(np.maximum(R1,G1),B1) - np.minimum(np.minimum(R1,G1),B1)) > 15)),R1>B1),np.logical_and(np.absolute(R1-G1) > 15,R1>G1))
    h5=np.array(tem).astype(np.uint8,order='C',casting='unsafe')

    h5=np.reshape(h5,(high,widt))
    h3[:,:,0]=h5
    h3[:,:,1]=h5
    h3[:,:,2]=h5
    kernel1 = np.ones((3,3),np.uint8)
    closedH3=np.copy(h3)
    for i in range(5):
        closedH3 = cv2.erode(closedH3,kernel1)
    for i in range(5):
        closedH3 = cv2.dilate(closedH3,kernel1)
    return closedH3

def __add_color(intensity):
    global x_aux 
    x_aux= []
    global y_aux 
    y_aux= []
    global image
    val = color.rgb2lab(
            (image[x, y] / 255.)
            .reshape(len(x), 1, 3)
        ).reshape(len(x), 3)
    
    x_aux=np.array(x_aux)
    y_aux=np.array(y_aux)
    x_aux=x_aux.astype(int)
    y_aux=y_aux.astype(int)
    
    vallips = color.rgb2lab((image[x_aux,y_aux]/255.).reshape(len(x_aux),1,3)).reshape(len(x_aux),3)
    
    L = (sum(val[:,0])-sum(vallips[:,0]))/(len(val[:,0])-len(vallips[:,0]))
    A = (sum(val[:,1])-sum(vallips[:,1]))/(len(val[:,1])-len(vallips[:,1]))
    bB = (sum(val[:,2])-sum(vallips[:,2]))/(len(val[:,2])-len(vallips[:,2]))
    
    L1,A1,B1 = color.rgb2lab(np.array((R/255.,G/255.,B/255.)).reshape(1,1,3)).reshape(3,)
    val[:,0] += (L1-L)*intensity
    val[:,1] += (A1-A)*intensity
    val[:,2] += (B1-bB)*intensity

    image[x, y] = color.lab2rgb(val.reshape(
            len(x), 1, 3)).reshape(len(x), 3) * 255
    
    scale = min(width/750, height/1000)
    
    # Blur Filter
    filter = np.zeros((height, width))
    cv2.fillConvexPoly(filter, np.array(np.c_[y, x], dtype='int32'), 1)
    
    sigma = (int(int(201 * scale)/2)*2) + 1

    filter = cv2.GaussianBlur(filter, (sigma,sigma), 0)
    
    # Erosion to reduce blur size
    kernel_size = int(12 * scale)
    kernel = np.ones((kernel_size,kernel_size),np.uint8)
    filter = cv2.erode(filter,kernel,iterations = 4)
    
    alpha=np.zeros([height,width,3],dtype='float64')
    alpha[:,:,0]=filter
    alpha[:,:,1]=filter
    alpha[:,:,2]=filter
    
    immask = imm
    skinalpha = checkForSkin(immask)
    
    image = (alpha*image+(1-alpha)*im_copy).astype('uint8')
    image = ((skinalpha)*image+(1-(skinalpha))*im_copy).astype('uint8')
    return image

def apply_foundation(imag, face_pts , im_c, landmarks, wt, ht, img, foundation_color):
    global im_copy , width, height,  imm, image
    global x_aux, y_aux , R, G, B
    global x,y
    x_aux=[]
    y_aux=[]
    x_face=[]
    y_face=[]
    x=[]
    y=[]
    image= imag
    im_copy= im_c
    height= ht
    width= wt
    imm= img
    h = foundation_color
    R, G, B = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    lfp=get_list_face_points(face_pts)
    fg =get_f_points(lfp)
    fx, fy=get_xy_face_points_separately(fg)
    fx=sorted(fx)
    fx=np.array(fx)
    fy=np.array(fy)
    #lower face points
    lower_face = univariate_plot(fx[:],fy[:])
    x_face.extend(lower_face[0][::-1])
    y_face.extend(lower_face[1][::-1])
    #upper face approximation
    (centerx,centery),(axesx,axesy),angel = getEllipse(fx,fy)
    (centerx,centery),(axesx,axesy),angel = getEllipse(fx,fy)
    centerpt = (int(centerx),int(centery))
    axeslen = (int(axesx),int(axesy*1.2))
    ellippoints = cv2.ellipse2Poly(centerpt,axeslen,int(angel),180,360,1)
    ellippoints = np.floor(ellippoints)
    ellipseabs = ellippoints[:,0].tolist()
    ellipseord = ellippoints[:,1].tolist()
    x_face.extend(ellipseabs)
    y_face.extend(ellipseord)
    x_face.append(x_face[0])
    y_face.append(y_face[0])
    x_face, y_face = getBoundaryPoints(x_face, y_face)
    x, y = getInteriorPoints(x_face, y_face)
    x=np.array(x)
    y=np.array(y)
    x=x.astype(int)
    y=y.astype(int)
    ######lips########
    l=get_lips(landmarks)
    llp=get_list_lips_points(l)
    uol, uil =get_l_points(llp)
    uolx, uoly=get_xy_lips_points_separately(uol)
    uilx, uily=get_xy_lips_points_separately(uil)
    uolx=np.array(uolx)
    uoly=np.array(uoly)
    uilx=np.array(uilx)
    uily=np.array(uily)
    l_u_l = inter_plot(uolx[:],uoly[:], 'quadratic')
    uilx= sorted(uilx)
    uily=sorted(uily)
    l_u_r = inter_plot(uilx[:],uily[:], 'quadratic')
    l_l = inter_plot(list(uolx[:]),list(uoly[:]),'cubic')
    lipinteriorx, lipinteriory = getInteriorPoints((list(l_u_l[0])) + (list(l_u_r[0])) + (list(l_l[0])), (list(l_u_l[1])) + (list(l_u_r[1])) + (list(l_l[1])))
    x_aux=list(x_aux)
    x_aux.extend(lipinteriorx)
    y_aux=list(y_aux)
    y_aux.extend(lipinteriory)
    #####EYES####
    e=get_eyebrow_eyelids(landmarks)
    lep=get_list_eye_points(e)
    pebl,pel, pebr, per =get_e_points(lep)
    peblx, pebly, pelx, pely, pebrx, pebry, perx, pery=get_xy_eyes_points_separately(pebl, pel, pebr, per)
    peblx=np.array(peblx)
    pebly=np.array(pebly)
    pelx=np.array(pelx)
    pely=np.array(pely)
    pebrx=np.array(pebrx)
    pebry=np.array(pebry)
    perx=np.array(perx)
    pery=np.array(pery)
    e_l_l = inter_plot(peblx[:],pebly[:], 'cubic')
    pelx=sorted(pelx)
    pely=sorted(pely)
    pelx=np.array(pelx)
    pely=np.array(pely)
    e_u_l = inter_plot(pelx[:],pely[:],'linear')
    lefteyex, lefteyey = getInteriorPoints(list(e_l_l[0]) + list(e_u_l[0]), list(e_l_l[1]) + list(e_u_l[1]))
    x_aux.extend(lefteyex)
    y_aux.extend(lefteyey)
    e_l_r = inter_plot(pebrx[:],pebry[:],'cubic')
    perx=sorted(perx)
    pery=sorted(pery)
    perx=np.array(perx)
    pery=np.array(pery)
    e_u_r = inter_plot(perx[:],pery[:],'linear')
    righteyex, righteyey = getInteriorPoints(e_l_r[0].tolist() + e_u_r[0].tolist(), e_l_r[1].tolist() + e_u_r[1].tolist())
    x_aux.extend(righteyex)
    y_aux.extend(righteyey)
    image= __add_color(inten)    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image