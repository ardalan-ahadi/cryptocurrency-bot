# huk
from concurrent.futures import ThreadPoolExecutor
def process_small(savg_lst):
    npsup, npsdn = 0, 0
    trendNow = ''
    for cind in range(1, len(savg_lst)):
        trendPrv = trendNow
        if savg_lst[cind] < savg_lst[cind - 1]:
            trendNow = '↑'
            npsup += (trendNow != trendPrv)
        if savg_lst[cind] > savg_lst[cind - 1]:
            trendNow = '↓'
            npsdn += (trendNow != trendPrv)
    npsml = max(int((npsup + npsdn) / 2), 1)
    ntfsml = int(round(len(savg_lst) / npsml, 0)) if npsml != 0 else 0
    ncksml = max(ntfsml, 3)
    return npsml, ntfsml, ncksml
def process_big(savg_lst, swid):
    npbup, npbdn = 0, 0
    tdiodNow = ''
    for cind in range(1, len(savg_lst)):
        tdiodPrv = tdiodNow
        if savg_lst[cind] < swid:
            tdiodNow = '↑'
            npbup += (tdiodNow != tdiodPrv)
        if swid < savg_lst[cind]:
            tdiodNow = '↓'
            npbdn += (tdiodNow != tdiodPrv)
    npbig = max(int((npbup + npbdn) / 2), 1)
    ntfbig = int(round(len(savg_lst) / npbig, 0)) if npbig != 0 else 0
    nckbig = max(ntfbig, 3)
    return npbig, ntfbig, nckbig
def fcook(ndgts, savg_lst, swid):
    with ThreadPoolExecutor() as executor:
        small_future = executor.submit(process_small, savg_lst)
        big_future = executor.submit(process_big, savg_lst, swid)
        npsml, ntfsml, ncksml = small_future.result()
        npbig, ntfbig, nckbig = big_future.result()
    return [npsml, ntfsml, ncksml, npbig, ntfbig, nckbig]