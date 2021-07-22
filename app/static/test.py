
def insertion_sort(array):
    #loop from 2nd to last
    for out in range(1,len(array)):
        inn = out
        ## 2nd element , 3rd element ....
        temp= array[inn]
 

        while inn > 0 and temp < array[inn-1]:
            print(array[inn])
            array[inn]=array[inn-1]
            inn-=1
        array[inn] =temp        
    return array
str_list='5,2,3,4,1,2,9,8'
str_list=str_list.split(',')

num_list = list(map(int,str_list))
new_sort=insertion_sort(num_list)
array_str = str(new_sort)

print(array_str)

