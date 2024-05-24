""" 
A estrutura tarifária:
Água (Residencial)
Consumo                                         Valor (R$)
Até 10.000 litros/mês	                         56,16 

Esgotamento Sanitário
(Residencial)
Tipo                                           Valor (R$)
Sistema Convencional	              Ligação Convecional ou ramal de calçada - 
                                            100% da tarifa de água
"""

def calcular_conta_agua_e_esgoto(consumo_litros, tarifa_agua):
    # Limitando o consumo máximo em 10.000 litros por mês
    consumo = min(consumo_litros, 10000)
    
    # Calculando o valor da conta de água
    valor_conta_agua = tarifa_agua * consumo
    
    # Calculando o valor da conta de esgoto (utilizando 100% da tarifa de água)
    valor_conta_esgoto = valor_conta_agua
    
    # Calculando o total da conta (água + esgoto)
    total_conta = valor_conta_agua + valor_conta_esgoto
    
    return total_conta

# Tarifa de água (por litro)
tarifa_agua = 0.005616  # R$0,005616 por litro

# Consumo em litros por mês
consumo_litros = 10000  # Exemplo de consumo de até 10.000 litros por mês

# Calculando o valor da conta de água e esgoto
conta_total = calcular_conta_agua_e_esgoto(consumo_litros, tarifa_agua)

print("\n####### Conta água e esgoto residencial #######\n")
print("O valor total da conta de água e esgoto é: R$%.2f" % conta_total)
