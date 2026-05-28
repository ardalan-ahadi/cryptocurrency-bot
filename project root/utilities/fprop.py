# imp
from concurrent.futures import ThreadPoolExecutor

# rel
from utilities.hprop_amar import frng, favg, fwvg, fvar, fvlt
from utilities.hprop_tune import fcook
def auto_round(num):
    if num == 0: return 0 
    ndcml = min(int((len(str(num).split('.')[1]))**.5)+1 if '.' in str(num) else 0, 6)
    return round(num, ndcml)

# cnf
from static.constants import key_Dfee

# fxs
def flist(tcoin, CHRT):
    # process
    def flist_thrd(cind):
        [sopn, shgh, slow, scls, nvol, rvol] = [float(CHRT[cind]["sopn"]), float(CHRT[cind]["shgh"]), \
                                                float(CHRT[cind]["slow"]), float(CHRT[cind]["scls"]), float(CHRT[cind]["nvol"]), float(CHRT[cind]["rvol"])]
        [savg, sdhl] = [(sopn + shgh + slow + scls) / 4, (shgh/slow) -1]
        return [sopn, shgh, slow, scls, nvol, rvol, savg, sdhl]
    with ThreadPoolExecutor() as executor: results = zip(*list(executor.map(flist_thrd, list(range(len(CHRT))))))
    # output
    [sopn_leest, shgh_leest, slow_leest, scls_leest, nvol_leest, rvol_leest, savg_leest, sdhl_leest] = results
    return [savg_leest, shgh_leest, slow_leest, sdhl_leest, nvol_leest, rvol_leest]
def fcalc(cind, tcoin, ntrol, SETUP, PERPS, CHRT): # , rmcap):
    # intel
    [set_Ntfrm, ndgts] = [SETUP['set_Ntfrm'], next((cpar['ndgts'] for cpar in PERPS if cpar['tcoin'] == tcoin), None)]
    [savg_leest, shgh_leest, slow_leest, sdhl_leest, nvol_leest, rvol_leest] = flist(tcoin, CHRT)
    [savg_lst, shgh_lst, slow_lst, sdhl_lst, nvol_lst, rvol_lst] = [savg_leest[cind-ntrol+1:cind+1], shgh_leest[cind-ntrol+1:cind+1], \
     slow_leest[cind-ntrol+1:cind+1], sdhl_leest[cind-ntrol+1:cind+1], nvol_leest[cind-ntrol+1:cind+1], rvol_leest[cind-ntrol+1:cind+1]]
    # process
    [smid, swid, dcvg, drng, dvar, dvlt, rzcv] = [favg(savg_lst, ndgts), fwvg(savg_lst, nvol_lst, ndgts), favg(sdhl_lst, 4), \
     frng(shgh_lst, slow_lst), fvar(sdhl_lst, nvol_lst, ndgts), fvlt(sdhl_lst, nvol_lst, ndgts), 1]
    # [dcvg, drng, dvar, dvlt, rzcv] = [min(dcvg, 1), min(drng, 1), min(dvar, 1), min(dvlt, 1), 1] #round(drng/dvlt, 2)] # because rr auto use -> x become 0
    [nvsec, rvsec, dvol] = [round(favg(nvol_lst, ndgts) / (set_Ntfrm*60), 1), auto_round(favg(rvol_lst, ndgts) / (set_Ntfrm*60)), rvol_lst[-1]]
    # nvsec = int(nvsec) if 1000 < nvsec else round(nvsec, 1) if 100 < nvsec else nvsec
    rvsec = round(rvsec, 1) if 100 < rvsec else (int(rvsec) if 1000 < rvsec else rvsec)
    [npsml, ntfsml, ncksml, npbig, ntfbig, nckbig] = fcook(ndgts, savg_lst, swid)
    # output
    return [smid, swid, dcvg, drng, dvar, dvlt, rzcv, nvsec, rvsec, dvol, npsml, ntfsml, ncksml, npbig, ntfbig, nckbig]