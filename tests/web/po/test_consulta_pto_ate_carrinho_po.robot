*** Settings ***
Resource    ../../../pages/base_page.robot

*** Test Cases ***
Consulta Produto até o Carrinho
    Clicar na Categoria
    Element Text Should Be    ${titulo_pagina}    BUQUÊ DE FLORES
    Adicionar Endereco
    Clicar no Produto
    Element Text Should Be    ${inventory_item_product_name}    Buquê De 6 Rosas Vermelhas
    Element Text Should Be    ${inventory_item_product_price}    R$ 109,90
    Adiciono ao Carrinho
    Element Text Should Be    ${titulo_pagina_carrinho}    MEU CARRINHO
    Element Text Should Be    ${carrinho_product_name}    Buquê De 6 Rosas Vermelhas
    Element Text Should Be    ${carrinho_product_price}    R$ 109,90