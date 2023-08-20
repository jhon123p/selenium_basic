from selenium import webdriver
from selenium.webdriver.common.by import By
#modulo update navegador 
from webdriver_manager.chrome import ChromeDriverManager as cm
from selenium.webdriver.chrome.service import Service
#verificar situação do navegador
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

servico = Service(EC().install())
#driver_navegador = webdriver.Chrome(service=servico)

path_extension_checkbox = ''
chrorume_options = webdriver.ChromeOptions()
chrorume_options.add_argument(f'--load-extension={path_extension_checkbox}')

url = 'https://www.google.com/recaptcha/api2/demo'

drive = webdriver.Chrome(options = chrorume_options,service=servico)

drive.get(url)
time.sleep(50)
#recaptcha-demo ,  recaptcha-demo-form0
#input[@name='username']
#form[@id='loginForm']
#form[input/@name='username']
chrorume_options = webdriver.ChromeOptions()
chrorume_options.add_argument(f'--load-extension={path_extension_checkbox}')

drive.find_element(By.ID,'recaptcha-anchor').click()





'''element = driver_navegador.find_element(By.XPATH, "//select[@name='name']")
all_options = element.find_elements(By.TAG_NAME, "option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()'''