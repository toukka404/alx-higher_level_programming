#!/usr/bin/python3

def magic_calculation(a, b):
result = 0
for i in range(1, 3):
try:
if i &gt; a:
raise Exception(&#39;Too far&#39;)
else:
result += a ** b / i
except:
result = b + a
break
return (result)
