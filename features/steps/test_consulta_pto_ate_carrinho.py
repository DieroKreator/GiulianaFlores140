import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


txtBuque = ""
priceBuque = ""

@given(u'que acesso o site da loja Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)    
    context.driver.get("https://www.giulianaflores.com.br/")

@given(u'sou direcionado para a pagina {pagina}')
def step_impl(context, pagina):
    context.driver.find_element(By.CSS_SELECTOR, ".item-3 > .link-menu-desktop").click()
    assert context.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == pagina
    context.driver.find_element(By.CSS_SELECTOR, "#inputSearchAddress").click()
    context.driver.find_element(By.CSS_SELECTOR, "#inputSearchAddress").send_keys("41195-665")
    context.driver.find_element(By.XPATH, "//li[contains(text(),'2ª Travessa Irmã Dulce, Barreiras, Salvador - BA, ')]").click()
    context.driver.find_element(By.XPATH, "//div[contains(text(),'Aplicar')]").click()

@given(u'seleciono o primeiro produto na lista')
def step_impl(context):
    txtBuque = context.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .title-item").text
    priceBuque = context.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .actual-price").text

    context.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .image-content > img").click()

@given(u'navego a pagina do produto')
def step_imp(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "li > span:nth-child(2)").text == txtBuque
    assert context.driver.find_element(By.CSS_SELECTOR, ".preco_prod > .precoPor_prod").text == priceBuque

@when(u'adiciono ao carrinho')
def step_imp(context):
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
    context.driver.execute_script("window.scrollTo(0,7)")
    context.driver.find_element(By.LINK_TEXT, "31").click()
    context.driver.find_element(By.ID, "btConfirmShippingData").click()
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click()

@then(u'sou direcionado a pagina do carrinho')
def step_imp(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "MEU CARRINHO"

@then(u'valido o nome e o preço do produto')
def step_imp(context):
    assert context.driver.find_element(By.LINK_TEXT, "Buquê 10 Girassóis").text == txtBuque
    assert context.driver.find_element(By.CSS_SELECTOR, ".precoPor_basket:nth-child(2)").text == priceBuque