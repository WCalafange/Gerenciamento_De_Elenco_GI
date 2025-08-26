print("===== DESCUBRA O OVERALL DO ATLETA PARA CADA POSICAO =====")

nome = input("Digite o nome do atleta: ")
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

#Overall Quarterback
qb = ((0.65*(passe+visao+inteligencia) + 0.35*(movimentacao+agilidade+forca))*100)/60
qb = str(round(qb,2))

#Overall WideReceiver
wr = ((0.65*(corrida+forca+agilidade) + 0.35*(velocidade+visao+movimentacao))*100)/60
wr = str(round(wr,2))

#Overall RunningBack
rb = ((0.65*(corrida+agilidade+bloqueio) + 0.35*(forca+movimentacao+velocidade))*100)/60
rb = str(round(rb,2))

#Overall FullBack
fb = ((0.65*(bloqueio+forca+corrida) + 0.35*(velocidade+movimentacao+agilidade))*100)/60
fb = str(round(fb,2))

#Overall TightEnd
te = ((0.65*(bloqueio+recepcao+forca) + 0.35*(movimentacao+agilidade+velocidade))*100)/60
te = str(round(te,2))

#Overall OfensiveLine
ol = ((0.65*(bloqueio+forca+visao) + 0.35*(movimentacao+agilidade+velocidade))*100)/60
ol = str(round(ol,2))

#Overall FreeSafety
fs = ((0.65*(movimentacao+inteligencia+velocidade) + 0.35*(forca+agilidade+visao))*100)/60
fs = str(round(fs,2))

#Overall StrongSafety
ss = ((0.65*(tackling+inteligencia+forca) + 0.35*(agilidade+velocidade+visao))*100)/60
ss = str(round(ss,2))

#Overall CornerBack
cb = ((0.65*(velocidade+posicionamento+tackling) + 0.35*(visao+agilidade+movimentacao))*100)/60
cb = str(round(cb,2))

#Overall LineBack
lb = ((0.65*(inteligencia+tackling+forca) + 0.35*(velocidade+agilidade+movimentacao))*100)/60
lb = str(round(lb,2))

#Overall NoseTackle
nt = ((0.65*(tackling+forca+agilidade) + 0.35*(movimentacao+posicionamento+visao))*100)/60
nt = str(round(nt,2))

#Overall DefensiveEnd
dl = ((0.65*(tackling+forca+velocidade) + 0.35*(agilidade+movimentacao+posicionamento))*100)/60
dl = str(round(dl,2))

print(nome + " |QB: " + qb + " |WR: " + wr + " |RB: " + rb + " |FB: " + fb + " |TE: " + te + " |OL: " + ol +
     " |FS: " + fs + " |SS: " + ss + " |CB: " + cb + " |LB: " + lb + " |NT: " + nt + " |DL: " + dl )