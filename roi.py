import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import random

path = os.getcwd()

def word_detect(path,kx=3,ky=1, display = False):

    os.chdir(path)
    myFolders = os.listdir(path)

    images = []
    for jpg in myFolders[ : ]:
        if ".jpg" in jpg:
            images.append(jpg)
    images = sorted(images)
    print("Total images in folder:",len(images))

    b = 0
    while b < len(images):
        image = cv2.imread(images[b])
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kx, ky))
        cv2.rectangle(image, (0, 0), (image.shape[1], image.shape[0]), (255, 255, 255), 15)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        t, thresh = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)
        ero = cv2.erode(thresh, kernel, iterations=2)
        morph = cv2.morphologyEx(ero, cv2.MORPH_OPEN, np.ones((7, 8)))
        cnt, h = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in cnt:
            x, y, w, h = cv2.boundingRect(c)
            if w > 35 and w < 440:
                cv2.drawContours(morph, [c], -1, (0, 0, 0), -1)
        cntrs, h1 = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        sort_cntrs = sorted(cntrs, key=lambda a: cv2.boundingRect(a)[0])
        print("Total contours:",len(cntrs))
        plt.imshow(morph)
        
        #cv2.imshow("morph", morph)
        #cv2.waitKey(0)
        bBoxes = []
        img2 = image.copy()
        for c1 in sort_cntrs:
            x1, y1, w1, h1 = cv2.boundingRect(c1)
            # area = cv2.contourArea(cnt
            if w1 > 20 and w1 < 500:
                box = image[y1:y1+h1, x1:x1+w1]
                bBoxes.append(box)
                if display == True:
                    cv2.rectangle(img2, (x1, y1), (x1 + w1, y1 + h1), 
                             (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 2)

        plt.imshow(img2)
        
        
        #cv2.imshow("Org", image)
        #cv2.waitKey(0)    
        b += 1
    return bBoxes

# çalıştırmak için:

boxes = word_detect(path,display=True)

plt.imshow(boxes[0])