# coding:utf-8

import psutil
import time
import os
import sys
sys.path.append(os.getcwd() + "/class/core/")
import public

from flask import Flask, session
from flask import Blueprint, render_template
from flask import jsonify
from flask import request
from flask import make_response
from flask import Response


dashboard = Blueprint('dashboard', __name__, template_folder='templates')


@dashboard.route("/")
def index():
    print session['code']
    return render_template('default/index.html')


@dashboard.route("/code")
def code():
    import vilidate
    vie = vilidate.vieCode()
    codeImage = vie.GetCodeImage(80, 4)
    try:
        from cStringIO import StringIO
    except:
        from StringIO import StringIO

    out = StringIO()
    codeImage[0].save(out, "png")

    session['code'] = public.md5("".join(codeImage[1]).lower())

    img = Response(out.getvalue(), headers={'Content-Type': 'image/png'})
    ret = make_response(img)
    return ret


@dashboard.route("/check_login")
def checkLogin():
    return render_template('default/login.html')


@dashboard.route("/login")
def login():
    return render_template('default/login.html')


@dashboard.route("/do_login", methods=['POST'])
def doLogin():
    return public.returnJson(False, 'LOGIN_USER_EMPTY')
