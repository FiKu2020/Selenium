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
    driver.quit()

    def optimal_price():
        wydajnosc_wszystkich_bud = []
        for i in range(20):
            cps_budynku = driver.execute_script(f'return Game.ObjectsById[{i}].storedCps')
            cena_budynku = driver.execute_script(f"return Game.ObjectsById[{i}].price")
            wydajnosc_danego_bud = cps_budynku / cena_budynku
            wydajnosc_wszystkich_bud.append(wydajnosc_danego_bud)
