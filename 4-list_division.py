#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
&quot;&quot;&quot;Divides two lists element by element.
Args:
my_list_1 (list): The first list.
my_list_2 (list): The second list.
list_length (int): The number of elements to divide.
Returns:
A new list of length list_length containing all the divisions.
&quot;&quot;&quot;
new_list = []
for i in range(0, list_length):
try:
div = my_list_1[i] / my_list_2[i]
except TypeError:
print(&quot;wrong type&quot;)
div = 0
except ZeroDivisionError:
print(&quot;division by 0&quot;)
div = 0
except IndexError:
print(&quot;out of range&quot;)
div = 0
finally:
new_list.append(div)
return (new_list)
