# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
# from scihub import SciHub
import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from bs4 import BeautifulSoup

form_class = uic.loadUiType("./sci_hub.ui")[0]


class Sci_Hub(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.pushButton_2.clicked.connect(self.fileopen)
        self.pushButton_3.clicked.connect(self.folderopen)
        self.pushButton_4.clicked.connect(self.appendTextFunction)

    def pushButtonClicked(self):
        print("Hello")
        return 0

    def appendTextFunction(self):
        # self.Textbrowser이름.append()
        # Textbrowser에 있는 글자를 가져오는 메서드
        self.textBrowser.append("Append Text")

    def fileopen(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        #print(filename[0])

        # self.DOI_CSV = ....

        self.textBrowser_2.append(filename[0])

    def folderopen(self):
        forderpath = QtWidgets.QFileDialog.getExistingDirectory()
        self.textBrowser_3.append(forderpath)

    # def download(self):
        for ii, doi in self.DOI_CSV:
            # URL

    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # 0. UI loading
    app = QApplication(sys.argv)
    sci_ui = Sci_Hub()
    sci_ui.show()

    # File 경로 PYQT
    # https://dotsnlines.tistory.com/501
    # https://balsamic-egg.tistory.com/19

    # result = sh.download('https://ieeexplore.ieee.org/document/6249598', path='paper.pdf')
    # 1. Read CSV at pandas
    IEEE_export_csv = pd.read_csv('export2022.02.12-08.35.51.csv')
    DOI_CSV = IEEE_export_csv['DOI']

    # print(csv_test.shape)  # C,R values output ex:(15,30)
    # print(type(DOI_CSV))  # 전체 출력
    # print(DOI_CSV[1])
    # print(DOI_CSV.head())          #앞에서부터 출력 df 5
    # print(DOI_CSV.tail())          #뒤에서부터 출력 df 5
    # print(csv_test.loc[[1,2,3]])   #열 출력 방법

    # 2. Target url
    URL_scihub = 'https://sci-hub.se/'
    URL_target = URL_scihub + DOI_CSV[10]

    for ii, doi in enumerate(DOI_CSV):
        print(ii, URL_scihub+doi)

    # 3. Chrom option
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_experimental_option("prefs", {
        "download.default_directory": str(os.getcwd())+"\Down_pdf",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome(options=options)
    # 4. Start loading and download
    driver.get(URL_target)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    soup.getText()
    DownScript = str(soup.button).rsplit(sep='"')[1]
    driver.execute_script(DownScript)

    # 5-1. 새로운 탭을 생성 하기
    # driver.execute_script('window.open("https://naver.com");')
    # time.sleep(1)

    # 6. 다운로드 경로 변경
    # https://cozynow.tistory.com/43

    # 7. 창안띄우고 하는 방법
    # https://ingus26.tistory.com/77
    # 8. qt 파일선택
    #https://balsamic-egg.tistory.com/19

    app.exec_()
