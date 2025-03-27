#Atividade realizada por Enrico Trevisan de Oliveira Batista | N°8 | 2°B

menu = {
    'lanche1': ['Single C. Burguer', '14.99'],
    'lanche2': ['Duple C. Burguer', '17.99'],
    'lanche3': ['Triple C. Burguer', '19.99'],
    'lanche4': ['X Certo', '12.99'],
    'lanche5': ['Egg Certo', '11.99'],
    'lanche6': ['Bacon Certo', '13.99'],
    'lanche7': ['Tudo Certo', '24.99'],
    'lanche8': ['Queijo Certo', '12.99']
}

print("Olá, seja bem-vindo ao Triple Certo Lanches!")
print("Este aqui é nosso cardápio: ", menu)

opcao = (input("Digite a sua escolha:"))

print('Certo, o seu pedido foi:', menu[opcao][0],"e seu o preço é", menu[opcao][1], ".")
print('Muito obrigado por pedir sua refeição aqui no Triple Certo Lanches!')