def safe_remove(list,i):
   return ('safe_remove invocado index:',list[i])

lista= [1,2,3,4,5]
chamada = lambda l,i,x : l == None and 'Lista vazia' or i > len(l)-1 and 'Index invalido' or x(l,i)

print()
print(chamada(lista,6,safe_remove(list, i)))
print(chamada(None,1))