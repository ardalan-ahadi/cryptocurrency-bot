# imp
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# rel
from utilities.altbcrl import ftbcrl
from utilities.faiml import fitm

# jsl
from model import jsave, jload

# def
def uaiml():
    # get: slave, SETUP, PERPS, PROP, CHRT, ANLZ, DCSN
    with open('database/slct_slave.txt', 'r') as file: tcoin = file.read()
    SETUP, PERPS, CHRT, PROP, ANLZ, DCSN, STEP = (jload(os.path.join('database', f'{prefix}_{tcoin}.json')) \
                                    for prefix in ['SETUP', 'PERPS', 'CHRT', 'PROP', 'ANLZ', 'DCSN', 'STEP'])
    # tbacrol
    [ntbac, ntrol] = ftbcrl(SETUP)
    # intel
    [df, dp] = [pd.DataFrame(CHRT), pd.DataFrame(PROP)]
    da = pd.DataFrame({ 'Y': 0,
        'nvol': pd.to_numeric(df['nvol'], errors='coerce'),
        'rvol': pd.to_numeric(df['rvol'], errors='coerce'),
        'sopn': pd.to_numeric(df['sopn'], errors='coerce'),
        'shgh': pd.to_numeric(df['shgh'], errors='coerce'),
        'slow': pd.to_numeric(df['slow'], errors='coerce'),
        'scls': pd.to_numeric(df['scls'], errors='coerce'),
        'dcvg': pd.to_numeric(dp['drng'], errors='coerce'),
        'drng': pd.to_numeric(dp['drng'], errors='coerce'),
        'dvlt': pd.to_numeric(dp['dvlt'], errors='coerce'), })
    da['slav'] = da[['sopn', 'shgh', 'slow', 'scls']].mean(axis=1)
    da['dscr1'] = (da['dvlt'] + .0001) / (da['drng'] + .0001)
    da['dscr2'] = da['dvlt'] / (da['dcvg'] + .0001)
    da['dscr3'] = da['drng'] / (da['dcvg'] + .0001)
    tdacol = da.columns[1:] # no Y
    da[tdacol + '_diff'] = da[tdacol].diff()
    da[tdacol + '_deff'] = da[tdacol].diff().diff()
    da[tdacol + '_mean_diff'] = da[tdacol + '_diff'].rolling(window=2).mean()
    da[tdacol + '_mean_deff'] = da[tdacol + '_deff'].rolling(window=2).mean()
    da[tdacol + '_minn_diff'] = da[tdacol + '_mean_diff'].rolling(window=2).mean()
    da[tdacol + '_minn_deff'] = da[tdacol + '_mean_deff'].rolling(window=2).mean()
    da[tdacol + '_lag_mean_diff'] = da[tdacol + '_mean_diff'].shift(1)
    da[tdacol + '_lag_mean_deff'] = da[tdacol + '_mean_deff'].shift(1)
    da[tdacol + '_lag_minn_diff'] = da[tdacol + '_minn_diff'].shift(1)
    da[tdacol + '_lag_minn_deff'] = da[tdacol + '_minn_deff'].shift(1)
    da = da.loc[:, da.columns.difference(['sopn', 'shgh', 'slow', 'scls'])]
    da = (da - da.mean()) / da.std()
    # process
    def uaiml_thrd(cind): return fitm(cind, tcoin, ntrol, SETUP, PERPS, CHRT, PROP, ANLZ, DCSN, STEP, da)
    with ThreadPoolExecutor() as executor: tchng_leest = list(executor.map(uaiml_thrd, list(range(ntbac))))
    for cind in range(len(tchng_leest)): ANLZ[cind]['tside'] = tchng_leest[cind]
    # output
    jsave(os.path.join('database', 'ANLZ_' + tcoin + '.json'), ANLZ)
    return ANLZ