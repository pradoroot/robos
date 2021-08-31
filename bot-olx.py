import time
from selenium import webdriver
from selenium.webdriver.common import keys
import pyautogui as gui

Chrome = webdriver.Chrome()
Chrome.get('https://mg.olx.com.br/belo-horizonte-e-regiao')
busca = Chrome.find_element_by__name('div.sc-hmzhuo rd4d6d-0 RyLDW sc-jTzLTM iwtnNi').click()



