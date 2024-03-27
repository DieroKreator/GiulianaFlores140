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

@then(u'uma nova conta é criada')
def step_impl(context):
        # valido cadastro com sucesso
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "li:nth-child(10) > a:nth-child(2)").click()
    assert context.driver.find_element(By.ID, "lblWelcome").text.__contains__ == "Boa Noite, Maya!"

    time.sleep(3)

    # teardown / encerramento
    context.driver.quit()