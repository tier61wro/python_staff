
'''
train_date: 10.05.2022
kata link: https://www.codewars.com/kata/5523b97ac8f5025c45000900
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
Physical Description

The plugboard crosswired the 26 letters of the latin alphabet togther,
so that an input into one letter could generate output as another letter.
If a wire was not present, then the input letter was unchanged.
Each plugboard came with a maximum of 10 wires, so at least six letters were not cross-wired.

For example:

    If a wire connects A to B, then an A input will generate a B output and a B input will generate an A output.

    If no wire connects to C, then only a C input will generate a C output.

Note

In the actual usage of the original Enigma Machine, punctuation was encoded as words transmitted in the stream,
in our code, anything that is not in the range A-Z will be returned unchanged.


Kata

The Plugboard class you will implement, will:

    Take a list of wire pairs at construction in the form of a string, with a default behaviour of no wires configured.
    E.g. "ABCD" would wire A <-> B and C <-> D.
    Validate that the wire pairings are legitimate. Raise an exception if not.
    Implement the process method to translate a single character input into an output.

-------------
TRANSLATION:
-------------
===TRAINED==
-------------
'''

import codewars_test as test


class Plugboard(object):
    def __init__(self, wires=''):
        """
        wires: This is the mapping of pairs of characters
        """
        comutations_dict = {}
        l = list(wires)
        for i in range(0, len(l), 2):
            if l[i] not in comutations_dict and l[i+1] in comutations_dict:
                return "Should not have accepted a second definition for a wire end"
            comutations_dict[l[i]] = l[i + 1]
            comutations_dict[l[i+1]] = l[i]
        if len(comutations_dict) > 20:
            return "Should not have accepted too many wires defined"
        self.comutations_dict = comutations_dict

    def process(self, c):
        """
        c: The single character to process
        """
        if c in self.comutations_dict:
            return self.comutations_dict[c]
        else:
            return c

#===TESTS====

# p = Plugboard()
p = Plugboard("AB")



test.it("Too many wires defined")
test.expect_error(
    "Should not have accepted too many wires defined",
    lambda: Plugboard("ABCDEFGHIJKLMNOPQRSTUV"))

test.it("Character processing")
plugboard = Plugboard("AB")
test.assert_equals(plugboard.process('A'), 'B')
test.assert_equals(plugboard.process('B'), 'A')
test.assert_equals(plugboard.process('C'), 'C')