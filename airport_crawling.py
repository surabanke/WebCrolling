from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


option = Options()
option.binary_location = "/Applications/Google Chrome.app"
service = Service('./chromedriver_mac_arm64/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get("https://www.airportal.go.kr/knowledge/statsnew/realtime/airline.jsp#")


time.sleep(5)
search_box=driver.find_element(By.CLASS_NAME, 'input1') 
search_box = driver.find_element(By.XPATH,'/html/body/form/table[3]/tbody/tr[2]/td[2]/table[3]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/table[1]/tbody/tr/td[3]/input')
search_box.send_keys('ID') # type the ID


search_box_1=driver.find_element(By.NAME, 'df_passwd')
search_box_1 = driver.find_element(By.XPATH,'/html/body/form/table[3]/tbody/tr[2]/td[2]/table[3]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/table[2]/tbody/tr/td[3]/input')
search_box_1.send_keys('Password') # type the ID
search_box_1.send_keys(Keys.RETURN)
time.sleep(3)

search_box_2 = driver.find_element(By.CLASS_NAME,'link')
search_box_2 = driver.find_element(By.XPATH,'//*[@id="content_areaSub"]/div[1]/div/ul/li[3]/a').send_keys(Keys.ENTER)

search_box_3 = driver.find_element(By.CLASS_NAME,'dep')
search_box_3 = driver.find_element(By.XPATH,'//*[@id="content_areaSub"]/div[1]/div/ul/li[3]/div/ul/li[2]/a').send_keys(Keys.ENTER) #  실시간 통계

search_box_4 = driver.find_element(By.CLASS_NAME,'link')
search_box_4 = driver.find_element(By.XPATH,'//*[@id="content_areaSub"]/div[1]/div/ul/li[4]/a').send_keys(Keys.ENTER) # 항공사별 운송실적

search_box_5 = driver.find_element(By.CLASS_NAME,'dep')
search_box_5 = driver.find_element(By.XPATH,'//*[@id="content_areaSub"]/div[1]/div/ul/li[4]/div/ul/li[3]/a').send_keys(Keys.ENTER)

time.sleep(3)

search_box_6 = driver.find_element(By.CLASS_NAME,'checkbox-inline.i-checks') # 외항사, space는 .로
search_box_6 = driver.find_element(By.XPATH,'//*[@id="realContents"]/div/div[2]/div[1]/div[2]/div/div/div[3]/label[2]').send_keys(Keys.ENTER)

search_box_7 = driver.find_element(By.CLASS_NAME,'mainSearchBtnArea') # 검색 
search_box_7 = driver.find_element(By.XPATH,'//*[@id="realContents"]/div/div[2]/div[1]/div[1]/a[2]').send_keys(Keys.ENTER)

time.sleep(2)

start_date = ['20170101', '20170201', '20170301', '20170401', '20170501', '20170601', '20170701', '20170801', '20170901', '20171001', '20171101', '20171201', '20180101', '20180201', '20180301', '20180401', '20180501', '20180601', '20180701', '20180801', '20180901', '20181001', '20181101', '20181201', '20190101', '20190201', '20190301', '20190401', '20190501',\
               '20190601', '20190701', '20190801', '20190901', '20191001', '20191101', '20191201', '20200101', '20200201', '20200301', '20200401', '20200501', '20200601', '20200701', '20200801', '20200901', '20201001', '20201101', '20201201', '20210101', '20210201', '20210301', '20210401', '20210501', '20210601', '20210701', '20210801', '20210901', '20211001',\
                  '20211101', '20211201', '20220101', '20220201', '20220301', '20220401', '20220501', '20220601', '20220701', '20220801', '20220901', '20221001', '20221101', '20221201', '20230101', '20230201', '20230301', '20230401', '20230501']
end_date = ['20170131', '20170228', '20170331', '20170430', '20170531', '20170630', '20170731', '20170831', '20170930', '20171031', '20171130', '20171231', '20180131', '20180228', '20180331', '20180430', '20180531', '20180630', '20180731', '20180831', '20180930', '20181031', '20181130', '20181231', '20190131', '20190228', '20190331', '20190430', '20190531', '20190630',\
             '20190731', '20190831', '20190930', '20191031', '20191130', '20191231', '20200131', '20200228', '20200331', '20200430', '20200531', '20200630', '20200731', '20200831', '20200930', '20201031', '20201130', '20201231', '20210131', '20210228', '20210331', '20210430', '20210531', '20210630', '20210731', '20210831', '20210930', '20211031', '20211130', '20211231',\
                  '20220131', '20220228', '20220331', '20220430', '20220531', '20220630', '20220731', '20220831', '20220930', '20221031', '20221130', '20221231', '20230131', '20230228', '20230331', '20230430', '20230531']

# 날짜 
end_date.sort(reverse=True)

for i in range(len(start_date)):
    end = int(end_date[i][6:8])
    
    search_box_8 = driver.find_element(By.CLASS_NAME,'ti-calendar').click() # 달력 이미지는 .click() 시작일
    search_box_8 = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/table/thead/tr[2]/th[1]').click()
    tbody = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/table/tbody') # /html/body/div[2]/div[1]/table/tbody/tr[1]/td[2]
    trs = tbody.find_elements(By.TAG_NAME,'tr')
    find = 0
    for index,tr in enumerate(trs):
        tds = tr.find_elements(By.TAG_NAME,'td')
        for index,td in enumerate(tds):
            if td.text == '1':
                td.click()
                find = 1
                break
            else:
                pass
        if find == 1:
            break

    time.sleep(1)
    find = 0
    cnt=0
    search_box_9 = driver.find_element(By.XPATH,'//*[@id="dateEnd"]/div/span/i').click() # 종료일 
    driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/table/thead/tr[2]/th[1]').click() # 뒤로가기 버튼
    tbody_2 = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/table/tbody')
    trs_2 = tbody_2.find_elements(By.TAG_NAME,'tr')

    for index,tr in enumerate(trs_2):
        tds = tr.find_elements(By.TAG_NAME,'td')
        
        for index,td in enumerate(tds):
            if cnt > 1 and (td.text == str(end)):
                find += 1
                td.click()
                break
            else:
                pass
        cnt += 1
        if find == 1:
            break
    
    driver.find_element(By.XPATH,'//*[@id="realContents"]/div/div[2]/div[1]/div[2]/div/div/div[3]/label[2]').send_keys(Keys.ENTER) 
    driver.find_element(By.XPATH,'//*[@id="realContents"]/div/div[2]/div[1]/div[1]/a[2]').send_keys(Keys.ENTER) # 검색
    driver.find_element(By.XPATH,'//*[@id="realContents"]/div/div[2]/div[1]/div[1]/a[1]').send_keys(Keys.ENTER) # 엑셀로 다운로드
    time.sleep(6)
