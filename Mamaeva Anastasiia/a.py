# функция, разбивающая число на цифры
def divide_by_numbers(number: int):
    arr = []
    if number == 0:
        arr.append(0)
    while number > 0:
        arr.append(number % 10)
        number = number // 10
    return arr


# функция, вычитающая два числа в нужной системе счисления
def sub(max_num, min_num, base):
    answer = []
    min = []
    max = []
    min = min_num.copy()
    max = max_num.copy()
    min.sort()
    max.sort()
    max.reverse()

    length = len(max_num)
    i = length - 1
    while i >= 0:
        if (min[i] > max[i]):
            answer.append(max[i] + base - min[i])
            max[i - 1] = max[i - 1] - 1
            i = i - 1
        else:
            answer.append(max[i] - min[i])
            i = i - 1
    answer = answer[::-1]
    return answer


# функция, преводящая число из десятичной системы счисления в нужную
def translation_to_need_system(number, base):
    alp = '0123456789ABCDEF'
    s = ''
    if number == 0:
        s = '0'
    while number > 0:
        number, y = divmod(number, base)
        s = alp[y] + s
    return s

# функция, переводящая полученное число в десятичную систему счисления
def translation_to_decimal(number, base):
    length = len(number)
    alp = '0123456789ABCDEF'
    # разбиваем на символы строку-число
    number = ''.join(reversed(number))
    num_symbol = list(number)
    if num_symbol == ['0']:
        return 0
    i = 0
    result = 0
    while i < length:
        result = result + alp.find(num_symbol[i]) * pow(base, i)
        i = i + 1
    return result


# функция, находящая есть ли цикл
# если цикл есть - возвратит 1, в обратном случае 0
def find_cycle(arr):
    ar = set(arr)
    if len(arr) == len(ar):
        return 0
    else:
        return 1

# функция делает из массива число
def make_number(arr, len):
    answer = 0
    i = len - 1
    factor = 1
    while i >= 0:
        answer = answer + arr[i] * factor
        factor = factor * 10
        i = i - 1
    return answer

# функция Капрекара
def my_kap(number, base):
    number = divide_by_numbers(number)
    # массив для проверки наличия циклов
    ar = []
    i = 0
    late_answer = [0]
    now_answer = sub(number, number, base)
    ar.append(make_number(now_answer, len(now_answer)))

    while now_answer != late_answer:
        late_answer = now_answer
        now_answer = sub(now_answer, now_answer, base)
        ar.append(make_number(now_answer, len(now_answer)))
        i = i + 1
        if ar[i-1] == ar[i]:
            now_answer = make_number(now_answer, len(now_answer))
            return now_answer
        tmp = find_cycle(ar)
        if tmp == 0:
            continue
        else:
            return -1
    now_answer = make_number(now_answer, len(now_answer))
    return now_answer

# функция, находящая длину цикла или кол-во шагов до числа капрекара
def steps(number, base):
    number = divide_by_numbers(number)
    # массив для проверки наличия циклов
    ar = []
    i = 0
    step = 0
    late_answer = [0]
    now_answer = sub(number, number, base)
    step = step + 1
    ar.append(make_number(now_answer, len(now_answer)))

    while now_answer != late_answer:
        late_answer = now_answer
        now_answer = sub(now_answer, now_answer, base)
        step = step + 1
        ar.append(make_number(now_answer, len(now_answer)))
        i = i + 1
        if ar[i - 1] == ar[i]:
            return step - 1
        tmp = find_cycle(ar)
        if tmp == 0:
            continue
        else:
            return step - 1
    return step

# точка входа в программу
# запускаем цикл
number_count = 6
base = 10

# часть кода, для поиска чисел капрекара и записи в таблицу
file = open('table.csv', 'w')
file.write('"digits", "base", "kaprekar"\n')

for j in range(1, number_count + 1):
    answer = []
    for i in range(2, base + 1):
        for num in range(i ** j):
            num = translation_to_need_system(num, i)
            num = int(num)
            kap = my_kap(num, i)
            if kap != -1:
                if len(str(num)) == j:
                    answer.append(kap)
        answer = set(answer)
        file.write('"%i","%i","%s"\n' % (j, i, answer))
        answer = list(answer)
        answer.clear()

file.close()

# часть кода, для поиска длины циклов и записи в таблицу
'''
file2 = open('steps.csv', 'w')
file2.write('"digits", "base", "count of steps"\n')

for j in range(1, number_count + 1):
    answer = []
    for i in range(2, base + 1):
        for num in range(i ** j):
            num = translation_to_need_system(num, i)
            num = int(num)
            kap = steps(num, i)
            answer.append(kap)
        a = max(answer)
        a = str(a)
        a = translation_to_decimal(a, i)
        file2.write('"%i","%i","%i"\n' % (j, i, a))
        answer.clear()

file2.close()'''