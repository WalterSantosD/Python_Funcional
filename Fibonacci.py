#soma = lambda x : x > 0 and x**2 + soma(x-1) or 0 

#soma = lambda x : x <= x and or  (x-(x-1))**2 + soma(1+(x-(x-1))) or 0 

#print(soma(6))

#filtro = lambda l : [x for x in l if "e" in x]
#nomes = ["walter","lucas","pedro","leon"]
#print (filtro(nomes))

#for x in nomes:
#    print(x)


codificar = lambda a : chr(ord(a)+1) 
descodificar = lambda a : chr(ord(a)-1) 
#print(resultado)

lista = ["luan",123]
lista02 = ["mvbo",234]
Cifra_codificadora = lambda l,i :i=="cd" and [ ''.join(list(map(codificar,str(x) )))  for x in l ] or i =="dc" and [ ''.join(list(map(descodificar,str(x) )))  for x in l ]

print(Cifra_codificadora(lista,"cd"))
print(Cifra_codificadora(lista02,"dc"))
