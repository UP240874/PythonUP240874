#ejercicio 1
print(3+4) #addition(+)
print(3-4) #subtraction (-)
print(3*4) #multiplication(*)
print(3%4) #modulus (%)
print(3/4) #division(/)
print(3**4) #exponential(+)
print(3//4) #

#ejercicio3
print("andrea")
print("irma, victor, lexcy, wanda")
print("mexico")
print("I am enjoying 30 days of python")


#ejercicio3 
print(type(10))
print(type(938))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh','Python','Finland']))
print(type("andrea"))
print(type("irma, victor, lexcy, wanda"))
print(type("mexico"))
#level 2

#level 3 
print(type({"name": "andrea"}))
#dictionary
print(type({}))
print(type())

print(integer = 10)  #num integer
print(float = 3.14)   #num float
print(complex = 2+3j)   #numcomplex


print(string = "hola mundo")
print(boolean = True)
print(list = [1,2,3, "a", True])
print(tuple = (4,5,6))
print(set = {1,2,3,3})
print(dictionary = {"nombre": "andrea", "edad": 18 })
import math
def distancia_euclidiana(x1,y1,x2,y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#puntos dados
punto1 = (2,3)
punto2 = (10, 8)
#calcurar distancia
distancia = distancia_euclidiana(punto1[0], punto1[1], punto2[0], punto2[1])
print(f"punto1: {punto1}")
print(f"punto2: {punto2}")
print(f"distancia euclidiana: {distancia:.2f}")


