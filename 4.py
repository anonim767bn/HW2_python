#   !!!!!ATTENTION!!!!! 
# этот код я написал сам без подсказок (могу объяснить каждую строку кода) и я поделился примером решения с несколькими людьми из группы 7.1 и 7.3, так что если вы увидете похожую реализацию, то списывал не я, а у меня


pastNumber = 0
# данная переменная будет хранить данные о предыдущем введеном числе
tempCount = 0
# данная переменная будет временным счетчиком, при этом и для возрастающих последовательностей и для убывающих
maxCount = 0
# эта переменная будет хранить максимальное значение модуля временного счетчика, 
# так как он может быть отрицательным в случае убывающей последовательности
while(number := int(input())) != 0: 
    # этот цикл будет работать до тех пор, пока мы не введем 0
    if number>pastNumber:
        # если введенное число больше предыдущего, то мы попадаем в этот сегмент кода
        maxCount = (maxCount, abs(tempCount))[abs(tempCount)>maxCount]# здесь мы сразу, не успев обнулить временный счетчик(в случае если до этого последовательность была отрицательная) 
        # передаем модуль временного счетчика(если его значение болье чем у конечного) конечному счетчику
        tempCount = (tempCount,1)[tempCount<0]
        # если предыдущая последовательность была отрицательная, то обнуляем(не обнуляем, а даем значение 1)временный счетчик, а после прибавляем 1
        tempCount +=1
        maxCount = (maxCount, abs(tempCount))[abs(tempCount)>maxCount]
        # еще раз проверяем больше ли модуль временного счетчика значения конечного счетчика и если да, то передаем ему(конечному счетчику) значение модуля временного счетчика, даже не смотря на то,
        # что мы при любом исходе сделали бы это в следующий раз, но вознакает проблема, вдруг эта итерация последняя и следующим введут 0 и цикл остановится
        pastNumber = number
        # также перезаписываем значение переменной отвечающей за предыдущее число на только что введенное
    elif number<pastNumber:
        # здесь проделываем аналогичные действия
        maxCount = (maxCount, abs(tempCount))[abs(tempCount)>maxCount]
        tempCount = (tempCount,-1)[tempCount>0]
        tempCount -=1
        maxCount = (maxCount, abs(tempCount))[abs(tempCount)>maxCount]
        pastNumber = number
    else:
        # а если введеное число равно предыдущему, то мы вначале проверяем, что модуль временного счетчика не больше значения конечного счетчика(если больше, то передаем модуль временного счетчика конечному)
        maxCount = (maxCount, abs(tempCount))[abs(tempCount)>maxCount]
        tempCount = 0
        # обнуляем временный счетчик
        pastNumber = number
print(maxCount) # выводим результат(значение конечного счетчика)
