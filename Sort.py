def sort(array):
  for f in range(len(array), 0, -1):
    ex = False
    for current in range(0,  f - 1):
      if array[current] > array[current + 1]:
        array[current], array[current + 1] = array[current + 1], array [corrent]
        ex = True
        
        if not  ex:
          break
     
array = sorted([8, 2, 4, 7, 3, 9, 1, 6, 5, 10])
sort(array)
print(array)
