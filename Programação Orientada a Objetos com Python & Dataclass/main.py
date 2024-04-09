from utilitarios import cadastrar_categoria, cadastrar_transacao, saldo_total

# categorias
categoria_receitas = cadastrar_categoria("Receitas")
categoria_contas = cadastrar_categoria("Contas Fixas")
categoria_lazer = cadastrar_categoria("Lazer")
categoria_viagens = cadastrar_categoria("Viagens")

# transações
cadastrar_transacao(descricao="Salário Jan/2024", valor=6000.0, categoria=categoria_receitas)
cadastrar_transacao(descricao="Cinema", valor=-50.0, categoria=categoria_lazer)
cadastrar_transacao(descricao="Conta de Energia", valor=-120.0, categoria=categoria_contas)
cadastrar_transacao(descricao="Férias em Miami", valor=-3000.0, categoria=categoria_viagens)

total = saldo_total()
print("Saldo Total: ", total)
