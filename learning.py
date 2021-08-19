# Python keywords

# import a module
import time

x = 42  # assigning a value to a variable; Python recognizes the type (int)
y = 2

# arithmetic operations
a = 2 + 2  # adding
b = 2 - 2  # subtracting
c = 3 * 2  # multiplying
d = 6 / 2  # dividing
e = 2 ** 4  # takes the 4th power
f = 16 ** (1 / 4)  # takes the 4th root
f_pow = pow(2, 4)  # raises 2 to the 4th power
g = 9 % 2  # Modulo divisions
h = 9 // 2  # Floor division
pi_rounded = round(pi, 4)  # rounds pi to 4 digits
absolute_value = abs(-3)  # takes the absolute value of -3

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
print('string')  # prints a string (print() converts input into before outputting it)
print(2)  # prints an integer
print('What\'s up?')  # print a  special character, which would otherwise cause problems
print('New\nline')  # print a new line
print(r'Raw text; \n doesn\'t work')  # prints a raw string

# strings
string1 = 'example string'  # assigns string to variable string; strings are immutable
string2 = string.replace('e', 'a')  # replaces every e in string with an a and stores it in string2
string3 = string + string2  # appends string2 to string1 and stores it in string3
string4 = 3 * string3  # strings three times string3 together
string5 = f'{string}{string2}'  # appends string2 to string1 and stores it in string5
length_string1 = len(string1)  # stores the length of string1 in length_string1
true_true = string1 == 'example string'  # checks if string1 is 'example string' and stores the boolean value in true
escape_characters = '\n (new line/ENTER), \t horizontal tab/TAB, ' \
                    '\\ masking character to indicates that the following character is no special character'
raw_string = r'\n and other escape characters are ignored'

name = 'Max Mustermann'
name_upper = name.upper()  # capitalizes every character
name_lower = name.lower()  # lowercases every character
name_title = name.title()  # capitalizes the first character of every word
name_capitalize = name.capitalize()  # capitalizes the first character of the string
start_Max = name.startswith('Max')  # checks if name starts with 'Max'
end_Mustermann = name.endswith('Mustermann')  # checks if name ends with 'Mustermann'
start_Karl = name.startswith(('Karl', 'Max'))  # checks if name starts with 'Karl' or 'Max' (args: str or tuple)
print(start_Karl)
name_list = ('Karl', 'Max')
start_Karl_or_Max = name.startswith(name_list)
print(name_list)
print(start_Karl_or_Max)

whitespaces = '\n             whitespace  whitespace\t  whitespace                             '
strip_whitespace = whitespaces.strip()  # removes \t, \n and whitespaces between the string and each quote
lstrip_whitespace = whitespaces.lstrip()  # removes \t, \n and whitespaces between the string and first quote
rstrip_whitespace = whitespaces.rstrip()  # removes \t, \n and whitespaces between the string and last quote
lines = 'first line\nsecond line\nthird line'
split_by_lines = lines.splitlines()  # creates a list with every line as a single element
characters = 'This is some     text: it\'s simple, easy to understand, and not redundant'
split_by_character = characters.split(',')  # creates a list with every string between two commas as a single element
split_by_whitespace = characters.split()  # without argument: every string between whitespaces, except for whitespaces
joined_by_whitespace = ' '.join(split_by_whitespace)  # creates string with whitespace between each element
text = 'This is some random text'
text.count('i')  # counts the number of occurrences of a string in another string
text.find('rand')   # returns the position of the string in another string
text.find('random')     # if a string contains more than one character, it returns the position of the first character
text.find('not included')   # if the function return -1, the string is not included
whitespace = ' \n\t'                    # checks if whitespace consists of anything else than
whitespace_true = whitespace.isspace()  # whitespaces/enters/tabs; returns bool
alphabet = 'abcdefghijklmnopqrstuvwxyz'  # checks if alphabet consists of anything else than
alphabet_true = alphabet.isalpha()       # the characters in the alphabet; returns bool
digit = '11'
digit_true = digit.isdigit()

data = 'Data'
str.encode(data)  # converts data to bytes
byte_data = data.encode()  # converts data to bytes
type(byte_data)  # reads type of byte_data
bytes.decode(byte_data)  # converts byte_data to string
string_data = byte_data.decode()  # converts byte_data to string


