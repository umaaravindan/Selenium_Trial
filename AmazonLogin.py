from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd

df = pd.read_csv('Input.csv')

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open Jenkins login page
driver.get("https://www.amazon.in")

searchText = driver.find_element(By.ID,"twotabsearchtextbox")
searchText.send_keys("USB")
searchText.send_keys(Keys.ENTER)
 
for link in df['NextLink']: 
 #USBMenu=driver.find_element(By.PARTIAL_LINK_TEXT,"See more")
 #USBMenu.click()
  USBOptions = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,link)))
  driver.find_element(By.PARTIAL_LINK_TEXT,link)
  USBOptions.click()
  
driver.quit()
