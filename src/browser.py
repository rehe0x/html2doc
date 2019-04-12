from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .FileUtils import *
import os
import time


#!/usr/bin/env python3
# encoding: utf-8
class Browser:
    def __init__(self):
        self.doc_path = os.path.abspath("./doc")
        #browser = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
    
    def generate_content(self,docid):
        # 生成内容html
        file_path = os.path.abspath(self.doc_path+'/docjs.html')
        self.browser.get("file://"+file_path+"?docid="+docid)
        #browser.implicitly_wait(30)
        time.sleep(5)

        self.browser.switch_to.frame("xreader")  

        js = 'document.getElementsByClassName("reader-container")[0].style.cssText="text-align: -webkit-center;"'
        self.browser.execute_script(js)
        in_file(self.doc_path+'/'+docid+'.html',self.browser.page_source)
        #print(browser.page_source)
        #self.browser.close()
        #self.browser.quit()
br =  Browser()