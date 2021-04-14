def Sum(list, s=0):
    for i in list:
        s += i
    return s

arr1 = [1, 2, 3, 4, 5]     # 15
arr2 = [5, -3, 4, -10]    # -4
arr3 = []                 # 0
print(Sum(arr1))
print(Sum(arr2))
print(Sum(arr3))
