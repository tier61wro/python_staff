def add():
    pass

print(f'Imported from: {__name__}')

#__name__ служебная переменная, изначально: __main__

# Return the dictionary containing the current scope's global variables.
# print(globals())

def main():
    print('main was called')

if __name__ == '__main__':
    print('this code only for direct launch of hello.py')
    main()


