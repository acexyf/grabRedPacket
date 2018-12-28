import os

dirPath = 'D://projects/grabRedPacket/screencap_img/'
imgName = 'list.png'
os.system('adb -s 1dd5a009 shell screencap -p /sdcard/' + imgName)
# os.system('adb pull /sdcard/' + imgName + ' ' + dirPath)



