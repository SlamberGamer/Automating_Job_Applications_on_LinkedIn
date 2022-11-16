import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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

total = 0
job_list = driver.find_elements(By.CSS_SELECTOR, '.job-card-container')

for job in job_list:
    total = total + 1
    print("--> capturing job list no: ", total)
    job.click()
    time.sleep(4)

    try:
        #CONDITION 1 - EASY APPLY -> SUBMIT APPLICATION
        try:
            easy_apply = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-apply-button--top-card button"))) #CLICK EASY APPLY BUTTON
            easy_apply.click()
            time.sleep(4)
            try:
                submit_application = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".display-flex button"))) #CLICK SUBMIT BUTTON
                submit_application.click()
                time.sleep(4)
            except:
                print("ALREADY APPLIED")
                pass
        except:
            print("ALREADY APPLIED")
            pass

    except NoSuchElementException:
        print("This Condition is not support yet :(")
        continue

time.sleep(210)
driver.close()

## Another Method to wait element
# WebDriverWait wait = new WebDriverWait(webDriver, timeoutInSeconds);
# wait.until(ExpectedConditions.visibilityOfElementLocated(By.id<locator>));
