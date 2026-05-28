# imp
import os, json, threading


# MY
# dbs
lock = threading.Lock()
json_lst = os.listdir('database')
# for resume
for cpar in json_lst:
    if cpar != 'ICONS.json': # and cpar not in ['PERPS.json', 'SRTR.json', 'VBSY.json', 'VLTD.json']:
        os.remove(os.path.join('database', cpar))
# for resume
def jinit():
    # for resume
    if True: # not os.path.exists(PERPS): # comment line
        jsave(os.path.join('database', 'PERPS.json'), [])
        jsave(os.path.join('database', 'SRTR.json'), [])
        jsave(os.path.join('database', 'VBSY.json'), [])
        jsave(os.path.join('database', 'VLTD.json'), [])
        jsave(os.path.join('database', 'RBSY.json'), [])
        jsave(os.path.join('database', 'RLTD.json'), [])
        with open('database/tab.txt', 'w') as file: file.write('hltd')
        with open('database/dfrk.txt', 'w') as file: file.write(f"inf")
        with open('database/dgud.txt', 'w') as file: file.write(f"-inf")
        with open('database/domd.txt', 'w') as file: file.write(f"-inf")
        with open('database/sneedtot.txt', 'w') as file: file.write('')
        jsave(os.path.join('database', 'norder_lst.json'), []) # troin nadare
        # with open('database/nprmsn.txt', 'w') as file: file.write(f"-1")
        # with open('database/brvrs_vl.txt', 'w') as file: file.write(f"-1")
    # for resume



"""
# GROK (begin)
if __name__ == '__main__':
    json_lst = os.listdir('database')
    for cpar in json_lst:
        if cpar != 'ICONS.json':
            try:
                os.remove(os.path.join('database', cpar))
            except FileNotFoundError:
                pass

def jinit():
    files_to_create = ['PERPS.json', 'SRTR.json', 'VBSY.json', 'VLTD.json',
                       'RBSY.json', 'RLTD.json', 'norder_lst.json']
    for fname in files_to_create:
        path = os.path.join('database', fname)
        if not os.path.exists(path):
            jsave(path, [])
    # rest of your jinit code...
    with open('database/tab.txt', 'w') as f: f.write('hltd')
    with open('database/dfrk.txt', 'w') as f: f.write("inf")
    with open('database/dgud.txt', 'w') as f: f.write("-inf")
    with open('database/domd.txt', 'w') as f: f.write("-inf")
    with open('database/sneedtot.txt', 'w') as f: f.write('')
    jsave(os.path.join('database', 'norder_lst.json'), []) # troin nadare
    # with open('database/nprmsn.txt', 'w') as file: file.write(f"-1")
    # with open('database/brvrs_vl.txt', 'w') as file: file.write(f"-1")
# GROK (end)
"""



def jsave(filepath, data):
    lock = threading.Lock()
    with lock:
        with open(filepath, 'w') as f: json.dump(data, f, indent=4)
def jload(filepath):
    lock = threading.Lock()
    data = None
    while data == None:
        with lock:
            try: 
                with open(filepath, 'r') as f: data = json.load(f)
            except: data = None
    return data

# cnf
from static.constants import \
    set_Nperps, set_Rassets_oto, set_Ndeals, set_Nserial, \
    set_Tsort, set_Tdscnd, set_Ntimer, set_Nturn, \
    set_Ntfrm, set_Troll, set_Tback, \
    set_Ncook_dyn_oto, set_Dsglm, set_Dfltr, set_Nwhale, set_Nrsdl,\
    set_Nzrrr_dyn_oto, set_Tzrrr, set_Rzrrr, set_Nzrrd, set_Nzrlm, set_Nzliq, \
    set_Nstep_dyn_oto, set_Dstep_dyn_oto, set_Nxbeg_dyn_oto, set_Dcbeg, set_Dcfin

# set
SETUP = {
    "set_Nperps": set_Nperps, "set_Rassets_oto": set_Rassets_oto, "set_Ndeals": set_Ndeals, "set_Nserial": set_Nserial,
    "set_Tsort": set_Tsort, "set_Tdscnd": set_Tdscnd, "set_Ntimer": set_Ntimer, "set_Nturn": set_Nturn,
    "set_Ntfrm": set_Ntfrm, "set_Troll": set_Troll, "set_Tback": set_Tback,
    "set_Ncook_dyn_oto": set_Ncook_dyn_oto, "set_Dsglm": set_Dsglm, "set_Dfltr": set_Dfltr, "set_Nwhale": set_Nwhale, "set_Nrsdl": set_Nrsdl,
    "set_Nzrrr_0": set_Nzrrr_dyn_oto[0], "set_Nzrrr_1": set_Nzrrr_dyn_oto[1], "set_Tzrrr": set_Tzrrr, "set_Rzrrr": set_Rzrrr, "set_Nzrrd": set_Nzrrd, "set_Nzrlm": set_Nzrlm, "set_Nzliq": set_Nzliq, 
    "set_Nstep_dyn_oto": set_Nstep_dyn_oto, "set_Dstep_dyn_oto": set_Dstep_dyn_oto, "set_Nxbeg_dyn_oto": set_Nxbeg_dyn_oto, "set_Dcbeg": set_Dcbeg, "set_Dcfin": set_Dcfin,
}
jsave(os.path.join('database', 'SETUP.json'), SETUP)
jsave(os.path.join('database', 'FORM.json'), SETUP)