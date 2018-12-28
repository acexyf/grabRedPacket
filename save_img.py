import time
import os

def saveImg(imgName = 'sh2.png'):
    # 截屏保存的文件目录
    dirPath = 'D://projects/grabRedPacket/screencap_img/'
    
    os.system('adb shell screencap -p /sdcard/' + imgName)
    os.system('adb pull /sdcard/' + imgName + ' ' + dirPath)

