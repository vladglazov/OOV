def FindMax(arr, x_arr=[], result=[]):
    x_arr = list(set(map(lambda x : x[0], arr)))
    result = sorted([max(filter(lambda x : i in x, arr)) for i in x_arr])
    return [(i,len(i)) for i in result]
 
print(FindMax(["xxx", "cc", "v", "iiiii", "tttttt", "jjjjjjjjj", "uuuu"]))
