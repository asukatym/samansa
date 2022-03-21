from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import sys
import csv



def autologin():
    csv_file_name = "samansa.csv"
    f = open(csv_file_name, mode = 'w', encoding='cp932', errors='ignore')
    writer = csv.writer(f, lineterminator='\n')
    csv_header = ["タイトル","いいね数"]
    writer.writerow(csv_header)

    driver = webdriver.Chrome(executable_path="/Users/tooyamaasuka/Downloads/chromedriver 2")
    url = "https://samansa.jp.auth0.com/login?state=hKFo2SA3SG1SR1hRWktjY2w0NUZ1N2w3VlpsMlEtNnBpQmN3NKFupWxvZ2luo3RpZNkgTkJNajdpaWVsaVJMdnVHeWlxX1lDZ3h5SFBDUnM0OGijY2lk2SBocjdLWXZsREx6UFdVanF3N1JNZ0c5emJhN004NFJ0Qw&client=hr7KYvlDLzPWUjqw7RMgG9zba7M84RtC&protocol=oauth2&response_type=token&access_type=&redirect_uri=https%3A%2F%2Fsamansa.com%2Fauth%2Fsigned-in&scope=openid%20profile%20email&code_challenge_method=implicit&audience=https%3A%2F%2Fsamansa.jp.auth0.com%2Fapi%2Fv2%2F&nonce=cS3omJHrmi"
    
    driver.get(url)
    time.sleep(5)

    login_id = driver.find_element_by_xpath("/html/body/div/div[3]/input[1]")
    login_pw = driver.find_element_by_xpath("/html/body/div/div[3]/input[2]")
    time.sleep(5)
    userid = "XX"
    userpasswd = "XX"

    login_id.send_keys(userid)
    login_pw.send_keys(userpasswd)
    time.sleep(5)
    login_btn = driver.find_element_by_xpath("/html/body/div/div[3]/button")
    login_btn.click()
    time.sleep(10)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(5)
    target = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/section[2]/div[1]/a')
    driver.execute_script('arguments[0].scrollIntoView(true);', target)
    time.sleep(5)
    popular = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/section[2]/div[1]/a")
    popular.click()
    time.sleep(5)
    for i in range(1,49):
        
        video = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div/div/div["+ str(i) + "]/div/a")
        driver.execute_script("arguments[0].scrollIntoView();", video)
        time.sleep(3)
        video.click()
        time.sleep(3)
       
        element1 = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div[2]/h1")
        title = element1.text
        element2 = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/p")
        string = element2.text
        csvlist = []
        csvlist.append(title)
        csvlist.append(string)
        writer.writerow(csvlist)
        driver.back()
        time.sleep(3)




autologin()

