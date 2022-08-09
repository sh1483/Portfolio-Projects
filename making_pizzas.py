# Importing pizza.py's functions, and then calling them from this file with,
# Pizza.function_name. File you are importing a function from needs to be in,
# The same directory as the file you are working in. Imports should be written,
# Right after any comments you have at the beginning of the file.

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

# Importing just a specific function form pizza.py.
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'pineapple', 'ham')

# Using as to Give a Function an Alias. Useful if there is a long name or the same,
# Name somewhere in the current file. Seen as:
# "From module_name import function_name as fn".
from pizza import make_pizza as mp

mp(24, 'hamburger')
mp(8, 'cheese')

# Using as to Give a Module an Alias. Seen as "import module_name as mn".
import pizza as p

p.make_pizza(12, 'spinach', 'tomato')
p.make_pizza(12, 'sausage')

# Importing All Functions in a Module. Seen as: "from module_name import *",
# It is best practice not to use this method as it can overwrite functions with,
# The same names and mess up your program.
from pizza import *

make_pizza(12, 'banana peppers', 'sausage', 'green peppers')
mp(16, 'pepperoni')
