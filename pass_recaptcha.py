# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import selenium


url = "https://patrickhlauke.github.io/recaptcha/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("./crx_folder/auto_recaptcha_solver.crx")
chrome_options.add_extension("./crx_folder/recaptcha_autoclick.crx")
driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)
