'''
Create a class Ghost
Ghost objects are instantiated without any arguments.
Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated
ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
'''
import codewars_test as test
from random import choice


class Ghost(object):
    def __init__(self):
        self.color = choice(['yellow', 'purple', 'red', 'white'])


ghosts = [Ghost().color for _ in range(100)]
test.expect(ghosts.count("white") >= 1)
test.expect(ghosts.count("yellow") >= 1)
test.expect(ghosts.count("purple") >= 1)
test.expect(ghosts.count("red") >= 1)