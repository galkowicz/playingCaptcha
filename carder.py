__author__ = 'orian'

from selenium import webdriver
import requests
import time




class Spider():

    __phantom = webdriver.PhantomJS(executable_path='C:/Users/orian/PycharmProjects/Penny/node_modules/phantomjs/bin/phantomjs.exe')

    def extractCaptch(self):
            xpath = '//*[@id="cards"]/div[2]/table/tbody/tr/td/table/tbody/tr[3]/td[1]/img'
            url = "https://carder007.org/"
            self.__phantom.get(url)

            time.sleep(3)

            location = self.__phantom.find_element_by_xpath(xpath)
            src = location.get_attribute('src')
            print ("captcha img url: ")
            print (src)

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
        print ("Captcha entered: "+ captcha)

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
        time.sleep(5)

        print (self.__phantom.page_source)







def main():

    spider = Spider()
    spider.extractCaptch()
    spider.login()


if __name__=='__main__':
    main()


