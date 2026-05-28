# imp
import requests, json

# sgn
from utilities.alhead import fhead

def faccpos():
    [jaccpos, Tmethod, Treqpath, Tquery] = [None, 'POST', '/api/mix/v1/account/setPositionMode', '']
    Tbody = json.dumps({ "productType": "umcbl", "holdMode": "double_hold" })
    [Trequrl, Theaders] = ['https://api.coincatch.com' + Treqpath + Tquery, fhead(Tmethod, Treqpath, Tquery, Tbody)]
    while jaccpos == None:
        try: jaccpos = requests.post(Trequrl, headers=Theaders, data=Tbody).json()['data']['dualSidePosition']
        except: jaccpos = None
    return jaccpos