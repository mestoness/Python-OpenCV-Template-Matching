import numpy as np
import cv2
kontrol_et = False
img_rgb = cv2.imread('C:\\Users\\mest\\Desktop\\py\\ocr\\tam.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('C:\\Users\\mest\\Desktop\\py\\ocr\\aranan.png',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    if np.amax(res) > threshold:
        kontrol_et = True
print("Durumu ", kontrol_et)