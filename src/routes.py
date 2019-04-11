#!/usr/bin/env python3
# encoding: utf-8

from flask import Flask,request,make_response
from .html2doc import pdfToDocStart

app = Flask(__name__)

@app.route('/downdoc',methods=['POST','GET'])
def downdoc():
    if request.method == 'POST':
        val = request.form.get("docid",None)
    else:
        val = request.args.get("docid",None)
    durl = pdfToDocStart(val)
    resp = make_response(durl)
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp