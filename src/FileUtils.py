#!/usr/bin/env python3
# encoding: utf-8

def in_file(url,data):
    with open(url, 'w+',encoding = 'utf-8') as p:
        p.write(str(data))

def read_file_last(url):
   with open(url, 'r',encoding = 'utf-8') as r:
        re = r.readlines()
        no = re[-1].strip()
        return int(no)