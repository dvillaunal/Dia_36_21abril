# Programación Orientada a Objetos (OOP) en Python:

Reto de Hoy en:

> Programación Orientada a Objetos. Clases, Objetos(instancias),  método constructor (__init__()).
> [Link de Referencia](https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/)

# Clases:

## ¿Que es una Clase?:

Una clase es vagamente como una Plantilla o modelo para crear a partir de ella ciertos Objetos. Esta plantilla es la que contiene la información; características y capacidades que tendrá el objeto que sea creado a partir de ella.

Así a su vez los objetos creados a partir de ella estarán agrupados en esa misma clase.

- __Nota:__
 Crear un objeto a partir de una clase se denomina instanciar.

## ¿Que es un Objeto?:

* Ejemplo para entender los Objetos:
 
  los objetos son como engranajes de nuestro programa; si habláramos más en términos de relojes podría decirse que estos son objetos que contienen una información especifica (tamaños; apertura de dientes; etc.) y a su vez realizan una acción determinada que resulta importante para el funcionamiento de un sistema. Faltando uno que otro engranaje nuestro reloj dejaría de funcionar.

* __Nota:__
   - No necesariamente todos deben derivar de una clase.

   - __casi todo es un objeto:__
     puesto que el concepto de la programación orientada a objetos consiste en resolver problemas grandes subdividiendo nuestro programa en otros más pequeños a cargo de objetos con determinadas características y tareas encomendadas.

## Atributos y Metodos:

Si los objetos almacenan información y realizan tareas, entonces:

+ __Los Atributos:__
 
 las características que definimos para este objeto

+ __Los metodos:__

 las tareas que son capaces de realizar.

### Ejemplo:

* Una __Clase:__ Insecto

+ El __Objeto instanciado__ (crados a partir de la clase anterior): Abeja

+ Tiene Atributos:
   - __tipo de abeja:__ Reina de la colmena
   - __Región:__ Americana (Mielera)
   - __Domesticada:__ Si

+ Tiene Metodos:
   - Agresiva
   - productora de más abejas
   - quien rige la colmena

# Sintaxis de clases:

Para Crear una clase recurrimos a la expresión ``class``
segida del nombre de la clase y entre paréntesis la clase de la cual "hereda" (una clase puede recibir atributos y metedos de otra).

> ### Nota:
Al momento de crear una clase si este parámetro entre paréntesis no se declara; la clase automáticamente heredara de ``Object`` (que es una clase predefinida osea existente en el propio lenguaje por defecto.).

Después de ``:`` definimos el __metodo constructor__ de la clase seguido tambien del paréntesis para establecer parámetros...teniendo así dentro de la clase otro bloque de código.

~~~
# Declaramos la clase nuestra que heredera Object:
class NombreDeLaClase(Object):
   # constructor de la case:
   def __init__(self, parámetros):
     # Declaración de atributos
~~~

# El metodo constructor de las clases en python ``__init__``:

Si hablamos de métodos de una clase puede existir diferentes tipos de ellos. Pero el mas importante es el __método constructor__; el cual dicho nombre hace referencia a inicializar los atributos del objeto creado a partir  de la clase que los posea.

Por supuesto no es necesario que este método exista dentro de una clase para que la clase exista.
Pero si es necesario para indicarle al interprete de Python que cuando se Instancia un objeto a dicha clase debe asignarle los argumentos que nosotros le damos al momento de la instancia. ___(inicialización de atributos == Reto de mañana)___

+ Este metodo se esccribe ``__init__``
   > Una clase que posea este método creara el objeto con     los “argumentos” para los atributos que se pasen al      momento de la instancia.

+ El metodo ``__init__`` __NO RETORNA NINGÚN DATO, ES OPCIONAL__
   + Cuando decimos que no retorna ningún valor significa que a diferencia de otros metodos este no puede retornar
   valores luego de ejecutado.

+ __Este metodo:__
   es llamado automáticamente al instanciar un objeto a la clase que tenga el constructor por lo que su uso es muy común y practico.
  
> ### Nota:
  el método constructor nos permitirá asignar atributos cada vez que creemos un objeto a partir de esa clase haciéndolo obligatorio. Y además nos permitirá llamar métodos de la clase sin instanciar; etc...

## Sintaxis:

>### Ejemplo:

>Debo crear un 100 ó 50 ó n objetos apartir de la misma clase todos esos métodos tendran el mismo atributo "Color"

>Creamos la clase producto y el método constructor donde definimos que el atributo color sera igual al parámetro color que pasemos en el indice “0” (cero; primer parámetro).

>Class Producto():
 Constructor __init__(self, color) :
   self.color = color # <= Atributo

>Instanciamos objetos:
  - Objeto1 = Producto(“AZUL”)
  - Objeto2 = Producto(“ROJO”)
  - Objeto3 = Producto(“NEGRO”)


# self:
+ Los métodos de ``class`` deben tener un primer parámetro    extra en la definición del método.
  No damos un valor para este parámetro cuando llamamos al método, Python lo proporciona.

+ Si tenemos un método que no toma argumentos, entonces todavía tenemos que tener un argumento.

> Cuando llamamos a un método de este objeto como:
``miclass.method(arg1, arg2)``, esto es automáticamente convertido por Python en:
``MiClass.method(myobject, arg1, arg2)``


