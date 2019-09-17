#include <Python.h>
#include <listobject.h>
#include <object.h>


/**
 * print_python_list_info - function description
 * @p: parameter description
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t alloc = ((PyListObject *)p)->allocated;
	Py_ssize_t i = 0;
	PyObject *tmp = NULL;
	PyTypeObject *elem;

	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)alloc);
	for (i = 0; i < size; i++)
	{
		tmp = PyList_GetItem(p, i);
		elem = Py_TYPE(tmp);
		printf("Element %d: %s\n", (int)i, elem->tp_name);
	}
}
