# Elaine Gonzalez

# This_integration_project_will_showcase_all_that_I_have_learned_in_this_Spring_semester_of_COP1500
# The_main_sources_I_used_were_W3schools, Think Python 2e and HackerRank.
# I was_aided_by_Professor_Vanselow_and_Rachel_Matthews_"."


def main():
    your_name = input("enter your name ")

    print("Welcome" + " " + your_name + "," + " " "to my Integration project.")
    print("This program will showcase all i have learned from my COP1500 class, HackerRank, and POGILS 1-15.")
    print()
    print(int("w = 2.01"))
    print("x = 3")
    print("y = 2")
    w = 2.0
    x = 3
    y = 2
    print("The w and y values might look similar but they are very different.")
    print("They have different names and are different class types.")
    print("The w value is a float, meaning it has a decimal component.")
    print("The y value is an integer, meaning only the number.")
    print()
    print()
    print("These next 50 or so lines are examples of numeric operators.")
    print("They tell the computer to do simple math calculations.")
    print()
    print("This operator is called an exponentiation, it raises the x=3 to the y=2")
    print("x ** y")
    # Line above is the formula.
    print(x ** y)
    # Line above is the calculation that the operator produces.
    print("This operator is called multiplication, it multiplies the x and y together.")
    print("x * y")
    # Line above is the formula"
    print(x * y)
    # Line above is the calculation.
    print("This operator is called division, it divides the x by y.")
    print("x / y")
    # line above is the formula.
    print(x / y)
    # ine above is the calculation that the operator produces.
    print("This operator is called modulus.")
    print("it produces the remainder of the 3 by 2, remainder is 1.")
    print("x % y")
    # line above is the formula.
    print(x % y)
    # line above is the calculation that the operator produces.
    print("This operator is called floor division, it rounds down. ")
    print("The 1.5 is rounded down to 1")
    print("x // y")
    # Line above is the formula.
    print(x // y)
    # line above is the calculation.
    print("This operator is called addition, it adds the x=3 and y=2 together")
    print("x + y")
    # Line above is the formula
    print(x + y)
    # Line above is calculation
    print("This operator is called subtraction, it subtracts y from x")
    print("x - y")
    # Line above is the formula
    print(x - y)
    # line above is the calculation
    print()
    print("These next few lines are examples of string operators.")
    print()
    print("'Computers' * 10")
    print("Computers" * 10)
    print("The setup above includes a multiplication operator with a string.")
    print("This will output the string 10 times.")
    print()
    print("a = 'Hello'")
    print("b = 'world!'")
    print("c = a + ' ' + b")
    a = "hello"
    b = "world"
    c = a + " " + b
    print(c)
    print("The setup above includes a concatenate=+.")
    print("it combines two strings or words within '' using a + ")
    print('hello ', ' world', sep=' ')
    print("The above line includes a separation parameter, sep")
    print()
    print()
    print("This next section is composed of shortcut operators.")
    print()
    print("This is the addition operator, it is the same as writing x=x+5")
    print("x += 5")
    number = 1
    number += 5
    print(number)
    print("This calculation can be done with any of the numeric operators.")
    print()
    print()
    print("conditionals are similar to true and false questions.")
    print("All conditions have to be correct to get the answer you seek.")
    print()
    print("The examples below show If, If-else, If-elif, and If-elif-else statements.")
    print("They are also known as conditional statements.")
    net_worth = int(input("Enter a large amount: "))
    if net_worth >= 1000000:
        print("You're are a millionaire or richer")
    else:
        print("You're not a millionaire or rich")
    print()
    print("This next example is of a conditional statement")
    print()
    grade = int(input("Enter your grade: "))
    if grade >= 90:
        print("You have earned an A")
    elif grade >= 80:
        print("you have earned a B")
    elif grade >= 70:
        print("you have earned a C")
    else:
        print("You have not passed the class")
    print()
    print()
    print("These next examples are relational operators.")
    print("They output a true or false depending on whether")
    print("the statement is true or not.")
    print()
    x = 1
    y = 2
    print(x == x)
    print("The example above is the equal operator. which is the same as 1=1.")
    print(x != y)
    print("the example above is the not equal to operator.")
    print(y > x)
    print(x > y)
    print("The examples above are the greater-than operator,")
    print("same as 2 > 1 and 1 > 2. one is true and the other false.")
    print()
    print()
    print("These next few examples are booleans.")
    print("Booleans are similar to conditionals ")
    print("but they are more restrictive, using AND, OR, and NOT.")
    print()
    a = 5
    b = 10
    c = 15
    if a < b < c:
        print("True, 5 < 10 and 10 < 15")
    print("The examples above is an AND Boolean ")
    print()
    if a < b or a < c:
        print("True, 5 < 10 or 5 < 15.")
    print("the example above is an OR Boolean.")
    print()
    print(not (a > b and a > c))
    print("true, 5 is not > 10 and 5 is not > 15.")
    print("The example above is a NOT Boolean.")
    print()
    print()
    print("The next set of examples are standard iterative structures.")
    print("They include WHILE, FOR, RANGE(), and IN.")
    print()
    print("This next examples is a while loop.")
    print()
    print("This program prints a person's name 1 time on 5 lines.")
    name = input("Enter your name: ")
    x = 0
    while x < 5:
        print(name)
        x = x + 1
    print()
    print("This next example is a FOR loop.")
    print()
    desserts = ["cakes", "cookies", "ice cream", "donuts"]
    for D in desserts:
        print(D)
    print()
    print("This next examples is a RANGE structure.")
    print()
    for T in range(10):
        print(T)
    else:
        print("You have successfully counted from 0 to 9 or 10 numbers")
    print()
    print("This next example is of an IN structure.")
    print()
    print("cook" in "chocolate chip cookies")
    print()
    print("This is my example of a function that accepts parameters.")
    print()

    def salutation(word):
        print(word)

    print()
    salutation("goodbye")
    print()
    print()
    print("Thank you for allowing me to show you what I have learned so far", end='.')


main()
