from distutils.core import setup

from autopath import __version__

name = 'autopath'

setup(
    name=name,
    version=__version__,
    author='Steven Armstrong',
    author_email='steven-%s@armstrong.cc' % name,
    url='http://github.com/asteven/%s/' % name,
    description='Simple PYTHONPATH handling',
    py_modules=[name],
)

