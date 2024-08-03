Feature: Login Cadastro

    Scenario: Criação de usuário
        Given que acesso o site Giuliana Flores
        When preencho com sucesso os campos obrigatorios de cadastro
        Then uma nova conta é criada

    Scenario: Login Positivo
        Given que acesso o site Giuliana Flores
        When preencho os campos de login com usuario maya_figueiredo@agenciadbd.com e senha uUhnjTD4PF
        Then o usuario esta conetado com sucesso

    Scenario: Login Negativo
        Given que acesso o site Giuliana Flores
        When preencho os campos de login com usuario maya_figueiredo@agenciadbd.com e senha melancia
        Then exibe a mensagem de erro e-mail ou senha inválidos! no login

    Scenario: Fluxo de compra a partir de um banner na home
        Given que acesso o site Giuliana Flores
        And preencho os campos de login com usuario maya_figueiredo@agenciadbd.com e senha uUhnjTD4PF
        And sou direcionado para a pagina PRESENTE DE PÁSCOA a partir do banner
        And navego a pagina do produto MARGARIDINHAS BRANCAS E FERRERO ROCHER
        And valido o produto na pagina MEU CARRINHO
        And preencho os dados na pagina ENTREGA
        When eu faco o PAGAMENTO
        Then a compra e realizada com sucesso