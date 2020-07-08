import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


driver = None

def launch():
    print("Loading...")
    global driver
    driver = webdriver.Chrome()
    driver.get('https://web.skype.com/')
    driver.set_window_size(1024, 768)
    print("Loaded Skype!")

def signIn(userName, password):
    print("Signing in...")
    userNameField = driver.find_element_by_name("loginfmt")
    userNameField.clear()
    userNameField.send_keys(userName)

    time.sleep(2)
    idSIButton9 = driver.find_element_by_id("idSIButton9")
    idSIButton9.click()

    passwordField = driver.find_element_by_name("passwd")
    passwordField.clear()
    passwordField.send_keys(password)

    time.sleep(2)
    idSIButton99 = driver.find_element_by_id("idSIButton9")
    idSIButton99.submit()

    print("Signed In!")

def quit():
    print("Quitting...")
    driver.quit()

def sendMessageToSelected(groupname,content):
    print("Grouping!")
    # 搜尋開始
    search = driver.find_element_by_xpath('//div[@data-text-as-pseudo-element="People, groups & messages"]')
    time.sleep(2)
    search.click()
    time.sleep(2)
    # 搜尋群組
    searchbar = driver.find_element_by_xpath('//input[@aria-label="Search Skype"]')
    searchbar.send_keys(groupname + Keys.RETURN)
    time.sleep(2)
    element = driver.find_element_by_xpath('//div[@aria-label="GROUP CHATS"]/div[contains(@aria-label,"'+groupname+'")]')
    element_id = element.get_attribute("id")
    print(element_id)
    element.click()
    message = driver.find_element_by_xpath('//div[@aria-label="Type a message"]')
    message.send_keys(content+ Keys.RETURN)

def main(args):
    try:
        launch()
        args = parser.parse_args()
        print(args.username)
        signIn(args.username, args.password)
        time.sleep(10)
        # 前面遮蔽物
        elem = driver.find_element_by_xpath('//button[@aria-label="Got it!"]')
        if elem.is_displayed():
            elem.click()

        group = "【Gtigaming例行维护通知】"

        str = "【Gtigaming例行维护通知】 \r" \
        +"Gtigaming游戏平台，本周三（07/08）进行维护 \r" \
        +"维护时间：09:00~12:00（UTC + 8） \r" \
        +"维护期间无法使用后台，载入游戏会显示维护讯息，请贵站于维护后再行访问，感谢您的支持〜"

        time.sleep(5)
        sendMessageToSelected(group,str)

        time.sleep(5)
        group = "English"
        str = "【Gtigaming Routine Maintenance】 \r" \
        +"Date：07/01 Wednesday】 \r" \
        +"Time：09:00 ~12:00 （UTC+8) \r" \
        +"Gtigaming Platform Maintenance \r" \
        +"Please ignore this msg, if not have the games above. \r" \
        +"Please note that access of game sites and backend will be disabled during the maintenance.Thank you for kindly understanding."
        sendMessageToSelected(group,str)
    except:
        print("Something went wrong")
    finally:
        quit()

if __name__ == "__main__":
    print("Starting up...")
    parser = argparse.ArgumentParser(description='pySkypeBot: Python Skype Bot')
    parser.add_argument('-u', '--username', help='Skype User Name')
    parser.add_argument('-p', '--password', help='Skype Password')
    
    main(parser.parse_args())
