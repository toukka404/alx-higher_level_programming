#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
&quot;&quot;&quot;Prints an integer with &quot;{:d}&quot;.format().
If a ValueError message is caught, a corresponding
message is printed to standard error.
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
print(&quot;Exception: {}&quot;.format(sys.exc_info()[1]), file=sys.stderr)
return (False)
