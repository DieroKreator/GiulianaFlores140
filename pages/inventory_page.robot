*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${titulo_pagina}    css=.titulo-dept

*** Keywords ***
Adicionar Endereco
    # Click Element    css=#inputSearchAddress
    Input Text    css=#inputSearchAddress    41195-665
    Click Element    XPATH=//li[contains(text(),'2ª Travessa Irmã Dulce, Barreiras, Salvador - BA, ')]
    Click Button    XPATH=//div[contains(text(),'Aplicar')]

Clicar no Produto
    Click Element    css=.item:nth-child(1) .image-content > img