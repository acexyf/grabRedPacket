import os



def tapPoint(point):
    x = point[0]
    y = point[1]
    os.system('adb shell input tap ' + str(x) + ' ' + str(y))

def tapBack():
    os.system('adb shell input keyevent 4')
