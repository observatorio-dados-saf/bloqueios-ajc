
import nltk
import pickle
from nltk import word_tokenize

# nltk.download('punkt')

# model = pickle.load(open('POS_tagger_bigram.pkl', 'rb'))
# 
# text = '''
# A Organização Mundial da Saúde (OMS), desde a década de 1970, 
# estimula a promoção de políticas que promovam o acesso a medicamentos, recomendando a adoção de listas nacionais por seus países-
# -membros e publicando periodicamente uma lista modelo. O Brasil 
# deu início à elaboração de listas de medicamentos classificados como 
# essenciais em 1964, por meio do Decreto n.º 53.612, de 26 de dezembro de 1964, que definiu a Relação Básica e Prioritária de Produtos 
# Biológicos e Materiais para Uso Farmacêutico Humano e Veterinário. 
# Em 1975, por meio da publicação da Portaria n.º 233 do Ministério da 
# Previdência e Assistência Social, a lista foi oficializada como Relação 
# Nacional de Medicamentos Essenciais (Rename)
# '''
# 
# res = model.tag(word_tokenize(text))
# 
# print(
# 	res,
# 	'\n\n',
# 	' '.join([i[0] for i in res if i[1] == 'NPROP'])
# )
#
