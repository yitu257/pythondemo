from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Firefox(executable_path =r'D:\Program Files\Python\Python37\Scripts\geckodriver.exe')
#binary=dirFirefox=FirefoxBinary(r"D:\Program Files\Mozilla Firefox\firefox.exe")
#caps=webdriver.DesiredCapabilities.FIREFOX
#caps["marionette"]=False
#driver=webdriver.Firefox(firefox_binary=binary,capabilities=caps)
for i in range(0,16):
    url="https://zh.airbnb.com/s/Enshi--Hubei--China/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=U3qRpqKd&section_offset=6&items_offset="+str(i*18)
    driver.get(url)
    listHome=driver.find_elements_by_css_selector('div._y89bwt')
    for item in listHome:
        #h_types=item.find_element_by_css_selector('span._14ksqu3j:first-child').find_elements('span')
        h_types = item.find_element_by_css_selector("div._v72lrv").find_element_by_css_selector('span._14ksqu3j').text
        h_types=h_types.replace(" ","")
        h_type_list=h_types.split('·')
        hName=item.find_element_by_css_selector('div._vbshb6').text
        comments=item.find_elements_by_css_selector('span._1u3ih39j')
        if len(comments)>0:
            hScore = item.find_element_by_xpath("//span[@class='_q27mtmr']/span[1]").get_attribute("aria-label")
            hComments=comments[0].text
        else:
            hScore='无'
            hComments='无'
        print("房名：{}，房类型：{}，房间：{}，评分：{}，评价数量：{}".format(hName,h_type_list[0],h_type_list[1],hScore,hComments))
