#-*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import cv2
import numpy as np

'''
    template matching
    ref https://opencv-python.readthedocs.io/en/latest/doc/24.imageTemplateMatch/imageTemplateMatch.html
    
'''


def show_img(compareImg):

    img = cv2.imread('2.jpg', 1)
    cap = cv2.VideoCapture('full.mp4')


    cv2.namedWindow("movie", cv2.WINDOW_NORMAL)
    cv2.namedWindow("compare_jpg", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("movie", 752, 512)
    cv2.resizeWindow("compare_jpg", 752, 512)

    
    count = 0
    while(True):
    # Capture frame-by-frame
        ret, frame = cap.read()
        count = count +1    
        
        cv2.imshow('movie',frame)
        cv2.imshow('compare_jpg',img)
        if count % 30 == 0 :
            print 'img compare'
            compare_img(frame, img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()




def compare_img() :
    #img_rgb = cv2.imread('mario.png')

    #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #template = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img1 = cv2.imread('messi.jpg',cv2.IMREAD_GRAYSCALE)
    img2 = img1.copy()
    
    template = cv2.imread('messi_face.jpg', cv2.IMREAD_GRAYSCALE)
    w, h = img1.shape[::-1]
    print w
    print h


    w, h = template.shape[::-1]
    print w
    print h
    
    methods = ['cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED',
               'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img1 = img2.copy()
        method = eval(meth)

        try :
            res = cv2.matchTemplate(img1, template, method)
            min_val, max_val, min_loc, max_loc, =cv2.minMaxLoc(res)
            print 'min_val', min_val
            print 'min_loc', min_loc
            print 'max_val', max_val
            print 'max_loc', max_loc

        except:
            print ('error', meth)
            continue
        
        #print img1
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        print top_left
        
        botton_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img1, top_left, botton_right, 255,2)

        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'),plt.xticks([]),plt.yticks([])

        plt.subplot(122),plt.imshow(img1,cmap = 'gray')
        plt.title('Detected Point'),plt.xticks([]),plt.yticks([])
        plt.suptitle(meth)

        plt.show()

    
if __name__ == '__main__':
    compareImg = '2.jpg'
    compare_img()
    #show_img(compareImg)
    #print 'a'
