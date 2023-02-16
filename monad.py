def safe_remove(list,i):
   return ('safe_remove invocado index:',list[i])

lista= [1,2,3,4,5]
chamada = lambda l,i : l == None and 'Lista vazia' or i > len(l)-1 and 'Index invalido' or safe_remove

print()
print(chamada(lista,6))
print(chamada(None,1))