from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import unittest


class TesteAdroidDesafio(unittest.TestCase):
    caps = {}
    driver = None
    def setUp(self):
        # Dicionário das configurações 
        self.caps["platformName"] = "Android"
        self.caps["deviceName"] = "7e898481"
        self.caps["appPackage"] = "com.iramarferreira.app_desafio"
        self.caps["appActivity"] = "com.iramarferreira.app_desafio.MainActivity"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.caps)
        self.driver.implicitly_wait(5)

    def test_botao1(self):
        text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "campo_info")
        bt1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "botao1")
        bt1.click()
        self.driver.implicitly_wait(1)
        #print(text.text)
        assert text.text == "texto 1", 'ERRO! O campo de informação deveria ser texto 1'

    def test_botao2(self):
        text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "campo_info")
        bt2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "botao2")
        bt2.click()
        self.driver.implicitly_wait(1)
        #print(text.text)
        assert text.text == "texto 2", 'ERRO! O campo de informação deveria ser texto 2'

    def test_botao3(self):
        text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "campo_info")
        bt3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "botao3")
        bt3.click()
        self.driver.implicitly_wait(1)
        #print(text.text)
        assert text.text == "texto 3", 'ERRO! O campo de informação deveria ser texto 3'



# # Campo de informação
# text = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "campo_info")

# # Botões
# bt1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "botao1")
# bt2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "botao2")
# bt3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "botao3")


# bt1.click()
# driver.implicitly_wait(1)
# #print(text.text)
# assert text.text == "texto 1", 'ERRO! O campo de informação deveria ser texto 1'



# bt2.click()
# driver.implicitly_wait(1)
# #print(text.text)
# assert text.text == "texto 2", 'ERRO! O campo de informação deveria ser texto 2'



# bt3.click()
# driver.implicitly_wait(1)
# #print(text.text)
# assert text.text == "texto 2", 'ERRO! O campo de informação deveria ser texto 3'



# driver.quit()