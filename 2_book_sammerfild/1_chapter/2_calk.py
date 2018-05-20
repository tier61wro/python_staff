##программа, которая в цикле while предлагала бы пользователю ввести число, постепенно накапливая список введенных чисел. Затем, когда пользователь завершит работу с программой (простым нажатием клавиши Enter), она выводила бы числа, введенные пользователем, количество введенных чисел, их сумму, наименьшее и наибольшее число и среднее значение (сумма / количество).

#!/usr/bin/env python3
numbers = []

while 1:
    line = input("please enter number ")
    #print ("type of line =",type(line))
    try :
        if (int(line))%1 == 0:
            print ("you entered", line)
            numbers.append(line)
    except ValueError:
        print ("end of work")
        break

count = len(numbers)
sum_all =0;
for num in numbers:
    sum_all += int(num)

#def count_median(a)

print ("numbers:", numbers)
print ("count = ", count)
print ("sum = ", sum_all)

