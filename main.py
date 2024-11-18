import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    wait = WebDriverWait(driver, 10)
    zgoda = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-button.fc-primary-button"))
    )
    zgoda.click()
    wyb_jezyk = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"div.langSelectButton#langSelect-EN"))
    )
    wyb_jezyk.click()
    przycisk_ciastka = wait.until(
        EC.element_to_be_clickable((By.ID, "bigCookie"))
    )
    while True:
        przycisk_ciastka.click()
        time.sleep(0.1)
finally:
    # driver.quit()
    print("jest git")