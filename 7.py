number = int(input())
count = 1
# данная переменная хранит количество делителей числа, ее значение по умолчанию 1, так как в цикле 1 мы не учитываем, а начинаем с 2
for i in range(2,number+1):
    count +=(0,1)[number%i==0]
    # в цикле мы перебираем все числа от 2 до введенного числа и если введенное число делится на итератор без остатка, то мы добаляем 1 к переменной каунт
print(count)