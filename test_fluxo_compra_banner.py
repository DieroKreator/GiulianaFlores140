import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFluxoCompraBanner():

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
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("oBaa9f2Lgi")
        self.driver.find_element(By.CSS_SELECTOR, "#ContentSite_ibtContinue").click()

        self.driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active .img_banner").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "PRESENTE DE PÁSCOA"
        
        self.driver.find_element(By.CSS_SELECTOR, "#inputSearchAddress").click()
        self.driver.find_element(By.CSS_SELECTOR, "#inputSearchAddress").send_keys("41195-665")
        self.driver.find_element(By.XPATH, "//li[contains(text(),'2ª Travessa Irmã Dulce, Barreiras, Salvador - BA, ')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Aplicar')]").click()
        self.driver.find_element(By.ID, "txtDsKeyWord").click()
        self.driver.find_element(By.ID, "txtDsKeyWord").send_keys("Margaridinhas Brancas e Ferrero Rocher")
        self.driver.find_element(By.ID, "btnSearch").click()
        self.driver.find_element(By.CSS_SELECTOR, ".image-content > img").click()
        assert self.driver.find_element(By.ID, "ContentSite_lblProductDsName").text == "MARGARIDINHAS BRANCAS E FERRERO ROCHER"
        assert self.driver.find_element(By.CSS_SELECTOR, ".precoPor_prod:nth-child(3)").text == "R$ 109,90"
        
        self.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
        self.driver.find_element(By.LINK_TEXT, "30").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".vlPriceCalendar").text == "R$ 28,90"
        self.driver.find_element(By.ID, "btConfirmShippingData").click()

        self.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
        assert self.driver.find_element(By.LINK_TEXT, "Margaridinhas Brancas e Ferrero Rocher").text == "Margaridinhas Brancas e Ferrero Rocher"
        assert self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .preco-total-produto > .precoPor_basket").text == "R$ 109,90"
        assert self.driver.find_element(By.CSS_SELECTOR, ".fretepago").text == "R$ 28,90"
        self.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_imbFinalize_0").click()
        
        self.driver.find_element(By.ID, "txtDsDestinationName").click()
        self.driver.find_element(By.ID, "txtDsDestinationName").send_keys("Ruan Arthur Barros")
        self.driver.find_element(By.CSS_SELECTOR, "#ContentSite_rptDeliveryAddress_rbtFgPersonalAddress_0_0_0").click()
        self.driver.find_element(By.ID, "txtDsNumber").click()
        self.driver.find_element(By.ID, "txtDsNumber").send_keys("838")
        self.driver.find_element(By.ID, "rbWhithoutGiftCard").click()
        self.driver.find_element(By.ID, "btnContinue").click()
        element = self.driver.find_element(By.ID, "ContentSite_spanPix")

        assert self.driver.find_element(By.XPATH, "//h2[contains(text(),'Pagamento')]").text == "PAGAMENTO"
        self.driver.find_element(By.CSS_SELECTOR, "#ContentSite_spanPix > img").click()
        self.driver.find_element(By.ID, "ContentSite_ibtFinalizeOrderWithPix").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "PEDIDO REALIZADO COM SUCESSO!"
        # assert self.driver.find_element(By.XPATH, "//h2[contains(text(),' NÚMERO DO SEU PEDIDO')]").text == " NÚMERO DO SEU PEDIDO"
        # elements = self.driver.find_elements(By.ID, "PixQrCode")
        # assert len(elements) > 0
        # elements = self.driver.find_elements(By.ID, "ContentSite_PrinPag")
        # assert len(elements) > 0
        
        # self.driver.find_element(By.CLASS_NAME, "logo_checkout").click()
        # assert self.driver.find_element(By.CSS_SELECTOR, ".custom-cesta-container").text == "Escolha o seu presente"
        # self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
        # self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(10) > a:nth-child(2)").click()
        # self.driver.close()