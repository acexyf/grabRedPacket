import time

from save_img import (saveImg)
from recoList import (recoWXList)
from phoneOperation import (tapPoint,tapBack)
from recoRedPack import (recoRedPacket)
from recoOpen import (recoOpen)

while True:
    time.sleep(1)
    saveImg('list.png', False)
    recoListRes = recoWXList()
    # 群里有人发红包了
    if len(recoListRes) > 0:
        tapPoint(recoListRes)
        time.sleep(0.5)
        saveImg('detail_red_screencap.png')
        redRes = recoRedPacket()
        # 识别红包的位置
        if len(redRes):
            # 点击领取红包
            tapPoint(redRes)

            lastOpenRes = ()

            for index in range(8):
                saveImg('open_screencap.png')
                openRes = recoOpen()
                if len(openRes):
                    lastOpenRes = openRes
                    break;
            
            if len(lastOpenRes):
                tapPoint(lastOpenRes)
                tapBack()
                tapBack()
            else:
                tapBack()
                tapBack()


        else:
            # 没识别到，返回
            tapBack()
