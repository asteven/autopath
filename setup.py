from distutils.core import setup

from autopath import __version__
setup(
    name=autopath.__name__,
    version=__version__,
    author='Steven Armstrong',
    author_email='steven-%s@armstrong.cc' % autopath.__name__,
    url='http://github.com/ungleich/%s/' % autopath.__name__,
    description='Simple PYTHONPATH handling',
    py_modules=[autopath.__name__],
)

