#dados a renda do consumidor e o preço de um bem, calcule a quantidade de demandada deste bem, sabendo que sua função de demanda é dada por q = renda/preco

def demanda():
    
    #entrada de dados
    renda_consumidor = float(input("Digite a renda do consumidor: "))
    preço_bem = float(input("Digite o preço do bem: "))
    
    #calculo de demanda
    quantidade_demandada = renda_consumidor/preço_bem
    
    #visualizaçao da demanda
    print (f"A quantidade demandada deste bem é {quantidade_demandada}")

demanda()



