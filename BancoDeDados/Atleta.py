class Atleta:
    def __init__(self, nome, idade, salario, talento, posicionamento,
                 visao, inteligencia, vontade, passe, recepcao, corrida,
                 movimentacao, tackling, bloqueio, chute, punt, velocidade,
                 forca, agilidade, vitalidade, disciplina, consistencia,
                 qb, wr, rb, fb, te, ol, fs, ss, cb, lb, nt, de):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.talento = float(talento)
        self.posicionamento = posicionamento
        self.visao = visao
        self.inteligencia = inteligencia
        self.vontade =  vontade
        self.passe = passe
        self.recepcao = recepcao
        self.corrida =  corrida
        self.movimentacao = movimentacao
        self.tackling = tackling
        self.bloqueio = bloqueio
        self.chute = chute
        self.punt = punt
        self.velocidade = velocidade
        self.forca = forca
        self.agilidade = agilidade
        self.vitalidade = vitalidade
        self.disciplina = disciplina
        self.consistencia = consistencia
        self.qb = qb
        self.wr = wr
        self.rb = rb
        self.fb = fb
        self.te = te
        self.ol = ol
        self.fs = fs
        self.ss = ss
        self.cb = cb
        self.lb = lb
        self.nt = nt
        self.de = de


    #Overall Quarterback
    def QB(self, passe, visao, inteligencia, movimentacao, agilidade, forca):
        self.qb = ((0.65*(passe+visao+inteligencia) + 0.35*(movimentacao+agilidade+forca))*100)/60
        self.qb = str(round(self.qb, 2))

    #Overall WideReceiver
    def WR(self, corrida, forca, agilidade, velocidade, visao, movimentacao):
        self.wr = ((0.65*(corrida+forca+agilidade) + 0.35*(velocidade+visao+movimentacao))*100)/60
        self.wr = str(round(self.wr, 2))

    #Overall RunningBack
    def RB(self, corrida, agilidade, bloqueio, forca, movimentacao, velocidade):
        self.rb = ((0.65*(corrida+agilidade+bloqueio) + 0.35*(forca+movimentacao+velocidade))*100)/60
        self.rb = str(round(self.rb, 2))

    #Overall FullBack
    def FB(self, bloqueio, forca, corrida, velocidade, movimentacao, agilidade):
        self.fb = ((0.65*(bloqueio+forca+corrida) + 0.35*(velocidade+movimentacao+agilidade))*100)/60
        self.fb = str(round(self.fb, 2))

    #Overall TightEnd
    def TE(self, bloqueio, recepcao, forca, movimentacao, agilidade, velocidade):
        self.te = ((0.65*(bloqueio+recepcao+forca) + 0.35*(movimentacao+agilidade+velocidade))*100)/60
        self.te = str(round(self.te, 2))

    #Overall OfensiveLine
    def OL(self, bloqueio, forca, visao, movimentacao, agilidade, velocidade):
        self.ol = ((0.65*(bloqueio+forca+visao) + 0.35*(movimentacao+agilidade+velocidade))*100)/60
        self.ol = str(round(self.ol, 2))

    #Overall FreeSafety
    def FS(self, movimentacao, inteligencia, velocidade, forca, agilidade, visao):
        self.fs = ((0.65*(movimentacao+inteligencia+velocidade) + 0.35*(forca+agilidade+visao))*100)/60
        self.fs = str(round(self.fs, 2))

    #Overall StrongSafety
    def SS(self, tackling,inteligencia, forca, agilidade, velocidade, visao):
        self.ss = ((0.65*(tackling+inteligencia+forca) + 0.35*(agilidade+velocidade+visao))*100)/60
        self.ss = str(round(self.ss, 2))

    #Overall CornerBack
    def CB(self, velocidade, posicionamento, tackling, visao, agilidade, movimentacao):
        self.cb = ((0.65*(velocidade+posicionamento+tackling) + 0.35*(visao+agilidade+movimentacao))*100)/60
        self.cb = str(round(self.cb, 2))

    #Overall LineBack
    def LB(self, inteligencia, tackling, forca, velocidade, agilidade, movimentacao):
        self.lb = ((0.65*(inteligencia+tackling+forca) + 0.35*(velocidade+agilidade+movimentacao))*100)/60
        self.lb = str(round(self.lb, 2))

    #Overall NoseTackle
    def NT(self, tackling, forca, agilidade, movimentacao, posicionamento, visao):
        self.nt = ((0.65*(tackling+forca+agilidade) + 0.35*(movimentacao+posicionamento+visao))*100)/60
        self.nt = str(round(self.nt, 2))

    #Overall DefensiveEnd
    def DE(self, tackling, forca, velocidade, agilidade, movimentacao, posicionamento):
        self.de = ((0.65*(tackling+forca+velocidade) + 0.35*(agilidade+movimentacao+posicionamento))*100)/60
        self.de = str(round(self.de, 2))