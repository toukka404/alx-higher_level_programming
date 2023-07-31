/*
* File: 103-python.c
* Auth: Type Your Name Here
*/
#include &lt;Python.h&gt;
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
* print_python_list - Prints basic info about Python lists.
* @p: A PyObject list object.

*/
void print_python_list(PyObject *p)
{
Py_ssize_t size, alloc, i;
const char *type;
PyListObject *list = (PyListObject *)p;
PyVarObject *var = (PyVarObject *)p;
size = var-&gt;ob_size;
alloc = list-&gt;allocated;
fflush(stdout);
printf(&quot;[*] Python list info\n&quot;);
if (strcmp(p-&gt;ob_type-&gt;tp_name, &quot;list&quot;) != 0)
{
printf(&quot; [ERROR] Invalid List Object\n&quot;);
return;
}
printf(&quot;[*] Size of the Python List = %ld\n&quot;, size);
printf(&quot;[*] Allocated = %ld\n&quot;, alloc);
for (i = 0; i &lt; size; i++)
{
type = list-&gt;ob_item[i]-&gt;ob_type-&gt;tp_name;
printf(&quot;Element %ld: %s\n&quot;, i, type);
if (strcmp(type, &quot;bytes&quot;) == 0)
print_python_bytes(list-&gt;ob_item[i]);
else if (strcmp(type, &quot;float&quot;) == 0)
print_python_float(list-&gt;ob_item[i]);

}
}
/**
* print_python_bytes - Prints basic info about Python byte objects.
* @p: A PyObject byte object.
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
PyBytesObject *bytes = (PyBytesObject *)p;
fflush(stdout);
printf(&quot;[.] bytes object info\n&quot;);
if (strcmp(p-&gt;ob_type-&gt;tp_name, &quot;bytes&quot;) != 0)
{

printf(&quot; [ERROR] Invalid Bytes Object\n&quot;);
return;
}
printf(&quot; size: %ld\n&quot;, ((PyVarObject *)p)-&gt;ob_size);
printf(&quot; trying string: %s\n&quot;, bytes-&gt;ob_sval);
if (((PyVarObject *)p)-&gt;ob_size &gt;= 10)
size = 10;
else
size = ((PyVarObject *)p)-&gt;ob_size + 1;
printf(&quot; first %ld bytes: &quot;, size);
for (i = 0; i &lt; size; i++)
{
printf(&quot;%02hhx&quot;, bytes-&gt;ob_sval[i]);
if (i == (size - 1))
printf(&quot;\n&quot;);
else
printf(&quot; &quot;);

}
}
/**
* print_python_float - Prints basic info about Python float objects.
* @p: A PyObject float object.
*/
void print_python_float(PyObject *p)
{
char *buffer = NULL;
PyFloatObject *float_obj = (PyFloatObject *)p;
fflush(stdout);
printf(&quot;[.] float object info\n&quot;);
if (strcmp(p-&gt;ob_type-&gt;tp_name, &quot;float&quot;) != 0)
{
printf(&quot; [ERROR] Invalid Float Object\n&quot;);
return;
}
buffer = PyOS_double_to_string(float_obj-&gt;ob_fval, &#39;r&#39;, 0,
Py_DTSF_ADD_DOT_0, NULL);

printf(&quot; value: %s\n&quot;, buffer);
PyMem_Free(buffer);
}
