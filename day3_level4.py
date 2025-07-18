#1 declare you age as integer variable
import math 
age=18
#2 declare you height
height=1.74
#3 declare a variable that stores a comple x number 
complex_number=3+4j
print("age:", age);
print("height:", height);
print("complex number:", complex_number);
print("-"*50);

#3 triangle area calculation 
base=float(input("ingresa la base: "))
height=float(input("ingresa la altura: "))
area= 0.5*base*height
print("el area del triangulo es:", area);
print("-"*50)

#4 triangle perimeter calculation
side_a=float(input("intoduce el lado a:"))
side_b=float(input("introduce el lado b:"))
side_c=float(input("introduce el lado c:"))
perimeter= side_a + side_b + side_c
print ("el perimetro del triangulo es:", perimeter)
print("-"*50)

#5 rectangle area and perimeter
length=float(input("introduce la longitud del rectangulo:"))
width=float(input("introduce el ancho del rectangulo:"))
area=length*width
perimeter=2*(length+width)
print("el area es:", area)
print("el perimetro es:", perimeter)
print("-"*50)

#6 circle area and circumference
radio = float(input("introduce el radio del circulo:"))
pi=3.14
area = pi*radio*radio 
circumference = 2*pi*radio
print("area:", area)
print("circunferencia:", circumference)
print("-"*50)

#7 calculate slope, x-intercept andy-intercepte of y=2x-2
#for y=2x-2
#slope(m)=2
#y-intercept: when x=0, y=-2
#x-intercept:whem y=0,0 =2x-2, sox=1
slope=2
y_intercept=-2
x_intercept=1
print("para la ecuacion y=2x-2:")
print("slope:", slope)
print("intercepcion y:", y_intercept)
print("intercepcion x:", x_intercept)
print("-"*50)

#8 slop and euclidean distance between tw o points
#points: (2,2) and(6,10)
x1,y1=2,2
x2,y2= 6,10
#9 slope calculation
slope = (y2-y1) / (x2-x1)
#10 euclidian distance
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"entre puntos ({x1},{y1}) and ({x2}, {y2}):")
print(f"slope: {slope}")
print("distancia euclidiana:", distance)
print("-"*50)

#11 compare slope from tasks 8 and 9
#pendiente del ejercicio 8 (y = 2x - 2)
slope_task8 =2
#12 pendiente del ejercicio 9 (puntos(2,2) y (6,10))
x1, y1 = 2,2 
x2, y2 = 6,10
slope_task9 = (y2 -y1) / (x2 - x1)
print(f"pendiente ejercicio 8: {slope_task8}")
print(f"pendiente ejercicio 9: {slope_task9}")
print(f"¿son iguales? {slope_task8 == slope_task9}")
print("-"*50);
#13 quadratic equation y=x 2 + 6x + 9
x_values = [-5, -4, -3, -2, -1, 0, 1]

for x in x_values:
    y = x**2 + 6*x + 9 
    print(f"cuando x = {x}, y = {y}")
print("y =0 cuando x = -3")

#14 string comparisons and operations 
python_len = len("python")
dragon_len = len("dragon")

print(f"Longitud de 'python': {python_len}")
print(f"Longitud de 'dragon': {dragon_len}")
print(f"¿'python' y 'dragon' tienen la misma longitud? {python_len == dragon_len}")
print("-"*50)

#15 Verifica si 'on' se encuentra en ambas 'python' and 'dragon'
print("on" in "python")
print("on" in "dragon")
dbas_have_on = "python".find("on") >= 0 and "dragon".find("on") >= 0
print(dbas_have_on)

print("-"*50)

#16 Usar 'and' en 'python' y 'dragon'
print("on" in "python" and "on" in "dragon")
print("not", not ("on" in "python" and "on" in "dragon"))
print("-"*50)
#17 'jargon' está en la oración
sentence = "The sentence is not full of jargon"
print("jargon" in sentence)
print("jargon" not in sentence)
print("-*50")

#18 Statement about 'on' in dragon and python
print("declaracion: 'No hay 'on' en dragon y python'")

print("Esta declaración es:", not ("on" in "dragon" and "on" in "python"))
print("(la declaracion es falsa porque 'python' si contiene 'on')")
print("-"*50)
#19 Convert string operations
text = "python"
length = len(text)
length_float = float(length)
length_string = str(length_float)
print("Texto:", text)
print(f"Longitud como flotante: {length_float}")
print(f"Longitud como string: {length_string}")
print(f"tipo de length:{type(length)}")
print(f"tipo de legth_float:{ type(length_float)}")
print(f"tipo de length_string:{type(length_string)}")
print("-"*50)
#20 Tipo de length
print("Tipo de length:", type(length))
print("Tipo de length_float:", type(length_float))
print("Tipo de length_string:", type(length_string))
print("-"*50)
#21 Check if number is even
number = 10
is_even = number % 2 == 0
print(f"{number} % 2 == 0?: {is_even}")
number2 = 7        #ejemplo con otra numeracion
is_even2 = number2 % 2 == 0
print(f"{number2} % 2 == 0?: {is_even2}")
print("-"*50)
#22  Floor division check
floor_div = 7 // 2
int_converted = int(2.7)
print(f"7//3 = {floor_div}")
print(f"int (2.7)= {int_converted}")
print(f"¿son iguales? {floor_div == int_converted}")
print("-"*50)

#23 Type comparison
type1 = type('10')
type2 = type(10)
print(f"type('10'): {type1}")
print(f"type(10): {type2}")
print("Son iguales:", { type1 == type2})
print("-"*50);

#24 Int conversion check

tryresult = int("9.8")
print(f"int('9.8)=={"result"}")
print("int(8.9) ==10: {result == 10}")

print("Except valueError as e:" )  
print(f"error: {"e"}")
print("int (9.8) un ValueError porque '9.8' no es una cadena entera válida")
#25 Pay calculator
rate = float(input("Introduce las horas: "))
hours = float(input("Introduce el rate por hora: "))
pay = hours * rate
print(f"Tu ganancia semanal son: {pay}")
print("-"*50)
#26 Seconds lived calculator
años = int(input("¿Cuántos años has vivido?: "))
seconds_per_year = 365 * 24 * 60 * 60
#27-  31,536,000 segundos por año
total_seconds = años * seconds_per_year
print(f"Has vivido por {total_seconds} segundos.")
print("-"*50)
#28 display table
for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")