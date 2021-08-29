import func_registro
import datetime

def mostrarAnimalTamanho(tamanho) :
    resultado = ''
    existeRegistro = True
    # mudança 1 - usar um try para não abrir se o arquivo não existir
    try :
        arquivo = open("registro_naoadotados.txt", 'r')
        listaDeAnimais = arquivo.readlines()
        arquivo.close()
    except :
        # erro: não existe registro_naoadotados.txt
        existeRegistro = False

    if not existeRegistro :  # se o arquivo não existe
        resultado = 'Nenhum Animalzinho :('
    else :  # se existe sim o registro
        # mudança 2 - usar a função mostrarAnimal(animal) (dentro do func_registro) para mostrar as informações em string no Resultado
        # só passar eval(listaDeAnimais[N].removesuffix("\n")) como o parâmetro da função
        if tamanho == 'grande' :
            for N in range(len(listaDeAnimais)) :
                # resultado += '%d - %s' %(N+1, listaDeAnimais[N])
                resultado +=  func_registro.mostrarAnimal(eval(listaDeAnimais[N].removesuffix("\n"))) + "\n"
        elif tamanho == 'medio' :
            for N in range(len(listaDeAnimais)) :
                if "'porte': 'pequeno'" in listaDeAnimais[N] or "'porte': 'medio'" in listaDeAnimais[N] :
                    # resultado += '%d - %s' % (N + 1, listaDeAnimais[N])
                    resultado +=  func_registro.mostrarAnimal(eval(listaDeAnimais[N].removesuffix("\n"))) + "\n"
        elif tamanho == 'pequeno' :
            for N in range(len(listaDeAnimais)) :
                if "'porte': 'pequeno'" in listaDeAnimais[
                    N] :  # ao invés de transformar a função em dicionario, faz uma busca em string
                    # resultado += '%d - %s' % (N + 1, listaDeAnimais[N])
                    resultado +=  func_registro.mostrarAnimal(eval(listaDeAnimais[N].removesuffix("\n"))) + "\n"
        else :
            resultado = 'Tamanho inválido'

        if resultado == '' :  # caso nenhum animal seja selecionado pela função
            resultado = 'Nenhum Animalzinho :('
    # mudança 3 - usar apenas um return
    return resultado
    # sugestão: essa função é pra ser usada na adoção, então teoricamente ela tem que retornar
    # uma lista lista_adotaveis com todos os dicionarios dos animais (só dar append à lista pra cada animal valido)
    # para que a função de adotar use essa lista.
    # remover os prints do resultado (inclusive os meus)


# ----------------------------------------------------------------------------------------------------------------------#

def listaAnimaisTamanho(tamanho) :
    # essa função retorna uma lista com todos os animais não adotados,
    # de mesmo tamanho ou menor que o especificado.
    
    existeRegistro = True
    # mudança 1 - usar um try para não abrir se o arquivo não existir
    try :
        arquivo = open("registro_naoadotados.txt", 'r')
        listaDeAnimais = arquivo.readlines()
        arquivo.close()
    except :
        # erro: não existe registro_naoadotados.txt
        existeRegistro = False

    if not existeRegistro :  # se o arquivo não existe
        return
    else :  # se existe sim o registro
        novalista = []
        # se a pessoa pode ter animais grandes, ela pode ter pequenos também!
        if tamanho == 'grande' : 
            for N in range(len(listaDeAnimais)) :
                novalista.append(eval(listaDeAnimais[N].removesuffix("\n")))
        elif tamanho == 'medio' :
            for N in range(len(listaDeAnimais)) :
                if "'porte': 'pequeno'" in listaDeAnimais[N] or "'porte': 'medio'" in listaDeAnimais[N] :
                    novalista.append(eval(listaDeAnimais[N].removesuffix("\n")))
        elif tamanho == 'pequeno' :
            for N in range(len(listaDeAnimais)) :
                if "'porte': 'pequeno'" in listaDeAnimais[N] :  

                   novalista.append(eval(listaDeAnimais[N].removesuffix("\n")))
        else :
            print('Tamanho inválido')
            return
        if novalista == [] :
            return
        else :
            return novalista

# ----------------------------------------------------------------------------------------------------------------------#

