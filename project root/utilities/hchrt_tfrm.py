# imp
import time

# huk
def ftfrm(tcoin, SETUP):
    # intel
    tcolnm = ['set_Ntfrm', 'set_Tback']
    [set_Ntfrm, set_Tback] = [SETUP[cpar] for cpar in tcolnm]
    # process
    [ntotbac, ttotvhd] = [int(set_Tback[:-1]), set_Tback[-1]]
    ntotvhd = (1 if ttotvhd == 'm' else 
        60 if ttotvhd == 'h' else 
        24 * 60 if ttotvhd == 'd' else 
        7 * 24 * 60 if ttotvhd == 'w' else 
        30 * 24 * 60 if ttotvhd == 'M' else 0)
    ntotbvt = int((ntotbac * ntotvhd) / set_Ntfrm)
    # output
    ntfreq = int(time.time() * 1000) # - (100 * (24*60*60*1000))
    ntsreq = int(ntfreq - ntotbvt * set_Ntfrm * 60 * 1000)
    ttfrm = (str(set_Ntfrm) + 'm' if set_Ntfrm < 60 else
             str(int(set_Ntfrm / 60)) + 'H' if 60 <= set_Ntfrm < (24 * 60) else
             str(int(set_Ntfrm / (24 * 60))) + 'D' if (24 * 60) <= set_Ntfrm < (7 * 24 * 60) else
             str(int(set_Ntfrm / (7 * 24 * 60))) + 'W' if (7 * 24 * 60) <= set_Ntfrm < (30 * 24 * 60) else
             'error:please adjust time frame request for price history!' if (30 * 24 * 60) <= set_Ntfrm else '')
    return [ntsreq, ntfreq, ttfrm]