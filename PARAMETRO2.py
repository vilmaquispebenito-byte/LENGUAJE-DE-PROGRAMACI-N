def sumar(**numeros): 
    print(numeros) 
    print(numeros['numero1'] + numeros['numero2']) 
sumar(numero1=10, numero2=20) # 30 
sumar(numero1=4, numero2=11) # 15 

def multiplica_por_5(numero): 
    print(f'{numero} * 5 = {numero * 5}') 
print('Comienzo del programa')     
multiplica_por_5(7) 
print('Siguiente') 
multiplica_por_5(10) 
print('Fin') 

def cuadrado_de_par(numero): 
     if not numero % 2 == 0: 
         return 
     else: 
         print(numero ** 2)   
cuadrado_de_par(8) 
cuadrado_de_par(3)

def es_par(numero): 
     if numero % 2 == 0: 
         return True 
     else:
        return False      
print(es_par(2)) 
print(es_par(5)) 

def cuadrado_y_cubo(numero): 
     return numero ** 2, numero ** 3 
cuad, cubo = cuadrado_y_cubo(4) 
print(cuad) 
print(cubo)

def tabla_del(numero): 
     resultados = [] 
     for i in range(11): 
         resultados.append(numero * i) 
     return resultados 
res = tabla_del(3) 
print(res)

def saludo(nombre): 
     print(f'Hola {nombre}') 
print(saludo('Juan')) 
#saludo('Juan')

def jose(): 
  num=int(input("que producto compraste 1)leche 2)pan 3)alcohol 4)otros; ")) 
  total=int(input("cuanto costo S/.? : ")) 
  if num==1: 
    im=10 
  elif num==2: 
    im=20 
  elif num==3: 
    im=30 
  else: 
    im=50 
  impu=(total*im/100) 
  print('impuesto de ese producto es S/.: ',impu) 
#  print(impu) 
  return impu 
jose() 
print("Programa terminado")

def calcula_media(x, y): 
  resultado = (x + y) / 2 
  return resultado 
media = calcula_media(y=5, x=3) 
#media = calcula_media(3, 5) 
print("La media es:") 
print(media) 
print("Programa terminado")

def suma(x,y): 
    return x+y 
def resta(x,y): 
    return x-y 
def multiplicacion(x,y): 
    return x*y 
def division(x,y): 
    return x/y 
x = 8 
y = 4 
print('%d + %d = %d' % (x, y, suma(x, y))) 
print('%d - %d = %d' % (x, y, resta(x, y))) 
print('%d * %d = %d' % (x, y, multiplicacion(x, y))) 
print('%d / %d = %d' % (x, y, division(x, y))) 

