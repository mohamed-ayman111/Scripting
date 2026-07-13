from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()
# Open website
print("Before open linkedin.")
driver.get("https://www.linkedin.com/signup")
print("URL:", driver.current_url)
print("Title:", driver.title)

with open("page.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("HTML Saved")
print("Linkedin opened.")
time.sleep(10)

# Click submit button.
#join_button = driver.find_element(By.ID, "join-form-submit")
buttons = driver.find_elements(By.TAG_NAME, "button")

print("Buttons:", len(buttons))

for b in buttons:
    print("----------------")
    print(b.get_attribute("outerHTML"))
join_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "join-form-submit"))
)
print("button element founded.")
join_button.click()
print("Finsh click button process.")
time.sleep(20)

# Find email, password and join elements
print("ُEmail element searching...")
email = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "email-or-phone"))
)
#email = driver.find_element(By.ID,"email-or-phone")
print("Email element founded.")
email.send_keys("test@gmail.com")
print("Email writed.")
email.click()
print("Finsh email process.")
time.sleep(3)


password = driver.find_element(By.ID, "password")
print("Password element founded.")
password.send_keys("Testpassword@123")
print("Password writed.")
password.click()
print("Finsh email process.")
time.sleep(3)

# Click submit button.
join_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "join-form-submit"))
)

print("putton element founded.")
join_button.click()
print("Finsh click button process.")
time.sleep(3)

# second page
# Write first name.
""""
firstname = driver.find_element(By.ID, "first-name")
firstname.send_keys("NameName1")
firstname.click()
time.sleep(3)
# Write last name.
lastname = driver.find_element(By.ID, "last-name")
lastname.send_keys("NameName2")
lastname.click()
time.sleep(3)
"""
"""
join_submit = driver.find_element(By.ID, "join-form-submit")
join_submit.click()
time.sleep(3)
"""
input("Press enter to exit.")
driver.quit()
