#include <Python.h>
#include <unistd.h>
#include <sys/io.h>     /* for ioperm outb and inb*/
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <time.h>

#define BASEPORT 0x378


static PyObject *
parport_open(PyObject *self, PyObject *args) {	
	if(ioperm(BASEPORT,1,1)!=0)     /* set the permissions for '1' byte (second parameter = 1) */
        {
		return NULL;                     
        }
	Py_RETURN_NONE;
}

static PyObject *
parport_close(PyObject *self, PyObject *args) {
        if(ioperm(BASEPORT,1,0)!=0)     /* set the permissions for '1' byte (second parameter = 1) */
        {                               
                return NULL;
        }
        Py_RETURN_NONE;
}


static PyObject *
parport_write(PyObject *self, PyObject *args) {
	int data;
	if (!PyArg_ParseTuple(args, "i", &data))
		return NULL;
	outb(data, BASEPORT);
	Py_RETURN_NONE;
}



static PyObject *
parport_write_frame(PyObject *self, PyObject *args) {
	PyObject *list;
	if (!PyArg_ParseTuple(args, "O", &list))
		return NULL;
}

static PyObject *
parport_write_with_clock(PyObject *self, PyObject *args) {
        int data;
        if (!PyArg_ParseTuple(args, "i", &data))
               return NULL;
        outb(data, BASEPORT);
        //usleep(1);
        outb((data|(1<<3)),BASEPORT);
        //usleep(1);
        Py_RETURN_NONE;
}

static PyMethodDef parportMethods[] = {
    {"open", parport_open, METH_VARARGS, "Set correct permissions for parport with ioperm(2)"},
    {"write", parport_write, METH_VARARGS, "Set correct permissions for parport with ioperm(2)"},
    {"writeWithClock", parport_write_with_clock, METH_VARARGS, "Set correct permissions for parport with ioperm(2)"},
    {"close", parport_close, METH_VARARGS, "Set correct permissions for parport with ioperm(2)"},
    {NULL, NULL, 0, NULL}
};
 
PyMODINIT_FUNC
initparport(void)
{
    (void) Py_InitModule("parport", parportMethods);
}

