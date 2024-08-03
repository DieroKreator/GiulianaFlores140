from selenium import webdriver
from selenium.webdriver.common.by import By


class TestConsultaPtoAteCarrinho():

  url = "https://www.giulianaflores.com.br/"

  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10) 
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_consulta_pto_ate_carrinho(self):
    self.driver.get(self.url)
    self.driver.maximize_window()
    self.driver.find_element(By.CSS_SELECTOR, ".item-3 > .link-menu-desktop").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "BUQUÊ DE FLORES"
    self.driver.find_element(By.CSS_SELECTOR, "#inputSearchAddress").click()
    self.driver.find_element(By.CSS_SELECTOR, "#inputSearchAddress").send_keys("41195-665")
    self.driver.find_element(By.XPATH, "//li[contains(text(),'2ª Travessa Irmã Dulce, Barreiras, Salvador - BA, ')]").click()
    self.driver.find_element(By.XPATH, "//div[contains(text(),'Aplicar')]").click()

    txtBuque = self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .title-item").text
    priceBuque = self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .actual-price").text

    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .image-content > img").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "li > span:nth-child(2)").text == txtBuque
    assert self.driver.find_element(By.CSS_SELECTOR, ".preco_prod > .precoPor_prod").text == priceBuque

    self.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
    self.driver.execute_script("window.scrollTo(0,7)")
    self.driver.find_element(By.LINK_TEXT, "31").click()
    self.driver.find_element(By.ID, "btConfirmShippingData").click()
    self.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "MEU CARRINHO"
    assert self.driver.find_element(By.LINK_TEXT, "Buquê 10 Girassóis").text == txtBuque
    assert self.driver.find_element(By.CSS_SELECTOR, ".precoPor_basket:nth-child(2)").text == priceBuque