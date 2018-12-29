import time

from save_img import (saveImg)
from recoList import (recoWXList)
from phoneOperation import (tapPoint,tapBack)
from recoRedPack import (recoRedPacket)
from recoOpen import (recoOpen)
from recoResult import (recoSuccess,recoFail)

while True:
    time.sleep(1)
    saveImg('list.png', False)
    recoListRes = recoWXList()
    # 群里有人发红包了
    if len(recoListRes) > 0:
        tapPoint(recoListRes)
        time.sleep(0.5)

        totalRedRes = ()
        for index in range(8):
            saveImg('detail_red_screencap.png')
            redRes = recoRedPacket()
            if len(redRes):
                totalRedRes = redRes
                break;

        # 识别红包的位置
        if len(totalRedRes):
            # 点击领取红包
            tapPoint(redRes)

            totalOpenRes = ()

            for index in range(8):
                saveImg('open_screencap.png')
                openRes = recoOpen()
                if len(openRes):
                    totalOpenRes = openRes
                    break;
            
            if len(totalOpenRes):
                # 识别到开的按钮
                tapPoint(totalOpenRes)

                # 识别结果0没识别到1成功2失败
                totalResultRes = 0
                for index in range(8):
                    saveImg('grab_result.png')
                    isSucc = recoSuccess()
                    isFail = recoFail()
                    if isSucc:
                        # 领取成功
                        totalResultRes = 1
                        break
                    elif isFail:
                        # 手慢了
                        totalResultRes = 2
                        break

                tapBack()
                time.sleep(0.1)
                tapBack()


            else:
                # 没有识别到开的按钮
                tapBack()
                time.sleep(0.1)
                tapBack()

        else:
            # 没识别到，返回
            tapBack()
