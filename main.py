from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
PATH = "C:\Program Files (x86)\chromedriver.exe"


def test_eight_components():
    driver = webdriver.Chrome(PATH, options=options)

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    #driver.quit()

def test_mbank():
    driver = webdriver.Chrome(PATH, options=options)

    driver.get("https://online.mbank.pl/pl/Login")

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="userID")
    text_box2 = driver.find_element(by=By.NAME, value="pass")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("loginlogin")
    text_box2.send_keys("password")
    submit_button.click()


    #driver.quit()

test_eight_components()
test_mbank()
