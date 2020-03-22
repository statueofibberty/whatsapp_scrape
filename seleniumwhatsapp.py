from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://web.whatsapp.com/')
input("scan qr")

driver.get('https://web.whatsapp.com/send?phone=PHONE_NUMBER&text=&source=&data=')
time.sleep(13)

test3 = driver.find_elements_by_xpath("//span[@class='_19RFN _1ovWX _F7Vk']")

for test in test3:
    print(test.get_attribute("title"))