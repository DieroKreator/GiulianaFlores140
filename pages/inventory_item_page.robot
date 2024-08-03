*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${titulo_pagina_item}    css=.titulo-dept
${inventory_item_product_name}    css=.item:nth-child(1) .title-item
${inventory_item_product_price}    css=.item:nth-child(1) .actual-price

*** Keywords ***
Adiciono ao Carrinho
    Click Element    css=#ContentSite_lbtBuy
    Click Element    LINK_TEXT=31
    Click Button    css=#btConfirmShippingData
    Click Button    css=#ContentSite_lbtBuy