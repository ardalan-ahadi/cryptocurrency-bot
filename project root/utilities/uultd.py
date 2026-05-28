# imp
import math, os

# rel
from utilities.altbcrl import ftbcrl
from utilities.fultd import furol

# jsl
from model import jsave, jload

# cnf
from static.constants import key_Dfee

# def
def uultd():
    # get: slave, SETUP, PERPS, PROP, CHRT
    with open('database/slct_slave.txt', 'r') as file: tcoin = file.read()
    SETUP, PERPS, PROP, CHRT = (jload(os.path.join('database', f'{prefix}_{tcoin}.json')) for prefix in ['SETUP', 'PERPS', 'PROP', 'CHRT'])
    # tbacrol
    [ntbac, ntrol] = ftbcrl(SETUP)
    # intel
    [set_Ntfrm, set_Ntimer, nxmax] = [SETUP['set_Ntfrm'], SETUP['set_Ntimer'], [j['nxmax'] for j in PERPS if j['tcoin'] == tcoin][0]]
    # process
    ULTD = furol(tcoin, ntbac-ntrol, nxmax, SETUP, CHRT)
    dbtxtul = min(round(math.prod([1 + (cpar['dbdec'] * cpar['rx']) for cpar in ULTD]) -1 , 2), 1000) # round(sum([(cpar['dbdec']*cpar['rx']) for cpar in ULTD]), 2)
    nthesab = ntbac - ntrol # min(ntbac - ntrol, max(1, len(ULTD) * SETUP['set_Ntimer'])) # ntbac - ntrol if 1 < len(ULTD) else set_Ntimer
    dbtxtuy = round(max(-1, 24 * (dbtxtul / ((nthesab * set_Ntfrm) / 60))), 2)
    # output: ULTD, dbxyu
    jsave(os.path.join('database', 'ULTD_' + tcoin + '.json'), ULTD)
    return [ULTD, dbtxtul, dbtxtuy]