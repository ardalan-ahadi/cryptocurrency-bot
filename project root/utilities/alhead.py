# imp
import time, base64, hmac

# cnf
from static.constants import key_Tacc, key_Tsec, key_Tpss

# huk
def fhead(Tmethod,Treqpath,Tquery,Tbody):
    timestamp = str(int(time.time()*1000))
    tmessage = str(timestamp) + str.upper(Tmethod) + str(Treqpath) + str(Tquery) + str(Tbody)
    tsignature = base64.b64encode(hmac.new(key_Tsec.encode('utf-8'), tmessage.encode('utf-8'), digestmod='sha256').digest()).decode('utf-8')
    Theaders = { "ACCESS-TIMESTAMP": timestamp,
                 "ACCESS-KEY": key_Tacc,
                 "ACCESS-SIGN": tsignature,
                 "ACCESS-PASSPHRASE": key_Tpss,
                 "locale": 'en-US',
                 "Content-Type": 'application/json'}
    return Theaders