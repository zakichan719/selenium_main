from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
options = uc.ChromeOptions()


# Set headless mode >> the Chrome browser will run without a graphical user interface.
#options.add_argument('--headless')  

driver = uc.Chrome(use_subprocess=True)
sleep(10)

# operate the driver as you would with selenium
driver.get('https://zakichan.com/') 
sleep(10)
driver.quit()