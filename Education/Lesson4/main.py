numb = [6,6,6,6,6,6]

half1 = []
half2 = []

length = len(numb)
midpoint = length // 2

if length % 2 == 0:
    half1 = numb[:midpoint]
    half2 = numb[midpoint:]
else:
    mid_element = numb.pop(midpoint)
    half1 = numb[:midpoint]
    half2 = numb[midpoint:]

if sum(half1) == sum(half2):
    print('Это счастливый билет')
else:
    print('Билет фигня')