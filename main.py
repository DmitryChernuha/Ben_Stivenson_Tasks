my_books = {
    'Эрик Мэтиз': 'Изучаем Python',
    'Марк Лутц': 'Изучаем Python 1',
    'Джон Дакет': 'HTML и CSS для начинающих',
    'Эрик Мейер': 'CSS полный справочник',
    'Дэвид Флэнаган': 'Java Script руководство',
    'Пол Берри': 'Python для начинающих',
    'Кирупа Чинамтамби': 'Изучаем React'
}

# Упражнение 1 Почтовый адрес


index = input('Введите почтовый индекс: ')
city = input('Введите город: ')
street = input('Введите улицу: ')
house = input('Введите номер дома: ')
flat = input('Введите номер квартиры: ')
family = input('Введите фамилию: ')
name = input('Введите имя: ')
lastname = input('Введите отчество: ')
print(index)
print(city)
print(f' улица {street}, дом № {house}, квартира № {flat}')
print(f'{family} {name} {lastname}')

# Упражнение 2 Приветствие

name = input()
text = 'привествую тебя на сайте'
print(f'{name}, {text}')

# Упражнение 3 Площадь комнаты

length = float(input('Введите длинну комнаты (м): '))
width = float(input('Введите ширину комнаты (м): '))
area = length * width
print(f'Площадь комнаты составляет {round(area, 2)} кв.м.')

# Упражнение 4 Площадь садового участка

SQRTFUT_SQRTACR = 43560
width = float(input('Введите длинну участка (фут): '))
length = float(input('Введите ширину участка (фут): '))
area_in_fut = width * length
area_in_acres = area_in_fut / SQRTFUT_SQRTACR
print(f'Площадь Вашего садового участка составляет {round(area_in_acres, 2)} акров')


# Упражнение 4 Сдаем бутылки
BIG_BOTTLE_COAST = 0.25
LITTLE_BOTTLE_COAST = 0.1
bottles_little = int(input('Введите количество маленьких бутылок: '))
bottles_big = int(input('Введите количество больших бутылок: '))
bottles_coast = bottles_little * LITTLE_BOTTLE_COAST + bottles_big * BIG_BOTTLE_COAST
print('За ваши бутылки вы получите $%.2f' % bottles_coast)

# Упражнение 6 Налоги и чаевые

TAX = 0.2
TIPS = 0.18
restaurant_bill = float(input('Введите сумму счета: '))
tax = restaurant_bill * TAX
tips = restaurant_bill * TIPS
total = restaurant_bill + tax + tips
print('Налог составил: $%.2f\nЧаевые: $%.2f\nОбщая сумма заказа: $%.2f' % (tax, tips, total))

# Упражнение 7 Сумма первых положительных чисел

Способ №1

number = int(input('Введите число: '))
total_number = (number * (number + 1)) / 2
print(f'Сумма чисел от 1 до {number} составляет {int(total_number)}')

# Способ №2

number = int(input('Введите число: '))
num_list = []
for num in range(1, number + 1):
    num_list.append(num)
sum_list = sum(num_list)
print(f'Сумма чисел от 1 до {number} составляет {sum_list}')

# Способ №3

number = int(input('Введите число: '))
number_list = [num for num in range(1, 11)]
number_list_sum = sum(number_list)
print(f'Сумма чисел от 1 до {number} составляет {number_list_sum}')

# Упражнение 8 Сувениры и безделушки

WEIGHT_SOUVENIR = 0.075
WEIGHT_TRINKET = 0.112
souvenir = int(input('Введите количество сувениров: '))
trinket = int(input('Введите количество безделушек: '))
total_weight = souvenir * WEIGHT_SOUVENIR + trinket * WEIGHT_TRINKET
print(f'Вес вашей посылки составит: {round(total_weight, 2)} кг.')

# Упражнение 9 Сложные проценты
DEPOSIT_RENT = 0.04
first_deposit = float(input('Сумма вашего первоначального депозита: '))
deposit_1 = first_deposit * DEPOSIT_RENT + first_deposit
deposit_2 = deposit_1 * DEPOSIT_RENT + deposit_1
deposit_3 = deposit_2 * DEPOSIT_RENT + deposit_2
print('Сумма вашего счета при ставке по депозиту 4 по истечению 1 года составит: $%.2f' % deposit_1)
print('Сумма вашего счета при ставке по депозиту 4 по истечению 2 года составит: $%.2f' % deposit_2)
print('Сумма вашего счета при ставке по депозиту 4 по истечению 3 года составит: $%.2f' % deposit_3)

