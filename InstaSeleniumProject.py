from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import *
# import requests
# from bs4 import BeautifulSoup
import time
hashtag = ["#데일리", "#선팔맞팔"] # 해시태그 목록


id = '' # id 입력
password = '' # pw 입력

url = "http://instagram.com"

browser = webdriver.Chrome("C:\\Users\yso00\OneDrive\바탕 화면\instagram\Instagram\chromedriver.exe")
browser.maximize_window()
browser.get(url)
time.sleep(3)

browser.find_element_by_name('username').send_keys(id)
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()  # 로그인 버튼
time.sleep(3)
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click() # 알림설정
time.sleep(2)

for i in hashtag:

    linklist =[] #hashtag 검색 했을 때 list
    feedlist =[] #profile에 들어갔을 때 list
    like_cnt = 0
    feed_cnt = 0
    error_cnt = 0


    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div').click()  # 검색창 클릭

    tag_name = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    tag_name.send_keys(i) # hashtag 입력
    time.sleep(1.5)
    tag_name.send_keys(Keys.ENTER)
    tag_name.send_keys(Keys.ENTER)
    time.sleep(3.5)
    browser.execute_script("window.scrollTo(0, 1080)")
    time.sleep(2)

    for j in range(1):
        photolink = browser.find_elements_by_tag_name("a")  # a 태그 링크 긁어오기
        for e in photolink:
            if e.get_attribute("href").count('/p/'): # a 태그 긁어온 것 중 /p/가 들어간 것만 긁어오기
                linklist.append(e.get_attribute("href"))  # linklist에 피드 링크 저장
    time.sleep(2)

    for k in range(9,18): # 최근게시물 첫 번째부터 아홉 번째 까지
        try:
            browser.get(linklist[k]) # hashtag 게시물 열기

        except:
            error_cnt += 1
            break

        profile = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a')
        profile.click() # 게시물 프로필 클릭
        time.sleep(3)


        for o in range(1):
            profile_photolink = browser.find_elements_by_tag_name("a")  # a 태그 링크 긁어오기
            
            if len(profile_photolink) <=3:
                for profile_photolinks in profile_photolink:
                    if profile_photolinks.get_attribute("href").count('/p/'): # a 태그 긁어온 것 중 /p/가 들어간 것만 긁어오기
                        feedlist.append(profile_photolinks.get_attribute("href"))  # linklist에 피드 링크 저장                    
            else:
                cnt = 0
                for profile_photolinks in profile_photolink:
                    if profile_photolinks.get_attribute("href").count('/p/'): # a 태그 긁어온 것 중 /p/가 들어간 것만 긁어오기
                        feedlist.append(profile_photolinks.get_attribute("href"))  # linklist에 피드 링크 저장
                        cnt += 1
                        if cnt == 3:
                            break
    
    for feed_open in feedlist:
        like_cnt += 1
        browser.get(feed_open)
        # 좋아요 누르기
        try:
            like = browser.find_element_by_xpath("//*[@aria-label='좋아요']")
            like.click()
        except:
            continue
        time.sleep(2)
    feed_cnt += len(feedlist)
    print("Hashtag : ", i , "\n게시물 수 : " , len(feedlist) , "\n좋아요 누른 수 :" , like_cnt , "\n오류 피드 : " , error_cnt)

browser.close()



