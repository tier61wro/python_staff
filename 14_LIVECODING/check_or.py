with open('file.txt', 'r') as file:
    data = file.read()

# __enter__()
# __exit__()


file = None
try:
    file = open('file.txt', 'r')
    data = file.read()
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors")
finally:
    if file:
        file.close()
