def blubblesort(alist):
    n = len(alist)

    for f in range(n-1):
        for i in range(0, n-1-f):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
            else:
              print("Ordem Crescente: ", f + 1,  alist)
            

alist = [8, 2, 5, 9, 3, 7, 10, 1, 4, 6]
blubblesort(alist)
