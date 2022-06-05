import pandas as pd


url = "https://gist.githubusercontent.com/tgcsantos/3bdb29eba6ce391e90df2b72205ba891/raw/22fa920e80c9fa209a9fccc8b52d74cc95d1599b/dados_imoveis.csv"
dados = pd.read_csv(url)
busca_vila_mariana = (dados["Bairro"]== "Vila Mariana")
vila_mariana = dados[busca_vila_mariana]
numeros_de_imoveis_por_bairro = dados["Bairro"].value_counts()
print(numeros_de_imoveis_por_bairro.plot.hist())
