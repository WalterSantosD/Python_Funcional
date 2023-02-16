lista = ['ma','b']

nova_lista = list(filter(lambda x : x[0]=='a',lista))
print(nova_lista)

dic = {'walter':[70,175]}
print(type(dic))

imc = lambda peso,altura : peso/pow(altura,2)
cadastrar_pessoa = lambda nome,peso,altura : {nome : imc(peso,altura)}


pessoa = cadastrar_pessoa('walter',70,1.75)
pessoa02 = cadastrar_pessoa('pedro',50,1.50)
print(pessoa)
print(pessoa02)