# glb
glb_Thost = "127.0.0.1"
glb_Tport = 8000

# key
key_Turl = "https://api.coincatch.com/api/mix/v1/market/"
key_Tacc = "cc_9cea9e73b46d6db117f8ecccd2d2f650"
key_Tsec = "43cdf400bcaaae16b27a5e7d58dd2600dbad7b90d0540a52b7f7d00ded65ffe3"
key_Tpss = 'aRd2248326'
key_Tucm = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
key_Tkcm = '60bbed19-6250-4600-89f7-6e22bf581c95'
key_Ticm = 'https://static-00.iconduck.com/assets.00/generic-cryptocurrency-icon-2048x2048-8uz1hlry.png'
key_Tgck = 'https://api.coingecko.com/api/v3/global'
set_Tzrrr = 'dpip'                      #{t}: [#'drng' #'dvar' #'dvlt' #'dcvg' #'dfee' #'dpip' #'rzvr']
set_Tsort = 'dbdec_H'                   #{t}: [#'sndmn', #'dmcap' / #'dcvg', #'drng', #'dvar', #'dvlt', #'rzcv' / #'drsk', #'drwd', #'nstp', #'nxfl', #'sndf' / #'dbpur_U' #'dbdec_U' / #'dbpur_H' #'dbdec_H' #'rz' #'nstep']
set_Tdscnd = 'yes'                      #{t}: [#'yes' #'no']
set_Troll = None                        #{t} (ai needs double roll)
key_Dfee = .0002                        #{d}
set_Dfltr = 0                           #{d}
set_Dsglm = 1                           #{d}
set_Dstep_dyn_oto = 'dfee'              #{d}: oto->{t}: [#'drng' #'dvar' #'dvlt' #'dcvg' #'dfee' #'dpip'] # step
set_Dcbeg = .1                          #{d} # step
set_Dcfin = 1-.1                        #{d} # step
set_Nstep_dyn_oto = 1                   #{n}: oto->{t}: [#'auto'] # step
set_Nperps = 1                          #{n}: oto->{t}: [#'max']
set_Nwhale = .05                        #{n}
set_Nzrrd = 0                           #{n}
set_Nrsdl = 0                           #{n}: [0,1]
set_Nturn = 1000                        #{n}
set_Ncook_dyn_oto = 'auto'              #{n}: oto->{t}: [#'auto']
set_Nzrrr_dyn_oto = ['auto', 'auto']    #{[n,n]}: oto->{[t,t]}: [#'auto']
set_Nxbeg_dyn_oto = 125                 #{n}: oto->{t}: [#'opt' #'max']

"""
    "XRP":      [14, 0],
    "TRX":      [14, 0],
    "LINK":     [7, 0],
    "ZEC":      [8, 0],
    "BNB":      [4, 0],
    "DOGE":     [11, 0],
    "SOL":      [3, 0],
    "AVAX":     [5, 0],
    "PAXG":     [10, 0],
"""
# "strnd1": [10, 3],
# "strnd2": [80, 8],
# "sma1": 200,
# "sma2": 50,
# "rsi":      [14, 50, 50],
# "stoch": [14, 20, 80],
# "macd": [12, 26, 9],
# "bb": [20, 2],
# "dc":       50,
# "kc": [20, 2],
# "adx":      [14, 18],
# "chop": [14, 50],
# "vwap":     [20],
# "nvs":      [200],
# "rng":      [14],

# history noghte shuru , hltd gir nabashe akhari
# negative db signal reverser (uhvr , 1 time ya kolan)
# tailing stop (uvhr)
# reverse z_score (anlz , threshold too)
# srtr timer = set_Ntimer/5 (js fsrt)
# set_Dsense = .01 (fanlz , auto too <btc ya khodesh>)
# timestrip = false (unalz)
# indics use (scls , slav)
# last hltd trd too deal munde ya na (ya mohem nis , vase vl)
# vl hamaro too ye saat o ye jahat posin nakone , har saat 1ki ya darsad ndeals
# vl rl: hltd (positive o ended), random deactive 0<hltd (vl rl o alsrtr)
# timer ye tori k vbsy bishtar az srtr bemoone (2 barabar)
# dslip too hlvl shabih sazi (market out o stop loss)
# vl ba askbid price enter
# bayad cndl akhario nagiri , roo open darvaghe trd haro bezani (mohasebat roo ghabli <prop anlz dcsn>)
# nblnc dare vlrl ke shrt long haye pend taadol dashte bashan (vase zede shock)
# anlz indc 5*ncko rol vase mixed warmup
# vlrl blnc tside vase vurud vltd rltd dar nazar
# "strnd": [25,25], "rsi": 14

# assets
set_Rassets_oto = 12                    #{r}: oto->{t}: [#'auto']
set_Ndeals = 1                          #{n}
set_Nserial = 20                        #{n}
set_Ntimer = 1                          #{n}

# setup
set_Ntfrm = 4*60                        #{n}
set_Tback = '3000d'                     #{t}
set_Ncook_dyn_oto = {
    "ema":      [200],
    "emac":     [13, 8, 5],
    "strnd":    [25, 2],
    "vol":      [20, 1.5],
    "atr":      [14, 20],
    }                                   #{n}: oto->{t}: [#'auto']
set_Rzrrr = [1, 0]                      #{[r,r]}
set_Nzrlm = [120, 150]                  #{n}
set_Nzliq = 1.2                         #{n}