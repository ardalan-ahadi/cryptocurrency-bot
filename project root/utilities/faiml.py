# imp
import warnings
import numpy as np
import pandas as pd

# rel
from utilities.haiml_lbly import flbly
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

# fxs
warnings.simplefilter(action='ignore')
def fitm(cind, tcoin, ntrol, SETUP, PERPS, CHRT, PROP, ANLZ, DCSN, STEP, da):  
    # process
    if cind < ntrol - 1: return ANLZ[cind]['tside']
    if ntrol - 1 <= cind:
        [da_lst, X_now] = [da.iloc[cind-ntrol+1:cind+1], da.iloc[cind].drop('Y')]
        da_lst.loc[:, 'Y'] = flbly(tcoin, ntrol, cind, PERPS, CHRT, PROP, ANLZ, DCSN, STEP)
        da_lst = da_lst[da_lst['Y'].isin([-1, 1])].replace({'Y': {-1: 0}})
        if (len(da_lst)<10) or not ((2<=(da_lst['Y'] == 0).sum()) and (2<=(da_lst['Y'] == 1).sum())): return ANLZ[cind]['tside']
        trn_indx, tst_indx = train_test_split(list(range(len(da_lst))), test_size=0.2, stratify=da_lst['Y'].tolist(), random_state=42)
        [da_trn, da_tst] = [da_lst.iloc[trn_indx], da_lst.iloc[tst_indx]]
        [X_trn, y_trn, X_tst, y_tst] = [da_trn.drop('Y', axis=1), da_trn['Y'], da_tst.drop('Y', axis=1), da_tst['Y']]
        mdl = DecisionTreeClassifier().fit(X_trn, y_trn)
        [y_pred, y_now] = [mdl.predict(X_tst), mdl.predict([X_now])[0]] 
        conf_mtrx = confusion_matrix(y_tst, y_pred)
        if (conf_mtrx.shape == (2,2)):
            [TP, TN, FP, FN] = [conf_mtrx[1, 1], conf_mtrx[0, 0], conf_mtrx[1, 0], conf_mtrx[0, 1]]
            [BM, PT] = [TP + TN, TP + FN]
            PRV = PT / (TP + TN + FP + FN) if (TP + TN + FP + FN) != 0 else 0
            ACC = (TP + TN) / (TP + TN + FP + FN) if (TP + TN + FP + FN) != 0 else 0
            BAL = (TP / (TP + FN) + TN / (TN + FP)) / 2 if (TP + FN) != 0 and (TN + FP) != 0 else 0
            [TPR, FNR] = [TP / (TP + FN) if (TP + FN) != 0 else 0, FN / (TP + FN) if (TP + FN) != 0 else 0]
            [FPR, TNR] = [FP / (FP + TN) if (FP + TN) != 0 else 0, TN / (TN + FP) if (TN + FP) != 0 else 0]
            [PPV, FDR] = [TP / (TP + FP) if (TP + FP) != 0 else 0, FP / (TP + FP) if (TP + FP) != 0 else 0]
            [FOR, NPV] = [FN / (TN + FN) if (TN + FN) != 0 else 0, TN / (TN + FN) if (TN + FN) != 0 else 0]
            F1S = (2 * PPV * TPR) / (PPV + TPR) if (PPV + TPR) != 0 else 0
            FMI = (TP / np.sqrt((TP + FP) * (TP + FN))) if (TP + FP) != 0 and (TP + FN) != 0 else 0
            [PLR, NLR] = [TPR / FPR if FPR != 0 else np.inf, FNR / TNR if TNR != 0 else np.inf]
            [MKK, DOR] = [PPV + NPV - 1, (TPR / FNR) / (FPR / TNR) if (FNR != 0 and FPR != 0) else np.inf]
            MCC = (TP * TN - FP * FN) / np.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)) if (TP + FP) * (TP + FN) * (TN + FP) * (TN + FN) != 0 else 0
            TSI = (TP + TN) / (TP + TN + FP + FN)
            score_dict = { "BM": BM, "PT": PT,
                        "PRV": PRV, "ACC": ACC, "BAL": BAL,
                        "TPR": TPR, "FNR": FNR, "FPR": FPR, "TNR": TNR,
                        "PPV": PPV, "FDR": FDR, "FOR": FOR, "NPV": NPV,
                        "F1S": F1S, "FMI": FMI, "PLR": PLR, "NLR": NLR,
                        "MKK": MKK, "DOR": DOR, "MCC": MCC, "TSI": TSI }
        if y_now == 0: return 'hodl'
        if y_now == 1: return ANLZ[cind]['tside']