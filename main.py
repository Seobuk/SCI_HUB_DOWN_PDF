# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
# from scihub import SciHub
import os

import requests
import PyQt5.QtCore
import pandas as pd
import time
import glob
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QFileInfo
from bs4 import BeautifulSoup

form_class = uic.loadUiType("./sci_hub.ui")[0]

URL_scihub = 'https://sci-hub.se/'
Count = 0



class Sci_Hub(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.PDF_Down)
        self.pushButton_2.clicked.connect(self.fileopen)
        self.pushButton_3.clicked.connect(self.folderopen)


    def PDF_Down(self):

        global URL_target
        global options
        global driver
        global html
        global soup
        global DownScript
        global Count


        IEEE_export_csv = pd.read_csv(filename[0])
        DOI_CSV = IEEE_export_csv['DOI']
        Title_CSV = IEEE_export_csv['Document Title']

        URL_target = URL_scihub + DOI_CSV[Count]

        self.textBrowser.append(Title_CSV[Count])
        self.textBrowser.append(URL_target)
        time.sleep(0)

        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        options.add_experimental_option("prefs", {
            "download.default_directory": str(os.getcwd()) + "\Down_pdf",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        driver = webdriver.Chrome(options=options)

        driver.implicitly_wait(10)
        driver.get(URL_target)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
        # soup.getText()
        # print(soup)
        #DownScript = str(soup.application).rsplit(sep='"')[1]
        # DownScript = str(soup.src)
        # print(DownScript)


        # url = 'https://zero.sci-hub.se/1814/fcdf3dd24538987f6cef0a45f0b50388/godler2000.pdf'
        # r = requests.get(url, stream=True)
        #
        # urllib.request.urlretrieve(url, "filename.pdf")
        # with open('/tmp/godler2000.pdf', 'wb') as f:
        #     f.write(r.content)
        #
        # options = webdriver.ChromeOptions()
        # #options.add_argument('headless')
        # options.add_experimental_option("prefs", {
        #     "download.default_directory": str(os.getcwd()) + "\Down_pdf",
        #     "download.prompt_for_download": False,
        #     "download.directory_upgrade": True,
        #     "safebrowsing.enabled": True
        # })
        # driver = webdriver.Chrome(options=options)
        #
        # driver.implicitly_wait(10)
        # driver.get(URL_target)
        # html = driver.page_source
        # soup = BeautifulSoup(html, 'html.parser')
        # soup.getText()
        # DownScript = str(soup.button).rsplit(sep='"')[1]
        # driver.execute_script(DownScript)
        #
        # time.sleep(1)
        # path_dir = str(os.getcwd()) + "\Down_pdf"+"\*.crdownload"
        # glob.glob(path_dir)
        # global Wait_flag
        # Wait_flag = bool(glob.glob(path_dir))
        #
        # while Wait_flag :
        #     Wait_flag = bool(glob.glob(path_dir))
        #     Count += 1
        #     return 0


        # 2. Target url
        # for i, DOI in enumerate(DOI_CSV):
        #
        #     URL_target = URL_scihub + DOI
        #
        #     self.textBrowser.append(Title_CSV[i])
        #     self.textBrowser.append(URL_target)
        #
        #     options = webdriver.ChromeOptions()
        #     #options.add_argument('headless')
        #     options.add_experimental_option("prefs", {
        #         "download.default_directory": str(os.getcwd()) + "\Down_pdf",
        #         "download.prompt_for_download": False,
        #         "download.directory_upgrade": True,
        #         "safebrowsing.enabled": True
        #     })
        #     driver = webdriver.Chrome(options=options)
        #
        #     driver.implicitly_wait(10)
        #     driver.get(URL_target)
        #     html = driver.page_source
        #     soup = BeautifulSoup(html, 'html.parser')
        #     soup.getText()
        #     DownScript = str(soup.button).rsplit(sep='"')[1]
        #     driver.execute_script(DownScript)
        #
        #     time.sleep(1)
        #     path_dir = str(os.getcwd()) + "\Down_pdf"+"\*.crdownload"
        #     glob.glob(path_dir)
        #     global Wait_flag
        #     Wait_flag = bool(glob.glob(path_dir))
        #
        #     while Wait_flag :
        #         Wait_flag = bool(glob.glob(path_dir))
        #         return 0
        # return 0


    def fileopen(self):
        global filename
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')

        print(filename[0])



        IEEE_export_csv = pd.read_csv(filename[0])
        DOI_CSV = IEEE_export_csv['DOI']
        Title_CSV = IEEE_export_csv['Document Title']

        self.textBrowser_2.append(filename[0])
        self.textBrowser.append(filename[0])


    def folderopen(self):
        global forderpath
        forderpath = QtWidgets.QFileDialog.getExistingDirectory()
        self.textBrowser_3.append(forderpath)



    # Press the green button in the gutter to run the script.


if __name__ == '__main__':

    # 0. UI loading
    app = QApplication(sys.argv)
    sci_ui = Sci_Hub()
    sci_ui.show()
    app.exec_()


