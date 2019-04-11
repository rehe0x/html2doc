#!/usr/bin/env python3
# encoding: utf-8

from flask import Flask,request,make_response
from .html2doc import pdfToDocStart
import config

app = Flask(__name__,static_folder='../doc',static_url_path='/s3')

@app.route('/downdoc',methods=['POST','GET'])
def downdoc():
    if request.method == 'POST':
        val = request.form.get("docid",None)
    else:
        val = request.args.get("docid",None)
    durl = pdfToDocStart(val)
    url = config.DOMAIN + '/s3/' +durl
    resp = make_response(url)
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp