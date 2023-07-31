#!/usr/bin/python3
import sys

def safe_function(fct, *args):
&quot;&quot;&quot;Executes a function safely.
Args:
fct: The function to execute.
args: Arguments for fct.

Returns:
If an error occurs - None.
Otherwise - the result of the call to fct.
&quot;&quot;&quot;
try:
result = fct(*args)
return (result)
except:
print(&quot;Exception: {}&quot;.format(sys.exc_info()[1]), file=sys.stderr)
return (None)
