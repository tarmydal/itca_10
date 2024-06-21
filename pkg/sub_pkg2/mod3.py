import os
import sys


def baz():
    print('[mod3] baz()')

class Baz:
    pass

# print(os.path.abspath('..'))
# print(sys.path)


if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath('..')))
    # print(sys.path)
    from pkg import sub_pkg1
    from pkg.sub_pkg1.mod1 import foo
else:
    from .. import sub_pkg1
    from ..sub_pkg1.mod1 import foo


if __name__ == '__main__':
    print(sub_pkg1)
    foo()