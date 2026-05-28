# imp
import requests, pickle, json, os
from concurrent.futures import ThreadPoolExecutor

# rel
from utilities.fperps import fjcon, fsnxi
from utilities.hperps_blnc import fblnc
def auto_round(num):
    if num == 0: return 0 
    ndcml = min(int((len(str(num).split('.')[1]))**.5)+1 if '.' in str(num) else 0, 9)
    return round(num, ndcml)

# jsl
from model import jsave, jload

# cnf
from static.constants import key_Tgck

# def
def uperps():
    # get: SETUP, VBSY
    [SETUP, VBSY] = [jload(os.path.join('database', 'SETUP.json')), jload(os.path.join('database', 'VBSY.json'))]
    with open('database/ICONS.json', 'r', encoding='utf-8') as f: ICONS = json.load(f)
    # ICONS=jload(os.path.join('database', 'ICONS.json'))
    # [SETUP, VBSY, ICONS] = [jload(os.path.join('database', 'SETUP.json')), jload(os.path.join('database', 'VBSY.json')), jload(os.path.join('database', 'ICONS.json'))]
    # intel
    tcolnm = ['set_Rassets_oto', 'set_Ndeals', 'set_Nserial', 'set_Nperps']
    [set_Rassets_oto, set_Ndeals, set_Nserial, set_Nperps] = [SETUP[cpar] for cpar in tcolnm]    
    sblnc = fblnc() if set_Rassets_oto == 'auto' else set_Rassets_oto
    sgmnt = round((sblnc/(set_Nserial+1))/set_Ndeals, 4) if set_Ndeals != 0 else 0
    # mcap = requests.get(key_Tgck).json()['data']
    # [rmcap_dict, dmcap_dict] = [mcap['total_market_cap'], mcap['market_cap_percentage']]
    # process
    Jcontracts = fjcon(set_Nperps, VBSY)
    [snow_lst, svol_lst, nxmax_lst, ICONS_sorted] = fsnxi(ICONS, Jcontracts)
    def uperps_thrd(cind):
        """
        # gtrade
        [ticon, tcoin, tcola, ndgts, nxmax] = [ICONS_sorted[cind]['ticon'], str(Jcontracts[cind]['from']), str(Jcontracts[cind]['to']), 21, nxmax_lst[cind]]
        [snow, svol, rqntm, gindx] = [snow_lst[cind], svol_lst[cind], Jcontracts[cind]['rqntm'], str(Jcontracts[cind]['groupIndex'])]
        """
        # binance
        [ticon, tcoin, tcola, ndgts, nxmax] = [ICONS_sorted[cind]['ticon'], str(Jcontracts[cind]['baseAsset']), 'USDT', int(Jcontracts[cind]['pricePrecision']), nxmax_lst[cind]]
        [snow, svol, rqntm, gindx] = [snow_lst[cind], svol_lst[cind], max(float(Jcontracts[cind]['filters'][1]['minQty']), float(Jcontracts[cind]['filters'][1]['stepSize'])), None]
        """
        # coincatch
        [ticon, tcoin, ndgts, nxmax] = [ICONS_sorted[cind]['ticon'], str(Jcontracts[cind]['baseCoin']), int(Jcontracts[cind]['pricePlace']), nxmax_lst[cind]]
        [snow, svol, rqntm] = [snow_lst[cind], svol_lst[cind], max(float(Jcontracts[cind]['minTradeNum']), float(Jcontracts[cind]['sizeMultiplier']))]
        """
        dcml = max(0, len(str(rqntm).split('.')[1]) if '.' in str(rqntm) else 0) if isinstance(rqntm, float) else 0
        rqntm = rqntm if (5 < rqntm * snow) else round((5 / snow), dcml)
        sqntm = auto_round(rqntm * snow)
        sndmn = auto_round(sqntm / nxmax)
        # rtotmcap = rmcap_dict.get('btc', None) / dmcap_dict.get('btc', None)
        # [rmcap, dmcap] = [rmcap_dict.get(tcoin.lower(), .0001 * rtotmcap), dmcap_dict.get(tcoin.lower(), .0001)]
        return { "ticon": ticon, "tcoin": tcoin, "tcola": tcola, "snow": snow, "svol": svol, "ndgts": ndgts, "spstp": 0,
                 "rqntm": rqntm, "sqntm": sqntm, "nxmax": nxmax, "sndmn": sndmn, "gindx": gindx } # , "rmcap": rmcap, "dmcap": dmcap }        
    with ThreadPoolExecutor() as executor: PERPS = list(executor.map(uperps_thrd, list(range(len(Jcontracts)))))
    # PERPS.sort(key=lambda d: float(d.get('gindx', 0)), reverse=False) # marketcap o reverse
    # output: sblnc, sgmnt, PERPS, ICONS, SETUP
    with open('database/sblnc.txt', 'w') as file: file.write(str(sblnc))
    with open('database/sgmnt.txt', 'w') as file: file.write(str(sgmnt))
    jsave(os.path.join('database', 'PERPS.json'), PERPS)
    # jsave(os.path.join('database', 'ICONS.json'), ICONS)
    def fps_thrd(cpar):
        jsave(os.path.join('database', 'PERPS_' + cpar['tcoin'] + '.json'), PERPS)
        jsave(os.path.join('database', 'SETUP_' + cpar['tcoin'] + '.json'), SETUP)
        with open('database/sblnc_' + cpar['tcoin'] + '.txt', 'w') as file: file.write(str(sblnc))
        with open('database/sgmnt_' + cpar['tcoin'] + '.txt', 'w') as file: file.write(str(sgmnt))
        if not os.path.exists(f"database/jordin_rl_{cpar['tcoin']}.txt"):
            with open('database/jordin_rl_' + cpar['tcoin'] + '.txt', 'w') as file: file.write('')
        if not os.path.exists(f"database/jordsl_rl_{cpar['tcoin']}.txt"):
            with open('database/jordsl_rl_' + cpar['tcoin'] + '.txt', 'w') as file: file.write('')
        if not os.path.exists(f"database/jordtp_rl_{cpar['tcoin']}.txt"):
            with open('database/jordtp_rl_' + cpar['tcoin'] + '.txt', 'w') as file: file.write('')
        if not os.path.exists(f"database/jordout_rl_{cpar['tcoin']}.txt"):
            with open('database/jordout_rl_' + cpar['tcoin'] + '.txt', 'w') as file: file.write('')
        if not os.path.exists(f"database/STEP_rl_{cpar['tcoin']}.pkl"):
            with open(os.path.join('database', f"STEP_rl_{cpar['tcoin']}.pkl"), 'wb') as f: pickle.dump([], f)
    with ThreadPoolExecutor() as executor: executor.map(fps_thrd, PERPS)
    return PERPS