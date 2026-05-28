# imp
import random
from concurrent.futures import ThreadPoolExecutor

# jsl
from model import jload

 #cnf
from static.constants import key_Dfee

# huk
def fstep(s, tside, drisk, drwrd, nxfl, dmmr, SETUP, PERPS):
    # if tside == 'hodl': return []
    # intel
    [set_Dcbeg, set_Dcfin] = [SETUP[i] for i in ['set_Dcbeg', 'set_Dcfin']]
    if s == 1: dc_lst = [0]
    if s == 2: dc_lst = [0, set_Dcfin] # round((set_Dcfin + set_Dcbeg) / 2, 2)]
    if 3 <= s: 
        def fstep_thrd1(cind): return round(set_Dcbeg - (cind * (set_Dcbeg - set_Dcfin) / (s - 2)), 2)
        with ThreadPoolExecutor() as executor: dc_lst = [0] + list(executor.map(fstep_thrd1, list(range(s - 1))))
    # process
    nx, step_lst = [nxfl, []]
    for cind,cpar in enumerate(dc_lst):
        if cpar == 0: [den, dvg] = [1, 1]
        if cpar != 0: 
            den = (round(((1-cpar)*dvg)+(cpar*dsl),4))
            dvg = (round(((cind*dvg)+den)/(cind+1),4))
        dtp = round((1 + (drwrd * (1 if tside == 'long' else -1))) * dvg, 4)
        dsl = round((1 - (drisk * (1 if tside == 'long' else -1))) * dvg, 4)
        drtn = round(((dtp/den - 1) * (1 if tside == 'long' else -1)), 4)
        dcvr = round(((1 - dsl) * (1 if tside == 'long' else -1)), 4)
        dlq = round((1 - (((1/nx) - dmmr - 2*key_Dfee) * (1 if tside == 'long' else -1))) * dvg , 4)
        dbrow = { 'ns': cind+1, 'nx': nx, 'dc': cpar, 'den': den, 'dvg': dvg, 
                  'dtp': dtp, 'dsl': dsl, 'dlq': dlq, 'dcvr': dcvr, 'drtn': drtn }
        step_lst.append(dbrow)
    # output
    return step_lst