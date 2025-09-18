# Sistema de pedidos do Restaurante Ragazzi...
# Feito para gerenciar o cardápio e mexer nos pratos pelo console.

# pratos cadastrados:
cardapio = [
    {
        "codigo": 1,
        "nome": "Spaghetti Carbonara",
        "descricao": "massa com molho de ovos, queijo parmesão e pancetta",
        "preco": 69.90,
        "estoque": 10
    },
    {
        "codigo": 2,
        "nome": "Fettuccine Alfredo",
        "descricao": "fettuccine com molho cremoso de parmesão",
        "preco": 59.90,
        "estoque": 12
    },
    {
        "codigo": 3,
        "nome": "Ravioli de Ricota e Espinafre",
        "descricao": "ravioli recheado com ricota e espinafre no pomodoro",
        "preco": 74.90,
        "estoque": 8
    },
    {
        "codigo": 4,
        "nome": "Nhoque ao molho Pesto",
        "descricao": "nhoque de batata com pesto de manjericão",
        "preco": 49.90,
        "estoque": 15
    },
    {
        "codigo": 5,
        "nome": "Lasanha Bolonhesa",
        "descricao": "lasanha tradicional ao molho bolonhesa",
        "preco": 98.90,
        "estoque": 6
    }
]

proximo_codigo = len(cardapio) + 1

def mostrar_cardapio():
    print("\n--- Cardápio Ragazzi ---")
    for prato in cardapio:
        print(f"{prato['codigo']} - {prato['nome']} | R$ {prato['preco']}")
        print(f"   {prato['descricao']} (estoque: {prato['estoque']})")
    print()

def adicionar_prato():
    global proximo_codigo
    nome = input("Nome do prato: ")
    desc = input("Descrição: ")
    preco = float(input("Preço: "))
    estoque = int(input("Quantidade em estoque: "))
    novo = {
        "codigo": proximo_codigo,
        "nome": nome,
        "descricao": desc,
        "preco": preco,
        "estoque": estoque
    }
    cardapio.append(novo)
    proximo_codigo += 1
    print("Prato adicionado!\n")

def editar_prato():
    codigo = int(input("Código do prato que quer mudar: "))
    for prato in cardapio:
        if prato["codigo"] == codigo:
            novo_nome = input(f"Novo nome (deixe vazio pra manter {prato['nome']}): ")
            if novo_nome:
                prato["nome"] = novo_nome
            nova_desc = input(f"Nova descrição (atual: {prato['descricao']}): ")
            if nova_desc:
                prato["descricao"] = nova_desc
            novo_preco = input(f"Novo preço (atual: {prato['preco']}): ")
            if novo_preco:
                prato["preco"] = float(novo_preco)
            novo_estoque = input(f"Novo estoque (atual: {prato['estoque']}): ")
            if novo_estoque:
                prato["estoque"] = int(novo_estoque)
            print("Prato atualizado!\n")
            return
    print("Não achei nenhum prato com esse código.\n")

def menu():
    while True:
        print("=== Sistema de Cardápio Ragazzi ===")
        print("1 - Ver cardápio")
        print("2 - Adicionar prato")
        print("3 - Editar prato")
        print("0 - Sair")
        op = input("Escolha: ")

        if op == "1":
            mostrar_cardapio()
        elif op == "2":
            adicionar_prato()
        elif op == "3":
            editar_prato()
        elif op == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
