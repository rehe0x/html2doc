from src.routes import app
from src.html2doc import pdfToDocStart

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
    #pdfToDocStart('doc-jd8y64sgus5f7mi')