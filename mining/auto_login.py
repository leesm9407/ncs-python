from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver')
driver.implicitly_wait(3) # Lazy Loading
driver.get('http://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('coolbeat')
driver.find_element_by_name('pw').send_keys('ilovejav@8')
driver.implicitly_wait(3) # Lazy Loading
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.implicitly_wait(3) # Lazy Loading
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(driver.page_source, 'html.parser')
notice = soup.select('div.p_inr > div.p_info > a > span')
for i in notice:
    print(i.text.strip())