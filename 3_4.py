import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    link = "https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    option = browser.find_element(By.CSS_SELECTOR, "#ember32")
    option.click()
    write_down = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    write_down.send_keys("mail")
    write_down1 = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    write_down1.send_keys("password")
    button = browser.find_element(By.CSS_SELECTOR, "#login_form > button")
    button.click()
    time.sleep(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, links):
        qq = math.log(int(time.time() + 2))
        link = links
        browser.get(link)
        time.sleep(5)
        write_down2 = browser.find_element(By.CLASS_NAME, "ember-text-area")
        write_down2.send_keys(qq)
        button = browser.find_element(By.CSS_SELECTOR, "#ember76 > div > section > div > div.attempt__inner > div.attempt__actions > button")
        button.click()
        time.sleep(7)
        a = browser.find_element(By.CSS_SELECTOR, "#ember79 > div > div > div > div.attempt__message > span")
        assert "Correct" in a.text
        if __name__ == "__main__":
            pytest.main()
