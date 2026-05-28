import numpy as np

# huk
def frng(datah, datal):
    # range
    drng = ((max(datah) + .000000000001) / (min(datal) + .000000000001)) - 1
    return round(drng, 4)
def favg(data, ndgts):
    # mean
    smid = float(np.mean(data))
    return round(smid, ndgts)
def fwvg(datas, datav, ndgts):
    datas = np.array(datas, dtype=float)
    datav = np.array(datav, dtype=float)
    if np.sum(datav) == 0: swid = np.mean(datas)
    else: swid = np.average(datas, weights=datav)
    return round(float(swid), ndgts)
def fwvg(datas, datav, ndgts):
    # waighted average
    #sdot_lst = []
    #for cind in range(len(datas)):
    #    sdot_lst.append(datas[cind] * datav[cind])
    #swid = sum(sdot_lst) / sum(datav)
    if sum(datav) == 0: swid = float(np.mean(datas))
    else: swid = float(np.average(datas, weights=datav))
    return round(swid, ndgts)
def fvar(datas, datav, ndgts):
    # variance
    swid = fwvg(datas, datav, ndgts)
    dvar = sum((cpar-swid) ** 2 for cpar in datas) / len(datas)
    return round(dvar, 9)
def fvlt(datas, datav, ndgts):
    # volatility
    dvar = fvar(datas, datav, ndgts)
    dvlt = dvar ** 0.5
    return round(dvlt, 5)