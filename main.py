import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # user_input = input()
    # if input == "kill":
    #     driver.quit()
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    wait = WebDriverWait(driver, 10)
    zgoda = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-button.fc-primary-button"))
    )
    zgoda.click()
    wyb_jezyk = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.langSelectButton#langSelect-EN"))
    )
    wyb_jezyk.click()
    przycisk_ciastka = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "bigCookie"))
    )
    def dostepnosc_budynku(i):
        return driver.execute_script(f"return Game.ObjectsById[{i}].locked ")
    def opt_cena_bud():
        id_opt_bud = None
        najw_opt_bud = float(0)
        for i in range(20):
            try:

                cps_danego_bud = driver.execute_script(f"return Game.ObjectsById[{i}].storedCps")
                cena_danego_bud = driver.execute_script(f"return Game.ObjectsById[{i}].price")
                dostepnosc_danego_bud = dostepnosc_budynku(i)

                if dostepnosc_danego_bud == True:
                    continue
                wydajnosc = cena_danego_bud / cps_danego_bud
                if wydajnosc < najw_opt_bud:
                    najw_opt_bud = wydajnosc
                    id_opt_bud = i
                
            except Exception as e:
                pass
        return id_opt_bud
    def kup_opt_bud(id_bud):
        try:
            driver.execute_script(f"Game.ObjectsById[{id_bud}].buy()")
        except:
            pass


    while True:
        try:
            przycisk_ciastka.click()
            ciastka = float(driver.execute_script("return Game.cookies"))
            print(ciastka)
            id_bud = opt_cena_bud()
            if id_bud is not None:
                cena_bud = float(driver.execute_script(f"return Game.ObjectsById[{id_bud}].price"))
                if ciastka >= cena_bud:
                    kup_opt_bud(id_bud)
        except Exception as e:
            print(f"cos walnelo: {e}")
        #time.sleep(0.1)
finally:
    driver.quit()
a