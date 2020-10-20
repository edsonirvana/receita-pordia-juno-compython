# Importando a Biblioteca Pandas, Numpy e Matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Caregando a base de dados em .xlsx, extração da área de extrato da Juno
origem_juno = pd.read_excel('arquivo.xlsx')

# Transformações quem que limpam a base deixando apenas dados de Pagamento e as colunas que serão utilizadas na análise
stage_transform0 = origem_juno.loc[origem_juno['Tipo']=='Pagamento']
stage_transform1 = stage_transform0.drop(["Descrição","Data","CPF/CNPJ Cliente","Nome Cliente"], axis=1)

# Transformação que agrupa a soma da receita por dia
stage_transform2 = stage_transform1.groupby(['Data de Liberação']).sum()

# Ao executar a chamada do ultimo DataFrame, terá de sáida algo parecido com isso :: OBs.: dados fictícios
# stage_transform2
#                     Valor
# Data de Liberação         
# 2020-08-01         3180.60
# 2020-08-04         6879.06
# 2020-08-05         2919.96
# 2020-08-06         5285.70
# 2020-08-07         2844.90
# 2020-08-08         5444.91
# 2020-08-11         9103.14
# 2020-08-12         3800.70
# 2020-08-13         2179.26
# 2020-08-14         1978.74
# 2020-08-18         3660.93
# 2020-08-19         1426.68
# 2020-08-20         1956.78
# 2020-08-21         2452.14
# 2020-08-22         1001.70
# 2020-08-25         6279.48
# 2020-08-26         1453.32
# 2020-08-27          954.00
# 2020-08-28         3699.90
# 2020-08-29         1011.60

# Para uma melhor análise, pode-se continuar a exploração executando um gráfico pizza.
# A continuação do código és no arquivo grafico.py, que possui dependêcia deste código scrip.py
