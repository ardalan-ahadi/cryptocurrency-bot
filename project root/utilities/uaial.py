# imp
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# rel
from utilities.altbcrl import ftbcrl
from utilities.faial import fdata, furol
from utilities.haial_fitm import fitm
from utilities.haial_rplc import fchng

# cnf
from static.constants import key_Dfee

# jsl
from model import jsave, jload

# def
def uaial():
    # get: slave, SETUP, PERPS, PROP, CHRT, ANLZ, DCSN
    with open('database/slct_slave.txt', 'r') as file: tcoin = file.read()
    SETUP, PERPS, CHRT, PROP, ANLZ = (jload(os.path.join('database', f'{prefix}_{tcoin}.json')) for prefix in ['SETUP', 'PERPS', 'CHRT', 'PROP', 'ANLZ'])
    # tbacrol
    [ntbac, ntrol] = ftbcrl(SETUP)
    # intel
    set_Tzrrr = SETUP['set_Tzrrr']
    # process
    da = fdata(tcoin, CHRT, PROP, ANLZ)
    def uaial_thrd1(cind): return [] if cind < (2*ntrol - 1) else furol(cind, tcoin, ntrol, SETUP, CHRT)
    with ThreadPoolExecutor() as executor: y_leest = list(executor.map(uaial_thrd1, list(range(ntbac))))
    def uaial_thrd2(cind): return fitm(cind, tcoin, ntrol, SETUP, da, y_leest)
    with ThreadPoolExecutor() as executor: tchng_leest = list(executor.map(uaial_thrd2, list(range(ntbac))))
    def uaial_thrd3(cind):
        if cind < (ntrol-1): return [[], { "nrsk": None, "nrwd": None, "tzrrr": None, "drsk": None, "drwd": None, "drrr": None, "dmnw": None,
                                            "nstp": None, "dstp": None, "nxfl": None, "sndf": None, "rzunt": None, "rztot": None }]
        if (ntrol-1) <= cind:
            [nrsk, nrwd, ydrsk, ydrwd, drrr, dmnw, nstp, dstp, nxfl, sndf, rzunt, rztot, STEP_lst] = \
             fchng(cind, tcoin, ntrol, SETUP, PERPS, CHRT, PROP, ANLZ, tchng_leest)
            return [STEP_lst, { 'nrsk': nrsk, 'nrwd': nrwd, 'tzrrr': set_Tzrrr, 'drsk': ydrsk, 'drwd': ydrwd, 'drrr': drrr, 'dmnw': dmnw, 
                                'nstp': nstp, 'dstp': dstp, 'nxfl': nxfl, 'sndf': sndf, 'rzunt': rzunt, 'rztot': rztot }]
    with ThreadPoolExecutor() as executor: [STEP, DCSN] = zip(*list(executor.map(uaial_thrd3, list(range(ntbac)))))
    # output
    jsave(os.path.join('database', 'STEP_' + tcoin + '.json'), STEP)
    jsave(os.path.join('database', 'DCSN_' + tcoin + '.json'), DCSN)
    ANLZ = jload(os.path.join('database', 'ANLZ_' + tcoin + '.json'))
    return [ANLZ, DCSN, STEP]