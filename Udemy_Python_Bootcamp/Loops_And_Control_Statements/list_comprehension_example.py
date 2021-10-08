# list comprehension -  creating a list out of a string
x = []
for i in "Hello World":
    x.append(i)
print(x)


# list comprehension - efficient way : saving memory
x_list = [letter for letter in "Mithi"]
print(x_list)

# list comprehension using if statement
num_even_list = [num for num in range(0,10) if num%2 == 0]
print(num_even_list)

# convert celcius to farenheit
celcius = [10,20, 30, 40.5]
farenheit = [((9/5)*cel+32) for cel in celcius]
print(farenheit)