# %%
import sympy as sp

# %%
#funcion input que recibe los valores de x_i , f(x_i)
def readInput(i):
    userInput = input(f"Ingresa x_{i}")
    x_i = userInput
    userInput2 = input(f"Ingresa f(x_{i})")
    fx_i = userInput2

    return x_i, fx_i    

# %%
def interpolacion(xvector):

    x = sp.symbols('x')
    lvector =[]
    
    for i in range(len(xvector)):
        l_i = 1
        for j in range(len(xvector)):
            if j != i:
                l_i *= (x-xvector[j]) / (xvector[i]-xvector[j]) 
        lvector.append(l_i)    
    return lvector 

# %%
def polinomio(lvector, fxvector):
    P_x = 0 
    for i in range(len(fxvector)):
        P_x += lvector[i] * fxvector[i]
        
    return P_x

# %%
#main
xvector =[]
fxvector = []

for i in range(100000):
    strx_i, strfx_i = readInput(i+1)
    if (strx_i or strfx_i) =="e":
        break    
    xvector.append(strx_i)
    fxvector.append(strfx_i)

#parsing xvector a sympy
sympyxvector = [] 
for strx_i in xvector:
    x_i = sp.sympify(strx_i)
    sympyxvector.append(x_i)

sympyfxvector = [] 
for strfx_i in fxvector:
    fx_i = sp.sympify(strfx_i)
    sympyfxvector.append(fx_i)


lvector = interpolacion(sympyxvector)
P_x = polinomio(lvector, sympyfxvector)

print(f"Polinomio de Interpolacion: {P_x}")