def cadastroPessoa() :
    nome = input('Qual seu nome?\n')
    while True :
        pergunta1 = input('Você possui condições financeiras para adotar um novo animal?'
                          ' Responda com Sim ou Nao.\n').lower().strip()
        if pergunta1 == 'sim' or pergunta1 == 'nao' :
            break
        else :
            print('Por favor, responda APENAS com Sim ou Nao.')
    while True :
        pergunta2 = input('Avaliando sua rotina, você possui tempo livre para se dedicar ao seu novo pet?'
                          ' Responda com Sim ou Nao.\n').lower().strip()
        if pergunta2 == 'sim' or pergunta2 == 'nao' :
            break
        else :
            print('Por favor, responda APENAS com Sim ou Nao.')
    while True :
        pergunta3 = input('Pense  agora  no  espaço  que  você  possui  em  casa:\n'
                          'Qual  o  porte  máximo  que  o animal deverá ter para viver confortavelmente com você?'
                          ' Pequeno, Medio ou Grande?\n').lower().strip()
        if pergunta3 == 'pequeno' or pergunta3 == 'medio' or pergunta3 == 'grande' :
            break
        else :
            print('Escolha apenas entre pequeno, medio ou grande.')
    if pergunta1 == 'sim' and pergunta2 == 'sim' :
        aptoParaAdocao = 'sim'
    else :
        aptoParaAdocao = 'nao'
    registroPessoa = {'nome' : nome, 'resposta1' : pergunta1, 'resposta2' : pergunta2,
                      'resposta3' : pergunta3, 'apto' : aptoParaAdocao,
                      'justificativa' : gerarJustificativa(pergunta1, pergunta2, pergunta3)}
    arquivo = open('registro_entrevistas.txt', 'a')  # nome padronizado
    arquivo.write(str(registroPessoa) + '\n')
    arquivo.close()
    print('Entrevista Realizada com sucesso!')
    return mostrarAnimalTamanho(pergunta3)
    # notar que a função retorna a outra função. se mostrarAnimalTamanho retorna uma string ou uma lista,
    # essa deve ser salva na variavel durante o processo da adoção


# ----------------------------------------------------------------------------------------------------------------------

def gerarJustificativa(pergunta1, pergunta2, pergunta3) :
    # recomendo apenas testar o mostrarAnimalTamanho uma vez, já que elas são feitas em ordem e essa função demora.
    # por exemplo, salvar o resultado das perguntas 1 e 2 numa terceira variavel, e testar essa contra a função do tamanho.
    # if mostrarAnimalTamanho(pergunta3) == nenhum:
    #    testes em cadeia
    # else:
    #    mais testes em cadeia
    if mostrarAnimalTamanho(pergunta3) == 'Nenhum Animalzinho :(' and pergunta1 == 'nao' and pergunta2 == 'nao' :
        return 'O Candidato nao possui condicoes financeiras nem tempo para adoçao do PET, alem de nao termos animais disponiveis.'
    elif mostrarAnimalTamanho(pergunta3) == 'Nenhum Animalzinho :(' and pergunta1 == 'nao' and pergunta2 == 'sim' :
        return 'O Candidato nao possui condicoes financeiras para o PET e nao possuimos animais disponiveis.'
    elif mostrarAnimalTamanho(pergunta3) == 'Nenhum Animalzinho :(' and pergunta1 == 'sim' and pergunta2 == 'nao' :
        return 'O Candidato possui condicoes financeiras mas nao possui o tempo em sua rotina para cuidar do PET, alem de nao termos animais disponiveis.'
    elif mostrarAnimalTamanho(pergunta3) == 'Nenhum Animalzinho :(' and pergunta1 == 'sim' and pergunta2 == 'sim' :
        return 'O Candidato possui as condicoes financeiras para a adoçao, mas nao temos animais disponiveis.'
    elif pergunta1 == 'nao' and pergunta2 == 'nao' :
        return 'O Candidato nao possui condicoes financeiras nem tempo para adoçao do PET.'
    elif pergunta1 == 'nao' and pergunta2 == 'sim' :
        return 'O Candidato nao possui condicoes financeiras para o PET.'
    elif pergunta1 == 'sim' and pergunta2 == 'nao' :
        return 'O Candidato possui condicoes financeiras mas nao possui o tempo em sua rotina para cuidar do PET.'
    else :
        return ''


# ----------------------------------------------------------------------------------------------------------------------

