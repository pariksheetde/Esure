parrot = "Norwegian Blue"
print(f'Length of parrot: {len(parrot)}')
print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(f'Printing the alphabets in reverse order: {alphabet[::-1]}')
print(f'Printing the alphabets in reverse order: {alphabet[:-27:-1]}')
print(f'Printing the alphabets in reverse order: {alphabet[27::-1]}')

print()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(f'Generating "qpo": {alphabet[-10:13:-1]}')
print(f'Generating "edcba": {alphabet[4::-1]}')
print(f'Generating "stuvwxyz": {alphabet[-8:][::-1]}')

print()

print("Hello " * 5)
print("Hello " * (2 + 1))
print("Hello " * (2 + 1), "7")

print()

print("PI is approximately: {0:5f}".format(22/7))
print("PI is approximately: {0:10f}".format(22/7))
print("PI is approximately: {0:15f}".format(22/7))
print("PI is approximately: {0:20f}".format(22/7))
print("PI is approximately: {0:25f}".format(22/7))

print()