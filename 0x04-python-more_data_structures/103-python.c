#include <Python.h>
#include <bytesobject.h>
#include <listobject.h>
#include <object.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - print info for a python list object
 * @p: the python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t alloc = ((PyListObject *)p)->allocated;
	Py_ssize_t i = 0;
	PyObject *tmp = NULL;
	PyTypeObject *elem;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)alloc);
	for (i = 0; i < size; i++)
	{
		tmp = (((PyListObject *)p)->ob_item)[i];
		elem = ((PyObject *)tmp)->ob_type;
		printf("Element %d: %s\n", (int)i, elem->tp_name);
		if (!strcmp(elem->tp_name, "bytes"))
			print_python_bytes(tmp);
	}
}

/**
 * print_python_bytes - print info for a python bytes object
 * @p: the python object
 */
void print_python_bytes(PyObject *p)
{

	Py_ssize_t size = 0;
	Py_ssize_t i = 0;
	char *str = NULL;
	Py_ssize_t maxprint = 10;


	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	if (maxprint > size + 1)
		maxprint = size + 1;

	printf("  size: %d\n", (int)size);
	printf("  trying string: %s\n", str);

	printf("  first %d bytes:", (int)maxprint);
	for (i = 0; i < maxprint; i++)
	{
		printf(" %02x", (unsigned char)(str[i]));
	}
	printf("\n");


}
