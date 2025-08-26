import pandas as pd
import openpyxl
from Atleta import Atleta
import os

#Criando novos atletas
def cria_atleta(tabela):

    nome = input("Digite o nome do atleta: ")
    idade = input("Idade: ")
    salario = int(input("Salario: "))
    talento = input("Talento: ")
    posicionamento = int(input("Posicionamento: "))
    visao = int(input("Visao: "))
    inteligencia = int(input("Inteligencia: "))
    vontade = int(input("Vontade: "))
    passe = int(input("Passe: "))
    recepcao = int(input("Recepcao: "))
    corrida = int(input("Corrida: "))
    movimentacao = int(input("Movimentacao: "))
    tackling = int(input("Tackling: "))
    bloqueio = int(input("Bloqueio: "))
    chute = int(input("Chute: "))
    punt = int(input("Punt: "))
    velocidade = int(input("Velocidade: "))
    forca = int(input("Forca: "))
    agilidade = int(input("Agilidade: "))
    vitalidade = int(input("Vitalidade: "))
    disciplina = int(input("Disciplina: "))
    consistencia = int(input("Consistencia: "))

    #Criando um novo atleta
    atleta_novo = Atleta(nome, idade, salario, talento, posicionamento,
             visao, inteligencia, vontade, passe, recepcao, corrida,
             movimentacao, tackling, bloqueio, chute, punt, velocidade,
             forca, agilidade, vitalidade, disciplina, consistencia,
             qb=0, wr=0, rb=0, fb=0, te=0, ol=0, fs=0, ss=0, cb=0, lb=0,
             nt=0, de=0)
    atleta_novo.QB(passe, visao, inteligencia, movimentacao, agilidade, forca)
    atleta_novo.WR(corrida, forca, agilidade, velocidade, visao, movimentacao)
    atleta_novo.RB(corrida, agilidade, bloqueio, forca, movimentacao, velocidade)
    atleta_novo.FB(bloqueio, forca, corrida, velocidade, movimentacao, agilidade)
    atleta_novo.TE(bloqueio, recepcao, forca, movimentacao, agilidade, velocidade)
    atleta_novo.OL(bloqueio, forca, visao, movimentacao, agilidade, velocidade)
    atleta_novo.FS(movimentacao, inteligencia, velocidade, forca, agilidade, visao)
    atleta_novo.SS(tackling,inteligencia, forca, agilidade, velocidade, visao)
    atleta_novo.CB(velocidade, posicionamento, tackling, visao, agilidade, movimentacao)
    atleta_novo.LB(inteligencia, tackling, forca, velocidade, agilidade, movimentacao)
    atleta_novo.NT(tackling, forca, agilidade, movimentacao, posicionamento, visao)
    atleta_novo.DE(tackling, forca, velocidade, agilidade, movimentacao, posicionamento)

    #Convertendo para um DataFrame
    novo_dado = {"Nome":atleta_novo.nome, "Idade":atleta_novo.idade, "Salario":atleta_novo.salario,
                 "Talento":atleta_novo.talento, "Posicionamento":atleta_novo.posicionamento,
                 "Visao":atleta_novo.visao, "Inteligencia":atleta_novo.inteligencia,
                 "Vontade":atleta_novo.vontade, "Passe":atleta_novo.passe,
                 "Recepcao":atleta_novo.recepcao, "Corrida":atleta_novo.corrida,
                 "Movimentacao":atleta_novo.movimentacao, "Tackling":atleta_novo.tackling,
                 "Bloqueio":atleta_novo.bloqueio, "Chute":atleta_novo.chute,
                 "Punt":atleta_novo.punt, "Velocidade":atleta_novo.velocidade,
                 "Forca":atleta_novo.forca, "Agilidade":atleta_novo.agilidade,
                 "Vitalidade":atleta_novo.vitalidade, "Disciplina":atleta_novo.disciplina,
                 "Consistencia":atleta_novo.consistencia, "QB":atleta_novo.qb, "WR":atleta_novo.wr,
                 "RB":atleta_novo.rb, "FB":atleta_novo.fb, "TE":atleta_novo.te, "OL":atleta_novo.ol,
                 "FS":atleta_novo.fs, "SS":atleta_novo.ss, "CB":atleta_novo.cb, "LB":atleta_novo.lb,
                 "NT":atleta_novo.nt, "DE":atleta_novo.de}

    #Concatenando com os dados existentes
    tabela = pd.concat([tabela, pd.DataFrame([novo_dado])], ignore_index=True)
    print(tabela)

    #Escreve DataFrame em arquivo Xlsx
    tabela.to_excel("Time GI.xlsx", index=False, engine="openpyxl")

    return tabela

#Verifica se há um arquivo Xls, caso contrario ira criar  um
if os.path.exists("Time GI.xlsx"):
    bd = pd.read_excel("Time GI.xlsx", engine="openpyxl")
else:
    bd = pd.DataFrame(columns=[])

#Menu que sera apresentando ao usuario
menu = ("-----------------------------------\n"
        "Selecione uma das seguintes opcoes:\n"
        "1 - Adicionar\n"
        "2 - Remover\n"
        "3 - Ver DataFrame\n"
        "0 - Sair\n"
        )

#Loop do Menu
while True:
    acao = int(input(menu))
    if acao == 1:
        bd = cria_atleta(bd)
    elif acao == 2:
        exclui = str(input("Digite o nome de quem deverá sair da lista: "))
        if exclui not in bd["Nome"].values:
            print("Jogador não cadastrado")
        else:
            bd = bd[bd["Nome"] != exclui]
            bd.to_excel("Time GI.xlsx", index=False, engine = "openpyxl")
            print(exclui + " removido com sucesso")
    elif acao == 3:
        if bd.empty:
            print("Não há nenhum jogador cadastrado.")
        else:
            print(bd)
    elif acao == 0:
        break
    else:
        acao = input(menu)