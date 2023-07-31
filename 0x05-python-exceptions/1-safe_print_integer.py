#!/usr/bin/python3

def safe_print_integer(value):
&quot;&quot;&quot;Print an integer with &quot;{:d}&quot;.format().
Args:
value (int): The integer to print.
Returns:
If a TypeError or ValueError occurs - False.
Otherwise - True.
&quot;&quot;&quot;
try:
print(&quot;{:d}&quot;.format(value))

return (True)
except (TypeError, ValueError):
return (False)
