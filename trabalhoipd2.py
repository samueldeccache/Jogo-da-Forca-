# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 07:44:32 2019

@author: Samsung
"""

#   Jogo: Adivinhe 
#Regras: #1- o jogador deverá botar seu nome
                 #2- o jogador deverá escolher um tema proposto
                 #3- o jogo sorteará uma palavra do tema escolhido pelo jogador
                 #4 - o jogador terá o mesmo numero de chances do que o numero de letras da palavra.
                 #5- cada letra que o jogador acertar contará um ponto.
                 #6- no final das tentativas, o jogador terá que adivinhar a palavra sorteada.
                 #7- se o jogador acertar a palavra sorteada ele somará 5 pontos + os pontos da letra que ele acertou.
                 #8 - se o jogador errar a palavra, mesmo que acertando as letras, ele somará 0 pontos. 
#primeiros importamos a biblioteca random e a biblioteca pandas
import random
import pandas as pd
#criamos os contadores cont e soma
cont=0
soma=0
nome=input('qual seu nome:')
while nome=='':
    nome=input('qual seu nome:')
#criamos tambem a variavel pontos_iniciais
pontos_iniciais=0
#criamos o vetor da palavra real
vet_real=[]
#o vetor com as letras escondidas
vet=[]
#criamos listas com temas como frutas e lugares
frutas=['uva','limao','caqui','figo','melao','pera']
lugares=['brasil','belgica','chile','china','israel','mexico','noruega']
#entramos para escolher o tema
escolha_tema=input('escolha um tema( frutas ou lugares):')
#se voce escolher qualquer outro tema, o programa retornará a mesma pergunta.
#determinando a condiçao de escolha do tema
while escolha_tema!='frutas' and escolha_tema!='lugares':
    escolha_tema=input('escolha um tema( frutas ou lugares):')
if escolha_tema=='frutas':
    x=random.choice(frutas)
elif escolha_tema=='lugares':
    x=random.choice(lugares)
    #escolhido o tema frutas, x e a variavel que vai escolher qual fruta da lista sera utilizada
    #percorrendo a palavra escolhida
for i in range(len(x)):
    #adicionando no lugar de cada letra um '-' para saber quantas letras tem. 
    vet.append('_')
    #separando as letras numa lista. cada letra sera um elemento da lista
    vet_real.append(x[i])
    soma+=1
#print(vet)
print('voce tem:',soma,'chances')
#percorrendo o vetor real
for i in range(len(vet_real)):
    #entrando com uma letra
    a=input('letra:')
    #se essa letra estiver na lista do vetor real, localizar aonde essa letra esta.
    if a in vet_real:
        b=vet_real.index(a)
        #o vetor da localização é igual a letra.
        vet[b]=a
        #imprimindo o vetor na localização da letra
        print(vet)
        #cada letra que tiver no vetor, sera contado um ponto
        cont+=1
        #caso contrario, voce tera uma chance disperdiçada, lembrando que o numero de chances e igual ao numero de letras da palavra
    else:
        print('letra inexistente na palavra.')
        #aqui voce tera a chance de acertar a palavra
palavra=input('digite o nome da palavra:')
#se acertar a palavra voce, a variavel cont tera +5 pontos
if palavra==x:
    cont+=5
    #os pontos iniciais serao a soma de todos os pontos somados durante a partida
    pontos_iniciais+=cont
    print('voce ganhou',pontos_iniciais,'pontos')
else:
    print('voce ganhou',pontos_iniciais,'pontos.')
#abrindo o arquivo ranking.txt e adicionando no arquivo o nome e os pontos ganhos na partida
arquivo=open('ranking13.txt','a')
arquivo.write(nome)
arquivo.write(' ')
arquivo.write(str(pontos_iniciais))
arquivo.write('\n')
arquivo.close()
#abrindo o arquivo para leitura
arquivo=open('ranking13.txt','r')
linhas=arquivo.readlines()
vetor_pontos=[]
vetor_nomes=[]
#percorrendo cada linha do arquivo
for linha in linhas:
    #aplicando a variavel jogador 'splitando' a linha
    jogador=linha.split()
    #o primeiro elemento do dicionario vai ser o nome
    nome=jogador[0]
    #transformando o 2 elemento, que são os pontos, em um vetor
    pontos=jogador[1:2]
    #transformar os nomes e os pontos em vetores para melhor analise de ranking
    for i in range(len(pontos)):
        vetor_pontos.append(int(pontos[i]))
        vetor_nomes.append(nome)
#print(vetor_pontos)
#print(vetor_nomes)
#criando um groupby com nomes e pontos e os respectivos vetores
data={'nomes':vetor_nomes,'pontos':vetor_pontos}
#criando um dataframe com o groupby
df=pd.DataFrame(data)
#print(df)
#criando uma coluna ranking com relação aos pontos
df['ranking'] = df.pontos.rank(method='dense', ascending = False).astype(int)
#botando em ordem crescente a coluna dos pontos
#o ascending indica se é em ordem crescente ou não
#o axis=0 significa a correlação das colunas 
#o inplace certifica que a operação é verdadeira 
df.sort_values("pontos",axis = 0, ascending = False,inplace = True)
print(df)
#só exemplo 
#só exemplo