import os
import cv2
import detectLandmarks
import eyeShadow
import lips
import foundation
import eyeLiner
import faceBlush

def applyMakeup(userImage, data):
    
    # Colours in Hex
    fo=data['foundation']
    el= data['eyeliner']
    es= data['e_shadow']
    ls= data['lipstick']
    bl= data['blush']

    #should apply foundation if value found.
    applyFoundation = True if type(fo) is tuple else False
    applyEyeliner = True if type(el) is tuple else False
    applyEyeShadow = True if type(es) is tuple else False
    applyLipstick = True if type(ls) is tuple else False
    applyBlush = True if type(bl) is tuple else False
    
    #####READ IMAGE without makeup#####
    image= cv2.imread(userImage)
    imm=image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    im_copy = image.copy()
    height, width = image.shape[:2]

    #####FULL FACE LANDMARK DETECTION#####
    landmarks= detectLandmarks.get_landmarks(image)

    #APPLY EYESHADOW
    if applyEyeShadow:
        eyeshadow_color = es[2]
        e=eyeShadow.get_eyebrow_eyelids(landmarks)
        im_copy=eyeShadow.apply_eyeshadow(image, e, im_copy, width, height , imm, eyeshadow_color)
        im_copy = cv2.cvtColor(im_copy, cv2.COLOR_BGR2RGB)

    #####APPLY LIPSTICK#####
    if applyLipstick:
        lipstick_color = ls[2]
        l=lips.get_lips(landmarks) 
        image=lips.apply_lipstick(image, l, im_copy, width, height, lipstick_color)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        im_copy=image

    #####APPLY FOUNDATION#####
    if applyFoundation:
        foundation_color= fo[2]
        f=foundation.get_Face_Points(landmarks)
        image=foundation.apply_foundation(image,f, im_copy, landmarks, width, height, imm, foundation_color)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        im_copy=image

    #####APPLY EYELINER#####
    if applyEyeliner:
        eyeliner_color = el[2]
        e=eyeLiner.get_upper_eyelids(landmarks)
        image=eyeLiner.apply_liner(image, e, im_copy , eyeliner_color)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #####APPLY BLUSH#####
    if applyBlush:
        blush_color = bl[2]
        b=faceBlush.get_blush_landmark(landmarks)
        bb=faceBlush.blush_points_list(b)
        a=faceBlush.blush_points_list_xy(bb)
        lfx, lfy=faceBlush.get_xy_blush_points_separately(a)
        lcx, lcy=faceBlush.apply_blush(lfx, lfy, 0)
        rcx, rcy= faceBlush.apply_blush(lfx, lfy, 1)
        image=faceBlush.add_blush_color(lcx, lcy, rcx, rcy, image, height, width , blush_color)

    #####OUTPUT IMAGE WITH MAKEUP#####
    directoryPath = os.path.split(userImage)
    cv2.imwrite(directoryPath[0] + "\\result.jpg", image)