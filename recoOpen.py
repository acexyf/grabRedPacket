import cv2
import numpy as np


recoPath = './screencap_img/open.png'
templatePath = './template_img/open_tmp.png'



recoList = []
receive = cv2.imread(recoPath)
receive_gray = cv2.cvtColor(receive,cv2.COLOR_BGR2GRAY)

template = cv2.imread(templatePath, 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(receive_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where( res >= threshold )

for pt in zip(*loc[::-1]):
    recoList.append((pt[0], pt[1]))

print(recoList)