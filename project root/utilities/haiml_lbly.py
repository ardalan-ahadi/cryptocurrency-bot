# imp
import random

# cnf
from static.constants import key_Dfee

# rel
def auto_round(num):
    if num == 0: return 0 
    ndcml = min(int((len(str(num).split('.')[1]))**.5)+1 if '.' in str(num) else 0, 6)
    return round(num, ndcml)

# huk
def flbly(tcoin, ntrol, cind, PERPS, CHRT, PROP, ANLZ, DCSN, STEP):
    # intel
    [rqntm, ndgts] = [[j['rqntm'] for j in PERPS if j['tcoin'] == tcoin][0], [j['ndgts'] for j in PERPS if j['tcoin'] == tcoin][0]]
    [y_lst, keys] = [[], ['sopn', 'shgh', 'slow', 'scls', 'nvol', 'rvol']]
    [sopn_leest, shgh_leest, slow_leest, scls_leest, nvol_leest, rvol_leest] = [[float(cpar[key]) for cpar in CHRT] for key in keys]
    slav_leest = [round((sopn_leest[cind]+shgh_leest[cind]+slow_leest[cind]+scls_leest[cind])/4, ndgts) for cind in range(len(CHRT))]
    dcml = len(str(rqntm).split('.')[1]) if isinstance(rqntm, float) and '.' in str(rqntm) else 0
    # process
    for cnt1 in range(cind-ntrol+1, cind+1):
        [y, tsdmc, tside, tpos] = [0, '', '', 'out']
        for cnt2 in range(cnt1, cind+1):
            if (cnt2 == cind): 
                y_lst.append(y)
                break
            if (tpos == 'out'):
                # position: new
                tside = ANLZ[cnt2]['tside']
                if tside in ['long', 'shrt']:
                    keys2 = ['ns', 'nx', 'dc', 'den', 'dvg', 'dtp', 'dsl', 'dlq', 'dcvr', 'drtn']
                    [ns_lst, nx_lst, dc_lst, den_lst, dvg_lst, dtp_lst, dsl_lst, dlq_lst, dcvr_lst, drtn_lst] = [[cpar[key] for cpar in STEP[cnt2]] for key in keys2]
                    [sprm, rzunt, drisk, drwrd] = [scls_leest[cnt2], DCSN[cnt2]['rzunt'], round(abs(1-dsl_lst[0]),4), round(abs(dtp_lst[0]-1),4)]
                    sent = round(den_lst[1] * sprm, ndgts) if (1<len(den_lst)) else None
                    [tsdmc, tpos, rx, rz, savg, nrent, ntent, sent, ntext, sext, dbpur, dbdec] = \
                    [tside, 'in', nx_lst[0], rzunt, sprm, 0, CHRT[cnt2]['tstmp'], sent, None, None, -key_Dfee, auto_round(-key_Dfee * (1/len(ns_lst)))]
                    continue
            if tpos == 'in':
                # position: update
                if tside == 'long':
                    brentchng = False
                    for cntr in range(nrent, len(dsl_lst)):
                        if (cntr < (len(dsl_lst)-1)) and ((slow_leest[cnt2]/sprm) <= den_lst[cntr+1]):
                            [brentchng, nrent, rz, sent, savg] = [True, cntr+1, round(cntr * rzunt, dcml), round(den_lst[cntr+1] * sprm, ndgts), round(dvg_lst[cntr+1] * sprm, ndgts)]
                            [dbpur, dbdec] = [round((scls_leest[cnt2]/savg)-1-key_Dfee, 4), auto_round(((scls_leest[cnt2]/savg)-1-key_Dfee) * ((nrent+1)/len(ns_lst)))]
                        if (cntr == nrent == (len(dsl_lst) - 1)) and ((slow_leest[cnt2]/sprm) <= dsl_lst[-1]):
                            dslip = random.uniform(0,1) * (1-(slow_leest[cnt2]/(sprm*dsl_lst[-1])))
                            [y, brentchng, tpos, ntext, sext] = [-1 ,True, 'out', CHRT[cnt2]['tstmp'], round(sprm*dsl_lst[nrent], ndgts)]
                            [dbpur, dbdec] = [round(max((dsl_lst[0]-1-key_Dfee-dslip), (dlq_lst[0]-1-key_Dfee)), 4), round(max((dsl_lst[0]-1-key_Dfee-dslip), (dlq_lst[0]-1-key_Dfee)), 4)]
                    if (brentchng == False) and (dtp_lst[nrent] <= (scls_leest[cnt2]/sprm)) and ((slav_leest[cnt2]/sprm) < slav_leest[cnt2-1]/sprm):
                        [y, brentchng, tpos, ntext, sext] = [1, True, 'out', CHRT[cnt2]['tstmp'], scls_leest[cnt2]]
                        [dbpur, dbdec] = [round(scls_leest[cnt2]/savg-1-key_Dfee, 4), auto_round((scls_leest[cnt2]/savg-1-key_Dfee) * ((nrent+1)/len(ns_lst)))]
                    if brentchng == False: [dbpur, dbdec] = [round(scls_leest[cnt2]/savg-1-key_Dfee, 4), auto_round((scls_leest[cnt2]/savg-1-key_Dfee) * ((nrent+1)/len(ns_lst)))]
                if tside == 'shrt':
                    brentchng = False
                    for cntr in range(nrent, len(dsl_lst)):
                        if (cntr < (len(dsl_lst)-1)) and (den_lst[cntr+1] <= (shgh_leest[cnt2]/sprm)):
                            [brentchng, nrent, rz, sent, savg] = [True, cntr+1, round(cntr * rzunt, dcml), round(den_lst[cntr+1] * sprm, ndgts), round(dvg_lst[cntr+1] * sprm, ndgts)]
                            [dbpur, dbdec] = [round(1-(scls_leest[cnt2]/savg)-key_Dfee, 4), auto_round((1-(scls_leest[cnt2]/savg)-key_Dfee) * ((nrent+1)/len(ns_lst)))]
                        if (cntr == nrent == (len(dsl_lst) - 1)) and (dsl_lst[-1] <= (shgh_leest[cnt2]/sprm)):
                            dslip = random.uniform(0,1) * ((shgh_leest[cnt2]/(sprm*dsl_lst[-1]))-1)
                            [y, brentchng, tpos, ntext, sext] = [-1, True, 'out', CHRT[cnt2]['tstmp'], round(sprm*dsl_lst[nrent], ndgts)]
                            [dbpur, dbdec] = [round(max((1-dsl_lst[0]-key_Dfee-dslip), (1-dlq_lst[0]-key_Dfee)), 4), round(max((1-dsl_lst[0]-key_Dfee-dslip), (1-dlq_lst[0]-key_Dfee)), 4)]                            
                    if (brentchng == False) and ((scls_leest[cnt2]/sprm) <= dtp_lst[nrent]) and ((slav_leest[cnt2-1]/sprm) < (slav_leest[cnt2]/sprm)):
                        [y, brentchng, tpos, ntext, sext] = [1, True, 'out', CHRT[cnt2]['tstmp'], scls_leest[cnt2]]
                        [dbpur, dbdec] = [round(1-scls_leest[cnt2]/savg-key_Dfee, 4), auto_round((1-scls_leest[cnt2]/savg-key_Dfee) * ((nrent+1)/len(ns_lst)))]
                    if brentchng == False: [dbpur, dbdec] = [round(1-scls_leest[cnt2]/savg-key_Dfee, 4), auto_round((1-scls_leest[cnt2]/savg-key_Dfee) * ((nrent+1)/len(ns_lst)))]
            if (tpos == 'out'): 
                y_lst.append(y)
                break
    return y_lst