#Видеокурс
#https://itvdn.com/ru/video/python-starter?utm_source=forum&utm_medium=post&utm_campaign=toster

#!/usr/bin/env python
Строка shebang обычно записывается в одной из двух форм:
#!/usr/bin/python3
или:
#!/usr/bin/env python3
В первом случае она определяет используемый интерпретатор. Вторая
форма может потребоваться для программ на языке Python, запускаемых вебсервером, хотя абсолютный путь в каждом конкретном случае может отличаться от того, что показан здесь. Во втором случае будет использован первый интерпретатор python3, найденный в текущем окружении.

# утф печать
# -*- coding: utf-8 -*-
....

y = "Who understand %r and who %s " % (binary, do_not)
# разделитель
print "." * 10

#импорт модуля
from sys import argv

# аргументы на вход
script_name, weight, height = argv