# imp
import logging, os
from flask import Flask
from flask_cors import CORS

# rel
from model import jinit
from router import api
from utilities.alaccpos import faccpos

# cnf
from static.constants import glb_Thost, glb_Tport

# opt
# logging.getLogger("werkzeug").setLevel(logging.ERROR)

# acc
jaccpos = faccpos()

# app
app = Flask(__name__)
CORS(app)
app.register_blueprint(api)

# run
if __name__ == "__main__":
    jinit()
    app.run(host=glb_Thost, port=glb_Tport, debug=True)