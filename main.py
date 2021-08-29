import func_registro
import entrevista
import consultas
# main
while True:
    print("\nQue operação deseja realizar?")
    # adicionar as novas operações (entrevista, adotar) aqui
    print("1: Adicionar um novo animal\n2: Modificar um animal no registro\n"
        + "3: Realizar uma entrevista pré-adoção\n4: Adotar um animal\n5: Listar os animais adotados")
    op = input("(1, 2, 3, 4, 5, 6, sair): ").lower().strip()
    if op == "1":
        func_registro.regAdicionar()
        print("Operação Concluída.")
    elif op == "2":
        func_registro.regModificar()
        print("Operação Concluída.")
    elif op == "3":
        entrevista.cadastroPessoa()
        print("Operação Concluída.")
    elif op == "4":
        entrevista.adotarAnimal()
        print("Operação Concluída.")
    elif op == "5":
        func_registro.regListarAdotados()
        print("Operação Concluída.")
    elif op == "6":
        consultas.regChecarNaoAdotados()
        print("Operação Concluída.")
    elif op == "sair":
        exit()
