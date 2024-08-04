# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import selenium


## example.1 Auto setting driver path
# url = "https://testrecaptcha.github.io/"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_extension("./crx_folder/auto_recaptcha_solver.crx")
# chrome_options.add_extension("./crx_folder/recaptcha_autoclick.crx")
# driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# driver.get(url)


## example.2 Setting driver path by yourself
# url = "https://testrecaptcha.github.io/"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_extension("./crx_folder/auto_recaptcha_solver.crx")
# chrome_options.add_extension("./crx_folder/recaptcha_autoclick.crx")
# driver_path = "please setting your driver path"
# svc = ChromeService(driver_path)
# driver = webdriver.Chrome(service=svc,options=chrome_options)
# driver.get(url)