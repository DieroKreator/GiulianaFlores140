Feature: Fluxo Consulta

Scenario Outline: Consulta producto ate o carrinho
    Given que acesso o site da loja Giuliana Flores
    And sou direcionado para a pagina BUQUÊ DE FLORES
    And seleciono o produto <produto> da lista
    And navego a pagina do <produto> com <preço>
    When adiciono ao carrinho
    Then sou direcionado a pagina do carrinho
    And valido o nome do <produto> e o <preço>

    Examples: Products
   | produto                         | preço     |
   | Buquê De 6 Rosas Vermelhas      | R$ 109,90 |
   | Buquê De 4 Girassóis Te Adoro   | R$ 81,83  |