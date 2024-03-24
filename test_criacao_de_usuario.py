from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCriacaoUsuario():

    url = "https://www.giulianaflores.com.br/"

    def setup_method(self, method):
        self.driver = webdriver.Chrome()

    def teardown_method(self, method)
        self.driver.quit()

    def test_criacao_usuario(self):
        self.driver.get(self.url)
        #self.driver.set_window_size(1181, 950)
        self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
        self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
        self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
        self.driver.find_element(By.ID, "ContentSite_txtName").click()
        self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Sérgio Thales Joaquim Alves")
        self.driver.find_element(By.ID, "ContentSite_txtCpf").click()
        self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("611.499.064-13")
        self.driver.find_element(By.ID, "ContentSite_txtEmail").click()
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("sergio_alves@danielvasconcelos.com.br")
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").click()
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("qo76jS62js")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("51340-310")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").click()
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("808")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").click()
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("(81) 98270-0702")
        self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
        self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
        assert self.driver.find_element(By.ID, "lblWelcome").text == "Boa Tarde, Sérgio!"
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(10) > a:nth-child(2)").click()
        self.driver.close()