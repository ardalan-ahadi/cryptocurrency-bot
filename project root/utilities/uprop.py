# imp
import json, os
from concurrent.futures import ThreadPoolExecutor

# rel
from utilities.altbcrl import ftbcrl
from utilities.fprop import fcalc

# jsl
from model import jsave, jload

# def
def uprop():
    # get: slave, SETUP, PERPS, CHRT
    with open('database/slct_slave.txt', 'r') as file: tcoin = file.read()
    SETUP, PERPS, CHRT = (jload(os.path.join('database', f'{prefix}_{tcoin}.json')) for prefix in ['SETUP', 'PERPS', 'CHRT'])
    # tbacrol
    [ntbac, ntrol] = ftbcrl(SETUP)
    # process
    def uprop_thrd(cind):
        print(f"{cind} / {ntbac}", end="\r")
        if cind-1 < ntrol-1: [smid, swid, dcvg, drng, dvar, dvlt, rzcv, nvsec, rvsec, dvol, npsml, ntfsml, ncksml, npbig, ntfbig, nckbig] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if ntrol-1 <= cind-1: [smid, swid, dcvg, drng, dvar, dvlt, rzcv, nvsec, rvsec, dvol, npsml, ntfsml, ncksml, npbig, ntfbig, nckbig] = fcalc(cind-1, tcoin, ntrol, SETUP, PERPS, CHRT) # , rmcap)
        return { "smid": smid, "swid": swid, "dcvg": dcvg, "drng": drng, "dvar": dvar, "dvlt": dvlt, "rzcv": rzcv,
                 "nvsec": nvsec, "rvsec": rvsec, "dvol": dvol, "npsml": npsml, "ntfsml": ntfsml, 'ncksml': ncksml, "npbig": npbig, "ntfbig": ntfbig, 'nckbig': nckbig }        
    with ThreadPoolExecutor() as executor: PROP = list(executor.map(uprop_thrd, list(range(ntbac))))
    """
    # finalize
    for cind in range(len(PROP)): 
        if cind < ntrol -1: PROP[cind]['rdif'] = 0
        if ntrol - 1 <= cind: PROP[cind]['rdif'] = round(PROP[cind]['rzcv'] - PROP[cind-1]['rzcv'], 4)
    """
    jsave(os.path.join('database', 'PROP_' + tcoin + '.json'), PROP)
    return PROP