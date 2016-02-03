__author__ = 'orian'

from selenium import webdriver
import requests
import time
import xml.etree.cElementTree as ET




class Spider():

    #__phantom = webdriver.PhantomJS(executable_path='C:/Users/orian/PycharmProjects/Penny/node_modules/phantomjs/bin/phantomjs.exe')
    #__phantom = webdriver.Firefox()


    def extractCaptch(self):
            xpath = '//*[@id="cards"]/div[2]/table/tbody/tr/td/table/tbody/tr[3]/td[1]/img'
            url = "https://carder007.org/"
            self.__phantom.get(url)

            time.sleep(3)

            location = self.__phantom.find_element_by_xpath(xpath)
            src = location.get_attribute('src')
            print("captcha img url: ")
            print(src)

            with open('captcha.jpg', 'wb') as handle:
                response = requests.get(src, stream=True)

                if not response.ok:
                    print (response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)

    def login(self):

        captcha = input("Captcha? ")
        print("Captcha entered: " + captcha)

        carder_username = "sinistar"
        carder_password = "coolice#9"

        userFieldID = "txtUser"
        passFieldID = "txtPass"
        captchFieldID = "security_code"

        userFieldElement = self.__phantom.find_element_by_id(userFieldID)
        passFieldElement = self.__phantom.find_element_by_id(passFieldID)
        captchFieldElement = self.__phantom.find_element_by_id(captchFieldID)
        loginButton = self.__phantom.find_element_by_id("btnLogin")

        userFieldElement.clear()
        userFieldElement.send_keys(carder_username)
        passFieldElement.clear()
        passFieldElement.send_keys(carder_password)
        captchFieldElement.clear()
        captchFieldElement.send_keys(captcha)

        loginButton.click()


    def navigate(self):
        last_page_xpath = '//*[@id="cards"]/div[2]/a[2]'
        url = "https://carder007.org/cards.php?category_id=4&stagnant=&txtBin=&page=0"
        self.__phantom.get(url)
        last_page = self.__phantom.find_element_by_xpath(last_page_xpath).text
        return last_page

    def table_traverse(self, page):
        data = []
        url = "https://carder007.org/cards.php?category_id=4&stagnant=&txtBin=&page=" + str(page)
        self.__phantom.get(url)
        jump = True
        for tr in self.__phantom.find_elements_by_xpath('//table[@class="content_table borderstyle td_border"]//tr'):
            if (jump):
                jump = False
                continue
            tds = tr.find_elements_by_tag_name('td')
            if tds:
                print(page)
                data.append([td.text for td in tds])
        return data

    def create_xml(self):
        tree = ET.parse('cards.xml')
        root = tree.getroot()
        print(root.tag)


def main():

    spider = Spider()
    '''
    spider.extractCaptch()
    spider.login()

    last_page = int(spider.navigate())
    for i in range(0, last_page+1):
        spider.table_traverse(i)
    '''
    spider.create_xml()


if __name__=='__main__':
    main()


