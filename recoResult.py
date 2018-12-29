import cv2
import numpy as np


recoPath = './screencap_img/grab_result.png'
succTemplatePath = './template_img/grab_succ_tmp.png'
failTemplatePath = './template_img/grab_fail_tmp.png'

def recoSuccess():
    recoList = []
    receive = cv2.imread(recoPath)
    receive_gray = cv2.cvtColor(receive,cv2.COLOR_BGR2GRAY)

    template = cv2.imread(succTemplatePath, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(receive_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold )

    for pt in zip(*loc[::-1]):
        recoList.append((pt[0], pt[1]))

    if len(recoList):
        return True
    else:
        return False


def recoFail():
    recoList = []
    receive = cv2.imread(recoPath)
    receive_gray = cv2.cvtColor(receive,cv2.COLOR_BGR2GRAY)

    template = cv2.imread(failTemplatePath, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(receive_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold )

    for pt in zip(*loc[::-1]):
        recoList.append((pt[0], pt[1]))

    if len(recoList):
        return True
    else:
        return False





