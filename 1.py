number = int(input())
#  вводим целое число и при помощи цикла считаем его наименьший делитель, кроме 1
# (если число без остатка делится на i, то выводим число и завершаем цикл)
for i in range(2,number + 1):
    if number % i==0:
        print(i)
        break
