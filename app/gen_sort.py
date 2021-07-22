import random

def gen_random_int(number, seed):
    result= None
    
    result= list(range(number))
    #mylist=[random.randint(0,(number-1)) for i in range(number)]
    
    random.seed(seed)
    random.shuffle(result)
    return result



# def heapsort(array):
#     n = len(array)
#     build_max_heap(array)
#     end = n - 1
#     while end > 0 :
#         array[0] , array[end] = array[end] , array[0]
#         n -= n - 1
#         max_heapify(array,0,n)
        

#     pass
array = gen_random_int(10,100)

# print(array)
array_str = ''
for item in array:
    
    array_str = array_str + ","+str(item)
array_str = array_str[1:] + "."

print(array_str)

