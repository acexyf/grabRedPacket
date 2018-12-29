import time

from save_img import (saveImg)
from recoList import (recoWXList)
from phoneOperation import (tapPoint,tapBack)
from recoRedPack import (recoRedPacket)
from recoOpen import (recoOpen)
from recoResult import (recoSuccess,recoFail)



# saveImg('open_result.png',True)


# while True:
#     time.sleep(0.5)
#     saveImg('list.png', True)
#     recoListRes = recoWXList()
#     print(recoListRes,'recoListRes')


isSucc = recoSuccess()
isFail = recoFail()
print(isSucc,isFail)