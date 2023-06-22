from itertools import count

iterator_infinity = count(1)
value_getted = None

for num in range(20):
  value_getted = next(iterator_infinity)
  print(f'Valor: {value_getted}')
