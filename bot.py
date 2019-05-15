from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import html2text
import time
import os
import csv


class cbaBot():
    def __init__(self, username, password):
        #self.browser = webdriver.Chrome(executable_path=r'/home/ubuntu/Desktop/webscrapper/chromedriver')
        self.browser = webdriver.Firefox(executable_path=r'/home/ubuntu/Desktop/webscrapper/geckodriver')
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("http://10.66.10.70/phpmyadmin/index.php")

        #print(self.browser.page_source.encode("utf-8"))

        usernameInput = self.browser.find_element_by_id("input_username")
        passwordInput = self.browser.find_element_by_id("input_password")
        goButton =  self.browser.find_element_by_id("input_go")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        goButton.send_keys(Keys.ENTER)

        time.sleep(1)

        return self.browser

    def closeBrowser(self):
        self.browser.close()

    def getAcessos(self, localBrowser):
        self.browser = localBrowser
        opco = self.browser.find_elements_by_class_name("expander")[2]
        opco.click()
        time.sleep(1)

        opco_dev = self.browser.find_element_by_partial_link_text("opco_dev")
        opco_dev.click()
        time.sleep(2)

        tb_cba_acessos = self.browser.find_element_by_partial_link_text("tb_cba_acessos")
        tb_cba_acessos.click()
        time.sleep(2)

        acessos_table = self.browser.find_element_by_class_name("table_results").get_attribute('innerHTML')

        crapp_table= html2text.html2text(acessos_table)
        list_crapp = crapp_table.split("\n")
        clean_list = []

        for i in range(len(list_crapp)):
            if i>25 and ((i-25)%11==0 or (i-26)%11==0):
                if((i-26)%11==0):
                    clean_list.append(list_crapp[i].replace('\n',''))
                else:
                    clean_list.append(list_crapp[i])
                    clean_list.append('\n')

        clean_table = ''.join(clean_list)

        text_file = open("Output.txt", "w")
        text_file.write(clean_table)
        text_file.close()

        #tbButton =  self.browser.find_element_by_partial_link_text("tb_cba_acessos")

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()
