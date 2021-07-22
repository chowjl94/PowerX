from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
    result = None
    result= list(range(number))
    random.seed(seed)
    random.shuffle(result)
    
    return result

def array_to_str(array):
	a_str = ''
	for item in array:
		a_str = a_str + ',' +str(item)
	a_str = a_str[1:] + '.'
	return a_str

def generate():
	global array
	number = 10
	seed = 200
	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	array = gen_random_int(number,seed)
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	array_str = array_to_str(array)
	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str

def insertion_sort(array):
    #loop from 2nd to last
    for out in range(1,len(array)):
        inn = out
        ## 2nd element , 3rd element ....
        temp= array[inn]

        while inn > 0 and temp < array[inn-1]:
            array[inn]=array[inn-1]
            inn-=1
        array[inn] =temp        
    return array
def sortnumber1():
	new_list = array
	new_sort=insertion_sort(new_list)
	array_str = array_to_str(new_sort)
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers").value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return


	# Your code should start from here
	# store the final string to the variable array_str
	str_list = value.split(',')
	num_list = list(map(int,str_list))
	new_sort = insertion_sort(num_list)
	array_str = str(new_sort)

	document.getElementById("sorted").innerHTML =  array_str



