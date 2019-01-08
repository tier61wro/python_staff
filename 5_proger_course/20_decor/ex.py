#!/usr/bin/env python3
def decorator (func):
	def wrapperc ():
		print ("Код до выполения функции")
		func ()
		print ("Код, который сработал после функции")
	return wrapperc

def test (func):
	def wrapper ():
		print ("Код до выполения функции 2")
		func ()
		print ("Код, который сработал после функции 2")
	return wrapper

@decorator
@test
def show ():
	print ("Я обычная функция")

# show = decorator (show)
show ()
