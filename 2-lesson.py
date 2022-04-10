# Вывод данных
"""name=input('Введите ваше имя: ')
first_name=input('Введите вашу фамилию: ')
invalue=input('Объём продаж за неделю: ')
print('Ваша фамилия:',first_name)
print('Ваше имя:',name)
print('Ваш объём продаж за неделю равен:',invalue)"""
# Форматирование
'''print(format(65.4321, '.2f'))
print(format(987654.129,',.2f'))
print('Пн\tВт\tСр')
print('Чт\tПт\tСб')'''
# Инструкция для 10% скидки
'''Full_price=int(input())
SALE=10
Sale_price=Full_price-Full_price*(10/100)
print(format(Sale_price, '.0f'))'''
# Черепаха
'''import turtle #Загрузка черепахи
turtle.showturtle() #Вызов окна с черепахой
turtle.forward(50) #Перемещение
turtle.setheading(90) #Направление
turtle.forward(100)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(50)
turtle.forward(50)
turtle.heading() #Градус черепахи
270.0
turtle.penup() #Не рисует
turtle.forward(200)
turtle.pendown() #Рисует
turtle.forward(100)
turtle.penup()
turtle.forward(100)
turtle.forward(100)
turtle.circle(100)
turtle.right(180) #Раправление
turtle.forward(500)
turtle.left(90)
turtle.forward(200)
turtle.pendown()
turtle.circle(100) #Рисование круга
turtle.dot() #Рисование точки
turtle.pendown()
turtle.forward(50)
turtle.dot()
turtle.forward(50)
turtle.pensize(10)#Изменение размера пера
turtle.pencolor('red')#Изменение цвета пера
turtle.bgcolor('white')#Изменение цвета заднего фона
turtle.setup(1400,800)#Задаёт размер графического окна
turtle.goto(0,0)#Рисование линии по координатам
turtle.write("Hello!")#Написание текста
'''
'''
#Орион(Созвездие)
#Создание переменных
import turtle
turtle.showturtle()
turtle.setup(500,600)
turtle.penup()
turtle.hideturtle()
LEFT_SHOULDER_X=-70
LEFT_SHOULDER_Y=200

RIGHT_SHOULDER_X=80
RIGHT_SHOULDER_Y=180

LEFT_BELTSTAR_X=-40
LEFT_BELTSTAR_Y=-20

MIDLE_BELTSTAR_X=0
MIDLE_BELTSTAR_Y=0

RIGHT_BELTSTAR_X=40
RIGHT_BELTSTAR_Y=20

LEFT_KNEE_X=-90
LEFT_KNEE_Y=-180

RIGHT_KNEE_X=120
RIGHT_KNEE_Y=-140
#Расположение звёзд
turtle.goto(LEFT_SHOULDER_X,LEFT_SHOULDER_Y)
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.dot()
turtle.goto(MIDLE_BELTSTAR_X,MIDLE_BELTSTAR_Y)
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X,RIGHT_BELTSTAR_Y)
turtle.dot()
turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.dot()
turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)
turtle.dot()

#Название звёзд
turtle.goto(LEFT_SHOULDER_X,LEFT_SHOULDER_Y)
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.write('Хатиса')
turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.write('Альнитак')
turtle.goto(MIDLE_BELTSTAR_X,MIDLE_BELTSTAR_Y)
turtle.write('Альнилам')
turtle.goto(RIGHT_BELTSTAR_X,RIGHT_BELTSTAR_Y)
turtle.write('Минтака')
turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.write('Саиф')
turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)
turtle.write('Ригель')

turtle.goto(LEFT_SHOULDER_X,LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.penup()

turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X,RIGHT_BELTSTAR_Y)
turtle.penup()

turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDLE_BELTSTAR_X,MIDLE_BELTSTAR_Y)
turtle.penup()

turtle.goto(MIDLE_BELTSTAR_X,MIDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X,RIGHT_BELTSTAR_Y)
turtle.penup()

turtle.goto(RIGHT_BELTSTAR_X,RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X,RIGHT_KNEE_Y)
turtle.penup()

turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X,LEFT_KNEE_Y)
turtle.penup()


turtle.done()'''

