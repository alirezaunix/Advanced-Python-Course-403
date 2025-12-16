import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait , Select
from selenium.webdriver.support import expected_conditions as EC


def simulate_user(user_id, url):
    options = Options()
    options.add_argument('--headless') 
    service = Service('')
    driver = webdriver.Firefox(service=service, options=options)
    drvicer2=webdriver.Chrome()
    try:
        driver.get(url)

        btn_1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,  '/html/body/main/div[2]/div/div[4]/div/div/div[2]/a[1]'))
        )
        btn_1.click()

        btn_2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,  '/html/body/main/div[5]/div/div[1]/div[2]/div/div[1]/div'))
        )
        btn_2.click()

        sel_1=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, '/html/body/main/div[5]/div/div[1]/div[4]/form/div[1]/label[1]/select')))
        Select(sel_1).select_by_value("1362")

        sel_2=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, '/html/body/main/div[5]/div/div[1]/div[4]/form/div[1]/label[2]/select')))
        Select(sel_2).select_by_visible_text("مرد")

        btn_3 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,  '/html/body/main/div[5]/div/div[1]/div[4]/form/div[2]/button'))
        )
        btn_3.click()

# /html/body/main/section/div[3]/label[1]
        radio_text = "آسان است"
        radio_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f'/html/body/main/section/div[3]/label[contains(text(), "{radio_text}")]'))
        )
        radio_button.click()


        print(f"[User {user_id}] Page Title after interaction: {driver.title}")

    except Exception as e:
        print(f"Error for User {user_id}: {e}")

    finally:
        driver.quit()

mbti_url = 'https://esanj.ir/myers-briggs-type-indicator-mbti'
num_users = 1

threads = []
for user_id in range(1, num_users + 1):
    thread = threading.Thread(target=simulate_user, args=(user_id, mbti_url))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Simulation for all users completed.")
