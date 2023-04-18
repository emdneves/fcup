capital_inicial = float(input("Digite o capital inicial: "))
taxa_juros_anual = float(input("Digite a taxa de juros anual (%): "))

taxa_juros_mensal = taxa_juros_anual / 12 / 100
# dividimos por 12 para obter a taxa mensal e por 100 para converter de porcentagem para decimal

print("Tabela de juros compostos após cada mês:")
print("Mês  | Capital Final")

for n in range(0, 25):
    capital_final = capital_inicial * (1 + taxa_juros_mensal)**n
    print(str(n - 1) + " | " + str(capital_final) + " €")
    print(n)
    print(capital_final)