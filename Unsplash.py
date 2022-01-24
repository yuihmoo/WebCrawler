import os
import time
import urllib.request

import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


my_driver = set_chrome_driver()

print("아래에 검색할 키워드를 입력하세요")
search_word = input()
# driver.find_element(By.XPATH, "/html/body/nav/form/div/input").send_keys(search_word)
my_driver.get("https://unsplash.com/s/photos/" + search_word)

SCROLL_PAUSE_TIME = 1

# 페이지 로딩 sleep
time.sleep(1)

last_height = driver.execute_script("return document.body.scrollHeight")
scroll_count = 3
# 스크롤 내리기
while True:
    my_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 대기 시간
    time.sleep(SCROLL_PAUSE_TIME)
    my_driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)

    new_height = my_driver.execute_script("return document.body.scrollHeight")
    # while 문 탈출조건
    scroll_count = scroll_count - 1
    if scroll_count == 0:
        break


def save_images(count):
    for image in images:
        try:
            image.click()
            print(image)
            time.sleep(2)
            # 클릭한 이미지 단수라서 element 를 사용해야한다.
            img_url = my_driver.find_element(By.CSS_SELECTOR,
                                             "body > div.ReactModalPortal > div > div > div.Lvlem.fBS9b > div > div > "
                                             "div:nth-child(1) > div.btXSB > div > div > button > div.omfF5.TyuJK > "
                                             "div.MorZF > div > img").get_attribute(
                "src")
            urllib.request.urlretrieve(img_url,
                                       "C:/work/python/Webcrawler/unsplash_" + str(search_word) + "/unsplash_" + str(
                                           search_word) + str(
                                           count) + ".png")
            count = count + 1
            my_driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/button").click()

        except:
            pass


if os.path.exists("unsplash_" + search_word):
    pass

if not os.path.exists("unsplash_" + search_word):
    os.mkdir("unsplash_" + search_word)
    print(search_word + " 폴더 생성 완료!")

# 페이지에 있는 모든 이미지 위치를 넣기 위해
# app > div > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div > a:nth-child(1) > div > div.MorZF > div > img
# app > div > div:nth-child(3) > div:nth-child(3) > div:nth-child(4) > div > div > div > div:nth-child(1) > figure:nth-child(1) > div > div.L34o8 > div > div > a > div > div.MorZF > div > img
# app > div > div:nth-child(3) > div:nth-child(3) > div:nth-child(4) > div > div > div > div:nth-child(2) > figure:nth-child(1) > div > div.L34o8 > div > div > a > div > div.MorZF > div > img
images = my_driver.find_elements(By.CLASS_NAME, "rEAWd")
print(images)
count = 1
save_images(count)

my_driver.close()
