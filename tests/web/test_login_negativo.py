import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginNegativo():

    url = "https://www.giulianaflores.com.br/"

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 

    def teardown_method(self, method):
        self.driver.quit()

    # @pytest.mark.skip(reason="temporaly ignore")
    def test_criacao_usuario(self):
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
        self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
        self.driver.find_element(By.ID, "ContentSite_txtEmail").click()
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("ruan_arthur_barros@dpi.indl.com.br")
        self.driver.find_element(By.ID, "ContentSite_txtPassword").click()
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("wrongPassword")
        self.driver.find_element(By.CSS_SELECTOR, "#ContentSite_ibtContinue").click()

        assert self.driver.find_element(By.XPATH, "//span[contains(text(),'e-mail ou senha inválidos!')]").text == "e-mail ou senha inválidos!"