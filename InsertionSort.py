def insertion_sort(alist):
  n = len(alist)
  for i in range(1, n):
    chave = alist[i]
    j = i - 1
    while j >= 0 and alist[j] > chave:
      alist[j+1] = alist[j]
      j = j - 1
      alist[j+1] = chave
  
n = [31, 7, 23, 1, 19, 5, 17, 11, 3, 25, 15, 9, 21,  27, 13, 29]

if _name_ == "_main_":
  alist = n
  insertion_sort(alist)
  print("\n Ordenado: ")
  print(alist)
