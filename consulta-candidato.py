import csv
import pandas as pd


print("=== CONSULTA RESULTADO ELEIÇÕES 2022 ES ===\n")
numero_cdt = int(input("DIGITE O NÚMERO DO CANDIDATO: "))

url_resultado = './votacao_secao_2022_ES.csv'
#resultados obtidos de: https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_2022_ES.zip

#realiza a leitura da tabela de resultados do TSE extraindo apenas as colunas desejadas
df = pd.read_csv(
    url_resultado,
    encoding='latin1',
    sep=';',
    usecols=['NM_MUNICIPIO','DS_CARGO','NR_VOTAVEL','NM_VOTAVEL','QT_VOTOS']
)

#Filtro separa os votos pelo Numero do Candidato
select_votos = df['NR_VOTAVEL'] == numero_cdt
votos = df[select_votos]
if votos.empty==False: #Se candidato encontrado realiza as operações
    print("CANDIDATO(A): ",votos.iat[0,3])
    print("CARGO: ",votos.iat[0,1])
    #Soma os votos por município e salva em um arquivo csv 
    municipios = votos.groupby('NM_MUNICIPIO')['QT_VOTOS'].sum()
    municipios.to_csv(r'.\resultado_'+votos.iat[0,3]+'_'+votos.iat[0,1]+'.csv', encoding='latin1', sep=';')
    #Soma e exibe o total de votos recebidos
    print("TOTAL DE VOTOS: ",municipios.sum())
    print("Arquivo de votos por município gerado com sucesso.")
else: #Candidato não encontrado
    print("CANDIDATO(A) NÃO ENCONTRADO(A)!")

