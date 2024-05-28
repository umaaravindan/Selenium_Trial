from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

df = pd.read_csv('username.csv')

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open Jenkins login page
driver.get("https://localhost:8080/login")

# Wait for username and password fields to be visible
username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "j_username")))
password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "j_password")))

# Enter username and password
username_input.send_keys(df['Username'])
password_input.send_keys(df['Password'])

# Submit the login form
password_input.submit()

# Wait for login success or failure
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tasks")))
    print("Login successful!")
except:
    print("Login failed!")

# Close the browser
driver.quit()


