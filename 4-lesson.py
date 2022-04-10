"""keep_going='д'
while keep_going=='д':
    number = int(input('Введите число:'))
    square = number ** 2
    print(square)
    keep_going=input('Хотите продолжить?' +
                     '(Введите д, если да):')

for num in [1,2,3,4,5]:
    print(num)
for x in range(5):
    print('Привет,мир!')

print('Число\tКвадрат числа')
print('----------------------')
for number in range(1,11):
    square=number**2
    print(number, '\t', square)

START_SPEED = 60
END_SPEED = 131
INCREMENT = 10
CONVERSION_FACTOR = 0.6214
print('KPH\tMPH')
print('-------------------')
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(kph, '\t', format(mph, '.1f'))

print('Эта программа показывает числа и их квадраты')
start=int(input('Введите начальное значение:'))
end=int(input('Введите конечное значение:'))
print('Число\tКвадрат числа')
print('------------------------------')
for x in range(start,end+1):
    square=x**2
    print(x,'\t',square)

total=0
for count in range(1,6):
    total+=count
    print(total)

number1=10
number2=5
number1+=number2
print(number1)
print(number2)

#Сигнальные метки

# Данная программа показывает налог на имущество
TAX_FACTOR=0.0065 # Налоговый коэффициент
print('Введите номер имущественного лота')
print('Либо 0,чтобы завершить работу')
lot=int(input('Введите номер имущественного лота:'))

while lot!=0:
    #Получить стоимость имущетсва
    value=float(input('Введите стоимость имущества:'))

    #Вычисление налога на имущество
    tax=value*TAX_FACTOR

    #Налог
    print('Налог на имущество: $', format(tax,'.2f'),sep='')

    #Получение следующего номера лота
    print('Введите номер имущественного лота')
    print('Либо 0,чтобы завершить работу')
    lot = int(input('Введите номер имущественного лота:'))

# Алгоритмический тренажёр
# 1 Задача
CONSTANTA=100
product = float(input('Введите число от 0 до 99:'))
while product<CONSTANTA:
    product = product * 10
    print(format(product,'.0f'))
    product = float(input('Введите число:от 0 до 99:'))

# 2 Задача
keep_going = 'д'
while keep_going == 'д':
    num_1=float(input('Введите число:'))
    num_2=float(input('Введите число:'))
    num_3 = num_2 + num_1
    print(format(num_3,'.0f'))
    keep_going = input('Хотите продолжить?' +
                       '(Введите д, если да):')

# 3 Задача
for num in range(0,1010,10):
    print(num)

# 4 Задача
MAX = 11
total = 0.0
print('Данная программа считывает сумму из')
print(MAX, 'чисел и суммирует их')
for counter in range(MAX):
    number = int(input('Введите число:'))
    total = total + number
print('Сумма чисел составляет', format(total, '.0f'))

#5 Задача
MAX = 31
MIN = 0
total = 0.0
for num in range(MAX):
    number = (MIN+1)/(MAX-1)
    total = total + number
    print(format(total, '.3f'))

#7 Задача
MIN = 10
MAX = 15
for r in range(MIN):
    for c in range(MAX):
        print('#',end='')
    print()

# 8 Задача
keep_going = 'д'
while keep_going == 'д' or keep_going == 'Д':
    num = float(input('Введите число:'))
    while num < 0:
        print('Ошибка! Введите валидное значение!')
        num = float(input('Введите число:'))
    print(format(num, '.2f'))
    keep_going = input('Хотите продолжить?' +
                           '(Введите д, если да):')

# 9 Задача
keep_going = 'д'
while keep_going == 'д' or keep_going == 'Д':
    num = float(input('Введите число:'))
    while num>100 or num<0:
        print('Ошибка! Введите валидное значение!')
        num = float(input('Введите число:'))
    print(format(num,'.2f'))
    keep_going = input('Хотите продолжить?' +
                       '(Введите д,если да):')

# Задачи по программированию
# 1 Задача
total = 0.0
for num in range (5):
    number = int(input('Введи число ошибок:'))
    total += number
print(format(total,'.0f'))

# 2 Задача
MIN = 10
MAX = 31
for num in range(MIN,MAX,5):
    print(format(num * 4.2, '.0f'))

# 3 Задача
summa = float(input('Введите сумму выделенную на месяц:'))
number_states = int(input('Сколько у вас отдельных статей?:'))
total = 0.0
for num in range(number_states):
    number = float(input('Введите суммы отдельных статей:'))
    total += number
print('Ваш остаток на счету:',format(summa-total,'.0f'))

# 4 Задача
miles = 0.0
hour = 0.0
speed = 0.0
speed = int(input('Введите скорость транспортного средства:'))
hour = int(input('Введите количество часов:'))
print('Час\tПройденное расстояние')
print('--------------------------')
for hour in range(1,hour+1):
    miles = speed * hour
    print(hour,'\t',miles)

# 5 Задача
average = 0.0
totalmonths = 0.0
totalrainfall = 0.0
monthrainfall = 0.0
year = 0.0
month = 0.0
year = int(input('Введите количество лет:'))
for years in range(year):
    print('Для года',years + 1,':')
    for months in range(12):
        monthrainfall = float(input('Введите количество осадков:'))
        totalmonths += 1
        totalrainfall += monthrainfall
average = totalrainfall/monthrainfall
print('Для', format(totalmonths,'.0f),'месяцев')
print('Суммарная толщина дождевых покровов:',format(totalrainfall,'.2f'),'см')
print('Среднемесячная толщина дождевых покровов:',format(average,'.2f'),'см')

# 6 Задача
START = 0
END = 21
INCREMENT = 1
print('Цельсий\tФаренгейт')
print('------------------')
for C in range(START,END,INCREMENT):
    F = (9 / 5) * C + 32
    print(C,'\t', format(F,'.0f'))

# 7 Задача
total_pay = 0.0
day = 0.0
pay = 1
day = int(input('Введите количество дней:'))
print('Дни\tЗарплата')
print('--------------')
for times in range(1, day + 1):
    print(times, '\t', float(pay / 100))
    total_pay += pay
    pay *= 2

# 8 Задача
print('Введите положительные числа,чтобы посчитать их сумму')
print('Либо отрицательное число,чтобы завершить программу')
print('----------------------------------------------------')
total = 0.0
num = 1.0
while num > 0:
    num = float(input('Введите положительное число:'))
    if num > 0:
        total += num
print('Сумма чисел равняется:',format(total,'.1f')) """

