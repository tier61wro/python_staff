'''
train_date: 12.05.2022
kata link: https://www.codewars.com/kata/588a00ad70720f2cd9000005
points: 6 kyu
type: OOP
-------------
DESCRIPTION:

In this Kata, you have to design a simple routing class for a web framework.

The router should accept bindings for a given url, http method and an action.

Then, when a request with a bound url and method comes in, it should return the result of the action.

Example usage:

router = Router()
router.bind('/hello', 'GET', lambda: 'hello world')

router.runRequest('/hello', 'GET') // returns 'hello world'

When asked for a route that doesn't exist, router should return:

'Error 404: Not Found'

-------------
TRANSLATION:
Вам нужно реализовать простой веб-фреймворк
у него два метода
- bind ставит в соответствие урлу и методу определенный ответ
- runRequest отдает ответ по урлу и запрошенному методу
если запросили что-то чего у нас нет - то возвращаем
Error 404: Not Found
-------------
===TRAINED====

красота
 my_dict['/admin', 'GET'] = 1
 так у нас в качестве ключа будет тапл вида ('/admin', 'GET')
-------------
'''

import codewars_test as test

class Router:
    def __init__(self):
        self.routes = {}

    def bind(self, path, method, func):
        if path not in self.routes:
            self.routes[path] = {}
        self.routes[path][method] = func


    def runRequest(self, path, method):
        resp = self.routes.get(path,{}).get(method, None)
        if not resp:
            return 'Error 404: Not Found'
        else:
            return resp()

# ===TESTS====
test.describe('Should handle GET routes')
router = Router()
router.bind('/hello', 'GET', lambda: 'hello world')
router.bind('/login', 'GET', lambda: 'Please log-in.')

test.assert_equals(router.runRequest('/hello', 'GET'), 'hello world')
test.assert_equals(router.runRequest('/login', 'GET'), 'Please log-in.')
test.describe('Should handle POST routes')

router = Router()
router.bind('/vote', 'POST', lambda: 'Voted.')
router.bind('/comment', 'POST', lambda:  'Comment sent.')

test.assert_equals(router.runRequest('/vote', 'POST'), 'Voted.')
test.assert_equals(router.runRequest('/comment', 'POST'), 'Comment sent.')

test.describe('Should handle mixed routes.')

router = Router()
router.bind('/login', 'GET', lambda: 'Please log-in.')
router.bind('/login', 'POST', lambda: 'Logging-in.')



test.assert_equals(router.runRequest('/login', 'GET'), 'Please log-in.');
test.assert_equals(router.runRequest('/login', 'POST'), 'Logging-in.');

test.describe('Should return 404 for non-existing routes.')

router = Router()
test.assert_equals(router.runRequest('/this-url-does-not-exist', 'GET'), 'Error 404: Not Found');


test.describe('Should modify existing routes')

router = Router()

router.bind('/page', 'GET', lambda: 'First binding.')
router.bind('/page', 'GET', lambda: 'Modified binding.')
test.assert_equals(router.runRequest('/page', 'GET'), 'Modified binding.');
