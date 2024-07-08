def modalidade (publi):
    modalidade = ''
    for palavra in publi:
        if 'alug' in publi:
            modalidade = 'Aluguel'

        elif 'vend' in publi:
            modalidade = 'Venda'

        else:
            modalidade = 'nao informado'
    
    return modalidade



def tipo (publi):
    tipo = ''
    for palavra in publi:
        if 'casa' in publi:
            tipo = 'Casa'
            
        elif 'apartamento' in publi:
            tipo = 'Apartamento'
            
        else:
            tipo = 'nao informado'
    return tipo



def endereço(publi):
    endereço = 'nao informado'
    separado = publi.split()
    limite = ''

    if 'Rua' in publi:
        limite = 'Rua'
    elif 'Avenida' in publi:
        limite = 'Avenida'

    achar_endereço = separado.index(limite) + 1
    lista_endereço = [limite]

    for i in separado[achar_endereço:]:
        if '.' in i:
            novo_i = i.replace('.' , '')
        elif ',' in i:
            novo_i = i.replace(',', '')
        else:
            novo_i = i

        if novo_i.isdigit():
            limite = f'{limite} {novo_i}'
            break
        else:
            limite = f'{limite} {i}'

    return limite



def cep(publi):
    n_cep = 'nao informado'
    for palavra in publi.split():
        if '-' in palavra:
            partes = palavra.split('-')
            if len(partes) == 2 and len(partes[1].replace(',', '').replace('.', '')) == 3:
                n_cep = palavra.rstrip(',.')
                break
    return n_cep



def area(publi):
    n_area = 'nao informado'
    palavras = publi.split()
    for i in range(len(palavras)):
        if 'm2' in palavras:
            nada='nada'
        if palavras[i].isdigit() and i+1 < len(palavras) and (palavras[i+1] == 'metros' or palavras[i+1] == 'm2' or palavras[i+1] == 'm2.' or palavras[i+1] == 'm2,'):
            n_area = palavras[i]
            break
    return n_area
            
 
 
def valor(publi):
    n_valor = 'nao informado'
    publi_separado = publi.split()
    for i , palavra in enumerate(publi_separado):
        if 'R$' in palavra:
            n_valor = palavra.replace('R$', '').rstrip('.')
            break
        elif 'reais' in palavra:
            n_valor = publi_separado[i-1]
            break
    if n_valor[-1] == ',':
        n_valor = n_valor[:-1] 
    return n_valor



def telefone (publi):
    n_tel = 'nao informado'
    lista_tel = []
    for palavra in publi.split():
        if '-' in palavra:
            partes = palavra.split('-')
            if len(partes) == 2 and len(partes[1].replace(',', '').replace('.', '')) == 4:
                n_tel = palavra.rstrip(',.')
                lista_tel.append(n_tel)
    formatado = ', '.join(lista_tel)
    if len(lista_tel) >= 2:
        formatado = 'Telefones: ' + formatado
    else:
        formatado = 'Telefone: ' + formatado

    return formatado



def responsavel(publi):
    responsavel = 'nao informado'
    sentencas = publi.split('. ')
    ultima_sentenca = sentencas[-1]

    palavras = ultima_sentenca.split()

    i = len(palavras) - 1
    while i >= 0:
        if palavras[i].istitle(): 
            responsavel = palavras[i]
            j = i - 1
            while j >= 0 and palavras[j].istitle():
                responsavel = palavras[j] + ' ' + responsavel
                if ',' in responsavel:
                    responsavel = responsavel.replace(',', '')
                elif '.' in responsavel:
                    responsavel = responsavel.replace('.' , '')
                j -= 1
            break
        i -= 1

    return responsavel
    
    

    

publi = input()
resultado_modalidade = f'Modalidade: {modalidade(publi.lower())}'
print(resultado_modalidade)
resultado_tipo = f'Tipo: {tipo(publi.lower())}'
print(resultado_tipo)
resultado_endereço = f'Endereco: {endereço(publi)}'
print(resultado_endereço)
resultado_cep = f'CEP: {cep(publi)}'
print(resultado_cep)
resultado_area = f'Area: {area(publi)}'
print(resultado_area)
resultado_valor = f'Valor: {valor(publi)}'
print(resultado_valor)
resultado_telefone = f'{telefone(publi)}'
print(resultado_telefone)
resultado_responsavel = f'Responsavel: {responsavel(publi)}'
print(resultado_responsavel)

"""
exemplos de input:

Rua da Lua 42 12345-678, 13 metros quadrados, apartamento para alugar. R$2357. Ligue dja! 9876-5432 ou 09876-5432. J J J.
Modalidade: Aluguel
Resultado:
Tipo: Apartamento
Endereco: Rua da Lua 42
CEP: 12345-678
Area: 13
Valor: 2357
Telefones: 9876-5432, 09876-5432
Responsavel: J J J


9876-5432. Aluguel de apartamento na Rua da Lua 42, 12345-678. R$2.357,00, 13 metros quadrados. J J.
Modalidade: Aluguel
Resultado:
Tipo: Apartamento
Endereco: Rua da Lua 42
CEP: 12345-678
Area: 13
Valor: 2.357,00
Telefone: 9876-5432
Responsavel: J J


Eu nao gostaria, mas estou endividado e preciso vender uma casa na Avenida Francisco Pereira Lopes, n. 7, no Cidade Jardim. A casa possui churrasqueira, piscina, 230 m2, 4 quartos, 1 suite, 3 vagas para carros, 1 sala e 1 quarto de servico. Tem um fusca velho guardado nos fundos, mas precisa quitar 20 parcelas vencidas do IPVA. O valor para venda eh 56234234 reais, mas faco desconto se quiser ficar com a minha sogra que soh sabe reclamar. Contato: 0000-0000. Falar com Illiarde Ubijara, tambem conhecido como jacare.
Modalidade: Venda
Resultado:
Tipo: Casa
Endereco: Avenida Francisco Pereira Lopes, n. 7
CEP: nao informado
Area: 230
Valor: 56234234
Telefone: 0000-0000
Responsavel: Illiarde Ubijara
"""