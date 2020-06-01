from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import string
import time

driver=webdriver.Chrome()
driver.get('https://oxu.az/interview')
for i in range(100, 1400000, 1000):
    try:
        driver.execute_script('window.scrollTo(1, '+str(i)+');')
    except:
        pass
urls = []
for x in range(0,3000):
    try:
        elems = driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/section/div["+str(x)+"]/a")
        for elem in elems:
            urls.append(elem.get_attribute('href'))
    except:
        pass
with open('news_urls_3.txt', 'w') as f:
    for item in urls:
        f.write("%s\n" % item)


filename = 'news_urls_3.txt'
file = open(filename, 'r',encoding="utf-8")
text = file.readlines()
file.close()
for i in range(len(text)):
   page = requests.get(text[i])
   time.sleep(3)
   soup = BeautifulSoup(page.content, 'html.parser')
   names = soup.findAll("div",{"class":"news-inner"})
   page = soup.find_all('p')
   y=[re.sub(r'<.+?>',r'',str(a)) for a in page]
   res = "".join(y[1:-2])
   news = 'news2.txt'
   file = open(news, 'a', encoding="utf-8")
   file.write("\n")
   file.write(res)
   file.close()