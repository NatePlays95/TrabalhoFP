import datetime
from prettytable import PrettyTable 

#tabela recebendo os dados do cabeçalho
myTable = PrettyTable(["Nome", "Idade" , "Porte" , "Raça", "Lar temporário"])

#função mostrando os animais não adotados em forma de tabela
def mostrarAnimalNaoAdotado(animal):
   #criando as linhas da tabela 
   myTable.add_row([animal['nome'] , str(animal['idade']) , animal['porte'] , animal['raca'] , animal['lar']])
   return (myTable)
#---------------------------------------------------------------------#

def lerNaoAdotados():
    arq = open("registro_naoadotados.txt", "r") # modo leitura
    velhalista_registro = arq.readlines()
    
    # converter strings pra dicts
    novalista_registro = []
    for linha in velhalista_registro:
        dic = eval(linha.removesuffix("\n")) # transformar string em dicionário
        novalista_registro.append(dic)
    arq.close()
    return novalista_registro
#---------------------------------------------------------------------#

def regChecarNaoAdotados():
    lista_adotados = lerNaoAdotados()
    #verificando se existem animais não adotados na lista
    if lista_adotados == []:
        print("Nenhum animal foi adotado.")
    else:
        novalista = lista_adotados
        print("Não adotados")
        
        #mostrando os valores em uma tabela
        for i in range(len(novalista)):
            mostrarAnimalNaoAdotado(novalista[i])

        print(myTable)

print("\n Operação Concluída.\n")
