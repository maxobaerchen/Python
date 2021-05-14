# Python keywords

# import a module
import numpy

x = 42  # assigning a value to a variable; Python recognizes the type (int)
y = 2

# basic arithmetic operations
a = 2 + 2  # adding
b = 2 - 2  # subtracting
c = 3 * 2  # multiplying
d = 6 / 2  # dividing
e = 2 ** 4  # takes the 4th power
f = 16 ** (1 / 4)  # takes the 4th root
f_pow = pow(2, 4)  # raises 2 to the 4th power
g = 9 % 2  # Modulo divisions
h = 9 // 2  # Floor division

# increment operators
x += 1  # adds 1 to x
x -= 1  # subtracts 1 from x
x *= 2  # multiplies x by 2
x /= 2  # divides x by 2
x **= 2  # takes x to the 2nd power
x **= 1 / 2  # takes the square root from x
x %= 3  # assigns x the modulo(3) of x
x //= 3  # assigns x the floor division by 3 of x

# comparison operators
i = 2 < 2  # checks if 2 is smaller than 2 and assigns a boolean (True/False)
j = 3 > 2  # checks if 3 is greater than 2
k = 2 <= 2  # checks if 2 is smaller or equal to 2
m = 2 >= 1  # checks if 2 is greater of equal to 1
n = 3 == 1  # checks if 3 equals 1
o = 3 != 1  # checks if 3 does not equal 1

# print statement
print('string')  # prints a string
print(2)  # prints an integer
print('What\'s up?')  # print a  special character, which would otherwise cause problems
print('New\nline')  # print a new line
print(r'Raw text; \n doesn\'t work')  # prints a raw string

# lists
my_list = [0, 1, 2, 3]  # creating a list
my_list2 = ['string1', 'string2']
my_list += [4, 5, 6]  # appends a list to my_list
my_list.append(7)  # appends a number to my_list
two_times_three = my_list[3] * my_list[4]  # multiplies to numbers from the list
summed_list = [my_list + my_list2]  # creates a list from two lists

# different operations
pi_rounded = round(pi, 4)  # rounds pi to 4 digits
absolute_value = abs(-3)  # takes the absolute value of -3
true = bool(1)  # converts variables to bool
false = bool(0)  # empty variables are false

# if-statement
if true:  # equivalent to 'if true == True:'
    print('True')
else:
    print('Unnecessary')

# while-loop
while y < 11:
    y += 1
print('Done')
print('y equals' + str(y))

# for-loop
for i in my_list:
    print(i)

# range-function
for i in range(1, 10, 2):  # counts from 1 to 9 in steps of 2
    print(i)

# break and continue
for i in range(100):
    if i % 2 == 1:  # if the number is odd
        continue  # go to the next number
    elif i == 42:  # if the number equals 42
        break  # leave loop
    else:
        print(f'The number({i}) is even')


# function
def prime_check(check_num):
    if check_num < 2:
        return False
    for pot_div in range(2, int(pow(check_num, 1 / 2))):
        if check_num % pot_div != 0:
            continue
        return False
    return True


prime = prime_check(57)
print(str(prime))


# recursive function
def fib(place=10):  # default argument is 10, has to be the last argument
    if place < 2:
        return place
    return fib(place - 1) + fib(place - 2)


# main
if __name__ == '__main__':
    print(fib())

# read files
bin_file = open('/home/maxo/Storage/Python/venv/text', 'rb')  # open a file in binary mode
append_file = open('text.txt', 'a')  # open a file in append mode
read_file = open('text.txt', 'r')  # open a file in read mode
write_file = open('text', 'w')  # open a file in write mode
file = open('/home/maxo/Storage/Python/venv/text', 'r+', encoding='latin-1')  # open a file in read + write mode
file_string = file  # declaring  a variable to be the string of the file
print(file.read(2))  # prints first two characters; \n counts as a character
print(file.readline())  # prints first line
file = open('/home/maxo/Storage/Python/venv/text', 'r+', encoding='latin-1')
for line in file:  # prints every line in
    print.ln(line)

# write files
file = open('/home/maxo/Storage/Python/venv/text', 'a', encoding='latin-1')
file.write('Zeile vier')
file.close()  # closes the file and waits for related processes to cease
file = open('/home/maxo/Storage/Python/venv/text', 'r', encoding='latin-1')
print(file.read())


# scope of variables
def function():
    nonlocal_string = 'non-local'
    global_string = 'global'

    def local_function():
        local_string = 'local'  # local string; callable in function or layers below
        print(local_string)

    def nonlocal_function():
        nonlocal nonlocal_string  # non-local string; callable like local and also one layer above
        nonlocal_string = 'non-local'
        print(nonlocal_string)

    def global_function():
        global global_string  # global string; callable everywhere
        global_string = 'global'
        print(global_string)

    local_function()
    nonlocal_function()
    global_function()
    string = 'string'
    print(nonlocal_string)
    print(global_string)
    print(string)


# objects
class FirstClass:
    def __init__(self, num=42):     # function that is called when calling the class
        self.num = num

    def add_one(self, number):
        number += 1
        return number


instance = FirstClass()
print(instance.add_one(41))
