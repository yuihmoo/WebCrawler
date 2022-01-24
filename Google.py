import os
import time
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


driver = set_chrome_driver()

URL = 'https://www.google.co.kr/'
driver.get(URL)
print("아래에 검색할 키워드를 입력하세요")
search_word = input()
print(driver.current_url)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(
    search_word,
    Keys.ENTER)

driver.find_element(By.XPATH, "/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[3]/a").click()

if not os.path.exists(search_word):
    os.mkdir(search_word)
    print(search_word + "폴더 생성 완료!")
# 페이지에 있는 모든 이미지 위치를 넣기 위해 elements
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1

for image in images:
    try:
        image.click()
        print(image)
        time.sleep(2)
        # 클릭한 이미지 단수라서 element 를 사용해야한다.
        imgUrl = driver.find_element(By.CSS_SELECTOR,
                                     "#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id > div > a > img").get_attribute(
            "src")
        urllib.request.urlretrieve(imgUrl,
                                   "C:/work/python/Webcrawler/" + str(search_word) + "/" + str(search_word) + str(
                                       count) + ".jpg")
        count = count + 1
    except:
        pass

driver.quit()
driver.close()
