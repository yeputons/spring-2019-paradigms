#!/usr/bin/env python3
import cv2
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

img = cv2.imread('logo.png')
cv2.rectangle(img, pt1=(0, 0), pt2=(200, 100), color=(255, 0, 0), thickness=10)

drawArgs = {
    'text': 'Hello Boogie',
    'fontFace': cv2.FONT_HERSHEY_SIMPLEX,
    'fontScale': 2,
    'thickness': 5
}
(width, height), baseLine = cv2.getTextSize(**drawArgs)

pos_y = img.shape[0] // 2 

cv2.putText(img, **drawArgs, org=(0, pos_y), color=(0, 0, 255))
cv2.line(img, pt1=(0, pos_y), pt2=(width, pos_y), color=(255, 0, 255), thickness=1)
cv2.imwrite('logo-out.png', img)
