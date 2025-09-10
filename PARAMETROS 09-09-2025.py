def sumar():
    print(5+10)
sumar()



def sumar(numero1, numero2):
    print(numero1+numero2)
sumar(10, 15)# 25


def sumar(numero1, numero2=20):
    print(numero1+numero2)
sumar(10, 15) # 25
sumar(10) # 30


def sumar(numero1,numero2=20): 
    print(numero1) 
    print(numero2) 
    print(numero1 + numero2) 
sumar(numero2=10, numero1=15)#15, 10 25 
#sumar(10) #10, 20, 30


def sumar(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
     #resultado=resultado+numer 
    print(resultado)
sumar([4,5]) # 9
sumar([2,3,1])# 6
