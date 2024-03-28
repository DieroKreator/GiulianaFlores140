import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'que acesso o site Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()              # instanciar o objeto do Selenium webDriver especializado para o Chrome
    context.driver.maximize_window()                 # maximizar a janela do navegador
    context.driver.implicitly_wait(10)    

    context.driver.get("https://www.giulianaflores.com.br/")  # abrir o navegador no endereco do site alvo

@given(u'sou direcionado para a pagina {pagina} a partir do banner')
def step_impl(context, pagina):
    context.driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active .img_banner").click()
    assert context.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == pagina

@given(u'navego a pagina do produto {produto}')
def step_impl(context, produto):
    context.driver.find_element(By.CSS_SELECTOR, "#inputSearchAddress").click()
    context.driver.find_element(By.CSS_SELECTOR, "#inputSearchAddress").send_keys("41195-665")
    context.driver.find_element(By.XPATH, "//li[contains(text(),'2ª Travessa Irmã Dulce, Barreiras, Salvador - BA, ')]").click()
    context.driver.find_element(By.XPATH, "//div[contains(text(),'Aplicar')]").click()
    context.driver.find_element(By.ID, "txtDsKeyWord").click()
    context.driver.find_element(By.ID, "txtDsKeyWord").send_keys("Margaridinhas Brancas e Ferrero Rocher")
    context.driver.find_element(By.ID, "btnSearch").click()
    context.driver.find_element(By.CSS_SELECTOR, ".image-content > img").click()
    assert context.driver.find_element(By.ID, "ContentSite_lblProductDsName").text == produto
    assert context.driver.find_element(By.CSS_SELECTOR, ".precoPor_prod:nth-child(3)").text == "R$ 109,90"

@given(u'valido o produto na pagina {pagina}')
def step_impl(context, pagina):   
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
    context.driver.find_element(By.LINK_TEXT, "29").click()
    time.sleep(5)
    context.driver.find_element(By.ID, "btConfirmShippingData").click()
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click()

    assert context.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == pagina
    assert context.driver.find_element(By.LINK_TEXT, "Margaridinhas Brancas e Ferrero Rocher").text == "Margaridinhas Brancas e Ferrero Rocher"
    assert context.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .preco-total-produto > .precoPor_basket").text == "R$ 109,90"
    assert context.driver.find_element(By.CSS_SELECTOR, ".fretepago").text == "R$ 28,90"
    context.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_imbFinalize_0").click()   

@given(u'preencho os dados na pagina {pagina}')
def step_impl(context, pagina): 
    assert context.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == pagina
    context.driver.find_element(By.ID, "txtDsDestinationName").click()
    context.driver.find_element(By.ID, "txtDsDestinationName").send_keys("Ruan Arthur Barros")
    context.driver.find_element(By.CSS_SELECTOR, "#ContentSite_rptDeliveryAddress_rbtFgPersonalAddress_0_0_0").click()
    context.driver.find_element(By.ID, "txtDsNumber").click()
    context.driver.find_element(By.ID, "txtDsNumber").send_keys("838")
    context.driver.find_element(By.ID, "rbWhithoutGiftCard").click()
    context.driver.find_element(By.ID, "btnContinue").click()
    element = context.driver.find_element(By.ID, "ContentSite_spanPix")

@when(u'eu faco o {pagina}')
def step_impl(context, pagina):
     assert context.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == pagina
     context.driver.find_element(By.CSS_SELECTOR, "#ContentSite_spanPix > img").click()
     context.driver.find_element(By.ID, "ContentSite_ibtFinalizeOrderWithPix").click()

@when(u'preencho com sucesso os campos obrigatorios de cadastro')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
    context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
    context.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Maya Vanessa Daiane Figueiredo")
    context.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("841.146.800-39")
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("maya_figueiredo@agenciadbd.com")
    context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("uUhnjTD4PF")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("93347-155")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("239")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("51986873890")
    context.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()

@given(u'preencho os campos de login com usuario {usuario} e senha {senha}')
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
        context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
        context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
        context.driver.find_element(By.ID, "ContentSite_txtEmail").click()
        context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(usuario)
        context.driver.find_element(By.ID, "ContentSite_txtPassword").click()
        context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys(senha)
        context.driver.find_element(By.CSS_SELECTOR, "#ContentSite_ibtContinue").click()

@then(u'o usuario esta conetado com sucesso')
def step_impl(context):
     context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()

     assert context.driver.find_element(By.ID, "lblWelcome").text == "Boa Noite, Maya!"
     # teardown / encerramento
     context.driver.quit()

@then(u'uma nova conta é criada')
def step_impl(context):
    # valido cadastro com sucesso
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "li:nth-child(10) > a:nth-child(2)").click()
    assert context.driver.find_element(By.ID, "lblWelcome").text.__contains__ == "Boa Noite, Maya!"

    # teardown / encerramento
    context.driver.quit()

@then(u'exibe a mensagem de erro {mensagem} no login')
def step_impl(context, mensagem):
     # validar a mensagem de erro
    assert context.driver.find_element(By.XPATH, "//span[contains(text(),'e-mail ou senha inválidos!')]").text == "e-mail ou senha inválidos!"
     # teardown / encerramento
    context.driver.quit()

@then(u'a compra e realizada com sucesso')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "PEDIDO REALIZADO COM SUCESSO!"

    # teardown / encerramento
    context.driver.quit()