# imp
import os

# rel
from utilities.altbcrl import ftbcrl
from utilities.frltd import freal

# jsl
from model import jload

# def
def urltd(troin):
    # get: SETUP, PERPS, CHRT, PROP, ANLZ, DCSN, STEP
    SETUP, PERPS, CHRT, PROP, ANLZ, DCSN, STEP = (jload(os.path.join('database', f'{prefix}_{troin}.json')) for prefix in ['SETUP', 'PERPS', 'CHRT', 'PROP', 'ANLZ', 'DCSN', 'STEP'])
    # tbacrol
    [ntbac, ntrol] = ftbcrl(SETUP)
    # process
    [RLTD, dbtxtrl, dbtxtry, ntrdwin_rl, ntrdone_rl, ratewin_rl] = freal(troin, ntbac, ntrol, SETUP, PERPS, CHRT, PROP, ANLZ, DCSN, STEP)
    # output: RLTD, dbxyh, ntrdwindone, ratewin
    return [RLTD, dbtxtrl, dbtxtry, ntrdwin_rl, ntrdone_rl, ratewin_rl]