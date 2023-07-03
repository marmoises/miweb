from itertools import count

iterator_infinity = count(1)
getted_value = None

for num in range(30):
  value_getted = next(iterator_infinity)
  print(f'Valor: {value_getted}')
