Feature: Fluxo Consulta

Scenario: Consulta producto ate o carrinho
    Given que acesso o site da loja Giuliana Flores
    And sou direcionado para a pagina BUQUÊ DE FLORES
    And seleciono o primeiro produto na lista
    And navego a pagina do produto
    When adiciono ao carrinho
    Then sou direcionado a pagina do carrinho
    And valido o nome e o preço do produto