'''
Challenge:

Given a two-dimensional array, return a new array which carries over only those arrays from the original,
which were not empty and whose items are all of the same type (i.e. homogenous).
For simplicity, the arrays inside the array will only contain characters and integers.

Example:

Given [[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]], your function should return [[1, 5, 4], ['b']].

Addendum:

Please keep in mind that for this kata, we assume that empty arrays are not homogenous.

The resultant arrays should be in the order they were originally in and should not have its values changed.

No implicit type casting is allowed. A subarray [1, '2'] would be considered illegal and should be filtered out.
----
как при помощи множества оставить только уникальные элементы в массиве
l = set(l)
'''

def list_check(l):
	if len(set([type(el) for el in l])) == 1:
		return True

def filter_homogenous(l_in):
	return [el for el in l_in if (list_check(el))]

print (filter_homogenous ([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]))

