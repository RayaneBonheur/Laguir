import pandas as pd
from sklearn.preprocessing import StandardScaler
#coloque o caminho do arquivo nao normalizado aqui abaixo entre as aspas 
#exmeplo C:\\Users\\Admin\\OneDrive\\Documents\\nomalizacao\\dadosDesnormalizados.xlsx
caminho_arquivo_excel = 'C:\\Users\\Admin\\OneDrive\\Documents\\nomalização\\dadosDesnormalizados.xlsx'
dados = pd.read_excel(caminho_arquivo_excel)


colunas_para_normalizar = ['Pais', 'Indice de Empoderamento Feminino', 'Grupo de Empoderamento Feminino - 2022', 'Indice Global de Paridade de Genero', 'Grupo de Paridade de Genero - 2022', 'Grupo de Desenvolvimento Humano - 2021', 'Regioes do Objectivo de Desenvolvimento Sustentavel']
dados_originais = dados[colunas_para_normalizar].copy()
scaler = StandardScaler()

dados_normalizados = scaler.fit_transform(dados[colunas_para_normalizar])
dados_normalizados = pd.DataFrame(dados_normalizados, columns=colunas_para_normalizar)
dados[colunas_para_normalizar] = dados_normalizados


colunas_para_reverter = ['Pais', 'Grupo de Empoderamento Feminino - 2022', 'Indice Global de Paridade de Genero', 'Grupo de Desenvolvimento Humano - 2021', 'Regioes do Objectivo de Desenvolvimento Sustentavel']  

mapeamento_country = {1: 'Australia', 2: 'Belgium', 3: 'Denmark', 4: 'Iceland', 5: 'Norway', 6: 'Sweden', 7: 'Austria', 8: 'Bulgaria', 9: 'Canada', 10: 'Croatia', 11: 'Czechia', 12: 'Estonia', 13: 'Finland', 14: 'France', 15: 'Germany', 16: 'Hungary', 17: 'Ireland', 18: 'Italy', 19: 'Latvia', 20: 'Lithuania', 21: 'Luxembourg', 22: 'Netherlands', 23: 'Poland', 24: 'Portugal', 25: 'Serbia', 26: 'Singapore', 27: 'Slovenia', 28: 'Spain', 29: 'Switzerland', 30: 'United Kingdom', 31: 'United States', 32: 'Albania', 33: 'Armenia', 34: 'Bolivia', 35: 'Brazil', 36: 'Chile', 37: 'China', 38: 'Costa Rica', 39: 'Cyprus', 40: 'Dominican Republic', 41: 'Ecuador', 42: 'Greece', 43: 'Israel', 44: 'Jamaica', 45: 'Japan', 46: 'Malta', 47: 'Mauritius', 48: 'Moldova', 49: 'Mongolia', 50: 'Montenegro', 51: 'Namibia', 52: 'North Macedonia', 53: 'Peru', 54: 'Philippines', 55: 'Romania', 56: 'Slovakia', 57: 'South Africa', 58: 'Thailand', 59: 'United Arab Emirates', 60: 'Uruguay', 61: 'Viet Nam', 62: 'Bangladesh', 63: 'Belize', 64: 'Benin', 65: 'Bhutan', 66: 'Bosnia and Herzegovina', 67: 'Botswana', 68: 'Burkina Faso', 69: 'Burundi', 70: 'Cambodia', 71: 'Cameroon', 72: 'Colombia', 73: 'Congo', 74: 'Côte d\'Ivoire', 75: 'Egypt', 76: 'El Salvador', 77: 'Gambia', 78: 'Ghana', 79: 'Guatemala', 80: 'Guinea', 81: 'Honduras', 82: 'India', 83: 'Indonesia', 84: 'Iran', 85: 'Iraq', 86: 'Jordan', 87: 'Kenya', 88: 'Laos', 89: 'Lebanon', 90: 'Lesotho', 91: 'Liberia', 92: 'Malawi', 93: 'Maldives', 94: 'Mali', 95: 'Mexico', 96: 'Myanmar', 97: 'Nepal', 98: 'Niger', 99: 'Nigeria', 100: 'Pakistan', 101: 'Panama', 102: 'Paraguay', 103: 'Rwanda', 104: 'Senegal', 105: 'Sierra Leone', 106: 'Sri Lanka', 107: 'Tanzania', 108: 'Togo', 109: 'Tunisia', 110: 'Türkiye', 111: 'Uganda', 112: 'Yemen', 113: 'Zambia', 114: 'Zimbabwe'}
mapeamento_wei_2022 = {4:'High', 3:'Upper-middle', 2:'Lower-middle', 1:'Low'} 
mapeamento_ggpi_2022 = {4:'High', 3:'Upper-middle', 2:'Lower-middle', 1:'Low'} 
mapeamento_hdi_2021 = {4:'Very high', 3:'High', 2:'Medium', 1:'Low'} 
mapeamento_sdg_regions = {1:'Australia and New Zealand', 2:'Europe and Northern America', 3:'Eastern Asia and South-Eastern Asia', 
 5: 'Northern Africa and Western Asia', 4:'Latin America and the Caribbean', 6:'Sub-Saharan Africa', 7:'Central Asia and Southern Asia'}


for coluna in colunas_para_reverter:
    if coluna in colunas_para_normalizar:
        mean = scaler.mean_[colunas_para_normalizar.index(coluna)]
        std = scaler.scale_[colunas_para_normalizar.index(coluna)]
        dados[coluna] = (dados[coluna] * std) + mean

dados['Pais'] = dados['Pais'].map(mapeamento_country)
dados['Grupo de Empoderamento Feminino - 2022'] = dados['Grupo de Empoderamento Feminino - 2022'].map(mapeamento_wei_2022)
dados['Indice Global de Paridade de Genero'] = dados['Indice Global de Paridade de Genero'].map(mapeamento_ggpi_2022)
dados['Grupo de Desenvolvimento Humano - 2021'] = dados['Grupo de Desenvolvimento Humano - 2021'].map(mapeamento_hdi_2021)
dados['Regioes do Objectivo de Desenvolvimento Sustentavel'] = dados['Regioes do Objectivo de Desenvolvimento Sustentavel'].map(mapeamento_sdg_regions)

caminho_arquivo_csv_normalizado = 'C:\\Users\\Admin\\OneDrive\\Desktop\\dados_normalizado.csv'
dados.to_csv(caminho_arquivo_csv_normalizado, index=False)

print("Dados normalizados salvos com sucesso em:", caminho_arquivo_csv_normalizado)
