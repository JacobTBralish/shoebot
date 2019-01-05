from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class getShoes():
    def bot(self):
        baseURL = "https://www.adidas.com/us"

        # Creating options to open chrome incognito
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(baseURL)

        searchbar = driver.find_element_by_css_selector(".searchinput___3ump9")
        searchbar.send_keys("Mens Ultraboost")
        searchbar.send_keys(u'\ue007')

        driver.find_element(By.CSS_SELECTOR, "a[href*='DB3198']").click()
        driver.find_element_by_class_name("gl-modal__close").click()
        driver.find_element_by_class_name("gl-dropdown").click()
        driver.find_element_by_xpath("//*[@title='11']").click()

        time.sleep(2)
        iframe = driver.find_element_by_xpath("//*[@id='g-recaptcha']/div/div/iframe")
        driver.switch_to.frame(iframe)
        # Scroll in attempt to simulate human use
        driver.execute_script("window.scrollTo(0, 500)")

        driver.find_element_by_class_name("recaptcha-checkbox").click()
        driver.switch_to.default_content()
        time.sleep(3)


        # iframe2 = driver.find_element_by_xpath("/html/body/div[7]/div[4]/iframe")
        # driver.switch_to.frame(iframe2)
        # driver.find_element_by_id("recaptcha-audio-button")


        # if captcha is not None:
        #     captcha.click()

        # driver.find_element(By.ID, "add-to-bag")
        # driver.find_element_by_link_text("Checkout")
        # firstName = driver.find_element_by_css_selector("#dwfrm_shipping_shiptoaddress_shippingAddress_firstName")
        # firstName.send_keys("Jacob")
        # lastName = driver.find_element_by_css_selector("#dwfrm_shipping_shiptoaddress_shippingAddress_lastName")
        # lastName.send_keys("Bralish")


buyUB = getShoes()
buyUB.bot()




