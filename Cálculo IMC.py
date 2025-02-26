#leia o peso e a altura de uma pessoa, calcule seu índice de massa corporal (IMC), classifique
#essa pessoa de acordo com a tabela e escreva na tela a condição da pessoa:

def calculo_imc():
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    
    IMC = peso / (altura **2)
    
    if IMC <= 18.5:
        print ("Você está excessivamente magro")
    elif IMC <= 25:
        print ("Seu peso está normal")
    elif IMC <= 30:
        print ("Você está com sobrepreso")
    else:
        print ("Você está obeso")
        
    print (f"O seu IMC é {IMC}  ")
calculo_imc()
