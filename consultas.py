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
    if lista_adotados == []:
        print("Nenhum animal foi adotado.")
    else:
        # reorganizar a lista em ordem de adoção
        novalista = sorted(lista_adotados, key=lambda a: a['data'], reverse=True)
        # sorted(lista, key=?) organiza a lista de acordo com a chave
        # a chave que eu quero é a 'data' de cada dicionario da lista
        # então eu crio uma lambda (função temporária) para pegar a data
        # como as datas são no formato datetime, elas podem ser comparadas
        # finalmente, reversed inverte a ordem, do mais recente pro mais antigo

        print("Adotados")
        
        
        for i in range(len(novalista)):
            mostrarAnimalNaoAdotado(novalista[i])

        print(myTable)

print("\n Operação Concluída.\n")
