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
            time.sleep(0.5)
            saveImg('open_screencap.png')
            openRes = recoOpen()
            if len(openRes):
                # 识别到开红包
                tapPoint(openRes)
                time.sleep(2)
                tapBack()
                tapBack()
            else:
                # 没识别到开红包，领取完了
                tapBack()
                tapBack()
        else:
            # 没识别到，返回
            tapBack()
