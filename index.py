from copy import copy
from math import fsum
from operator import index
with open('c://Users//pveni//OneDrive//Documentos//Teste_interlitrader//Produtos.txt','r') as produtos:
    content = produtos.read()
    produtos.close()
    produtos = content.split('\n')
    for c in range(len(produtos)):
        produtos[c] = produtos[c].split(';')
with open('c://Users//pveni//OneDrive//Documentos//Teste_interlitrader//vendas.txt','r') as vendas:
    contvendas= vendas.read()
    vendas.close()
    vendas= contvendas.split('\n')
    for  c in range(len(vendas)):
        vendas[c] = vendas[c].split(';')
    vendas.pop()
#  Passo 1   
    qtv=[]
    for c in vendas:
        if c[2] == "100" or  c[2] == "102":
            qtv.append(c[0:2])
    def preencher(lista, valores):
        for j in lista:
            for k in valores:
                if j[0] == k[0]:
                    j.append(int(*k[1:]))
    preencher(produtos,qtv)   
    
    totvendas=[]
    for c in produtos:
        totvendas.append(c[3:])
    for c in produtos:
        del c[3:] 
    qtvendidas=[]
    for c in totvendas:
        qtvendidas.append(sum(c))
    for c in range(len(produtos)):
        produtos[c].append(qtvendidas[c])
    for c in produtos:
        c[1]= int(c[1])
    estoque=[] 
    for c in produtos:
        estq= c[1]-c[3]
        estoque.append(estq)
    for c in range(len(produtos)):
        produtos[c].append(estoque[c])
    for c in produtos:
        c[2]= int(c[2])

    necess=[]
    for c in produtos:
        if c[4] >= c[2]:
            necess.append(0)
        else:
            soma= c[4]-c[2]
            necess.append(soma-soma-soma)
    for c in range(len(produtos)):
        produtos[c].append(necess[c])
    transf=[]
    for c in produtos:
        if c[5] >= 1 and c[5] <= 10:
            transf.append(10)
        else: 
            transf.append(c[5])        
    for c in range(len(produtos)):
        produtos[c].append(transf[c])
    
    print(f'''{'Produto'}       {'QtCo'}       {'QtMin'}        {'QtVendidas'}      {'Estq.ápos vendas'}        {'Necess.'}        {'Transf. de Arm p/ CO'}''''')
    print ('=-'*60)
    for c in produtos:
        print(f'{c[0]}         {c[1]}         {c[2]}             {c[3]}               {c[4]}                 {c[5]}                  {c[6]}')
    print('=-'*60)
#  Passo 2
    for c in vendas:
        c[0] = int(c[0])
    for c in produtos:
        c[0] = int(c[0])
    for c in vendas:
        c[2] = int(c[2]) 
    cv=[]
    cp=[]
    for c in produtos:
        cp.append(c[0])
    for c in vendas:
        cv.append(c[0])
    
            
    for v,c in enumerate(vendas):
        if c[2] == 135:
            print(f' Linha {v} - Venda cancelada.')
        elif c[2] == 190:
            print(f' Linha {v} - Venda não finalizada.')
        elif c[2] == 999:
            print(f' Linha {v} - Erro desconhecido. acionar equipe de TI.')
    for c,v  in enumerate(cv):
        if v not in cp:
            print(f' Linha {c} - Código de produto não encontrado {v}')
          
    print('=-'*60) 
# Passo 3  
    canais=[]        
    for c in vendas:
        if c[2] == 100 or  c[2] == 102:
            canais.append(c[:])
    for c in canais:
        c[1]= int(c[1])   
    repre=[]
    web=[]
    android=[]
    iphone=[]
    for c in canais:
        if c[3] == '1':
            repre.append(c[1])
        elif c[3] == '2':
            web.append(c[1])
        elif c[3] == '3':
            android.append(c[1])  
        else:
            iphone.append(c[1])
    print(f'''1 - representantes     {sum(repre)}
2 - website     {sum(web)}
3 - App movel android   {sum(android)}   
4 - App movel iphone     {sum(iphone)}''')
print('=-'*60)