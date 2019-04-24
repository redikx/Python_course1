greeting = "Welcome, "
age = 45
name = "Radek"
print(greeting + str(name) + " you have " + str(age) + " age")

# using format
print(greeting + """{0} you have {1} age
it is nice to see you {0}""".format(name, age))

# Format of {a:n}, where n is size of str. <n will do left
for i in range(1,10):
    print('Value {0:1} : squared is {1:4} and cubed is {2:4}'.
          format(i, i ** 2, i ** 3))

# Format of float :12 is size of str, .50 is precision
print(" Pi equals {0:12.50}".format(22/7))

# Slice the string
value = "A:1 B:2 C:3 D:4 E:5 F:6"
# from field 1 to end
print(value[1:])
# from field 1 to 5 without 5
print(value[1:5])
# from field 0 to the end, each 5th
print(value[::5])

