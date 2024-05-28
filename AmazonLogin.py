from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os

df = pd.read_csv('Input.csv')
current_directory = os.getcwd()

# Create a directory named "screenshots" if it doesn't exist
screenshots_directory = os.path.join(current_directory, "screenshots")
if not os.path.exists(screenshots_directory):
    os.makedirs(screenshots_directory)
# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open Jenkins login page
driver.get("https://www.amazon.in")

searchText = driver.find_element(By.ID,"twotabsearchtextbox")
searchText.send_keys("USB")
searchText.send_keys(Keys.ENTER)
 
for i,link in enumerate(df['NextLink']): 
 #USBMenu=driver.find_element(By.PARTIAL_LINK_TEXT,"See more")
 #USBMenu.click()
  USBOptions = WebDriverWait(driver,25).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,link)))
  driver.find_element(By.PARTIAL_LINK_TEXT,link)
  USBOptions.click()
  
  screenshot_filename = os.path.join(screenshots_directory, f"Screenshot_{i}.png")
  driver.save_screenshot(screenshot_filename) 
  
driver.quit()
