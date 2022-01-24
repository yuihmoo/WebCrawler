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


driver = set_chrome_driver()
print("아래에 검색할 키워드를 입력하세요")
search_word = input()
# driver.find_element(By.XPATH, "/html/body/nav/form/div/input").send_keys(search_word)
driver.get("https://www.iconfinder.com/search?q=" + str(search_word) + "&price=free")

SCROLL_PAUSE_TIME = 2

last_height = driver.execute_script("return document.body.scrollHeight")
scroll_count = 3
# 스크롤 내리기
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # 대기 시간
#     time.sleep(SCROLL_PAUSE_TIME)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
#     time.sleep(SCROLL_PAUSE_TIME)
#
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     # while 문 탈출조건
#     scroll_count = scroll_count - 1
#     if scroll_count == 0:
#         break


def saveImages(count):
    for image in images:
        try:
            print(image)
            time.sleep(2)

            # 클릭한 이미지 단수라서 element 를 사용해야한다.
            imgUrl = driver.find_element(By.CSS_SELECTOR,
                                         "#search-results > div.continuous-pagination.icon-preview-inline > div > div:nth-child(" + str(
                                             count) + ") > div > a > div > img").get_attribute(
                "src")
            urllib.request.urlretrieve(imgUrl,
                                       "C:/work/python/Webcrawler/icon_" + str(search_word) + "/icon_" + str(
                                           search_word) + str(
                                           count) + ".png")
            count = count + 1
            if count == 26:
                break

        except:
            pass


if not os.path.exists(search_word):
    os.mkdir("icon_" + search_word)
    print(search_word + " 폴더 생성 완료!")
# 페이지에 있는 모든 이미지 위치를 넣기 위해
images = driver.find_elements(By.CLASS_NAME, "d-block")
count = 1
saveImages(count)

driver.close()
