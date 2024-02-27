#AUTOR Kevin Morales, ALejandro Brito
import tkinter as tk

#Este metodo sirve para convertir los datos ingresados por el usuario a un conjunto de datos 
def convertirConjuntos(entryConjunto):
    conjunto = set(entryConjunto.get().split())

    return conjunto

#Este metodo sirve para unir dos conjuntos y retorna un conjunto con todos los elementos, este es para 2 conjuntos   
def unionConjunto():
    conjunto1 = set([])
    conjunto2 = set([])
    conjunto1.update(convertirConjuntos(entry1))
    conjunto2.update(convertirConjuntos(entry2))
    for i in conjunto1:
      conjunto2.add(i)
    result_label.config(text=f"Unión: {conjunto2}")

#Este metodo sirve para encontrar los elementos comunes entre los 2 conjuntos
def interseccionConjuntos():
    conjunto1 = set([])
    conjunto2 = set([])
    conjunto1.update(convertirConjuntos(entry1))
    conjunto2.update(convertirConjuntos(entry2))
    interseccion = set([])
    for i in conjunto1:
      for j in conjunto2:
         if i == j:
           interseccion.add(i)

    result_label.config(text=f"Intersección: {interseccion}")

#Este metodo sirve para encontrar los elementos comunes entre los 2 conjuntos
def interseccionConjuntosAux(entryConjunto1,entryConjunto2):
   conjunto1 = set([])
   conjunto2 = set([])
   conjunto1.update(convertirConjuntos(entryConjunto1))
   conjunto2.update(convertirConjuntos(entryConjunto2))
   interseccion = set([])
   for i in conjunto1:
     for j in conjunto2:
        if i == j:
           interseccion.add(i)
         
   return interseccion 

#Este metodo sirve para eliminar los elemetos del conjunto 2 en el conjunto 1
def diferenciaConjuntos():
    conjunto1  = set([])
    conjunto2  = set([])
    diferencia = set([])
    conjunto1.update(convertirConjuntos(entry1))
    conjunto2.update(convertirConjuntos(entry2))
    diferencia.update(conjunto1)
    for i in conjunto1:
       for j in conjunto2:
         if i == j:
            diferencia.remove(i)
    result_label.config(text=f"Diferencia (Conjunto 1 - Conjunto 2): {diferencia}")

#Este metodo sirve para encontrar los todos los elemtos que no oertenecen a el conjunto entrante por parametro
def complementoConjunto():
    aux = True
    conjunto1 = set([])
    conjunto2  = set([])
    conjunto1.update(convertirConjuntos(entry1))
    conjunto2.update(convertirConjuntos(entry2))
    complemento = set([])
    for i in conjunto2:
       aux = True
       for j in conjunto1:
          if i == j:
             aux = False
         
       if(aux==True):
          complemento.add(i)
          aux = False
    result_label.config(text=f"Complemento de conjunto 1 : {complemento}")

#Posible combinacion de todos los elementos de un conjunto con otro
def combinacion():
    conjunto1 = set([])
    conjunto2 = set([])
    combinacion = []
    conjunto1.update(convertirConjuntos(entry1))
    conjunto2.update(convertirConjuntos(entry2))
    for x in conjunto1:
        for y in conjunto2:
          if(x != y):
            combinacion.append((x, y))
    result_label.config(text=f"Combinación entre los elementos de los conjuntos: {combinacion}")

#En este metodo se retorna True o False dependiendo si el conjunto 1 es subconjunto del conjunto 2
def subconjunto():
    conjunto1 = set([])
    conjunto2 = set([])
    conjunto1.update(convertirConjuntos(entry1))
    conjunto2.update(convertirConjuntos(entry2))
    aux = True
    if(cardinalidadConjunto(entry2)>=cardinalidadConjunto(entry1)):
        for i in conjunto1:
            if(aux == True ):
                for j in conjunto2:
                      if i == j:
                         aux = True
                         break
                      else:
                         aux = False
            else:
                 aux
    else:
         aux = False      
    result_label.config(text=f"conjunto 1 es subconjunto de conjunto 2:" + str(aux))

#Este metodo cuenta el numero de elementos que componen el conjunto
def cardinalidadConjunto(entryConjunto):
    count = 0
    conjunto = set([])
    conjunto.update(convertirConjuntos(entryConjunto))
    for i in conjunto:
        count += 1
    return count

#Este metodo cuenta el numero de elementos que componen el conjunto sin parametro
def cardinalidad():
    count = 0
    conjunto = set([])
    conjunto.update(convertirConjuntos(entry1))
    for i in conjunto:
        count += 1
    result_label.config(text=f"Cardinalidad conjunto 1: "+ str(count) )

#Este metodo cuenta el numero de elementos que componen el conjunto con parametro y sin result_label
def cardinalidadConjuntoAux(conjunto):
    count = 0
    for i in conjunto:
        count += 1
    return count

#En este metodo se determina si dos conjuntos no tienen elementos en comun
def disjuntos():
    aux = True
    interseccion = set([])
    interseccion.update(interseccionConjuntosAux(entry1,entry2))
    count = 0
    count = cardinalidadConjuntoAux(interseccion)
    if count > 0:
      aux = False
    result_label.config(text=f"Cardinalidad conjunto 1: "+ str(aux) )


# Crear la ventana principal
root = tk.Tk()
root.title("Operaciones de conjuntos")

# Crear etiquetas y campos de entrada para los conjuntos
label1 = tk.Label(root, text="Conjunto 1:")
label1.grid(row=0, column=4)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=5)

label2 = tk.Label(root, text="Conjunto 2:")
label2.grid(row=1, column=4)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=5)

espacio = tk.Label(root, text="")
espacio.grid(row=3, column=5)

# Botones para realizar operaciones
union_button = tk.Button(root, text="Unión", command=unionConjunto)
union_button.grid(row=4, column=3)

intersection_button = tk.Button(root, text="Intersección", command=interseccionConjuntos)
intersection_button.grid(row=4, column=4)

difference_button = tk.Button(root, text="Diferencia", command=diferenciaConjuntos)
difference_button.grid(row=4, column=5)

complement_button = tk.Button(root, text="Complemento", command=complementoConjunto)
complement_button.grid(row=4, column=6)

combination_button = tk.Button(root, text="Combinación", command=combinacion)
combination_button.grid(row=5, column=3)

complement_button = tk.Button(root, text="Cardinalidad", command=cardinalidad)
complement_button.grid(row=5, column=4)

complement_button = tk.Button(root, text="Subconjunto", command=subconjunto)
complement_button.grid(row=5, column=5)

complement_button = tk.Button(root, text="Disjuntos", command=disjuntos)
complement_button.grid(row=5, column=6)

espacio = tk.Label(root, text="")
espacio.grid(row=6, column=5)
# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="Resultado:")
result_label.grid(row=7, column=1)
result_label.grid(row=7, column=2, columnspan=2)

# Aumentar el tamaño de la ventana a 500x300 píxeles
root.geometry("500x300")

# Ejecutar el bucle principal
root.mainloop()