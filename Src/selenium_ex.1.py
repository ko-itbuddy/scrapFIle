from selenium import webdriver


# Chrome의 드라이버 위치를 입력
driver = webdriver.Chrome('Ext/chromedriver')

#암묵적으로 웁 자원 로드를 위해 3초까지 기다료 준다.
driver.implicitly_wait(3)

#웹페이지에 접근
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

#로그인 정보 입력
driver.find_element_by_name('id').send_keys('skvudrms54')

driver.find_element_by_name('pw').send_keys('!hcnask2211PT!')

#로그인 버튼 클릭

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
# PhantomJS의 위치

driver = webdriver.PhantomJS('Ext\phantomjs')


