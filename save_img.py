import time
import os

serialNum = '10.101.160.116:5555'


def saveImg(imgName = 's1.png', isBackup = True):
    # 截屏保存的文件目录
    dirPath = 'D://projects/grabRedPacket/screencap_img/'
    
    serialStr = ''

    if serialNum != '':
        serialStr = '-s ' + serialNum

    os.system('adb ' + serialStr + ' shell screencap -p /sdcard/' + imgName)
    os.system('adb ' + serialStr + ' pull /sdcard/' + imgName + ' ' + dirPath)
    # 备份图片
    if isBackup:
        os.system('adb ' + serialStr + ' pull /sdcard/' + imgName + ' ' + 'D://projects/screencap/' + str(int(time.time()))+'.png')

