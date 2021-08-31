from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com")
time.sleep(20)
busca = navegador.find_element_by_css_selector('div._13NKt.copyable-text.selectable-text')
busca.send_keys('Nega', Keys.ENTER)
time.sleep(2)
enviar = navegador.find_element_by_css_selector('div.p3_M1')
enviar.send_keys('Te amo!', Keys. ENTER)
