#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
&quot;&quot;&quot;Print the first x elements of a list that are integers.
Args:
my_list (list): The list to print elements from.
x (int): The number of elements of my_list to print.
Returns:
The number of elements printed.
&quot;&quot;&quot;
ret = 0
for i in range(0, x):
try:
print(&quot;{:d}&quot;.format(my_list[i]), end=&quot;&quot;)
ret += 1
except (ValueError, TypeError):
continue
print(&quot;&quot;)
return (ret)
