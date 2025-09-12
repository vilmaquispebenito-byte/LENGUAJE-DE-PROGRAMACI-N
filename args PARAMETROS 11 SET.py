def sum(x, y): 
    return x + y 
#utilizando sum como función 
print(sum(3,5)) 
print(sum(2,3))
print("="*110)

def product(a, b):
  """This function calculates the product of two numbers."""
  return a * b

# Using the product function
print(product(4, 6))
print(product(7, 2))
print("="*110)

def sum(x, y, z): 
    return x + y + z 
#utilizando sum como función 
print(sum(2,3,4)) 
print(sum(5,2,3)) 
print(sum(60,10,40))
print("="*110)


def average(w,x, y, z):
  """This function calculates the average of three numbers."""
  return (w - x + y + z) / 3

# Using the average function
print(average(8,2, 3, 4))
print(average(9,5, 2, 3))
print(average(100,60, 10, 40))
print("="*110)


 
def sum(*args): 
    valor = 0 
    for n in args: 
        valor = valor + n 
    return valor 
print(sum(10,3)) 
print(sum(1,2,3))
print("="*110)

# declarar una variable de cadena 
x = "Juan" 
# añadir una cadena dentro de una cadena 
print("Hola, %s!" % x) 
print(sum(3,2,4,1)) 
print(sum()) 
print("="*110)

def find_maximum(*args):
  """This function finds the maximum value among a variable number of arguments."""
  if not args:
    return None  # Return None if no arguments are provided
  maximum = args[0]
  for num in args:
    if num > maximum:
      maximum = num
  return maximum
print("="*110)

# Using the find_maximum function
print(find_maximum(10, 3))
print(find_maximum(1, 2, 3))
print(find_maximum(3, 2, 4, 1))
print(find_maximum())
print("="*110)

nombre = "Laura" 
edad = 22 
print("Usando %s ") 
print ("%s's tiene %s años."%(nombre,edad))
print("="*110)


nombre = "sonia" 
edad = 38 
print("Usando %s ") 
print ("%s's tiene %s años."%(nombre,edad))
print("="*110)


# declarar una variable de cadena 
var1 = "yunior!" 
var2 = "Ciudad de moquegua" 
# añadir varias cadenas dentro de una cadena 
print("Hola %s estas en %s para trabajar?." % (var1, var2))
print("="*110)

def read_list_args(*args): 
    for count, arg in enumerate(args): 
        print( '%d - %s' % (count, arg)) 
read_list_args('Ricardo', 'jarroba.com') 
read_list_args('Ricardo', 23, 'Ramon', [1, 2, 3], 'jarroba.com') 
read_list_args(10,"juan",5.5,(5,2,0), 'cetpropuno.edu.pe',0)
print("="*110)


def read_list_args_with_type(*args):
    """This function iterates through a variable number of arguments and prints each one along with its type."""
    print("Arguments and their types:")
    for count, arg in enumerate(args):
        print(f"{count} - {arg} (Type: {type(arg).__name__})")

# Using the read_list_args_with_type function
read_list_args_with_type('Ricardo', 'jarroba.com')
read_list_args_with_type('Ricardo', 23, 'Ramon', [1, 2, 3], 'jarroba.com')
read_list_args_with_type(10, "juan", 5.5, (5, 2, 0), 'cetpropuno.edu.pe', 0)
print("="*110)

def read_list_args(*args): 
    for count, arg in enumerate(args): 
        print( '%d - %s' % (count, arg)) 
read_list_args('manuel', 'jaker.com') 
read_list_args('LFREDO', 35, 'Ramon', [5, 6, 7], 'jarroba.com') 
read_list_args(10,"juan",5.5,(5,2,0), 'cetpropuno.edu.pe',0)
print("="*110)

