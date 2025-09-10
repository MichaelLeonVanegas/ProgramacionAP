#-------------------LISTAS-------------------#

mi_lista = ["Amarillo","Azul","Morado","Rojo","Violeta","Marron" ] #Crea una lista
print(mi_lista) #Imprime lista
print(type(mi_lista)) #Imprime que tipo es la lista
print(mi_lista[5]) #Imprime el elemento 5 de mi lista

print()

print("Tamaño de lista: ", len(mi_lista)) # Imprime el tamaño de la lista
print(mi_lista[1:4]) #Imprime una parte de inicio a fin definidos
print(mi_lista[:3]) #Imprime una parte de fin definido

print()

mi_lista.append("Cian") #Agrega un nuevo elemento al final
print(mi_lista) #Imprime la nueva lista

print()

mi_lista.insert(4, "Dorado") #Agrega un nuevo elemento en la posicion 4
print(mi_lista) #Imprime la nueva lista

print()

mi_lista.extend(["Purpura","Naranja","Gris"]) #Concatena otra lista a la lista principal
print(mi_lista) #Imprime la nueva lista

print()

print(mi_lista.index("Gris")) #Imprime la posicion del elemento en la lista

print()

mi_lista.remove("Amarillo") #Elimina el elemento de la lista
print(mi_lista) #Imprime la nueva lista

print()

mi_lista.insert(0,"Amarillo") #Ingresa un elemento en la posicion 0
print(mi_lista) #Imprime la nueva lista

print()

print(mi_lista.pop()) #Imprime el ultimo elemento y lo elimina
size = len(mi_lista) #Crea la variable Size 
print("Size: ",size) #Imprime la variable Size

print()

mi_lista_2 = mi_lista*2 #Dupliuca los elementos de la lista y lo agraga a una variable
print("Mi_lista_2: ",mi_lista_2) #Imprime la variable

print()

print("sort:") #Imprime un string
print()
mi_lista_sort = mi_lista.sort() #Ordena la lista de menor a mayor y agrega la funcion a una variable
print(mi_lista_sort) #Imprime None

print()

mi_lista_numerica = [2, 4, 7, 3, 20, 11, 25, 37, 8] #Crea lista con elementos enteros
print("mi_lista_numerica: ") #Imprime un String
mi_lista_numerica.sort() #Ordena la lista de menor a mayor
print(mi_lista_numerica) #Imprime la nueva lista

print()

mi_lista_numerica.sort(reverse= True) #Ordena la lista de mayor a menor
print("De mayor a menor: ",mi_lista_numerica) #Imprime la nueva lista

print("-----------------------------------------------------------------------------")

#-------------------TUPLAS-------------------#

mi_tupla = tuple(mi_lista) #Convierte una lista a una tupla y lo agrega a una variable
print()
print()
print("mi_tupla: ",mi_tupla) #Imprime la tupla

print()

print(mi_tupla[5]) #Imprime el elemento en la posicion 5 en la tupla
print(mi_tupla[7]) #Imprime el elemento en la pisicion 7 en la tupla

print()

print("Rojo" in mi_tupla) #Revisa si existe el elemento solicitado en la tupla y imprime False/True si esta o no
print(mi_tupla.count("Rojo")) #Imprime la cantidad de elementos iguales al solicitado

print()

mi_tupla_unitaria = ("Patata") #Crea una nueva tupla de un solo elemento
print(mi_tupla_unitaria) #Imprime la tupla unitaria

print()

mi_tupla = "Patata", "Pollo", 2020, 500 #Crea una tupla sin usar parentesis
print(mi_tupla) #Imprime la nueva tupla

print()

producto, sabor, año, peso = mi_tupla #Desempaqueta la tupla y le agrega a cada variable el elemento de la tupla
print(producto) #imprime la variable 1
print(sabor) #Imprime la variable 2
print(año) #Imprime la variable 3
print(peso) #Imprime la variable 4
print("Producto: ",producto,", Sabor: ",sabor,", Año: ",año," y Peso: ",peso) #Imprime las variables con su respectivo nombre

print()

mi_lista2 = list(mi_tupla) #Convierte la tupla en una lista
print(mi_lista2) #Imprime la nueva lista
