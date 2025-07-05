# Lists - mutable
l = ['a', 'a', 'b']

# Tuples - immutable
t = ('a', 'a', 'b')

# Sets - non-repeatable elements
s = {'a', 'b', 'c'}


print(l[0]) # get the first element in list

l.append('c')
l.remove('c')

s.add('d')
s.remove('d')


# Sets

countries = {'Germany', 'Hungary', 'Montenegro'}
eu_countries = {'Germany', 'Hungary'}

non_eu_countries = countries.difference(eu_countries)
print(non_eu_countries)

all_countries = non_eu_countries.union(eu_countries)
print(all_countries)


euro_countries = {'Germany', 'Austria', 'Italy'}
eu_countries = {'Germany', 'Poland', 'Austria', 'Italy', 'Hungary'}

both = euro_countries.intersection(eu_countries)
print(f'EU countries with euro currency: {both}')


# Task

# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [20, 10, 70]

# Create a tuple, called my_tuple, with a single value in it
my_tuple = (1, )

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}