# Упражнение 10 Арифметка

from math import log

num_1, num_2 = int(input('Введте первое число: ')), int(input('Введте второе число: '))
amount = num_1 + num_2
print(f'Сумма чисел {num_1} и {num_2} составит: {amount}')
difference = num_1 - num_2
print(f'Разность чисел {num_1} и {num_2} составит: {difference}')
composition = num_1 * num_2
print(f'Произведение {num_1} и {num_2} составит: {composition}')
quotient = num_1 / num_2
print(f'Частное от деления {num_1} и {num_2} составит: {round(quotient, 2)}')
remain = num_1 % num_2
print(f'Остаток от деления {num_1} и {num_2} составит: {round(remain)}')
whole_part = num_1 // num_2
print(f'Целая часть от деления {num_1} и {num_2} составит: {round(remain)}')
degree = num_1 ** num_2
print(f'{num_1} и {num_2} составит: {degree}')
log_10 = log(10, num_1)
print(f'Десятичный логарфм {num_1} составит {log_10}')

# Упражнение 11

LPG = 3.785
KMPM = 1.609
miles_per_gallon = float(input('Введите расход в миля/галл: '))
km_per_litres = (100 * LPG) / (miles_per_gallon * KMPM)
print('Расход бензина %.2f миля/галл. составит %.2f л/100 км.' % (miles_per_gallon, km_per_litres))

# Упражнение 12 Широта и долгота

import math

RADIUS = 6371.01
latitude_start = int(input('Введите широту начальной точки в градусах: '))
longitude_start = int(input('Введите долготу начальной точки в градусах: '))
latitude_finish = int(input('Введите широту конечной точки в градусах: '))
longitude_finish = int(input('Введите долготу конечной точки в градусах: '))
latitude_start_radians = math.radians(latitude_start)
longitude_start_radians = math.radians(longitude_start)
latitude_finish_radians = math.radians(latitude_finish)
longitude_finish_radians = math.radians(longitude_finish)
distance = RADIUS * math.acos(math.sin(latitude_start_radians) * math.sin(latitude_finish_radians) +
                              math.cos(latitude_start_radians) * math.cos(latitude_finish_radians) *
                              math.cos(longitude_start_radians - longitude_finish_radians))
print(f'Расстояние между точками с координатами:\n{latitude_start} {longitude_start}\n{latitude_finish}'
      f' {longitude_finish}\составит {int(distance)} км')


# Упражнение 14 Рост

INCH_IN_FUT = 12
INCH_IN_SM = 2.54
height_in_futes = int(input('Введите рост, футы: '))
height_in_inches = int(input('Введите рост, дюймы: '))
height_in_sm = height_in_futes * INCH_IN_FUT * INCH_IN_SM + height_in_inches * INCH_IN_SM
print(f'Ваш рост {round(height_in_sm)} см.')


# Упражнение 15 Расстояние

import math

INCHES_FEET = 12
YARDS_FEET = 0.333
MILES_FEET = 0.00019
METRES_FEET = 0.3048
distance_in_feet = int(input('Введите дистанцию в футах: '))
distance_in_inches = distance_in_feet * INCHES_FEET
distance_in_yards = distance_in_feet * YARDS_FEET
distance_in_miles = distance_in_feet * MILES_FEET
distance_in_metres = distance_in_feet * METRES_FEET
print(f'Расстояние в {distance_in_feet} футов составит:\n{distance_in_inches} дюймов\n{distance_in_yards} ярда\n'
      f'{(distance_in_miles)} мили\n{distance_in_metres} метра')


# Упражнение 16 Площадь и обьем

from math import pi
radius = float(input('Введите радиус: '))
area = pi * radius ** 2
volume = (4 / 3) * pi * radius ** 3
print('Площаль окружности составит %0.2f' % area)
print('Обьем шара составит %0.2f' % volume)


