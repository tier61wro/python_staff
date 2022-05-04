'''
train_date: 04.05.2022
kata link: https://www.codewars.com/kata/57520361f2dac757360018ce
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
Professor Oak has just begun learning Python and he wants to program his new Pokedex prototype with it.

For a starting point, he wants to instantiate each scanned Pokemon as an object that is stored at Pokedex's memory. He needs your help!

Your task is to:

    Create a PokeScan class that takes in 3 arguments: name, level and pkmntype.

    Create a info method for this class that returns some comments about the Pokemon, specifying it's name,
     an observation about the pkmntype and other about the level.

    Keep in mind that he has in his possession just three Pokemons for you to test the scanning function:
    Squirtle, Charmander and Bulbasaur, of pkmntypes water, fire and grass, respectively.

    The info method shall return a string like this: Charmander, a fiery and strong Pokemon.

    If the Pokemon level is less than or equal to 20, it's a weak Pokemon.
    If greater than 20 and less than or equal to 50, it's a fair one. If greater than 50, it's a strong Pokemon.

    For the pkmntypes, the observations are wet, fiery and grassy Pokemon, according to each Pokemon type.

IMPORTANT: The correct spelling of "Pokémon" is "Pokémon", with the "é", but to maximize the compatibility of the code
I've had to write it as "Pokemon", without the "é". So, in your code, don't use the "é".

-------------
TRANSLATION:
-------------
===TRAINED====
-------------
'''

import codewars_test as test

class PokeScan:
    # your awesome code goes here!
    pass


#===TESTS====
test.it('Basic Tests')
test.assert_equals(PokeScan('Squirtle', 0, 'water').info(), 'Squirtle, a wet and weak Pokemon.')
test.assert_equals(PokeScan('Charmander', 0, 'fire').info(), 'Charmander, a fiery and weak Pokemon.')
test.assert_equals(PokeScan('Bulbasaur', 0, 'grass').info(), 'Bulbasaur, a grassy and weak Pokemon.')

test.assert_equals(PokeScan('Squirtle', 20, 'water').info(), 'Squirtle, a wet and weak Pokemon.')
test.assert_equals(PokeScan('Charmander', 20, 'fire').info(), 'Charmander, a fiery and weak Pokemon.')
test.assert_equals(PokeScan('Bulbasaur', 20, 'grass').info(), 'Bulbasaur, a grassy and weak Pokemon.')

test.assert_equals(PokeScan('Squirtle', 21, 'water').info(), 'Squirtle, a wet and fair Pokemon.')
test.assert_equals(PokeScan('Charmander', 21, 'fire').info(), 'Charmander, a fiery and fair Pokemon.')
test.assert_equals(PokeScan('Bulbasaur', 21, 'grass').info(), 'Bulbasaur, a grassy and fair Pokemon.')

test.assert_equals(PokeScan('Squirtle', 50, 'water').info(), 'Squirtle, a wet and fair Pokemon.')
test.assert_equals(PokeScan('Charmander', 50, 'fire').info(), 'Charmander, a fiery and fair Pokemon.')
test.assert_equals(PokeScan('Bulbasaur', 50, 'grass').info(), 'Bulbasaur, a grassy and fair Pokemon.')

test.assert_equals(PokeScan('Squirtle', 51, 'water').info(), 'Squirtle, a wet and strong Pokemon.')
test.assert_equals(PokeScan('Charmander', 51, 'fire').info(), 'Charmander, a fiery and strong Pokemon.')
test.assert_equals(PokeScan('Bulbasaur', 51, 'grass').info(), 'Bulbasaur, a grassy and strong Pokemon.')

test.assert_equals(PokeScan('Squirtle', 100, 'water').info(), 'Squirtle, a wet and strong Pokemon.')
test.assert_equals(PokeScan('Charmander', 100, 'fire').info(), 'Charmander, a fiery and strong Pokemon.')
test.assert_equals(PokeScan('Bulbasaur', 100, 'grass').info(), 'Bulbasaur, a grassy and strong Pokemon.')
