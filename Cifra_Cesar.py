#clientes = {"557.161.950-32":["Russell Wolfe",24,123],"793.199.640-2":["Rebecca Martinez",30,321]}
#print(clientes["557.161.950-32"])

deslocamento = 1

codificar_senha = lambda senha :  chr(ord(senha)+deslocamento) # type(senha)==int and senha+deslocamento or type(senha) == str and  

cadastrar_cliente = lambda cpf,nome,idade,senha : {cpf:[nome,idade,  "".join(list(map(codificar_senha,str(senha))))  ]}# codificar_senha(senha)

lista_clientes = [ 
cadastrar_cliente("557.161.950-32","Russell Wolfe",24,123),
cadastrar_cliente("793.199.640-2","Rebecca Martinez",30,'abc') ]
print(lista_clientes)