# lists
my_list = [0, 1, 2, 3]  # creating a list; lists are mutable
my_list2 = ['string1', 'string2']
my_list += [4, 5, 6]  # appends a list to my_list
my_list.append(7)  # appends a number to my_list
print(my_list[0:3])  # prints the first three elements of list 'my_list'
two_times_three = my_list[3] * my_list[4]  # multiplies to numbers from the list
summed_list = my_list + my_list2  # creates a list from two lists/adds them together
print(summed_list)  # -> one big list
summed_list.append(my_list)  # inserts one list into the other
print(summed_list)  # -> one big list and one smaller inside
summed_list = [my_list, my_list2]  # creates a list with both lists inside
print(summed_list)  # -> two lists inside the big list
print(summed_list[0][0])
print(summed_list[3:])  # outputs every element in summed_list starting from (and including) the fourth element
summed_list.sort()  # sorts summed_list
one_to_hundred = list(range(0, 100))    # creates a list from 0 to (and including) 99
one_to_hundred.clear()   # removes all items
one_to_hundred = list(range(0, 100))
print(one_to_hundred.pop(0))    # returns an element by index and returns its value
one_to_hundred.remove(20)    # removes an element by value
del one_to_hundred[20:30]  # removes an element/elements by index


# different operations
true = bool(1)  # converts variables to bool
false = bool(0)  # empty variables are false


# data types and type casting
int()
float()
str()
bool()
list()

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
for i in range(1, 10, 2):  # creates a list from 1 to 9 in steps of 2
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
file_string = file  # assigning the file to a variable
print(file.read(2))  # reads and prints first two characters; \n counts as a character
print(file.readline())  # reads and prints first line
file = open('/home/maxo/Storage/Python/venv/text', 'r+', encoding='latin-1')
for line in file:  # prints every line in
    print(line)

# write files
file = open('/home/maxo/Storage/Python/venv/text', 'a', encoding='latin-1')
file.write('Zeile vier')
file.close()  # closes the file and waits for related processes to cease
file = open('/home/maxo/Storage/Python/venv/text', 'r', encoding='latin-1')
print(file.read())
with open('/home/maxo/Storage/Python/venv/text', 'r', encoding='latin-1') as file:
    for line in file:
        print(line)


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
    def __init__(self, num=42):  # function that is called when calling the class
        self.num = num
        self.list = []

    def add_one(self, number):
        number += 1
        self.list.append(42)
        return number


instance = FirstClass()
print(instance.add_one(41))


# inheritance
class Creature:
    ears = 2

    def __init__(self):
        self.vertebrate_class = 'mammal'

    def ears(self):
        self.ears += 1


class Pet:
    paws = 4


class Dog(Pet):  # class Dog inherits from class pet and therefore from Creature
    eyes = 2
    ears = 42  # overwrites variable/attribute from Creature
    legs = 4
    name = 'Dog'

    def __init__(self, new_class):
        Creature.__init__()
        self.vertebrate_class = new_class

    def ears(self):  # overwrites method ears with new method
        self.ears = dog_ears
        Creature.ears = creature_ears


Creature = Creature()
Dog = Dog('animal')
print(Creature.vertebrate_class)
print(Dog.vertebrate_class)


# exceptions
class Ex(Exception):
    pass


try:
    raise Ex()
except Ex:
    print('Exception')
except ZeroDivisionError:
    print('Division by zero')
except Exception:
    print('Some exception')

file = open('/home/maxo/Storage/Python/venv/text', 'r', encoding='latin-1')
text = file.read()
print(text)
for character in text:
    time.sleep(0.25)
    print(character, end='')

# tkinter
import tkinter

root = Tk()  # creating an instance


def respond_to_click():
    response_label = Label(root, text='You successfully clicked the button!')
    response_label.pack()


first_label = Label(root, text='Window title')  # creating a label
# creating a button
first_button = Button(root, text='Click me!', padx=50, pady=50, command=respond_to_click, bg='white', fg='black')

first_label.pack()  # displaying the label
first_button.pack()  # displaying the button

root.mainloop()  # looping through the process, otherwise, there would be just one frame

# threading
import threading
import time


class myFred(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.iD = thread_id
        self.name = name

    def run(self):  # the function run() will be run on separate cores by the start() function
        lock_me.acquire()   # stops every other thread/locks them
        print('Starting Thread ' + str(self.iD))
        time.sleep(2)
        lock_me.release()   # continues every other thread/releases them
        print('Terminating Thread ' + str(self.iD))


lock_me = threading.Lock()  # creates an instance of class Lock()
thread1 = myFred(0)     # creates an instance of myFred() running on a separate core
thread2 = myFred(1)

thread1.start()     # starts Thread 1
thread2.start()
thread1.join()  # waits for Thread 1 to finish its process
thread2.join()
if thread1.isAlive():   # checks if Thread 1 is running
    print('Impossible')

print('Done')


