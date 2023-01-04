#-----------------------
# Задачка:
# реверсни заданную строку
#Решение:
a = 'Luna'
def solution(str):
  return str[::-1]
print (solution(a))
# еще решение
solution = lambda s: s[::-1]

# через реверс
def solution(string):
  return ''.join(i for i in reversed(string))
#-----------------------