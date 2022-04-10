"""y = 20
if y == 20:
    x = 0
    print(x)

sales = 12000
if sales >= 10000:
    comissionRate = 0.2
    print(comissionRate)


s1 = 'New-York'
s2 = 'Boston'
if s1 > s2:
    print(s1)
    print(s2)
else:
    print(s2)
    print(s1)


number=int(input('Введите число от 1 до 3:'))
if number==1:
    print('Один')
elif number == 2:
    print('Два')
elif number==3:
    print('Три')
else:
    print('Введите число от 1 до 3')


speed = int(input('Введите значение вашей скорости:'))
if 0 >= speed and speed <= 200:
    print('Ваша скорость в предехал правил')
if speed < 0 or speed > 200:
    print('Вы нарушаете ПДД')


#Метание снаряда
import turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)

turtle.penup()
turtle.goto(TARGET_LLEFT_X,TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

turtle.goto(0,0)
turtle.setheading(EAST)
turtle.speed(PROJECTILE_SPEED)

angle=float(input('Введите угол снаряда:'))
force=float(input('Введите пусковую силу (1-10):'))

distance=force*FORCE_FACTOR
turtle.setheading(angle)
turtle.pendown()
turtle.forward(distance)

if(turtle.xcor()>=TARGET_LLEFT_X and
   turtle.xcor()<=(TARGET_LLEFT_X+TARGET_WIDTH) and
   turtle.ycor()>=TARGET_LLEFT_Y and
   turtle.ycor()<=(TARGET_LLEFT_Y+TARGET_WIDTH)):
    print('Вы попали в цель')
else:
    print('Вы промахнулись')
turtle.done()"""

