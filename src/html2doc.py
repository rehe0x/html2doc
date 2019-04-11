from .apis import upload,convert,status,download,getHtml
from .browser import br
import pdfkit

def htmlToPdf(pname):
    pdfkit.from_file('./doc/content.html',"./doc/"+pname)

def pdfToDoc(filename):
    re = upload(filename)
    sid = re['sid']
    fid = re['id']

    rec = convert(sid,fid)
    if rec['status'] != 'success':
        pass
    durl = ''
    y = True
    while (y):
        res = status(sid,fid)
        print(res['progress'])
        if res['progress'] == 100:
            y = False
            durl = download(sid,fid,res['convert_result'])

    return durl

def pdfToDocStart(docid):
     #生成内容html
    br.generate_content(docid)
    #html to pdf
    htmlToPdf('content.pdf')
    #pdf to doc
    durl = pdfToDoc('content.pdf')
    print(durl)
    return durl