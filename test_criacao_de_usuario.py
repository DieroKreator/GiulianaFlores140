import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCriacaoUsuario():

    url = "https://www.giulianaflores.com.br/"

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 

    def teardown_method(self, method):
        self.driver.quit()

    @pytest.mark.skip(reason="temporaly ignore")
    def test_criacao_usuario(self):
        self.driver.get(self.url)
        self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
        self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
        self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
        self.driver.find_element(By.ID, "ContentSite_txtName").click()
        self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Ruan Arthur Barros")
        self.driver.find_element(By.ID, "ContentSite_txtCpf").click()
        self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("077.381.423-08")
        self.driver.find_element(By.ID, "ContentSite_txtEmail").click()
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("ruan_arthur_barros@dpi.indl.com.br")
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").click()
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("oBaa9f2Lgi")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("41195-665")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("838")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").click()
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("71999285159")
        self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
        self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()

        assert self.driver.find_element(By.ID, "lblWelcome").text.__contains__ == "Boa Noite, Ruan!"

        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(10) > a:nth-child(2)").click()
        self.driver.close()