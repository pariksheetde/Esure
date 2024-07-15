menu = [['egg', 'bacon'], 
        ['egg', 'sausage', 'bacon'], 
        ['egg', 'spam'], 
        ['egg', 'bacon', 'spam'],
        ['egg', 'bacon', 'sausage','spam'],
        ['spam', 'bacon', 'sausage', 'spam'],
        ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
        ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam']
        ]

# print out the item from each list where there is no 'spam'

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == 'spam':
            del meal[index]
    print(meal)