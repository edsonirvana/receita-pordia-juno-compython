# Transformações que separam Data de Liberação e Valor em listas, para compor o gráfico
# Há também a conversão de data para retirar valores zerados na exibição
array00=stage_transform2.index.to_numpy()
array0=pd.DatetimeIndex(array00).date
array1=stage_transform2['Valor'].to_numpy()

# Criação e Plotagem do gráfico de pizza
cores=['gold','goldenrod', 'red', 'blue', 'magenta', 'green','lightskyblue','orange','lightgreen',
       'yellowgreen', 'gray', 'yellow', 'green','teal','aqua', 'blue','purple','brown','darkcyan','lightblue']

# o atributo explode indica quais fatias do gráfico serão destacadas, 0.1 = destacar fatia  
explode = (0, 0, 0, 0, 0, 0.1, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 0)  # explode 1st slice

plt.title('Faturamento por Dia')

plt.pie(array1, labels=array0, explode=explode  ,colors=cores, autopct='%1.1f%%', shadow=True, startangle=90)

# Adiciona Legenda , neste caso está desativado, caso queira reciclar o código, retire o comentário para legendas flutuantes
# plt.legend(array0, bbox_to_anchor=(1.3, 1.3),loc='upper right')

# Ajustes de Espaçamento e Posição do gráfico
plt.axis('equal')
plt.tight_layout()
plt.show()
