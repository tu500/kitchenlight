from distutils.core import setup, Extension
 
module1 = Extension('parport', sources = ['module.c'])
 
setup (name = 'parport',
        version = '1.0',
        description = 'This is a demo package',
        ext_modules = [module1])
