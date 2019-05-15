from selenium import webdriver
from datetime import datetime
class WebBot():
        def __init__(self):
                self.now = datetime.now()
                self.driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
                self.driver.get("https://web.whatsapp.com/")

        def EnviarMensagem(self, quem, mensagem):
                self.quem = quem
                self.mensagem = mensagem 
                span_perfis = self.driver.find_elements_by_class_name("_1wjpf")
                for span_perfil in span_perfis:
                        if span_perfil.text == self.quem:
                                span_perfil.click()

                span_input = self.driver.find_element_by_class_name("_2S1VP")
                span_input.send_keys(self.mensagem)
                span_button = self.driver.find_element_by_class_name("_35EW6")
                span_button.click()
        def Quit(self):
                self.driver.quit()