# Упражнение 17 Теплоемкость

WATER_HEAT_CAPACITY = 4.186
ELECTRICITY_PRICE = 8.9
J_TO_KWT = 2.777E-7
water_volume = float(input('Введите объем воды в милилитрах: '))
delta_t = float(input('Введите повышение температуры воды в гр. Цельсия: '))
q = WATER_HEAT_CAPACITY * water_volume * delta_t
print(f'Для нагрева воды, объемом {int(water_volume)} милилитров необходимо {int(q)} джоулей')
cost = J_TO_KWT * q * ELECTRICITY_PRICE
print('Для нагрева воды, объемом %0.1f милилитров будет стоить $%0.2f' % (water_volume, cost))

# Упражнение 18 Объем цилиндра

import math

radius = float(input('Введите радиус цилиндра: '))
height = float(input('Введите высоту цилиндра: '))
volume = math.pi * radius ** 2 * height
print('Обьем цилиндра составит %.1f' % volume)


# Упражнение 19 Свободное падение

import math

G = 9.8
height = float(input('Введите высоту опускания в метрах: '))
speed = math.sqrt(2 * G * height)
print('При соприкосновении с землей скрость обьекта составит %.2f м/с' % speed)


# Упражнение 21 Площадь треугольника

footing = float(input('Введите основание треугольника: '))
height = float(input('Введите высоту треугольника: '))
area = (footing * height) / 2
print(f'Площадь треугольника с высотой {height} и основанием {footing} составит {area}')

# Упражнение 22 Площадь треугольника

from math import sqrt

side_1 = float(input('Введите динны первой стороны треугольника в метрах: '))
side_2 = float(input('Введите динны второй стороны треугольника в метрах: '))
side_3 = float(input('Введите динны третей стороны треугольника в метрах: '))
half_m = (side_3 + side_2 + side_1) / 2
area = sqrt(half_m * (half_m - side_1) * (half_m - side_2) * (half_m - side_3))
print('Площадь треугольника составит %.2f метров квадратных' % area)


# Упражнение 35 Чет или нечет

number = int(input('Введите число: '))
if number % 2 == 0:
    print('Число четное')
else:
    print('Число нечетное')


# Упражнение 36 Собачий возраст

dog_age = int(input('Введите возраст собаки: '))
if 0 < dog_age <= 2:
    print(f'Возраст собаки {int(dog_age * 10.5)}')
elif dog_age > 2:
    print(f'Возраст собаки {int(2 * 10.5) + (dog_age - 2) * 4}')
elif dog_age < 0:
    print('Введите положительное число')


# Упражнение 37 Гласные и согласные

letter = input('Введите букву английского алфавита: ')
vowel_let = ['a', 'e', 'i', 'о', 'u']
consonant_let = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
another_letters = ['y']
if letter in vowel_letters:
    print(f'Буква глассная')
elif letter in consonant_letters:
    print(f'Буква согласная')
elif letter in another_letters:
    print(f'Буква может быть и глассной и согласной')

# Упражнение 38 Угадай фигуру

sides_of_figure = int(input('Введите количество сторон фигуры (от 1 до 10): '))
if sides_of_figure == 3:
    print(f'Фигура с количеством сторон {sides_of_figure} это треугольник')
elif sides_of_figure == 4:
    print(f'Фигура с количеством сторон {sides_of_figure} это четырехугольник')
elif sides_of_figure == 5:
    print(f'Фигура с количеством сторон {sides_of_figure} это пятиугольник')
elif sides_of_figure == 6:
    print(f'Фигура с количеством сторон {sides_of_figure} это шестиугольник')
elif sides_of_figure == 7:
    print(f'Фигура с количеством сторон {sides_of_figure} это семиугольник')
elif sides_of_figure == 8:
    print(f'Фигура с количеством сторон {sides_of_figure} это восьмиугольник')
elif sides_of_figure == 9:
    print(f'Фигура с количеством сторон {sides_of_figure} это девятиугольник')
elif sides_of_figure == 10:
    print(f'Фигура с количеством сторон {sides_of_figure} это десятиугольник')
else:
    print('Введенное число находится за границами указанного диапазона')
















