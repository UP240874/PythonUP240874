#exercise 1
first_name = "andrea"
last_name= "iñiguez"
full_name= "andrea iñiguez"
country= "mexico"
city= "aguascalientes"
age= 18
year= 30 
is_married= False
is_true= True
is_light_on= True
a, b, c= 1, 2, 3

#exercise 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a), (type(b)), (type(c)))

#longitud del primer nombre 
print(len(first_name)> len(last_name)) #true 
print(len(first_name)== len(last_name)) #false
print(len(first_name) < len(last_name)) #false

#operaciones matematicas 
num_one=9
num_two=4
total = print (num_one+ num_two)
diff= print(num_one -num_two)
product= print(num_one * num_two)
division= print(num_one / num_two)
remainder= print(num_one % num_two)
exp = print(num_one ** num_two)
floor_division= print (num_one // num_two)

#circulo con radio de 30 metros
radius=30
pi= 3.1416
area_of_circle= pi * radius ** 2
circumference_of_circle= 2* pi * radius
#resultado del circulo
print("area del circulo:", area_of_circle)
print("circunferencia del circulo:", circumference_of_circle)

#solicitar datos al usuario
first_name = input ("enter your first name: ")
last_name = input("enter your last name: ")
country = input("enter your country: ")
age = input("enter your age: ")

#mostrarlos valores ingresados
print("first name:", first_name)
print("last name:", last_name)
print("country:", country)
print("age:", age)