'''#Алгоритмический тренажёр
#1 Задача
x=float(input('Введите число:'))

if x>100:
    y=20
    z=40
    print('Число x:',format(x,'.0f'))
    print('Число y:',format(y,'.0f'))
    print('Число z:',format(z,'.0f'))

#2 Задача
a=float(input('Введите число:'))

if a<10:
    b=0
    c=1
    print('Число a:',format(a,'.0f'))
    print('Число b:',format(b,'.0f'))
    print('Число c:',format(c,'.0f'))

#3 Задача
a=float(input('Введите значение:'))

if a<10:
    b=0
else:
    b=99
print(format(b,'.0f'))

#4 Задача
if score >= A_score:
    print('Ваш уровень - A.')
else:
    if score >= B_score:
        print('Ваш уровень - B.')
    else:
        if score >= C_score:
            print('Ваш уровень - C.')
        else:
            if score >= D_score:
                print('Ваш уровень - D.')
            else:
                print('Ваш уровень - F.')

# 5 Задача
amount1 = float(input('Введите значение:'))
amount2 = float(input('Введите значение:'))

if amount1 > 10 and amount2 < 100:
    print('Большее число:', max(amount2, amount1))
else:
    print('Недопустимое число')

#6 Задача
speed=float(input('Введите значение скорости:'))

if speed>=24 and speed<=56:
    print('Скорость нормальная')
else:
    print('Скорость аварийная')

# 7 Задача
points=float(input('Введите значение точки:'))

if points>=9 and points<=56:
    print('Допустимые точки')
else:
    print('Недопустимые точки')

# 8 Задача

import turtle

turtle.showturtle()
if turtle.heading() >= 0 and turtle.heading() <= 45:
    turtle.penup()
else:
    turtle.pendown()
turtle.done()

# 9 Задача
import turtle

turtle.showturtle()
turtle.pencolor('red')
if turtle.pencolor() == 'red' or turtle.pencolor() == 'blue':
    turtle.pensize(5)
else:
    turtle.pensize(1)
turtle.forward(25)
turtle.done()

#10 Задача
TURTLE_LLEFT_X=100
TURTLE_LLEFT_Y=100
TURTLE_UP_X=100
TURTLE_UP_Y=200
TURTLE_RIGHT_UP_X=200
TURTLE_RIGHT_UP_Y=200
TURTLE_RIGHT_X=200
TURTLE_RIGHT_Y=100
SCREEN_WIDTH=600
SCREEN_HEIGHT=600

import turtle
turtle.showturtle()
turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
turtle.penup()
turtle.goto(TURTLE_LLEFT_X,TURTLE_LLEFT_Y)
turtle.pendown()
turtle.goto(TURTLE_UP_X,TURTLE_UP_Y)
turtle.goto(TURTLE_RIGHT_UP_X,TURTLE_RIGHT_UP_Y)
turtle.goto(TURTLE_RIGHT_X,TURTLE_RIGHT_Y)
turtle.goto(TURTLE_LLEFT_X,TURTLE_LLEFT_Y)
turtle.penup()
turtle.goto(100,200)

if (turtle.xcor()>=TURTLE_LLEFT_X and
   turtle.xcor()<=(TURTLE_LLEFT_X+SCREEN_WIDTH) and
   turtle.ycor()>=TURTLE_LLEFT_Y and
   turtle.ycor()<=(TURTLE_LLEFT_Y+SCREEN_WIDTH)):
    turtle.hideturtle()
else:
    print('Вы находитесь не в прямоугольнике!')


turtle.done()

#Задачи по програмированию

#1 Задача
Day=int(input('Введите число от 1 до 7:'))

if Day == 1:
    print('Понедельник')
elif Day == 2:
    print('Вторник')
elif Day == 3:
    print('Среда')
elif Day == 4:
    print('Четверг')
elif Day == 5:
    print('Пятница')
elif Day == 6:
    print('Суббота')
elif Day == 7:
    print('Воскресенье')
else:
    print('Введите число от 1 до 7')

#2 Задача
L_1=float(input('Введите длину первого прямоугольника:'))
L_2=float(input('введите длину второго прямоугольника:'))
W_1=float(input('Введите ширину первого прямоугольника:'))
W_2=float(input('Введите ширину второго прямоугольника:'))
S_1=L_1*W_1
S_2=L_2*W_2
if S_1>S_2:
    print('Площадь первого прямоугольника больше')
elif S_1<S_2:
    print('Площадь второго прямоугольника больше')
else:
    print('Они равны')

# 3 Задача
AGE=int(input('Введите ваш возраст:'))

if AGE==1 or AGE<1:
    print('Вы являетесь младенцем')
elif AGE>1 and AGE<13:
    print('вы явялетесь ребеёнком')
elif AGE>=13 and AGE<=20:
    print('Вы являетесь подростком')
else:
    print('Вы являетесь взрослым')

# 4 Задача
number=int(input('введите число от 1 до 10:'))

if number==1:
    print('I')
elif number == 2:
    print('II')
elif number == 3:
    print('III ')
elif number == 4:
    print('IV')
elif number == 5:
    print('V')
elif number == 6:
    print('VI')
elif number == 7:
    print('VII')
elif number == 8:
    print('VIII')
elif number == 9:
    print('IX')
elif number == 10:
    print('X')
else:
    print('Введите число от 1 до 10')

# 5 Задача
massa=float(input('Введите массу тела:'))
Ves=massa*9.8
if Ves>=100 and Ves<=500:
    print('Ваша масса тела равна:', format(Ves,'.0f'))
elif Ves>500:
    print('Вы слишком тяжёлый')
elif Ves<100:
    print('Вы слишком лёгкий')
else:
    print('Введите вашу массу тела от 100 до 500')

# 6 Задача
year=int(input('Введите две последние цифры года:'))
day=int(input('Введите день в числовом формате:'))
month=int(input('Введите месяц в числовом формате:'))
magic=month*day
if magic==year:
    print('Это волшебное число:', format(magic,'.0f'))
else:
    print('Данное число не является волшебным:',format(magic,'.0f'))

# 7 Задача
color_1=input('Введите название основного цвета:')
color_2=input('Введите название основного цвета:')

if color_1 == 'Жёлтый' and color_2 == 'Красный':
    print('Оранжевый')
elif color_1 == 'Красный' and color_2 == 'Синий':
    print('Фиолетовый')
elif color_1 == 'Синий' and color_2 == 'Жёлтый':
    print('Зелёный')
else:
    print('Введите основные цвета, такие как: "Жёлтый","Синий","Красный"')

# 8 Задача
user=int(input('Введите число посетителей:'))
hot_dog=int(input('Введите количество предложенных хот-догов посетителям:'))

sum_hot_dog=user*hot_dog

if user<=0 or hot_dog<=0:
    print('Введите количество посетителей или хот-догов больше 0')
else:
    if user>0 and hot_dog>0:
        sos_upak=sum_hot_dog//10
        bull_upak=sum_hot_dog//8
        sos_ost=sum_hot_dog%10
        bull_ost=sum_hot_dog%8
        print('Необходимо упаковок сосисок:',format(sos_upak,'.0f'))
        print('Необходимо упаковок булочек:',format(bull_upak,'.0f'))
        print('Осталось сосисок:',sos_ost)
        print('Осталось булочек:',bull_ost)

# 9 Задача
color=int(input('Введите номер кармана:'))

if color == 0:
    print('зеленый')
elif (color>=1 and color<=10 and color%2!=0):
    print('красный')
elif (color>=1 and color<=10 and color%2==0):
    print('черный')
elif (color>=11 and color<=18 and color%2!=0):
    print('черный')
elif (color)>=11 and color<=18 and color%2==0:
    print('красный')
elif (color>=19 and color<=28 and color%2!=0):
    print('красный')
elif (color>=19 and color<=28 and color%2==0):
    print('черный')
elif (color>=29 and color<=36 and color%2!=0):
    print('черный')
else:
    print('Введите число от 0 до 36')

#10 Задача
money_5=int(input('Введите количество копеек номиналом:5:'))
money_10=int(input('Введите значение по 10 копеек:'))
money_50=int(input('Введите значение монет по 50 копеек:'))
Money_5=money_5*5
Money_10=money_10*10
Money_50=money_50*50
money_1=(Money_5+Money_50+Money_10)//100
if money_1==1:
    print('Поздравляем, вы выиграли!')
elif money_1>1:
    print('Введите меньшую сумму!')
elif money_1<1:
    print('Вы ввели сумму меньшую сумму:')
elif money_5!=5 or money_10!=10 or money_50!=50:
    print('Попробуйте ещё раз!')

#11 Задача
money=int(input('Введите количество купленных книг:'))
if money==0:
    print('0 бонусов')
elif money==2:
    print('5 бонусов')
elif money==4:
    print('15 бонусов')
elif money==6:
    print('30 бонусов')
elif money==8:
    print('60 бонусов')
elif money<0 or money>8:
    print('Введите цифры от 0 до 8!')

#12 Задача
product=int(input('Введите количество купленного продукта:'))
product_cost=product*99
final_price_1=product_cost-(product_cost*0.1)
final_price_2=product_cost-(product_cost*0.2)
final_price_3=product_cost-(product_cost*0.3)
final_price_4=product_cost-(product_cost*0.4)
if product>=10 and product<=19:
    print('Ваша скидка:10%')
    print('Итоговая стоимость:',format(final_price_1,'.0f'))
elif product>=20 and product<=49:
    print('Ваша скидка:20%')
    print('Итоговая стоимость:',format(final_price_2,'.0f'))
elif product>=50 and product<=99:
    print('Ваша скидка:30%')
    print('Итоговая стоимость:',format(final_price_3,'.0f'))
elif product>=100:
    print('Ваша скидка:40%')
    print('Итоговая стоимость:',format(final_price_4,'.0f'))

#13 Задача
massa=int(input('Введите массу покупки:'))
massa_1=massa*150//100
massa_2=massa*300//100
massa_3=massa*400//100
massa_4=massa*475//100
if massa<=200:
    print('Плата за доставку:',massa_1)
elif massa>200 and massa<=600:
    print('Плата за доставку:',massa_2)
elif massa>600 and massa<=1000:
    print('Плата за доставку:',massa_3)
elif massa>1000:
    print('Плата за доставку:',massa_4)

#14 Задача
massa=float(input('Введите ваш вес:'))
height=float(input('Введите ваш рост:'))
IMT=massa/height
if IMT>=18.5 and IMT<=25:
    print('Ваш ИМТ оптимальный')
elif IMT<18.5:
    print('Вы весите ниже нормы')
elif IMT>25:
    print('Вы весите больше нормы')

#15 Задача

seconds=int(input('Введите количество секунд:'))

if seconds<60 and seconds>0:
    print('Количество минут:',seconds//60)
    print('Количество секунд:',seconds%60)
elif seconds>=60 and seconds<3600:
    print('Количество минут:',format(seconds/60,'.0f'))
    print('Количество секунд:',format(seconds%60))
elif seconds >= 3600 and seconds<86400:
    print('Количество часов:',seconds//3600)
    print('Количество минут:',format(seconds/60,'.0f'))
    print('Количество секунд:', format(seconds % 60))
elif seconds>=86400:
    print('Количество дней', seconds//86400)
    print('Количество часов:', seconds // 3600)
    print('Количество минут:', format(seconds / 60, '.0f'))
    print('Количество секунд:', format(seconds % 60))
elif seconds<0:
    print('Введите количество секунд начиная с 0')

# 17 Задача
print('Перезагрузите компьютер и попробуйте подключиться.')
message = input('Вы исправили проблему?')

if message != 'Нет' and message != 'Да':
    print('Ошибка!')
elif message == 'Да':
    print('Поздравляем! Вы исправили ошибку.')
elif message == 'Нет':
    print('Перезагрузите маршутизатор и попробуйте подключиться.')
    message_1 = input('Вы исправили проблему?')
    if message_1 != 'Нет' and message_1 != 'Да':
        print('Ошибка!')
    elif message_1 == 'Да':
        print('Поздравляем! Вы исправили ошибку.')
    elif message_1 == 'Нет':
        print('Убедитесь, что кабели между маршутизатором и модемом прочно подсоеденены.')
        message_2 = input('Вы исправили проблему?')
        if message_2 != 'Нет' and message_2 != 'Да':
            print('Ошибка!')
        elif message_2 == 'Да':
            print('Поздравляем! Вы исправили ошибку.')
        elif message_2 == 'Нет':
            print('Переместите маршутизатор на новое место.')
            message_3 = input('Вы исправили проблему?')
            if message_3 != 'Нет' and message_3 != 'Да':
                print('Ошибка!')
            elif message_3 == 'Да':
                print('Поздравляем! Вы исправили ошибку.')
            elif message_3 == 'Нет':
                print('Возьмите новый маршутизатор.')

# 18 Задача
a = input('Будет ли на ужине вегетарианец?')
b = input('Будет ли на ужине веганец?')
c = input('Будет ли на ужине приверженец безглютеновой диеты?')
if a == 'Нет' and b == 'Нет' and c == 'Нет':
    print('Вот ваши варианты ресторанов:')
    print('Изысканные гамбургеры от Джо')
elif a == 'Да' and b == 'Нет' and c == 'Да':
    print('Вот ваши варианты ресторанов:')
    print('Центральная пиццерия')
elif a == 'Да' and b == 'Да' and c == 'Да':
    print('Вот ваши варианты ресторанов:')
    print('Кафе за углом')
    print('Кухня шеф-повара')
elif a == 'Да' and b == 'Нет' and c == 'Нет':
    print('Вот ваши варианты ресторанов:')
    print('Блюда от итальянской мамы')
elif a != 'Да' and a != 'Нет' and b != 'Да' and b != 'Нет' and c != 'Да' and c != 'Нет':
    print('Ошибка!')

import turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.speed(PROJECTILE_SPEED)

angle = float(input('Введите угол снаряда:'))
force = float(input('Введите пусковую силу (1-10):'))

distance = force * FORCE_FACTOR
turtle.setheading(angle)
turtle.pendown()
turtle.forward(distance)

if angle < 64 and force < 9.1:
    print('Введите больший угол!')
    print('Введите большую силу!')
elif angle < 64:
    print('Введите больший угол!')
elif angle > 69:
    print('Введите меньший угол!')
elif angle > 69 and force > 9.8:
    print('Введите меньший угол!')
    print('Введите меньшую силу!')
elif force < 9.1:
    print('Введите большую силу!')
elif force > 9.8:
    print('Введите меньшую силу!')

if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Вы попали в цель')
else:
    print('Вы промахнулись')
turtle.done()'''


