from datetime import datetime

# Obter a primeira data
data1_str = input("Digite a primeira data (formato: DD/MM/AAAA): ")
data1 = datetime.strptime(data1_str, "%d/%m/%Y")

# Obter a segunda data
data2_str = input("Digite a segunda data (formato: DD/MM/AAAA): ")
data2 = datetime.strptime(data2_str, "%d/%m/%Y")

# Calcular a diferença em dias
diferenca = data2 - data1
dias = diferenca.days

# Exibir o resultado
print("A diferença em dias entre as datas é:", dias)
