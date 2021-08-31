from prettytable import PrettyTable 
import datetime

#CONSULTA NÃO ADOTADOS --------------------------------------------------------------------------

#tabela recebendo os dados do cabeçalho
tabelaNaoAdotados = PrettyTable(["Nome", "Idade" , "Porte" , "Raça", "Lar temporário"])

#função mostrando os animais não adotados em forma de tabela
def mostrarAnimalNaoAdotado(animal):
   #criando as linhas da tabela 
   tabelaNaoAdotados.add_row([animal['nome'] , str(animal['idade']) , animal['porte'] , animal['raca'] , animal['lar']])
   return (tabelaNaoAdotados)
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

def regListarNaoAdotados():
    lista_naoadotados = lerNaoAdotados()
    #Verificando se existem animais que ainda não foram adotados
    if lista_naoadotados == []:
        print("Nenhum animal foi adotado.")
    else:
        #reorganizando a lista pela idade
        novalista = sorted(lista_naoadotados, key=lambda a: a['idade'], reverse=True)
        print("Não adotados")
        
        #Imprimindo a tabela com os não adotados
        for i in range(len(novalista)):
            mostrarAnimalNaoAdotado(novalista[i])

        print(tabelaNaoAdotados)

print("\n Operação Concluída.\n")

#CONSULTA ADOTADOS --------------------------------------------------------------------------

tabelaAdotados = PrettyTable(["Nome", "Idade" , "Porte" , "Raça", "Lar temporário", "Dono","Data de adoção"])

def mostrarAnimalAdotado(animal):
    tabelaAdotados.add_row([animal['nome'] , str(animal['idade']) , animal['porte'] , animal['raca'] , animal['lar'], animal['dono'], animal['data'].strftime("%d/%m/%y")])
    return tabelaAdotados
#---------------------------------------------------------------------

def lerAdotados(): 
    arq = open("registro_adotados.txt", "r") # modo leitura
    velhalista_registro = arq.readlines()
    
    # converter strings pra dicts
    novalista_registro = []
    for linha in velhalista_registro:
        dic = eval(linha.removesuffix("\n")) # transformar string em dicionário
        novalista_registro.append(dic)
    arq.close()
    return novalista_registro
#---------------------------------------------------------------------

def regListarAdotados():
    lista_adotados = lerAdotados()
    if lista_adotados == []:
        print("Nenhum animal foi adotado.")
    else:
       #reorganizando a lista pela idade
        novalista = sorted(lista_adotados, key=lambda a: a['data'], reverse=True)
        print("Adotados")
        
        #Imprimindo a tabela com os não adotados

        for i in range(len(novalista)):
            mostrarAnimalAdotado(novalista[i])
        print(tabelaAdotados)
