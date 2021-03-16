# The practical task 1: 15/03/2021
# 1.Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

mgc_word = 'abracadabra'
print(f'The magic word is: {mgc_word:*^15} ', end='')
rpt_qntt = int(input('How many times to repeat it?: '))

# Check quantity of repetitions
while rpt_qntt == 0 or len(rpt_qntt * mgc_word) > 256:
    if rpt_qntt == 0:
        rpt_qntt = int(input('Ups, you must say the magic word at least once. So, how many times to repeat it?: '))
    elif len(rpt_qntt * mgc_word) > 256:
        rpt_qntt = int(input('The mantra is too long. Enter fewer repetitions, please: '))

# Print string with adapted phrase
if rpt_qntt == 1:
    print(f'Print the word "{mgc_word}" once: ', mgc_word)
else:
    print(f'Print the word "{mgc_word}" {rpt_qntt} times: ', end='')
    count = 1
    while count <= rpt_qntt:
        print(count, mgc_word, sep='', end='')
        count += 1

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Введите количество секунд: '))
# без контроля превышения 99 часов
print(f'Это будет: \t{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

# без контроля выхода суммы за sys.maxsize
n = int(input('Введите число n: '))
while n <= 0:
    n = int(input('Должно быть целое положительное число: '))
i, summ = 1, 0
symbol, summ_str = str(n), ''
while i <= n:
    summ = summ + int(symbol * i)
    if i != n:
        summ_str = summ_str + symbol * i + " + "
    else:
        summ_str = summ_str + symbol * i
    i += 1
print(summ_str, '=', summ)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте
# цикл while и арифметические операции.

n = input('Введите целое положительное число: ')
if not n:
    print('Не хотите, не надо. Bye.')
else:
    n = int(n)
    while n <= 0:
        n = int(input('Должно быть целое положительное число: '))
    max_number = n % 10
    while n != 0:
        if n % 10 > max_number:
            max_number = n % 10
        n //= 10
    print(f'Максимальное число: {max_number}')

# 5. Запросите у пользователя значение выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input('Объем выручки, попуг.: '))
losses = int(input('Объем убытков, попуг.: '))
if proceeds < 0 or losses < 0:
    print('Ой все')
elif proceeds > losses:
    print(f'Поздравляем, прибыльное предприятие. Рентабельность составляет {(proceeds - losses) * 100 / proceeds:.2f}%')
    staff = int(input('Какова численность сотрудников фирмы?: '))
    if staff <= 0:
        print('А вы кто?')
    else:
        print(f'Каждый сотрудник принес фирме {(proceeds / staff):.2f} попугаев')
elif proceeds == losses:
    print('Самое время продавать.')
else:
    print(f'Безнадежно, предприятие убыточно.')

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.

while True:
    distance = input('Сколько пробежал в первый день, км.?: ')
# TODO: не предусмотрена обработка ввода не цифр, запятой в числе и значений <=0
    if distance:
        distance = float(distance)
        break
while True:
    goal_distance = input('Какая целевая ежедневная дистанция, км.?: ')
    if goal_distance:
        goal_distance = float(goal_distance)
        break
days_count = 1
while True:
    print(f'{days_count}-й день: {distance:.3f}')
    if distance > goal_distance:
        break
    days_count += 1
    distance *= 1.1
