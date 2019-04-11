import requests
import math, random, time, string
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

domain = "https://pdf2doc.com"

def getHtml():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    url = 'http://1s1k.eduyun.cn/portal/redesign/index/index.jsp?t=2&sdResIdCaseId=8aee80bf69fff344016a028c9b5d0b70&sessionKey=TjhiVU3pUB3ejHXqrj1r'
    r = requests.get(url,headers=headers)
    print(r.text)

def upload(filename):
    sid = __sid()
    url = domain + "/upload/" + sid
    formdata = [
			("name", filename),
			("id", __fid()),
			("file", (filename, open("./doc/"+filename, "rb"), "application/pdf"))
		]
    formdata = MultipartEncoder(formdata)
    boundary = formdata.boundary[2:]
    header = {"Content-Type": "multipart/form-data, boundary=" + boundary}
    re = requests.post(url,data=formdata,headers=header)
    reJ = re.json()
    reJ['sid'] = sid
    return reJ

def convert(sid,fid):
    url = domain + "/convert/%s/%s" % (sid, fid)
    re = requests.get(url)
    return re.json()

def status(sid,fid):
    url = domain + "/status/%s/%s" % (sid, fid)
    re = requests.get(url)
    return re.json()

def download(sid,fid,filename):
    url = domain + "/download/%s/%s/%s" % (sid, fid, filename)
    return url


def __sid():
		chars = "0123456789abcdefghiklmnopqrstuvwxyz"
		result = ""
		for x in range(16):
			char = int(math.floor(random.random() * len(chars)))
			result += chars[char:char + 1]
		return result

def __fid():
    uid = __base32(int(time.time() * 1000)) # Python equivalent of new Date().getTime().toString(32)
    for x in range(5):
        uid += __base32(int(math.floor(random.random() * 65535)))
    return "o_" + uid + __base32(1)

def __base32(x):
		# Heavily modified version of https://www.quora.com/How-do-I-write-a-program-in-Python-that-can-convert-an-integer-from-one-base-to-another/answer/Nayan-Shah?srid=uVDVH
		result = ""
		while x > 0:
			result = string.printable[x % 32] + result
			x //= 32
		return result