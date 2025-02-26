#calcule o salário de um professor horista na Universidade XYZ
#O programa deve perguntar o número de horas trabalhadas, calcular e imprimir na tela o valor do salário bruto, o salário líquido e do total de descontos, sabendo que o desconto do imposto é 30% e
#que o valor da hora-aula é R$ 40,00

def calcular_salario():
    # Definição das constantes
    VALOR_HORA_AULA = 40.00
    IMPOSTO = 0.30  # 30%
    
    # Entrada de dados
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
    
    # Cálculo do salário
    salario_bruto = horas_trabalhadas * VALOR_HORA_AULA
    total_descontos = salario_bruto * IMPOSTO
    salario_liquido = salario_bruto - total_descontos
    
    # Exibição dos resultados
    print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
    print(f"Total de Descontos: R$ {total_descontos:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Execução da função
calcular_salario()