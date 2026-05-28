# imp
import threading, os
from flask import Blueprint, request, jsonify, render_template

# rel
from utilities.uperps import uperps
from utilities.alsets import fsets
from utilities.alcpad import fcpad
from utilities.alsrtr import fsrtr
from utilities.aldotm import ftrd, fmng

# jsl
from model import jload

# api
api = Blueprint('api', __name__)

# rut
@api.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')
# rol
@api.route("/cpad/", methods=["GET"])
def cpad():
    [tcoin, tcola, tsorc] = [request.args.get('tcoin'), request.args.get('tcola'), request.args.get('tsorc')]
    with open('database/slct_slave.txt', 'w') as file: file.write(tcoin)
    if tsorc == 'btn': 
        with open('database/slct_master.txt', 'w') as file: file.write(tcoin)
        with open('database/slct_cola.txt', 'w') as file: file.write(tcola)
    for filename in os.listdir('database'):
        if filename.startswith('cpad_'):
            file_path = os.path.join('database', filename)
            with open(file_path, 'w') as file: file.write('0')
    with open('database/cpad_' + tcoin + '.txt', 'w') as file: file.write('1')
    # thread = threading.Thread(target=fcpad, args=(tcoin,))
    return fcpad(tcoin, tcola, tsorc)
@api.route('/srtr/', methods=["GET"])
def srtr():
    return fsrtr()
@api.route('/vrtrd/', methods=["GET"])
def vrtrd():
    vrlsf = request.args.get('vrlsf')
    ftrd(vrlsf)
    VBSY = jload(os.path.join('database', 'VBSY.json'))
    RBSY = jload(os.path.join('database', 'RBSY.json'))
    return jsonify({'VBSY': VBSY, 'RBSY': RBSY })
@api.route('/vrmng/', methods=["GET"])
def vrmng():
    vrlsf = request.args.get('vrlsf')
    fmng(vrlsf)
    VBSY = jload(os.path.join('database', 'VBSY.json'))
    RBSY = jload(os.path.join('database', 'RBSY.json'))
    return jsonify({'VBSY': VBSY, 'RBSY': RBSY })
# rcv
@api.route('/cpad-r/', methods=["GET"])
def cpad_r():
    with open('database/slct_slave.txt', 'r') as file: tcoin = file.read()
    with open('database/cpad_' + tcoin + '.txt', 'r') as file: tcpad = file.read()
    return jsonify({'tcpad': tcpad})
@api.route('/srtr-r/', methods=["GET"])
def srtr_r():
    SRTR = jload(os.path.join('database', 'SRTR.json'))
    return jsonify({'SRTR': SRTR})
@api.route('/setup-r/', methods=["GET"])
def setup_r():
    SETUP = jload(os.path.join('database', 'FORM.json'))
    return jsonify({'SETUP': SETUP})
@api.route('/tab-r/', methods=["GET"])
def tab_r():
    with open('database/tab.txt', 'r') as file: tab = file.read()
    return jsonify({'tab': tab})
@api.route("/perps/", methods=["GET"])
def perps():
    PERPS = uperps()
    with open('database/sblnc.txt', 'r') as file: sblnc = file.read()
    return jsonify({'PERPS': PERPS, 'balance': sblnc})
@api.route('/master/', methods=["GET"])
def master():
    with open('database/slct_master.txt', 'r') as file: tcoin = file.read()
    with open('database/slct_cola.txt', 'r') as file: tcola = file.read()
    return jsonify({'tcoin': tcoin, 'tcola': tcola}) 
@api.route("/vbsy/", methods=["GET"])
def vbsy():
    VBSY = jload(os.path.join('database', 'VBSY.json'))
    return jsonify({'VBSY': VBSY})  
@api.route("/rbsy/", methods=["GET"])
def rbsy():
    RBSY = jload(os.path.join('database', 'RBSY.json'))
    return jsonify({'RBSY': RBSY})
@api.route('/uhvr/', methods=["GET"])
def uhvr():
    tcoin = request.args.get('tcoin')
    ULTD = jload(os.path.join('database', 'ULTD_' + tcoin + '.json'))
    HLTD = jload(os.path.join('database', 'HLTD_' + tcoin + '.json'))
    VLTD = jload(os.path.join('database', 'VLTD.json'))
    RLTD = jload(os.path.join('database', 'RLTD.json'))
    return jsonify({'ULTD': ULTD, 'HLTD': HLTD, 'VLTD': VLTD, 'RLTD': RLTD})
@api.route('/vr/', methods=["GET"])
def vr():
    VLTD = jload(os.path.join('database', 'VLTD.json'))
    VLTD_none = [cpar['tcoin'] for cpar in VLTD if cpar['ntext'] is None]
    RLTD = jload(os.path.join('database', 'RLTD.json'))
    RLTD_none = [cpar['tcoin'] for cpar in RLTD if cpar['ntext'] is None]
    return jsonify({'VLTD_none': VLTD_none, 'RLTD_none': RLTD_none})
@api.route('/sneedtot/', methods=["GET"])
def sneedtot():
    with open('database/sneedtot.txt', 'r') as file: sneedtot = file.read()
    return jsonify({'sneedtot': sneedtot})
# snd
@api.route('/setup-w/', methods=["POST"])
def setup_w():
    data = request.json
    return fsets(data)    
@api.route('/tab-w/', methods=["GET"])
def tab_w():
    tab = str(request.args.get('tab'))
    with open('database/tab.txt', 'w') as file: file.write(tab)
    return jsonify({'tab': tab})