#Dado o número de horas trabalhadas por um empregado de uma empresa que paga R$20,00 por hora trabalhada e desconta imposto de renda (ir) segundo a tabela abaixo,
#determine o salário líquido do empregado.

def salario():
    
    #entrada de dado
    horas_trabalhadas = float(input("Quantas horas você trabalha por mês? "))
    
    #variaveis
    valor_hora = 20 
    salario_bruto = horas_trabalhadas * valor_hora
    
    #condições 
    if salario_bruto <= 1000:
        aliquota = 0
    elif salario_bruto <= 2500:
        aliquota = 0.1
    elif salario_bruto <= 5000:
        aliquota = 0.2 
    else:
        aliquota = 0.35
        
     #calculos
    imposto = salario_bruto * aliquota
    salario_liquido = salario_bruto - imposto
     
    print (f"O Salário Bruto é R$ {salario_bruto}")
    print (f"O Valor de desconto é R$ {imposto}")
    print (f"O Salário Líquido é R$ {salario_liquido}")
salario()



        
        
        
        
        
        
        
        