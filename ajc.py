
from pandas import read_excel, DataFrame
from datetime import datetime
from re import sub
import json

df = read_excel(
	'BLOQUEIOS E DEPÓSITOS 2023 - AJC (1).xlsx', 
	usecols = 'B:L', 
	skiprows = 1,
	sheet_name = 'BLOQUEIOS JUDICIAIS 2023'
)

df = df.filter(
	[
		'PROCESSO REGULARIZAÇÃO', 'PROCESSO JUDICIAL', 'DATA TRANSFERÊNCIA', 
		'OBJETO DETALHADO', 'JUSTIFICATIVA P/ O NÃO CUMPRIMENTO'
	]
)

df['CHAVE'] = df['PROCESSO JUDICIAL'] + '#' + df['PROCESSO REGULARIZAÇÃO'] + '#' + df['DATA TRANSFERÊNCIA'].apply(datetime.strftime, format = '%d%m%Y')

df['OBJETO DETALHADO'] = [sub('\.', ',', i) for i in df['OBJETO DETALHADO']]

df = df.filter(['CHAVE', 'OBJETO DETALHADO']).groupby(['CHAVE']).agg({'OBJETO DETALHADO': ', '.join}).reset_index().to_dict('records')

for i in df:

	i['OBJETO DETALHADO'] = [j.strip().capitalize() for j in i['OBJETO DETALHADO'].split(',')]

print(DataFrame(df).explode('OBJETO DETALHADO').to_excel('DATA.xlsx', index = False))
