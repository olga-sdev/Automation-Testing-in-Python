# Exercise Variables

# Create two variables, var1 and var2, both with the same value.
var1 = 'var'
var2 = 'var'

# Create two variables, num1 and num2, which multiply together to give 16.
num1 = 2
num2 = 8


# Formatting options
city = 'Warsaw'
time_arrival = '16:50'
statement = 'Arrival time to {} is {}'
sentence = statement.format(city, time_arrival)
print(sentence)


# Data input
data = input('Enter number: ')
print(int(data))


# Creating a tuple:
x = (100, 100)
y = 100, 100

print(x)  # (100, 100)
print(y)  # (100, 100)

h, j = 100, 100
print(h)  # 100
print(j)  # 100

my_tuple = 10, 10
n, m = my_tuple

print(n)  # 10
print(m)  # 10


# Destructing variables
countries = [('Poland', 'PLN'), ('Slovakia', 'EUR')]

for country, currency in countries:
    print(f'The currency of {country} is {currency}')


country = ('Poland', 'PLN', 'Warsaw')

name, _, capital = country  # _ not important variable

print(name, capital)


# head and tail collection
head, *tail = ['a', 3, 7, 'z']
print(head)  # first element in a list: a
print(*tail)  # rest of elements in a list: 3 7 z

# in case of:
*head, tail = ['a', 3, 7, 'z']
print(*head)  # all elements except the last one: a 3 7
print(tail)  # the last element in a list: z
