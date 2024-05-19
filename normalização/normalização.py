import pandas as pd

csv_file = "women_empowerment_index.csv"

dados = pd.read_csv(csv_file)

print(dados.head())

countries = dados[['Country']].drop_duplicates()
wei_data = dados[['Country', "Women's Empowerment Index (WEI) - 2022", "Women's Empowerment Group - 2022"]].drop_duplicates()
ggpi_data = dados[['Country', "Global Gender Parity Index (GGPI) - 2022", "Gender Parity Group - 2022"]].drop_duplicates()
hdi_data = dados[['Country', "Human Development Group - 2021"]].drop_duplicates()
sdg_data = dados[['Country', "Sustainable Development Goal regions"]].drop_duplicates()

countries.to_csv("countries.csv", index=False)
wei_data.to_csv("wei_data.csv", index=False)
ggpi_data.to_csv("ggpi_data.csv", index=False)
hdi_data.to_csv("hdi_data.csv", index=False)
sdg_data.to_csv("sdg_data.csv", index=False)

print("concluido com sucesso :D")
