# %%
import sympy as sp

# %%
'''Menú 1 
    Muestra el menú y pide al usuario teclear 1 o 2 
    Devuelve 1 para resolver por metodo de newton 
    Devuelve 2 para resolver por metodo de la secante
'''
def menu1():
 
    print("ingrese 1 para metodo de Newton")
    print("ingrese 2 para metodo de la secante \n")

    try:
        userInput = int(input())
    except ValueError:
        print("ERROR: Debes ingresar un número") 
        menu1()

    if userInput == 1 or userInput == 2:
        return userInput
    else:
        print("ERROR: Debes ingresar sólo 1 ó 2")
        menu1() 

# %%
'''Menu Newton 
    Pide al usuario elegir entre ejemplos preconfigurados 
    o ingresar los parametros(funcion, aproximacion, iteraciones)
'''
def menuNewton():
    print("ingrese 1 para utilizar un ejemplo ")
    print("ingrese 2 para dar ingresar uno propio \n")

    try:
        userInput = int(input())
    except ValueError:
        print("ERROR: Debes ingresar un número") 
        menu1()

    if userInput == 1 or userInput == 2:
        return userInput
    else:
        print("ERROR: Debes ingresar sólo 1 ó 2")
        menu1() 


# %%
'''Menu Secante
    Pide al usuario elegir entre ejemplos preconfigurados 
    o ingresar los parametros (funcion, aproximacion 1, aproximación 2, iteraciones)
'''
def menuSecante():
    print("ingrese 1 para utilizar un ejemplo ")
    print("ingrese 2 para dar ingresar uno propio \n")

    try:
        userInput = int(input())
    except ValueError:
        print("ERROR: Debes ingresar un número") 
        menu1()

    if userInput == 1 or userInput == 2:
        return userInput
    else:
        print("ERROR: Debes ingresar sólo 1 ó 2")
        menu1() 


# %%
'''Menu Ejemplos Newton
    Muestra ejemplos y te permite elegir uno 
'''
def menuEjemplosNewton():
    Ejemplos = ['(x**2)-2,2,50','x**2,3,30']
    for i in range(len(Ejemplos)):
        print(f"Ingrese {i} para usar el Ejemplo {Ejemplos[i]} ")   
    
    try:
        userInput = int(input())
    except ValueError:
        print("ERROR: Debes ingresar un número") 
        menu1()
 
    return Ejemplos[userInput] 

# %%
'''Menu Ejemplos Secante 
    Muestra ejemplos y te permite elegir uno 
'''
def menuEjemplosSecante():
    Ejemplos = ['(x**2)-2,1,2,50','x**2,3,4,30']
    for i in range(len(Ejemplos)):
        print(f"Ingrese {i} para usar el Ejemplo {Ejemplos[i]} ")   
    
    try:
        userInput = int(input())
    except ValueError:
        print("ERROR: Debes ingresar un número") 
        menu1()
 
    return Ejemplos[userInput] 

# %%
##aquí se podría implementar manejo de excepciones
'''Menu Ejemplo propio Newton 
    Te dice los parametros que debes ingresar para el metodo Newton y devuelve lo que ingreses en forma de string
'''
def menuEjemploPropioNewton():
     srtUserInput = input("da la funcion, aproximacion,  y numero de iteraciones separadas por comas \n")

     return srtUserInput

# %%
##aquí se podría implementar manejo de excepciones
'''Menu Ejemplo propio Secante
    Te dice los parametros que debes ingresar para el metodo Secante y devuelve lo que ingreses en forma de string
'''
def menuEjemploPropioSecante():
     srtUserInput = input("da la funcion, aproximacion 1 , aproximacion 2, y numero de iteraciones separado por comas \n")

     return srtUserInput

# %%
'''Método de Newton
    Recibe un string que es la función, una aproximacion que es un entero, un numero de iteraciones que es un entero
 '''
def metodoNewton(funcion, aproximacion, iteraciones):
    x = sp.symbols('x')

    f= sp.sympify(funcion)
    fprima = sp.diff(f,x)

    x_n = int(aproximacion)
    x_nmas1 = 0 
    

    ## paso iterativo
    for i in range (int(iteraciones)):
        f_n = f.subs(x,x_n)
        fprima_n = fprima.subs(x,x_n)
        
        x_nmas1 = x_n -(f_n.evalf(100) / fprima_n.evalf(100))

        print(f"Iteracion: {i+1}  x_{i+1} = {x_nmas1}")

        x_n = x_nmas1

# %%
'''Método de la Secante
    Recibe un string que es la función, una aproximacion 1 que es un entero,
    una aproximación 2 que es un entero,  y  un numero de iteraciones que es un entero
 '''
def metodoSecante(funcion, aproximacion_x_cero, aproximacion_x_uno, iteraciones):
    x = sp.symbols('x')

    f = sp.sympify(funcion) 

    x_nmenos1 = int(aproximacion_x_cero)
    x_n = int(aproximacion_x_uno)
    x_nmas1 = 0

    for i in range(int(iteraciones)):
         f_n = f.subs(x,x_n)
         f_nmenos1 = f.subs(x,x_nmenos1)

         x_nmas1 = x_n - (((x_n - x_nmenos1)* f_n.evalf(100)) / (f_n.evalf(100) - f_nmenos1.evalf(100) ))

         print(f"Iteracion: {i+1}  x_{i+2} = {x_nmas1}")
         
         x_nmenos1 = x_n
         x_n = x_nmas1


    

# %%
'''Logica del programa ( Main )
'''
intInputMenu1 = menu1()
if intInputMenu1 == 1:
    intInputMenuNewton = menuNewton()
    if intInputMenuNewton == 1:
        strInputMenuEjemplosNewton = menuEjemplosNewton()
        funcion, aproximacion, iteraciones = strInputMenuEjemplosNewton.split(",")
        metodoNewton(funcion, aproximacion,iteraciones)
    elif intInputMenuNewton == 2:
        strInputMenuEjemploPropioNewton = menuEjemploPropioNewton()
        funcion, aproximacion, iteraciones = strInputMenuEjemploPropioNewton.split(",")
        metodoNewton(funcion, aproximacion, iteraciones)

elif intInputMenu1 == 2:
    intInputMenuSecante = menuSecante()
    if intInputMenuSecante == 1 :
        strInputMenuEjemplosSecante = menuEjemplosSecante()
        funcion, aproximacion_1, aproximacion_2, iteraciones = strInputMenuEjemplosSecante.split(',')
        metodoSecante(funcion, aproximacion_1, aproximacion_2, iteraciones)
    elif intInputMenuSecante == 2 :
        strInputMenuEjemploPropioSecante = menuEjemploPropioSecante()
        funcion, aproximacion_1, aproximacion_2, iteraciones = strInputMenuEjemploPropioSecante.split(',')
        metodoSecante(funcion, aproximacion_1, aproximacion_2, iteraciones)



