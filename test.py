from start import get_list, exec_cmd
from cmd_config import *

def test_get_list():
    a = [1, 2, 4]
    res1 = get_list(a, None, None)
    print(res1)

    res1 = get_list(a, -1, None)
    print(res1)

    res1 = get_list(a, 0, None)
    print(res1)


# test_get_list()


def test_exec_cmd():
    l = ['a', 'b', 'c', 'd', 'e']
    print(l[2:])
    exec_cmd(li_cmd=l, start=2, end=None, name="test", debug=True)

test_exec_cmd()