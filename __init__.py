import os
import sys


def extend_path(lib_dir):
    '''Extend the path to include python packages in the lib dir'''
    packages = []
    for path, dirs, files in os.walk(lib_dir, topdown=True):
        if '__init__.py' in files:
            packages.append(os.path.split(path)[0])
            del dirs[:]
    # reverse the list as it's reversed back again below when extending sys.path
    packages.reverse()

    # reverse so we can add to the end instead of front which is much more efficient
    sys.path.reverse()
    # extend the path with packages found in lib_dir
    # but preserve the current working directory as the first path entry
    cwd_path = sys.path.pop()
    sys.path.extend([p for p in packages if p not in sys.path])
    sys.path.append(cwd_path)
    # restore previous order
    sys.path.reverse()
    #print 'sys.path:', sys.path

