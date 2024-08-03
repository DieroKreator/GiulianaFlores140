*** Settings ***
Library    SeleniumLibrary

Resource    cart_page.robot
Resource    inventory_item_page.robot
Resource    inventory_page.robot

*** Variables ***
${timeout}    5000ms
${url}        https://www.giulianaflores.com.br/
${browser}    Chrome
${date}

*** Keywords ***
Abrir navegador
    Register Keyword To Run On Failure    Tirar Screenshot
    Open Browser    url=${url}    browser=${browser}
    Maximize Browser Window
    Set Browser Implicit Wait    10000ms
    Wait Until Element Is Visible    css=.login_logo    ${timeout}

Clicar na Categoria
    Click Element    css=.item-3 > .link-menu-desktop
    Wait Until Element Contains    css=.titulo-dept    BUQUÊ DE FLORES    ${timeout}

Fechar navegador
    Sleep    500ms
    Close Browser