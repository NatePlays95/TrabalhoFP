from func_registro import mostrarAnimal

def mostrarAnimalTamanho(tamanho):
    resultado = ''
    existeRegistro = True
    # mudança 1 - usar um try para não abrir se o arquivo não existir
    try:
        arquivo = open("registro_naoadotados.txt", 'r')
        listaDeAnimais = arquivo.readlines()
        arquivo.close()
    except:
        # erro: não existe registro_naoadotados.txt
        existeRegistro = False
    
    if not existeRegistro: # se o arquivo não existe
        resultado = 'Nenhum Animalzinho :('
    else: # se existe sim o registro
        # mudança 2 - usar a função mostrarAnimal(animal) (dentro do func_registro) para mostrar as informações em string no Resultado
        # só passar eval(listaDeAnimais[N].removesuffix("\n")) como o parâmetro da função
        if tamanho == 'grande':
            for N in range(len(listaDeAnimais)):
                    #resultado += '%d - %s' %(N+1, listaDeAnimais[N])
                    resultado += str(N+1) + ' - ' + mostrarAnimal(eval(listaDeAnimais[N].removesuffix("\n"))) + "\n"
        elif tamanho == 'medio':
            for N in range(len(listaDeAnimais)):
                if "'porte': 'pequeno'" in listaDeAnimais[N] or "'porte': 'medio'" in listaDeAnimais[N]:
                    #resultado += '%d - %s' % (N + 1, listaDeAnimais[N])
                    resultado += str(N+1) + ' - ' + mostrarAnimal(eval(listaDeAnimais[N].removesuffix("\n"))) + "\n"
        elif tamanho == 'pequeno':
            for N in range(len(listaDeAnimais)):
                if "'porte': 'pequeno'" in listaDeAnimais[N]: # ao invés de transformar a função em dicionario, faz uma busca em string
                    #resultado += '%d - %s' % (N + 1, listaDeAnimais[N])
                    resultado += str(N+1) + ' - ' + mostrarAnimal(eval(listaDeAnimais[N].removesuffix("\n")))  + "\n"
        else:
            resultado = 'Tamanho inválido'
        
        if resultado == '': # caso nenhum animal seja selecionado pela função
            resultado = 'Nenhum Animalzinho :('
    # mudança 3 - usar apenas um return
    return resultado
    # sugestão: essa função é pra ser usada na adoção, então teoricamente ela tem que retornar
    # uma lista lista_adotaveis com todos os dicionarios dos animais (só dar append à lista pra cada animal valido)
    # para que a função de adotar use essa lista.
    # remover os prints do resultado (inclusive os meus)
    # se mudar, tambem mudar a parte do 

#----------------------------------------------------------------------------------------------------------------------#

def cadastroPessoa():
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
                      'resposta3' : pergunta3, 'apto' : aptoParaAdocao, 'justificativa' : gerarJustificativa(pergunta1,pergunta2,pergunta3)}
    arquivo = open('registro_entrevistas.txt', 'a') # nome padronizado
    arquivo.write(str(registroPessoa) + '\n')
    arquivo.close()
    print('Entrevista Realizada com sucesso!')
    return mostrarAnimalTamanho(pergunta3)
    # notar que a função retorna a outra função. se mostrarAnimalTamanho retorna uma string ou uma lista,
    # essa deve ser salva na variavel durante o processo da adoção

#----------------------------------------------------------------------------------------------------------------------

def gerarJustificativa(pergunta1,pergunta2,pergunta3):
    # recomendo apenas testar o mostrarAnimalTamanho uma vez, já que elas são feitas em ordem e essa função demora.
    # por exemplo, salvar o resultado das perguntas 1 e 2 numa terceira variavel, e testar essa contra a função do tamanho.
    # if mostrarAnimalTamanho(pergunta3) == nenhum:
    #    testes em cadeia
    # else:
    #    mais testes em cadeia
    if mostrarAnimalTamanho(pergunta3)=='Nenhum Animalzinho :(' and pergunta1 == 'nao' and pergunta2 == 'nao':
        return 'O Candidato nao possui condicoes financeiras nem tempo para adoçao do PET, alem de nao termos animais disponiveis.'
    elif mostrarAnimalTamanho(pergunta3)=='Nenhum Animalzinho :(' and pergunta1 == 'nao' and pergunta2 == 'sim':
        return 'O Candidato nao possui condicoes financeiras para o PET e nao possuimos animais disponiveis.'
    elif mostrarAnimalTamanho(pergunta3) == 'Nenhum Animalzinho :(' and pergunta1 == 'sim' and pergunta2 == 'nao' :
        return 'O Candidato possui condicoes financeiras mas nao possui o tempo em sua rotina para cuidar do PET, alem de nao termos animais disponiveis.'
    elif mostrarAnimalTamanho(pergunta3) == 'Nenhum Animalzinho :(' and pergunta1 == 'sim' and pergunta2 == 'sim':
        return 'O Candidato possui as condicoes financeiras para a adoçao, mas nao temos animais disponiveis.'
    elif pergunta1 == 'nao' and pergunta2 == 'nao':
        return 'O Candidato nao possui condicoes financeiras nem tempo para adoçao do PET.'
    elif pergunta1 == 'nao' and pergunta2 == 'sim':
        return 'O Candidato nao possui condicoes financeiras para o PET.'
    elif pergunta1 == 'sim' and pergunta2 == 'nao':
        return 'O Candidato possui condicoes financeiras mas nao possui o tempo em sua rotina para cuidar do PET.'
    else:
        return ''

#----------------------------------------------------------------------------------------------------------------------

def pesquisarAnimalNome(nomeAnimal):
    arquivo = open("registro_naoadotados.txt", 'r')
    lista = arquivo.readlines()
    for N in range(len(lista)):
        if lista[N].find(nomeAnimal)!=-1:
            return lista[N]
            break
    return 'Nenhum Animal Encontrado'
    # bug: se não converter o animal de string pra dicionario com eval(listaDeAnimais[N].removesuffix("\n")),
    # o usuario pode pesquisar 'porte' e receber todos os animais
    # ao invés disso, comparar nomeAnimal com animal['nome'], e retornar a lista dos animais validos
#----------------------------------------------------------------------------------------------------------------------

cadastroPessoa()
