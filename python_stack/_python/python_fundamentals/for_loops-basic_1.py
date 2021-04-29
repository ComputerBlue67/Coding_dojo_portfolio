
# basic loop
for x in range(0,151,1):
    print(x)
#multiples of five
for x in range(5,1005,1):
    if x % 5 == 0:
        print(x)
#counting the dojo way
def the_dojo_way():
    for x in range(1,101,1):
        if x % 10 == 0:
            print("Coding")
        elif x % 5 == 0:
            print("Coding Dojo")
        else: 
            print(x)
the_dojo_way()
#whoa that suckers huge
def big_number():
    final_sum = 0 
    for x in range (0,500000,1):
        if x % 2 == 1:
            final_sum += x
    print(final_sum)
big_number()

def woah_huge():
    final_sum = 0
# some may feel I'm cheating by not checking for odd values using modulo
# fair point but this is easier and IMO equally valid
    for i in range(1, 500000, 2):
        final_sum += i
    print(final_sum)
woah_huge()

#countdown by fours
for x in range(2018,1,-4):
    if x % 2 == 0:
        print(x)
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum = 2, highNum = 9, and mult = 3, the loop should print 3, 6, 9 (on successive lines)
def flexible_counter(low_num, high_num, mult):
    for i in range(low_num, high_num + 1):
        if i % mult == 0:
            print(i)

flexible_counter(2, 9, 3)