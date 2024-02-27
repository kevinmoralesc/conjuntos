# AUTOR : Kevin Morales y Alejandro Brito
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib_venn import venn3

# titulo de la interfaz
root = tk.Tk()
root.title("Diagrama de Venn")

# Crear etiquetas y campos de entrada para los conjuntos
labelConjunto1 = tk.Label(root, text="Conjunto 1:")
labelConjunto1.pack()
entryConjunto1 = tk.Entry(root)
entryConjunto1.pack()

labelConjunto2 = tk.Label(root, text="Conjunto 2:")
labelConjunto2.pack()
entryConjunto2 = tk.Entry(root)
entryConjunto2.pack()

labelConjunto3 = tk.Label(root, text="Conjunto 3:")
labelConjunto3.pack()
entryConjunto3 = tk.Entry(root)
entryConjunto3.pack()


#---------------------------------------------------OPERACIONES-----------------------------------------------------

#Este metodo sirve para convertir los datos ingresados por el usuario a un conjunto de datos 
def convertirConjuntos(entryConjunto):
    conjunto = set(entryConjunto.get().split())

    return conjunto

#Este metodo sirve para unir dos conjuntos y retorna un conjunto con todos los elementos, este es para 3 conjuntos
def unionConjuntos(entryConjunto1,entryConjunto2,entryConjunto3):
   conjunto1 = set([])
   conjunto2 = set([])
   conjunto3 = set([])
   conjunto1.update(convertirConjuntos(entryConjunto1))
   conjunto2.update(convertirConjuntos(entryConjunto2))
   conjunto3.update(convertirConjuntos(entryConjunto3))
   for i in conjunto1:
     conjunto3.add(i)
   for j in conjunto2:
      conjunto3.add(j)
   return conjunto3
   
#Este metodo sirve para unir dos conjuntos y retorna un conjunto con todos los elementos, este es para 2 conjuntos   
def unionConjuntosAux(entryConjunto1,entryConjunto2):
   conjunto1 = set([])
   conjunto2 = set([])
   conjunto1.update(convertirConjuntos(entryConjunto1))
   conjunto2.update(convertirConjuntos(entryConjunto2))
   for i in conjunto1:
     conjunto2.add(i)
        
   return conjunto2

#Este metodo sirve para encontrar los elementos comunes entre los 3 conjuntos 
def interseccionConjuntos(entryConjunto1,entryConjunto2,entryConjunto3):
   conjunto1 = set([])
   conjunto2 = set([])
   conjunto3 = set([])
   conjunto1.update(convertirConjuntos(entryConjunto1))
   conjunto2.update(convertirConjuntos(entryConjunto2))
   conjunto3.update(convertirConjuntos(entryConjunto3))
   interseccion = set([])
   interseccionAux = set([])
   for i in conjunto1:
     for j in conjunto2:
        if i == j:
           interseccionAux.add(i)

   for k in conjunto3:
      for l in interseccionAux:
             if l == k:
                interseccion.add(l)

   if cardinalidadConjuntoAux(interseccion) > 0:
       return interseccion

   return set([""])

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
def diferenciaConjuntos(entryConjunto1,entryConjunto2):
    conjunto1  = set([])
    conjunto2  = set([])
    diferencia = set([])
    conjunto1.update(convertirConjuntos(entryConjunto1))
    conjunto2.update(convertirConjuntos(entryConjunto2))
    diferencia.update(conjunto1)
    for i in conjunto1:
       for j in conjunto2:
         if i == j:
            diferencia.remove(i)
         
    return diferencia 

#Este metodo sirve para eliminar los elemetos del conjunto 2 en el conjunto 1 este a diferencia del metodo
# diferenciaConjuntos recibe conjuntos y no datos de la interfaz
def diferenciaConjuntosAux(conjunto1,conjunto2):
    diferencia = set([])
    diferencia.update(conjunto1)
    
    for i in conjunto1:
         for j in conjunto2:
            if i == j:
              diferencia.remove(i)
 
    return diferencia 

#Este metodo sirve para encontrar los todos los elemtos que no oertenecen a el conjunto entrante por parametro
def complementoConjuntos(entryConjunto):
    aux = True
    conjunto1 = set([])
    conjunto2  = set([])
    conjunto1.update(convertirConjuntos(entryConjunto))
    conjunto2.update(convertirConjuntos(entryConjunto2))
    complemento = set([])
    for i in conjunto2:
       aux = True
       for j in conjunto1:
          if i == j:
             aux = False
         
       if(aux==True):
          complemento.add(i)
          aux = False
    return complemento 

#Este metodo cuenta el numero de elementos que componen el conjunto
def cardinalidadConjunto(entryConjunto):
    count = 0
    conjunto = set([])
    conjunto.update(convertirConjuntos(entryConjunto))
    for i in conjunto:
        count += 1
    return count

#Este metodo cuenta el numero de elementos que componen el conjunto, es lo mismo que el metodo
#cardinalidadConjunto pero recibe un conjunto y no una entrada de edatos
def cardinalidadConjuntoAux(conjunto):
    count = 0
    for i in conjunto:
        count += 1
    return count
