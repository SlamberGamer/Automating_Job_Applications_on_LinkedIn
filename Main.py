import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# https://www.youtube.com/watch?v=zV508AcOzM0

username = "username"
password = "password"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3337056475&f_AL=true&keywords=debug&refresh=true")
driver.implicitly_wait(10)

element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//header/nav[1]/div[1]/a[2]")))
element.click()

element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']")))
element.click()
element.send_keys(username)

element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
element.click()
element.send_keys(password)
element.send_keys(Keys.RETURN)
time.sleep(3)
job_list = driver.find_elements(By.CSS_SELECTOR, '.job-card-container')

total = 0

for job in job_list:
    total = total + 1
    print("--> capturing job list no: ",total)
    job.click()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)

time.sleep(210)
driver.close()