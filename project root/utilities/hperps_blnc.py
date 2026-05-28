# imp
import requests

# sgn
from utilities.alhead import fhead

# huk
def fblnc():
    # request
    [sblnc, Tmethod, Treqpath, Tquery, Tbody] = [None, 'GET', '/api/mix/v1/account/accounts', '?productType=umcbl', '']
    [Trequrl, Theaders] = 'https://api.coincatch.com' + Treqpath + Tquery, fhead(Tmethod, Treqpath, Tquery, Tbody)
    while sblnc is None:
        try: sblnc = round(float(requests.get(Trequrl, headers=Theaders).json()['data'][0]['usdtEquity']), 4) # 'fixedMaxAvailable'
        except: sblnc = None
    return sblnc