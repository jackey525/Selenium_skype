# Selenium_skype

## headless來關閉瀏覽器的方式執行程式
```    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
```

## docker 執行

```
$ git clone https://github.com/jackey525/Selenium_skype.git
$ cd Selenium_skype
$ docker run -it -v $(pwd):/usr/workspace joyzoursky/python-chromedriver:3.6-alpine3.7-selenium sh
$ cd /usr/workspace
$ pip3 install requests
$ python3 skype.py -u 帳號 -p 密碼
```
## 指令
python3 skype.py -u 帳號 -p 密碼

## 功能
跑 chrome 模擬操作   搜尋群組  傳送訊息


## Requirements

### Basic requirements (for Mac):

 1. [Homebrew](http://brew.sh/)

 2. Python

	```
	$ brew install python
	```

 3. Chromedriver

	```
	$ brew install chromedriver
	```

## ubuntu Setup

```
$ pip3 install selenium
$ pip3 install requests
```
```
如果 機器本身沒有 chrome ，請安裝google-chrome

$ sudo apt update

$ sudo apt install google-chrome-stable
```
```
機器本身已經安裝 chrome
請查詢 chrome 版本

進入此頁面選擇下載Chromedriver： 
http://chromedriver.storage.googleapis.com/index.html

下載並安裝

$ wget http://chromedriver.storage.googleapis.com/83.0.4103.14/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip
$ chmod +x chromedriver
$ sudo mv chromedriver /usr/bin/
```


## Test run

```
$ git clone https://github.com/jackey525/Selenium_skype.git
$ cd Selenium_skype
$ python3 skype.py -u 帳號 -p 密碼
```

