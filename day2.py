# Exercise 1: Write a program that asks the user for a number and prints whether it’s even or odd.

num = int(input("Give me a number: "))

if num % 2 == 0:
    print(num, "is even!")
else:
    print(num, "is odd!")


# Exercise 2: Write a program that prints numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)


#Exercise 3: Write a program that keeps asking for user input until they type "exit"

print("Please type 'exit' when done")
name = input("What is your name?")

while name != "exit":
    print("Hi" + name)
    name = input("What is your name?")
else:
    quit

# Exercise 4: Bonus: Write a simple password checker. If the user enters "secret123", print "Access Granted", otherwise, "Access Denied".

password = input("Type the correct password:")

if password == "secret123":
    print("Access Granted")
else:
    print("Access Denied")



