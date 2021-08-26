import func_registro

# main
while True:
    print("Que operação deseja realizar?")
    # adicionar as novas operações (entrevista, adotar) aqui
    print("1: Adicionar um novo animal\n2: Modificar um animal no registro\n3: Listar os animais adotados")
    op = input("(1, 2, 3, sair): ")
    if op == "1":
        func_registro.regAdicionar()
    elif op == "2":
        func_registro.regModificar()
    elif op == "3":
        func_registro.regChecarAdotados()
    elif op == "sair":
        exit()