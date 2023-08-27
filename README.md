# Selenium Automation with undetected_chromedriver | headless mode

This repository provides an example of using Selenium along with undetected_chromedriver for automating web browsing tasks.
The combination of Selenium and undetected_chromedriver can help bypass certain detection mechanisms that websites might have in place.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- Python (version X.X)
- undetected_chromedriver (install using `pip install undetected-chromedriver`)
- Selenium (install using `pip install selenium`)

## Getting Started

1. Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/zakichan719/selenium_main.git
   ```

3. Open the `undetected_chromedriver.py` file in your preferred text editor.

 

## Explanation

The provided Python script demonstrates how to use Selenium along with undetected_chromedriver to automate web browsing. Here's a breakdown of the script:

```python
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

options = uc.ChromeOptions()

# Create a new undetected Chrome driver instance
driver = uc.Chrome(use_subprocess=True)
# Set headless mode  >> the Chrome browser will run without a graphical user interface.
# options.add_argument('--headless') 
# Add any necessary configurations to 'options' if required
 

# Pause the script for 10 seconds
sleep(10)

# Open the specified URL using the Chrome driver
driver.get('https://zakichan.com/')
sleep(10)

driver.quit()


```

## Note

- The `undetected_chromedriver` library is used to provide an undetectable WebDriver instance. This can help avoid detection mechanisms that some websites employ to prevent automated access.
- By enabling headless mode (--headless), the Chrome browser will run without a graphical user interface.
  all lign >> options.add_argument('--headless')   

 
