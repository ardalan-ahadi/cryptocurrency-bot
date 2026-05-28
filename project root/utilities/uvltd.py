# imp
import os

# rel
from utilities.altbcrl import ftbcrl
from utilities.fvltd import fveal

# jsl
from model import jload

# def
def uvltd(tvoin):
    # get: SETUP, PERPS, CHRT, PROP, ANLZ, DCSN, STEP
    SETUP, PERPS, CHRT, PROP, ANLZ, DCSN, STEP = (jload(os.path.join('database', f'{prefix}_{tvoin}.json')) for prefix in ['SETUP', 'PERPS', 'CHRT', 'PROP', 'ANLZ', 'DCSN', 'STEP'])
    # tbacrol
    [ntbac, ntrol] = ftbcrl(SETUP)
    # process
    [VLTD, dbtxtvl, dbtxtvy, ntrdwin_vl, ntrdone_vl, ratewin_vl] = fveal(tvoin, ntbac, ntrol, SETUP, PERPS, CHRT, PROP, ANLZ, DCSN, STEP)
    # output: VLTD, dbxyh, ntrdwindone, ratewin
    return [VLTD, dbtxtvl, dbtxtvy, ntrdwin_vl, ntrdone_vl, ratewin_vl]