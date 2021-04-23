'''
Nombre: Daniel Felipe Villa

Lenguaje: Python

Tema: Programación Orientada a Objetos. Clases, Objetos(instancias), método constructor (init()).

Fuentes Consultadas:
https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/

https://www.w3schools.com/python/python_classes.asp
'''

# Clases:
print('# Clases:')
## Definimos una clase:
print('\n## Definimos una clase:')

'''
En el siguiente ejemplo,
la palabra clave class indica
que se está creando una clase
seguida del nombre de la clase (Can en este caso).
'''
print('<class Insect>')
class Insect:
  '''
   # Insect de insecto
   Esta clase es un ejemplo
   No contiene objetos
  '''
  pass

## Volvamos con class Can:

class Insect:
  '''
  # Una clase simple
  ## Atributo (Tienen...):
  La clase Insect
  contiene dos atributos:
  Alas y Son pequeños
  con el metodo imprime:
  los atributos Uno y Dos
  '''
  a1 = 'Alas'
  a2 = 'Pequeños'

  ## Un metodo:
  def met(self):
    print('Los insectos tienen ', self.a1)
    print('Los insectos son ', self.a2)

## Metodo constructor:
print('## Metodo constructor:')
## Instanciar objetos:
print('## Instanciar objetos:')

ant = Insect()

print('ant = Insect()')
print(ant)

## Acceso a los atributos de la clase y a los metodos através de objetos:
print('## Acceso a los atributos de la clase y a los metodos através de objetos:')

print(ant.a1)
ant.met()

print('\nEn el ejemplo anterior, se crea un objeto que es básicamente un insecto atribuido a una hormiga (ant). Esta clase solo tiene dos atributos de clase que nos dicen que ant tiene alas (hay hormigas con alas) y son pequeños .')

# __init__:
print('\n# __init__:')

## Definimos un class simple:

'''
esta clase lo que hacce es define un objeto llamado carrera
el cual al darle un valor imprimira
que esta estudiando
el estudiante definido en class
'''

class Estudiante:
  '''
  Esta Clase se llama Estudiante
  tiene un metodo constructor donde define
  que carrera estudia el estudiante
  por ultimo imprime "La carrera que estudio es"
  '''
  # método init o constructor:
  def __init__(self, carrera):
    self.carrera = carrera

  # Definimos un metod simple:
  def what_study(self):
    print("La carrera que estudio es: ", self.carrera)

'Aqui le damos el valor a "e", que el estudiante cursa la carrera de estadistica'
e = Estudiante('Estadística')
## Imprimimos los resultados
e.what_study()


# Clases e Instancias:
print('\n# Clases e Instancias:')
## Creamos la clase Boligrafo:
print('\n## Creamos la clase Boligrafo:')
print('\nclass Boligrafo:')

class Boligrafo:
  def __init__(self, tinta, retractil): # Definimos los atributos tinta y retractil.
    self.tinta = tinta # Definimos el atributo tinta, sera el color que contiene el boligrafo
    self.retractil = retractil # Definimos el atributo Retractil, sera True si es un lapicero, donde la mina se guarda, False en caso contrario

## Definimos a un boligrafo con:
print('\n## Definimos a un boligrafo con:')
print('\nBoligrafo1 = Boligrafo("Roja", True)')

Boligrafo1 = Boligrafo('Roja', True)

respuesta = 'Es decir el boligrafo es de tinta roja y es retractil'
print('\n',respuesta)