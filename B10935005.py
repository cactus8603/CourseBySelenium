from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait  # for implicit and explict waits
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import requests 
from bs4 import BeautifulSoup
import sys


def openChrome():
    # driver = webdriver.Chrome() # Chrome
    
    # driver = webdriver.Firefox() # Firefox

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome( options=options )

    # ,options=option
    return driver

def getRand(driver):
    
    driver.get("http://cos3.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW")

    time.sleep(3)
    driver.find_element_by_id("imageBoxTurnIntoTextButton-btnIconEl").click()
    time.sleep(1)
    driver.find_element_by_id("button-1005-btnIconEl").click()

    element = driver.find_element_by_id("messagebox-1001-displayfield-inputEl")

    soup = BeautifulSoup(driver.page_source, "html.parser")

    a_tags = soup.select('div#messagebox-1001-displayfield-inputEl b')
    for t in a_tags:
        return t.text
    

def deleteTime(driver):
    deleteTime = "var element = document.getElementById('now'); element.parentNode.removeChild(element);"
    driver.execute_script(deleteTime)

def login(driver, account, password):

    # 取得驗證碼
    Rand = getRand(driver)
    time.sleep(1)

    # 自動輸入帳號
    input_account = driver.find_element_by_id("userid-inputEl")
    input_account.send_keys( account )
    time.sleep(1)

    # 自動輸入密碼
    input_password = driver.find_element_by_id("password-inputEl")
    input_password.send_keys( password )
    time.sleep(1)

    # 自動輸入驗證碼
    input_validCode = driver.find_element_by_id("validateCode-inputEl")
    input_validCode.send_keys( Rand )
    time.sleep(1)

    # 登入
    driver.find_element_by_id("button-1016").click()
    time.sleep(2)

    # 教育學分
    driver.find_element_by_id("button-1005-btnIconEl").click()
    time.sleep(1)

    # 點選"開始選課"
    driver.find_element_by_id("button-1017-btnIconEl").click()
    time.sleep(2)
    

def selectCourseInNTNU(driver, classSerialNumber):
    # 基本資料
    account = '40642104S'
    password = 'pig78563'
    login(driver, account, password)

    # 刪除時間
    time.sleep(2)
    deleteTime = "document.getElementById('now').remove();"
    driver.execute_script(deleteTime)

    # 切換frame
    time.sleep(2)
    driver.switch_to.frame("stfseldListDo")
    
    # 點選"查詢"
    # driver.find_element_by_id("query-btnInnerEl").click()

    # 點選"加選"
    driver.find_element_by_id("add-btnInnerEl").click()

    #####選課畫面#####

    # 輸入開課序號
    input_classSerialNumber = driver.find_element_by_id("serialNo-inputEl")
    input_classSerialNumber.send_keys( classSerialNumber )

    # 開始查詢
    driver.find_element_by_id("button-1059-btnInnerEl").click()
    time.sleep(1)

    # 點選課程
    driver.find_element_by_id("grid-body").click()
    driver.find_element_by_id("gridview-1123-body").click()

    # 點選"課程大綱"
    # driver.find_element_by_id("book_open1-btnInnerEl").click()

    while True:
        # 點選"加選"
        driver.find_element_by_id("save-btnInnerEl").click()
        time.sleep(10)

        # 點選"OK"
        driver.find_element_by_id("button-1005-btnIconEl").click()
        time.sleep(10)
    

def selectCourseInNTU(driver, classSerialNumber):
    # 基本資料
    account = ''
    password = ''
    login(driver, account, password)

    # 刪除時間
    time.sleep(2)
    deleteTime = "document.getElementById('now').remove();"
    driver.execute_script(deleteTime)

    # 切換frame
    time.sleep(2)
    driver.switch_to.frame("stfseldListDo")
    
    # 點選"查詢"
    driver.find_element_by_id("query-btnInnerEl").click()

    #####選課畫面#####

    # 輸入開課序號
    input_classSerialNumber = driver.find_element_by_id("serialNo-inputEl")
    input_classSerialNumber.send_keys( classSerialNumber )

    # 開始查詢
    driver.find_element_by_id("button-1059-btnInnerEl").click()
    
    # 點選課程
    driver.find_element_by_id("grid-body").click()
    driver.find_element_by_id("gridview-1123-body").click()

    # 點選"課程大綱"
    driver.find_element_by_id("book_open1-btnInnerEl").click()


if __name__ == '__main__':
    driver = openChrome()

    selectCourseInNTNU(driver, 2842)
    time.sleep(10)
    
    # 印出抓到的
    # soup = BeautifulSoup(driver.page_source, "html.parser")
    # print(soup.prettify())
    

