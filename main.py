import func_registro

# main
while True:
    print("Que operação deseja realizar?")
    # adicionar as novas operações (entrevista, adotar) aqui
    print("1: Adicionar um novo animal\n2: Modificar um animal no registro")
    op = input("(1, 2, sair): ")
    if op == "1":
        func_registro.regAdicionar()
    elif op == "2":
        func_registro.regModificar()
    elif op == "sair":
        exit()