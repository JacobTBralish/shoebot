from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class getShoes():
    def bot(self):
        baseURL = "https://www.adidas.com/us"
        driver = webdriver.Chrome()
        driver.get(baseURL)

        searchbar = driver.find_element_by_css_selector(".searchinput___3ump9")
        searchbar.send_keys("Mens Ultraboost")
        searchbar.send_keys(u'\ue007')

        driver.find_element(By.CSS_SELECTOR, "a[href*='DB3198']").click()
        driver.find_element_by_class_name("gl-modal__close").click()
        driver.find_element_by_class_name("gl-dropdown").click()
        driver.find_element_by_xpath("//*[@title='11']").click()

        time.sleep(3)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_xpath("//*[@id='recaptcha-anchor-label']").click()
        driver.switch_to.default_content()
        # if captcha is not None:
        #     captcha.click()

        driver.find_element(By.ID, "add-to-bag")
        driver.find_element_by_link_text("Checkout")
        firstName = driver.find_element_by_css_selector("#dwfrm_shipping_shiptoaddress_shippingAddress_firstName")
        firstName.send_keys("Jacob")
        lastName = driver.find_element_by_css_selector("#dwfrm_shipping_shiptoaddress_shippingAddress_lastName")
        lastName.send_keys("Bralish")


buyUB = getShoes()
buyUB.bot()