# Задачи
'''#1 Задача
height=input('Введите ваш рост:')
print('Ваш рост:',height)'''
'''#2 Задача
color=input('Ваш любимый цвет?')
print('Вашим любимым цветом,является:',color)'''
'''#3 Задача
a,b,c=int(input('Введите число a:')),int(input('введите число b:')),int(input('введите число c:'))
b=a+2
a=b*4
b=a/3.14
a=8-b
print('Число a, равняется:',a)'''
'''# 4 Задача
w = 5
x = 4
y = 8
z = 2
result = x + y
# noinspection PyRedeclaration
result = z * 2
# noinspection PyRedeclaration
result = y / x
# noinspection PyRedeclaration
result = y - z
# noinspection PyRedeclaration
result = w // z
print(result)'''
'''# 5 Задача
x = 10
y = 14
total=x+y
print(total)'''
'''# 6 Задача
total=int(input('Введите итоговую сумму:'))
down_payment=int(input('Введите сумму предоплаты:'))
due=total-down_payment
print('К оплате:', due)'''
'''#7 Задача
subtotal=int(input('Введите число:'))
total=subtotal*0.15
print(format(total,'.0f'))'''
'''#10 Задача
sales=float(input('Введите значение:'))
print(format(sales,'.2f'))'''
'''#11 Задача
number=1234567.456
print(format(number,',.1f'))'''
'''#13 Задание
import turtle
turtle.showturtle()
turtle.circle(75)
turtle.done()'''
'''#14 Задание
import turtle
turtle.showturtle()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()
turtle.done()'''
'''#15 Задание
import turtle
turtle.showturtle()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.goto(10,100)
turtle.forward(50)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.done()'''

#Задачи по программированию
'''#1 Задача
name=input('Введите ваше имя:')
address=input('Введите ваш адрес:')
phone_number=int(input('Введите ваш телефон:7+'))
job=input('Введите вашу специализацию в учебном заведении:')
print('Ваше имя:',name)
print('Ваш адрес:',address)
print('Ваш телефон:',phone_number)
print('Ваша специализация:',job)'''
'''#2 Задача
PERCENT=0.23
Pay=float(input('Введите объём продаж:'))
Total_pay=Pay*PERCENT
print('Ваша прибыль равна:',Total_pay)'''


'''
#Черепашья графика
import turtle
turtle.showturtle()
turtle.circle(25)
turtle.penup()
turtle.goto(12,0)
turtle.goto(20,0)
turtle.circle(25)
turtle.goto(20,-15)
turtle.circle(25)
turtle.goto(20,-20)
turtle.goto(25,-25)
turtle.circle(25)
turtle.pendown()
turtle.circle(25)
turtle.penup()
turtle.goto(50,0)
turtle.goto(75,0)
turtle.circle(25)
turtle.circle(25)
turtle.goto(60,0)
turtle.circle(25)
turtle.pendown()
turtle.circle(25)
turtle.reset()
turtle.circle(140)
turtle.reset()
turtle.circle(13)
turtle.reset()
turtle.circle(25)
turtle.penup()
turtle.goto(0,25)
turtle.goto(0,50)
turtle.goto(0,37)
turtle.goto(0,0)
turtle.goto(0,13)
turtle.goto(25,13)
turtle.goto(0,0)
turtle.goto(0,20)
turtle.undo()
turtle.goto(20,0)
turtle.circle(25)
turtle.goto(25,0)
turtle.goto(50,0)
turtle.circle(25)
turtle.goto(50,-25)
turtle.circle(25)
turtle.goto(25,-25)
turtle.circle(25)
turtle.pendown()
turtle.circle(25)
turtle.penup()
turtle.goto(50,50)
turtle.goto(75,50)
turtle.circle(25)
turtle.goto(50,25)
turtle.goto(75,0)
turtle.circle(25)
turtle.goto(70,0)
turtle.circle(25)
turtle.goto(60,0)
turtle.goto(25)
turtle.circle(25)
turtle.pendown()
turtle.circle(25)
turtle.reset()
turtle.circle(25)
turtle.penup()
turtle.goto(30,-25)
turtle.circle(25)
turtle.pendown()
turtle.circle(25)
turtle.penup()
turtle.goto(60,0)
turtle.circle(25)
turtle.pendown()
turtle.circle(25)
turtle.penup()
turtle.goto(60,-25)
turtle.goto(90,-25)
turtle.circle(25)
turtle.pendown()
turtle.circle(25)
turtle.penup()
turtle.goto(120,0)
turtle.circle(25)
turtle.pendown()
turtle.circle(25)
turtle.reset()
turtle.goto(0,140)
turtle.goto(140,140)
turtle.goto(140,0)
turtle.goto(0,0)
turtle.goto(140,-140)
turtle.goto(280,-140)
turtle.goto(280,0)
turtle.goto(140,0)
turtle.goto(140,-140)
turtle.penup()
turtle.goto(280,0)
turtle.pendown()
turtle.goto(140,140)
turtle.penup()
turtle.goto(140,0)
turtle.pendown()
turtle.goto(0,140)
turtle.penup()
turtle.goto(280,-140)
turtle.pendown()
turtle.goto(140,0)
'''
