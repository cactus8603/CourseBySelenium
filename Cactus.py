from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait  # for implicit and explict waits
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui
import time
import requests 
from bs4 import BeautifulSoup

def openChrome():
    # driver = webdriver.Chrome() # Chrome
    
    # driver = webdriver.Firefox() # Firefox

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome( options=options )

    # ,options=option
    return driver

def getRand(driver):
    
    driver.get("http://cos2.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW")

    driver.find_element_by_id("imageBoxTurnIntoTextButton-btnIconEl").click()
    time.sleep(1)
    driver.find_element_by_id("button-1005-btnIconEl").click()

    element = driver.find_element_by_id("messagebox-1001-displayfield-inputEl")

    soup = BeautifulSoup(driver.page_source, "html.parser")

    a_tags = soup.select('div#messagebox-1001-displayfield-inputEl b')
    for t in a_tags:
        return t.text
    
# 在NTNU端選課，刷新時間
def refreshTimeNTNU(driver):
    # 點選"校際選課"
    driver.find_element_by_id("tab-1027-btnInnerEl").click()

    # 等待彈出視窗並點選OK
    time.sleep(1)
    driver.find_element_by_id("button-1005-btnIconEl").click()

    # 點選"師大選課"
    driver.find_element_by_id("tab-1023-btnInnerEl").click()

# 在NTU端選課，刷新時間
def refreshTimeNTU(driver):
    # 點選"師大選課"
    driver.find_element_by_id("tab-1023-btnInnerEl").click()
    
    # 點選"校際選課"
    time.sleep(1)
    driver.find_element_by_id("tab-1027-btnInnerEl").click()

def login(driver, account, password):

    # 取得驗證碼
    Rand = getRand(driver)
    time.sleep(1)

    # 自動輸入帳號
    input_account = driver.find_element_by_id("userid-inputEl")
    input_account.send_keys( account )

    # 自動輸入密碼
    input_password = driver.find_element_by_id("password-inputEl")
    input_password.send_keys( password )

    # 自動輸入驗證碼
    input_validCode = driver.find_element_by_id("validateCode-inputEl")
    input_validCode.send_keys( Rand )

    # 登入
    driver.find_element_by_id("button-1016").click()

    time.sleep(2)

    # 點選"開始選課"
    driver.find_element_by_id("button-1017-btnIconEl").click()


# 點選"登記"
def clickAddClass():
    time.sleep(1)

    # 筆電
    # pyautogui.click(75, 310)

    # 赫彩
    pyautogui.click(25, 270)

    # 桌電
    # pyautogui.click(x, y)

    time.sleep(1)
    pyautogui.click()
    

# 刪除時間限制
def deleteTime():
    time.sleep(1)
    # 筆電
    # pyautogui.click(158, 225)

    # 赫彩
    pyautogui.click(130, 125)

    # 桌電
    # pyautogui.click(x, y)

    time.sleep(1)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.press('n')
    time.sleep(1)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.press('n')
    time.sleep(1)
    pyautogui.press('backspace')

    # 關閉devtools
    pyautogui.hotkey('ctrl', 'shift', 'j')


def selectCourseInNTNU(driver):
    account = '40747043S'
    password = 'cactus415646851'
    login(driver, account, password)
    
    # wait(driver, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, "//span[text()='登記']"))).click()
    # driver.find_element_by_id("add-btnInnerEl").click()
    # element = driver.find_elements_by_css_selector('span')
    # print(len(element))
    # element[23].click()
    # print(element)
    # element[4].click()

    # 點選"登記"
    clickAddClass()

    # 刪除時間
    deleteTime()

    # 點選到"開課序號"
    pyautogui.click(175, 255)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.press('n')
    time.sleep(1)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.press('n')
    time.sleep(1)

    # 關閉devtools
    pyautogui.hotkey('ctrl', 'shift', 'j')
"""
    # 點選"查詢"
    pyautogui.click(670, 620)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.press('n')
    time.sleep(1)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.press('n')
    time.sleep(1)
"""
    # 點選"查詢"
    # driver.find_element_by_id("button-1059-btnInnerEl").click()
"""
    try:
        driver.find_element_by_id("button-1059-btnInnerEl").click()
    except NoSuchElementException:
        print("error")
"""


if __name__ == '__main__':
    driver = openChrome()

    selectCourseInNTNU(driver)
    # time.sleep(10)
    
    # 印出抓到的
    # soup = BeautifulSoup(driver.page_source, "html.parser")
    # print(soup.prettify())
    

