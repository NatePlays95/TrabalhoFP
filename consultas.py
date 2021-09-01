from prettytable import PrettyTable 
import datetime
from func_registro import lerNaoAdotados, lerAdotados, mostrarAnimal

#CONSULTA NÃO ADOTADOS --------------------------------------------------------------------------

#tabela recebendo os dados do cabeçalho
tabelaNaoAdotados = PrettyTable(["Nome", "Idade" , "Porte" , "Raça", "Lar temporário"])

#função mostrando os animais não adotados em forma de tabela
def mostrarAnimalNaoAdotado(animal):
   #criando as linhas da tabela 
   tabelaNaoAdotados.add_row([animal['nome'] , str(animal['idade']) , animal['porte'] , animal['raca'] , animal['lar']])
   return (tabelaNaoAdotados)
#---------------------------------------------------------------------#

def regListarNaoAdotados():
    tabelaNaoAdotados.clear_rows()
    # limpar a tabela para não repetir entradas

    lista_naoadotados = lerNaoAdotados()
    #Verificando se existem animais que ainda não foram adotados
    if lista_naoadotados == []:
        print("Nenhum animal no sistema.")
    else:
        #reorganizando a lista pela idade
        novalista = sorted(lista_naoadotados, key=lambda a: a['idade'], reverse=True)
        print("Não adotados")
        
        #Imprimindo a tabela com os não adotados
        for i in range(len(novalista)):
            mostrarAnimalNaoAdotado(novalista[i])

        print(tabelaNaoAdotados)


#CONSULTA ADOTADOS --------------------------------------------------------------------------

tabelaAdotados = PrettyTable(["Nome", "Idade" , "Porte" , "Raça", "Lar temporário", "Dono","Data de adoção"])

def mostrarAnimalAdotado(animal):
    tabelaAdotados.add_row([animal['nome'] , str(animal['idade']) , animal['porte'] , animal['raca'] , animal['lar'], animal['dono'], animal['data'].strftime("%d/%m/%y")])
    return tabelaAdotados
#---------------------------------------------------------------------

def regListarAdotados():
    tabelaAdotados.clear_rows()
    # limpar a tabela para não repetir entradas
    
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
