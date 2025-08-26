import pandas as pd

df = pd.read_excel(r"C:\Users\Calafange\PycharmProjects\GridIron\BancoDeDados\Time GI.xlsx")

manutencaoEstadio = 12680
salarioTreinadores = 12500
salarioMedicos = 2250
salariosAtletas = df['Salario'].sum()
idade_media = str(round(df["Idade"].mean(),2))
elenco = str(df["Nome"].count())
despesas = manutencaoEstadio + salarioMedicos + salarioTreinadores + salariosAtletas

top3_qb = df.nlargest(3,"QB")[['Nome','QB',"Consistencia"]]
top5_wr = df.nlargest(5,"WR")[['Nome','WR',"Consistencia"]]
top3_rb = df.nlargest(3,"RB")[['Nome','RB',"Consistencia"]]
top3_fb = df.nlargest(3,"FB")[['Nome','FB',"Consistencia"]]
top4_te = df.nlargest(4,"TE")[['Nome','TE',"Consistencia"]]
top7_ol = df.nlargest(7,"OL")[['Nome','OL',"Consistencia", "Passe"]]
top3_fs = df.nlargest(3,"FS")[['Nome','FS',"Consistencia"]]
top3_ss = df.nlargest(3,"SS")[['Nome','SS',"Consistencia"]]
top5_cb = df.nlargest(5,"CB")[['Nome','CB',"Consistencia"]]
top6_lb = df.nlargest(6,"LB")[['Nome','LB',"Consistencia", "Inteligencia"]]
top7_dl = df.nlargest(7,"DE")[['Nome','DE',"Consistencia"]]


print(top3_qb)
print(top7_ol)
print(top3_rb)
print(top5_wr)
print(top3_fb)
print(top4_te)
print(top3_fs)
print(top3_ss)
print(top5_cb)
print(top6_lb)
print(top7_dl)


print("Folha de pagamento: " + str(despesas))
print("Media de idade: " + idade_media)
print("Tamanho do elenco: " + elenco)