import os

serialNum = '10.101.160.116:5555'

if serialNum != '':
    serialStr = '-s ' + serialNum

def tapPoint(point):
    x = point[0]
    y = point[1]
    os.system('adb ' + serialStr + ' shell input tap ' + str(x) + ' ' + str(y))

def tapBack():
    os.system('adb ' + serialStr + ' shell input keyevent 4')