#Este metodo cuenta el numero de elementos que componen el conjunto, es lo mismo que el metodo
#cardinalidadConjunto pero recibe un conjunto y no una entrada de datos, pero en este el contador
#inicia en 1 porque asi se necesitaba en la interfaz
def contadorElementos(conjunto):
    count = 1
    for i in conjunto:
        count += 1
    return count

#En este metodo se retorna True o False dependiendo si el conjunto 1 es subconjunto del conjunto 2
def subconjunto(entryConjunto1,entryConjunto2):
    conjunto1 = set([])
    conjunto2 = set([])
    conjunto1.update(convertirConjuntos(entryConjunto1))
    conjunto2.update(convertirConjuntos(entryConjunto2))
    aux = True
    if(cardinalidadConjunto(entryConjunto2)>=cardinalidadConjunto(entryConjunto1)):
        for i in conjunto1:
            if(aux == True ):
                for j in conjunto2:
                      if i == j:
                         aux = True
                         break
                      else:
                         aux = False
            else:
                return aux
    else:
         return False      
    return aux

#En este metodo se determina si dos conjuntos no tienen elementos en comun
def disjuntos(entryConjunto1,entryConjunto2):
   conjunto1 = set([])
   conjunto2 = set([])
   interseccion = set([])
   conjunto1.update(convertirConjuntos(entryConjunto1))
   conjunto2.update(convertirConjuntos(entryConjunto2))
   interseccion.update(interseccionConjuntos(entryConjunto1,entryConjunto2))
   count = 0
   count = cardinalidadConjuntoAux(interseccion)
   if count > 0:
      return False
   return True  


#En este metodo se determina los elemtos unicos que tiene un conjunto respecto a los otros dos, esto
#porque la interfaz nos lo pide
def elementosUnicos (conjunto1,conjunto2,conjunto3,interseccion):
   elementosUnicos = set([])
   elementosUnicos1 = set([])
   elementosUnicos2 = set([])
   elementosUnicos.update(diferenciaConjuntosAux(conjunto1,conjunto2))
   elementosUnicos1.update(diferenciaConjuntosAux(elementosUnicos,conjunto3))
   elementosUnicos2.update(diferenciaConjuntosAux(elementosUnicos1,interseccion))
   return elementosUnicos2
   

#Metodo para generar el diagarama de venn
def generate_venn():
    conjunto1 = convertirConjuntos(entryConjunto1)
    conjunto2 = convertirConjuntos(entryConjunto2)
    conjunto3 = convertirConjuntos(entryConjunto3)

    #if len(conjunto1) == 0 or len(conjunto2) == 0 or len(conjunto3) == 0:
     #   return

    # Calcular intersecciones y elementos únicos
    intersection = interseccionConjuntos(entryConjunto1,entryConjunto2,entryConjunto3)
    soloConjunto1 = elementosUnicos(conjunto1, conjunto2,conjunto3,intersection)
    soloConjunto2 = elementosUnicos(conjunto2, conjunto1,conjunto3,intersection)
    soloConjunto3 = elementosUnicos(conjunto3, conjunto1,conjunto2,intersection)
    soloConj1Conj2 = diferenciaConjuntosAux(interseccionConjuntosAux(entryConjunto1,entryConjunto2),intersection)
    soloConj1Conj3 = diferenciaConjuntosAux(interseccionConjuntosAux(entryConjunto1,entryConjunto3),intersection)
    soloConj2Conj3 = diferenciaConjuntosAux(interseccionConjuntosAux(entryConjunto2,entryConjunto3),intersection)
    figure = Figure(figsize=(12, 12))
    ax = figure.add_subplot(111)
    
    
    # Dibujar el diagrama de Venn
    venn_diagram = venn3(subsets=(contadorElementos(soloConjunto1), contadorElementos(soloConjunto2), contadorElementos(intersection),
                                  contadorElementos(soloConjunto3), contadorElementos(diferenciaConjuntosAux(unionConjuntosAux(entryConjunto1,entryConjunto2),conjunto3)),
                                  contadorElementos(diferenciaConjuntosAux(unionConjuntosAux(entryConjunto1,entryConjunto3),conjunto2)), 
                                  contadorElementos(diferenciaConjuntosAux(unionConjuntosAux(entryConjunto2,entryConjunto3),conjunto1)),
                                  contadorElementos(intersection)), ax=ax, set_labels=('Conjunto 1', 'Conjunto 2', 'Conjunto 3'))


    # Mostrar los elementos únicos y los elementos comunes en el diagrama de Venn
    venn_diagram.get_label_by_id('100').set_text('\n'.join(soloConjunto1))
    venn_diagram.get_label_by_id('010').set_text('\n'.join(soloConjunto2))
    venn_diagram.get_label_by_id('001').set_text('\n'.join(soloConjunto3))
    venn_diagram.get_label_by_id('110').set_text('\n'.join(soloConj1Conj2))
    venn_diagram.get_label_by_id('101').set_text('\n'.join(soloConj1Conj3))
    venn_diagram.get_label_by_id('011').set_text('\n'.join(soloConj2Conj3))
    venn_diagram.get_label_by_id('111').set_text('\n'.join(intersection))

    # Mostrar el diagrama en la ventana
    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

button = tk.Button(root, text="Generar Diagrama de Venn", command=generate_venn)
button.pack()

# Aumentar el tamaño de la ventana a 700x500 píxeles
root.geometry("700x500")

# Ejecutar el bucle principal
root.mainloop()