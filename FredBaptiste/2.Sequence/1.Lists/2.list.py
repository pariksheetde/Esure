marks = [10, 20, 30, 40, 50]

print(f'All the elements : {marks[:]}')
print(f'All the elements : {marks}')
print()

grades = [10, 20, 30, 40, 50]
print(f'Top 2 grades : {grades[0:3]}')
print(f'Last 2 grades : {grades[-2:]}')
print()

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f'Every 2nd elements : {lst[2::2]}')
print(f'Every 1st elements : {lst[1::2]}')
print()

map = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f'Backward elements : {map[::-1]}')
print(f'Last 3 backward elements : {map[9:6:-1]}')
print(f'Last 3 backward elements : {map[:6:-1]}')
print()

maps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f'First 5 elements in reverse order : {maps[4::-1]}')
print(f'Print all the elements in reverse order : {maps[::-1]}')
print()