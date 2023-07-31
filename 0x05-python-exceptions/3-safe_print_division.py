#!/usr/bin/python3
def safe_print_division(a, b):
&quot;&quot;&quot;Returns the division of a by b.&quot;&quot;&quot;
try:
div = a / b
except (TypeError, ZeroDivisionError):
div = None
finally:
print(&quot;Inside result: {}&quot;.format(div))
return (div)
