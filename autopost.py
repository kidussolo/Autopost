from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv

load_dotenv()

# Locate the driver
options = Options()
options.add_argument("no-sandbox")
options.add_argument("headless")
options.add_argument("start-maximized")
options.add_argument("window-size=1900,1080")
driver = webdriver.Chrome(chrome_options=options, executable_path="./chromedriver")

print("Start Adding new Article....")
driver.get("https://ks.quintype.com/login")
sleep(3)

print("Logging in.")
# Signin to the editor dashboard
username = driver.find_element(By.XPATH, './/*[@id="em-text-field"]')
username.send_keys(os.environ.get("USERNAME"))
password = driver.find_element(By.XPATH, './/*[@id="password-field-Password"]')
password.send_keys(os.environ.get("PASSWORD"))
signin = driver.find_element(
    By.XPATH, './/*[@id="root"]/div[2]/div/div[3]/div/div[1]/span[1]/button'
)
signin.click()

sleep(5)

# Click the Add new button
add_new = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div[1]/div/div')
add_new.click()
sleep(1)

# Click story from the list
story = driver.find_element(By.XPATH, './/*[@id="add-new"]/ul/span[1]/li')
story.click()

sleep(1)

driver.switch_to.window(driver.window_handles[1])

# html_source_code = driver.execute_script("return document.body.innerHTML;")
# print(html_source_code)
# driver.close()
# go to the add story page and add title
title = driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div/div[3]/div/main/div/div[1]/div/section/div[2]/section/div[2]/div/textarea',
)
title.send_keys("A test title in headless mode :)")
sleep(1)

# add subtitle
driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div/div[3]/div/main/div/div[1]/div/section/div[2]/section/div[4]/div/textarea',
).send_keys(
    "Multiple users can login to Quintype to perform different activities. Publishers can control access to their users using fine grained permissions and roles. "
)
sleep(1)

# Add new card
driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div/div[3]/div/main/div/div[1]/div/div/span/div/div/button[1]',
).click()
sleep(1)

# Add paragraph section
driver.find_element(
    By.XPATH, '//*[contains(@class,"text_story-element-text-container")]'
).send_keys(
    "You can also create users by letting them login via some of the social authentication platforms like Facebook, Twitter, Linkedin and Google. The same is not enabled in the demo account. Please reach out to us if you need more information"
)

sleep(20)

# switch to the previous window
# driver.switch_to.window(driver.window_handles[0])

# click Submit button
driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div/header/div[2]/ul/li[3]/button',
).click()

sleep(5)

# Select sections dropdown list
driver.find_element(By.XPATH, '//*[@id="react-select-Sections"]/div[1]').click()
sleep(5)

# select section option
driver.find_element(By.ID, "react-select-2-option-5").click()
sleep(3)

# Close the side menu
driver.find_element(By.XPATH, '//*[@id="inspector-container"]/header/div[1]').click()
sleep(3)

# click Submit button
driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div/header/div[2]/ul/li[3]/button',
).click()
sleep(5)

# click Approve button
driver.find_element(
    By.XPATH,
    '//*[@id="root"]/div/header/div[2]/ul/li[3]/button',
).click()

sleep(3)
print("Finished Adding new Article.")

driver.close()
