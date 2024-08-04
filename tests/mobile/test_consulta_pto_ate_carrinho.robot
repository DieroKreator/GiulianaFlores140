# This sample code supports Appium Robot client >=2
# pip install robotframework-appiumlibrary
# Then you can paste this into a file and simply run with Robot
#
# Find keywords at: http://serhatbolsu.github.io/robotframework-appiumlibrary/AppiumLibrary.html
#
# If your tests fails saying 'did not match any elements' consider using 'wait activity' or
# 'wait until page contains element' before a click command

*** Settings ***
Library           AppiumLibrary
Test Teardown     Close Application

*** Variables ***
${SAUCE_USERNAME}    karklose  
${REMOTE_URL}    https://${SAUCE_USERNAME}:5c1fd24c-1340-40fb-92b7-9915dd2fdc98@ondemand.us-west-1.saucelabs.com:443/wd/hub


*** Test Cases ***
Test Case Name
    Open Application    ${REMOTE_URL}    
    ...    platformName=Android    appium:platformVersion=9.0    
    ...    appium:deviceName=Samsung Galaxy S9 FHD GoogleAPI Emulator    
    ...    appium:deviceOrientation=portrait    
    ...    appium:app=storage:filename=Giuliana Flores_2.0.56_APKPure.apk    
    ...    appium:appPackage=br.com.giulianaflores.android    
    ...    appium:appActivity=br.com.giulianaflores.android.MainActivity    
    # ...    browserName=undefined    
    ...    appium:ensureWebviewsHavePages=${True}    
    ...    appium:nativeWebScreenshot=${True}    
    # ...    sauce:options=[object Object]    
    ...    appium:newCommandTimeout=${3600}    
    ...    appium:connectHardwareKeyboard=${True}
    
    Swipe    ${568}    ${504}    ${378}    ${1442}
    ${link_pular} =    Set Variable     xpath=//android.widget.TextView[@text="Pular"]
    Click Element    ${link_pular}
    ${btn_entrar} =    Set Variable     xpath=//android.view.ViewGroup[@content-desc="Entrar"]
    Click Element    ${btn_entrar}
    ${field_email} =    Set Variable     xpath=//android.widget.EditText[@text="   Digite seu e-mail ou CPF"]
    Input Text    ${field_email}    amanda_dacosta@structureesquadrias.com.br
    ${field_senha} =    Set Variable     xpath=//android.widget.EditText[@text="Digite sua senha"]
    Input Text    ${field_senha}    Choco@2024
    ${btn_entrar} =    Set Variable     xpath=//android.view.ViewGroup[@content-desc="Entrar"]
    Click Element    ${btn_entrar}
    Swipe    ${576}    ${351}    ${488}    ${1141}
    ${link_resposta} =    Set Variable     xpath=//android.widget.TextView[@text="NÃO, OBRIGADO"]
    Click Element    ${link_resposta}
    @{finger} =    Create List    ${88}    ${1213}
    @{positions} =    Create List    ${finger}
    Tap With Positions    ${100}    ${positions}
    ${el7} =    Set Variable     xpath=//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]
    Click Element    ${el7}
    ${btn_burger} =    Set Variable     xpath=//android.widget.TextView[@text=""]
    Click Element    ${btn_burger}
    ${link_cestas} =    Set Variable     xpath=//android.widget.TextView[@text="Cestas"]
    Click Element    ${link_cestas}
    ${link_cestas_romanticas} =    Set Variable     xpath=//android.widget.TextView[@text="Cestas Românticas"]
    Click Element    ${link_cestas_romanticas}
    ${lbl_nome_produto} =    Set Variable     xpath=//android.widget.TextView[@text="Cesta Café Com Pelúcia"]
    Click Element    ${lbl_nome_produto}
    Element Text Should Be    ${lbl_nome_produto}    Cesta Café Com Pelúcia
    ${lbl_preco_produto} =    Set Variable     xpath=//android.widget.TextView[@text=" R$ 299,90"]
    Element Text Should Be    ${lbl_preco_produto}     R$ 299,90
    ${btn_continuar} =    Set Variable     xpath=//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup
    Click Element    ${btn_continuar}
    ${link_txt_day} =    Set Variable     xpath=//android.widget.TextView[@text="30"]
    Click Element    ${link_txt_day}
    ${btn_continuar} =    Set Variable     xpath=//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup
    Click Element    ${btn_continuar}
    Swipe    ${626}    ${423}    ${572}    ${942}
    ${lbl_titulo_pagina} =    Set Variable     xpath=//android.widget.TextView[@text="Sacola de Compras"]    #Pagina Carrinho
    Element Text Should Be    ${lbl_titulo_pagina}    Sacola de Compras
    Element Text Should Be    ${lbl_nome_produto}    Cesta Café Com Pelúcia
    Element Text Should Be    ${lbl_preco_produto}    R$ 299,90