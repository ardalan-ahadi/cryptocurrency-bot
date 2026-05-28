# imp
import os
from flask import jsonify

# jsl
from model import jsave

# fxs
def fsets(data):
    # set: SETUP
    b = data['b']
    otobus = [ data['set_Rassets_oto'], data['set_Nzrrr_0'], data['set_Nzrrr_1'], 
               data['set_Nstep_dyn_oto'], data['set_Dstep_dyn_oto'], data['set_Nxbeg_dyn_oto'], data['set_Ncook_dyn_oto'] ]
    SETUP = {
        "set_Nperps": int(data['set_Nperps']),
        "set_Rassets_oto": str(otobus[0]) if otobus[0][0]=='a' else float(otobus[0]),
        "set_Ndeals": int(data['set_Ndeals']),
        "set_Nserial": int(data['set_Nserial']),
        "set_Tsort": str(data['set_Tsort']),
        "set_Tdscnd": str(data['set_Tdscnd']),
        "set_Ntimer": int(data['set_Ntimer']),
        "set_Nturn": int(data['set_Nturn']),
        "set_Ntfrm": int(data['set_Ntfrm']),
        "set_Troll": str(data['set_Troll']),
        "set_Tback": str(data['set_Tback']),
        "set_Ncook_dyn_oto": str(otobus[6]) if otobus[6][0] =='a' else int(otobus[6]),
        "set_Dsglm": float(data['set_Dsglm']),
        "set_Dfltr": float(data['set_Dfltr']),
        "set_Nwhale": int(data['set_Nwhale']),
        "set_Nrsdl": int(data['set_Nrsdl']),
        "set_Nzrrr_0": str(otobus[1]) if otobus[1][0]=='a' else int(otobus[1]),
        "set_Nzrrr_1": str(otobus[2]) if otobus[2][0]=='a' else int(otobus[2]),
        "set_Tzrrr": str(data['set_Tzrrr']),
        "set_Rzrrr": float(data['set_Rzrrr']),
        "set_Nzrrd": int(data['set_Nzrrd']),
        "set_Nzrlm": int(data['set_Nzrlm']),
        "set_Nzliq": int(data['set_Nzliq']),
        "set_Nstep_dyn_oto": str(otobus[3]) if otobus[3][0]=='a' else int(otobus[3]),
        "set_Dstep_dyn_oto": str(otobus[4]) if otobus[4][0]=='d' else float(otobus[4]),
        "set_Nxbeg_dyn_oto": str(otobus[5]) if otobus[5][0] in ['o','m'] else int(otobus[5]),
        "set_Dcbeg": float(data['set_Dcbeg']),
        "set_Dcfin": float(data['set_Dcfin']),
    }
    # output: SETUP
    jsave(os.path.join('database', 'FORM.json'), SETUP)
    if b == 'setup': jsave(os.path.join('database', 'SETUP.json'), SETUP)
    return jsonify({'message': 'success!'})