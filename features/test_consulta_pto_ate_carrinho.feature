Feature: Fluxo Consulta

Scenario: Consulta producto ate o carrinho
    Given que acesso o site Giuliana Flores
    And sou direcionado para a pagina BUQUES
    And seleciono o primeiro produto na lista
    And navego a pagina do produto
    When adiciono ao carrinho
    Then sou direcionado a pagina do carrinho
    E valide o nome e o preço do produto