def pesquisarAnimalNome(nomeAnimal) :
    arquivo = open("registro_naoadotados.txt", 'r')
    lista = arquivo.readlines()
    arquivo.close()
    for N in range(len(lista)) :
        if lista[N].find("'nome': '%s'" %nomeAnimal) != -1 :
            return lista[N] # retorna o primeiro animal com esse nome
    return 'Nenhum Animal Encontrado'
    # ok!

def pesquisarAnimalPorNomeEmLista(nomeAnimal, lista) :
    for animal in lista :
        if animal.get('nome') == nomeAnimal : # dict.get('chave') funciona que nem dict['chave']
            return animal # retorna o primeiro animal (dic) com esse nome
    # caso não houver, retorna um None

#-----------------------------------------------------------------------------------------------------------------------

def pesquisarDonoNome(nomeDono) :
    arquivo = open("registro_entrevistas.txt", 'r')
    lista = arquivo.readlines()
    arquivo.close()
    for N in range(len(lista)) :
        if lista[N].find("'nome': '%s'" %nomeDono) != -1 :
            return lista[N] # string
                            # retorna o primeiro dono com esse nome
                            # note que se uma pessoa fizer duas entrevistas,
                            # ela vai ter duas entradas...

# ----------------------------------------------------------------------------------------------------------------------

def adotarAnimal(): # processo do main para adotar o animal.
    # pegar o futuro dono:
    nomeDono = input("Digite o nome da pessoa a adotar: ")
    try:
        dono = eval(pesquisarDonoNome(nomeDono).removesuffix("\n"))
        # dono é um dicionário
        # se pesquisarDonoNome não achar nenhum, vai retornar nada, 
        # gerando um erro, o que ativa o except
    except: 
        print('Dono não cadastrado')
        return # sai da função de adoção, de volta pro main.
    
    # esse dono pode realizar uma adoção?
    if dono['apto'] == "nao" :
        print("Essa pessoa não está apta a adotar um animal.")
        print("Justificativa:\n"+dono['justificativa'])
        return
    elif dono['apto'] == "sim" :
        # pegar a lista de animais que o dono pode manter
        listaAdotaveis = listaAnimaisTamanho(dono['resposta3'])
        listaAdotaveis = func_registro.ordernarIdade(listaAdotaveis)
        # print(listaAdotaveis)
        # mostrar todas as opções
        print("--Animais Disponíveis--") 
        # usando mostrarAnimal manualmente
        # para mostrar eles na ordem de idade
        for animal in listaAdotaveis :
            print(func_registro.mostrarAnimal(animal))
        
        # perguntar se o dono deseja prosseguir
        print("Deseja adotar um desses animais?")
        while True :
            inp = input("Responda com Sim ou Nao: ").lower().strip()
            if inp == "nao" : return # sair de volta para o main
            elif inp == "sim" : break # sai desse loop

        # pegar o animal por nome:
        nomeAnimal = input("Digite o nome do animal que deseja adotar: ")
        animal = pesquisarAnimalPorNomeEmLista(nomeAnimal, listaAdotaveis)
        if  animal == None : # se a função de pesquisa não achou um animal
            print('Esse animal não está na lista.')
            return  

        # digitar a data da adoção
        while True:
            try:
                ano = int(input('Digite o Ano Atual:'))
                mes = int(input('Digite o Mês(em número):'))
                dia = int(input('Digite o dia:'))
                data = datetime.date(ano,mes,dia)
                break
            except: print('Data inválida, tente novamente.')
        
        func_registro.regMoverAnimalAdotado(animal, nomeDono, data)
        return 'Animal Adotado com Sucesso!'

#----------------------------------------------------------------------------------------------------------------------

# def removerAnimalnaoAdotado(animal):
#     try:
#         arquivo = open('registro_naoadotados.txt','r')
#         lista = arquivo.readlines()
#     except: print('Arquivo não existe.')
#     try:
#         lista.remove(str(animal)+'\n')
#     except: print('Animal não está na Lista de Não Adotados.')
#     arquivo.close()
#     arquivo = open('registro_naoadotados.txt','w')
#     for N in range(len(lista)):
#         arquivo.write(lista[N])
#     arquivo.close()
    #fiz usando dois arquivos pois o precisava ler e dps escrever por cima, o R+ ele append e o W+ tava apagando tudo,
    #por que ele precisa primeiro escrever e dps ler senão ele apaga
