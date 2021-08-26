def mostrarAnimalTamanho(tamanho):
    resultado = ''
    arquivo = open("registro_naoadotados.txt", 'r')
    listaDeAnimais = arquivo.readlines()
    arquivo.close()
    if tamanho == 'grande':
        for N in range(len(listaDeAnimais)):
                resultado += '%d - %s' %(N+1, listaDeAnimais[N])
    elif tamanho == 'medio':
        for N in range(len(listaDeAnimais)):
            if "'porte': 'pequeno'" in listaDeAnimais[N] or "'porte': 'medio'" in listaDeAnimais[N]:
                resultado += '%d - %s' % (N + 1, listaDeAnimais[N])
    elif tamanho == 'pequeno':
        for N in range(len(listaDeAnimais)):
            if "'porte': 'pequeno'" in listaDeAnimais[N]:
                resultado += '%d - %s' % (N + 1, listaDeAnimais[N])
    else:
        resultado = 'Tamanho inválido'
        return resultado
    if resultado == '':
        resultado = 'Nenhum Animalzinho :('
        return resultado
    else:
        return resultado

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
        aptoParaAdocao = 'não'
    registroPessoa = {'nome' : nome, 'resposta1' : pergunta1, 'resposta2' : pergunta2,
                      'resposta3' : pergunta3, 'apto' : aptoParaAdocao, 'justificativa' : gerarJustificativa(pergunta1,pergunta2,pergunta3)}
    arquivo = open('registroEntrevistas.txt', 'a')
    arquivo.write(str(registroPessoa) + '\n')
    arquivo.close()
    print('Entrevista Realizada com sucesso!')
    return mostrarAnimalTamanho(pergunta3)

#----------------------------------------------------------------------------------------------------------------------

def gerarJustificativa(pergunta1,pergunta2,pergunta3):
    if mostrarAnimalTamanho(pergunta3)=='Nenhum Animalzinho :(' and pergunta1 == 'nao' and pergunta2 == 'nao':
        return 'O Candidato não possui condições financeiras nem tempo para adoção do PET, além de não termos animais disponíveis.'
    elif mostrarAnimalTamanho(pergunta3)=='Nenhum Animalzinho :(' and pergunta1 == 'nao' and pergunta2 == 'sim':
        return 'O Candidato não possui condições financeiras para o PET e não possuímos animais disponíveis.'
    elif mostrarAnimalTamanho(pergunta3) == 'Nenhum Animalzinho :(' and pergunta1 == 'sim' and pergunta2 == 'nao' :
        return 'O Candidato possui condições financeiras mas não possui o tempo em sua rotina para cuidar do PET, além de não termos animais disponíveis.'
    elif mostrarAnimalTamanho(pergunta3) == 'Nenhum Animalzinho :(' and pergunta1 == 'sim' and pergunta2 == 'sim':
        return 'O Candidato possui as condições necessárias para a adoção, mas não temos animais disponíveis.'
    elif pergunta1 == 'nao' and pergunta2 == 'nao':
        return 'O Candidato não possui condições financeiras nem tempo para adoção do PET.'
    elif pergunta1 == 'nao' and pergunta2 == 'sim':
        return 'O Candidato não possui condições financeiras para o PET.'
    elif pergunta1 == 'sim' and pergunta2 == 'nao':
        return 'O Candidato possui condições financeiras mas não possui o tempo em sua rotina para cuidar do PET.'
    else:
        return ''

#----------------------------------------------------------------------------------------------------------------------

def pesquisarAnimalNome(nomeAnimal):
    arquivo = open("registro_naoadotados.txt", 'r')
    lista = arquivo.readlines()
    for N in range(len(lista)):
        if lista[N].find(nomeAnimal.capitalize())!=-1:
            return lista[N]
            break
    return 'Nenhum Animal Encontrado'