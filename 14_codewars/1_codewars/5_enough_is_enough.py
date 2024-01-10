'''
train_date: 6.05.2020
kata link: https://www.codewars.com/kata/554ca54ffa7d91b236000023
points: 6 kyu
type: LISTS
-------------
DESCRIPTION:

Enough is enough!
Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, 
and now they want to show Charlie their entire collection. 
However, Charlie doesn't like this sessions, since the motive usually repeats. 
He isn't fond of seeing the Eiffel tower 40 times. 
He tells them that he will only sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number. 
Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

Task
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. 
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, 
and then take 3, which leads to [1,2,3,1,2,3].

Example
  delete_nth ([1,1,1,1],2) # return [1,1]
  delete_nth ([20,37,20,21],1) # return [20,37,21]
-------------
TRANSLATION:


Элис и Боб были в отпуске. Оба они сделали множество фотографий мест, где они побывали, и теперь они хотят показать Чарли всю свою коллекцию.
 Однако Чарли не любит эти сеансы, так как мотив обычно повторяется. Ему не нравится видеть Эйфелеву башню 40 раз.
Он говорит им, что согласится посмотреть сеанс, только если они покажут один и тот же мотив не более N раз. 
К счастью, Элис и Боб могут закодировать мотив как число. 
Можете ли вы помочь им удалить числа так, чтобы в их списке каждое число встречалось не более N раз, не меняя порядок?

Задача
Дан список и число, создайте новый список, который содержит каждое число из исходного списка не более N раз, не меняя порядка.
Например, если входное число равно 2, а входной список - [1,2,3,1,2,1,2,3], вы берете [1,2,3,1,2], отбрасываете следующие [1,2], так как это привело бы к тому, что 1 и 2 встречались бы в результате 3 раза, а затем берете 3, что приводит к [1,2,3,1,2,3].
Со списком [20,37,20,21] и числом 1 результат будет [20,37,21].

-------------
===TRAINED====
лучший способ увеличить индекс словаря это через проверку гетом
freq_dict[el] = freq_dict.get(el, 0) + 1
-------------
'''


def delete_nth(order, max_e):
    list_result = []
    freq_dict = {}
    for el in order:
        freq_dict[el] = freq_dict.get(el, 0) + 1
        if freq_dict[el] <= max_e:
            list_result.append(el)
    return list_result


print(delete_nth([1,1,1,1],2))# return [1,1]
print(delete_nth([20,37,20,21],1))
