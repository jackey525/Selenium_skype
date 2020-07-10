import argparse
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

driver = None


def launch():
    print("Loading...")
    global driver
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome()
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
    
    time.sleep(5)
    while True:
        try:
            if driver.find_element_by_id("passwordError").is_displayed():
                print("Signed In error!")
                raise EOFError
                break
        except EOFError:
            print('got it')
            raise
        except:
            break

    print("Signed In!")

def quit():
    print("Quitting...")
    driver.quit()

def sendMessageToSelected(groupname,content):
    print(groupname+"Grouping!")
    # 搜尋開始
    number = 0
    while True:
        number += 1
        try:
            if driver.find_element_by_xpath('//div[@data-text-as-pseudo-element="人員、群組與訊息"]').is_displayed():
                driver.find_element_by_xpath('//div[@data-text-as-pseudo-element="人員、群組與訊息"]').click()
                break
        except:
            print("沒有 人員、群組與訊息")
            pass
        print("找英文")
        try:
            if driver.find_element_by_xpath('//div[@data-text-as-pseudo-element="People, groups & messages"]').is_displayed():
                driver.find_element_by_xpath('//div[@data-text-as-pseudo-element="People, groups & messages"]').click()
                print("找到搜尋按鈕")
                break
        except:
            if number > 10:
                print("搜尋按鈕 失敗")
                break
            print("在找一次 搜尋按鈕")
            
            # 可能前面有遮蔽物  去除
            while True:
                try:
                    if driver.find_element_by_xpath('//button[@aria-label="Got it!"]').is_displayed():
                        driver.find_element_by_xpath('//button[@aria-label="Got it!"]').click()
                        break
                except:
                    print("Got it!")    
                    break
            
            time.sleep(2)
            continue


    time.sleep(1)
    # 搜尋群組
    while True:
        try:
            if driver.find_element_by_xpath('//input[@aria-label="搜尋 Skype"]').is_displayed():
                searchbar = driver.find_element_by_xpath('//input[@aria-label="搜尋 Skype"]')
                break
        except:
            pass
        
        try:
            if driver.find_element_by_xpath('//input[@aria-label="Search Skype"]').is_displayed():
                searchbar = driver.find_element_by_xpath('//input[@aria-label="Search Skype"]')
                print("開始搜尋")
                break
        except:
            break

    searchbar.send_keys(groupname + Keys.RETURN)
    time.sleep(3)

    
    try:
        if driver.find_element_by_xpath('//div[@aria-label="GROUP CHATS"]/div[contains(@aria-label,"'+groupname+'")]').is_displayed():
            driver.find_element_by_xpath('//div[@aria-label="GROUP CHATS"]/div[contains(@aria-label,"'+groupname+'")]').click()
    except:
        print("沒抓到群組="+groupname)
        str_split = groupname.split("-", 1)
        print("重新搜尋群組="+str_split[0])
        searchbar.clear()
        time.sleep(1)
        searchbar.send_keys(str_split[0] + Keys.RETURN)
        time.sleep(3)
        try:
            if driver.find_element_by_xpath('//div[@aria-label="GROUP CHATS"]//div[@data-text-as-pseudo-element="MORE"]').is_displayed():
                driver.find_element_by_xpath('//div[@aria-label="GROUP CHATS"]//div[@data-text-as-pseudo-element="MORE"]').click()
                time.sleep(2)
                print("塞選抓群組="+groupname)
                driver.find_element_by_xpath('//div[@aria-label="'+groupname+', "]').click()
        except:
            print("塞選抓群組="+groupname)
            driver.find_element_by_xpath('//div[@aria-label="GROUP CHATS"]/div[contains(@aria-label,"'+groupname+'")]').click()
        

    # element = driver.find_element_by_xpath('//div[@aria-label="GROUP CHATS"]/div[contains(@aria-label,"'+groupname+'")]')
    # element_id = element.get_attribute("id")
    # print(element_id)
    
    # 輸入談話訊息
    print("傳送訊息")
    message = driver.find_element_by_xpath('//div[@aria-label="Type a message"]')
    arrContent = content.split('\n')
    for str in arrContent:
        message.send_keys(str)
        message.send_keys(Keys.SHIFT,'\n')
    message.send_keys('\n')
    print("傳送訊息結束")

def main(args):
    try:
        launch()
        args = parser.parse_args()
        print(args.username)
        signIn(args.username, args.password)
        time.sleep(5)
        # 前面遮蔽物
        while True:
            try:
                if driver.find_element_by_xpath('//button[@aria-label="Got it!"]').is_displayed():
                    driver.find_element_by_xpath('//button[@aria-label="Got it!"]').click()
                    break
            except:
                print("Got it! error")    
                break

        # group = "【Gtigaming例行维护通知】"

        with open('./group/gtioo', 'r') as file:
            groupArr = file.readlines()
        print(groupArr)


        str = '【Gtigaming例行维护通知】 \n' \
        +'Gtigaming游戏平台，本周三（07/08）进行维护 \n' \
        +'维护时间：09:00~12:00（UTC + 8） \n' \
        +'维护期间无法使用后台，载入游戏会显示维护讯息，请贵站于维护后再行访问，感谢您的支持〜'

        time.sleep(5)
        for group in groupArr:
            # 搜尋開始
            groupname = group.replace('\n', '')
            print("groupname is"+ groupname)
            if groupname:
                sendMessageToSelected(groupname,str)
                time.sleep(10)

        metadata= {
            "chat_id": "-1001413107249",
            "text": "skype 通知客戶 佈署成功",
        }
        r = requests.post("https://api.telegram.org/botxxxxxx:yyyyyyyyyyyyyyyyyyyyyyyyyy/sendMessage", metadata, headers={'Content-Type':'application/x-www-form-urlencoded', 'Accept': 'application/json'})        

    except:
        print("Something went wrong")
        metadata= {
            "chat_id": "-1001413107249",
            "text": "skype 通知客戶 佈署失敗",
        }
        r = requests.post("https://api.telegram.org/botxxxxxx:yyyyyyyyyyyyyyyyyyyyyyyyyy/sendMessage", metadata, headers={'Content-Type':'application/x-www-form-urlencoded', 'Accept': 'application/json'})

    finally:
        quit()

if __name__ == "__main__":
    print("Starting up...")
    parser = argparse.ArgumentParser(description='pySkypeBot: Python Skype Bot')
    parser.add_argument('-u', '--username', help='Skype User Name')
    parser.add_argument('-p', '--password', help='Skype Password')
    
    main(parser.parse_args())
