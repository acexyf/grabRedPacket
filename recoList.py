import cv2
import numpy as np


highDiff = 60
toLeft = 125


recoPath = './screencap_img/list.png'
templatePath = './template_img/list_red_tmp.jpg'


def recoWXList():
    recoList = []
    receive = cv2.imread(recoPath)
    receive_gray = cv2.cvtColor(receive,cv2.COLOR_BGR2GRAY)


    template = cv2.imread(templatePath, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(receive_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold )


    for pt in zip(*loc[::-1]):
        cv2.rectangle(receive, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)
        itemx = pt[0]
        itemy = pt[1]
        imgRGB = receive[itemy - highDiff, toLeft]
        # 左上角是否有小圆圈，判断是否领过
        hasRedDot = np.array_equal(imgRGB, [62,62,255])
        # hasRedDot = True
        if hasRedDot:
            recoList.append((itemx, itemy))

    if len(recoList):
        return recoList[0]
    else:
        return ()
    # for item in recoList:
    #     (itemx, itemy) = item
    #     # [62 62 255]
    #     imgRGB = receive[itemy - highDiff, toLeft]
    #     print(imgRGB,itemx, itemy)


# cv2.imwrite('./output.jpg', receive)





