import time
import os

def saveImg(imgName = 's1.png', isBackup = True):
    # 截屏保存的文件目录
    dirPath = 'D://projects/grabRedPacket/screencap_img/'
    
    os.system('adb shell screencap -p /sdcard/' + imgName)
    os.system('adb pull /sdcard/' + imgName + ' ' + dirPath)
    # 备份图片
    if isBackup:
        os.system('adb pull /sdcard/' + imgName + ' ' + 'D://projects/screencap/' + str(int(time.time()))+'.png')

