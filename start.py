import os,sys,random
import subprocess
from cmd_config import l_init, l_download, l_install

def red_print(text):
    print('\033[5;31m{}\033[0m'.format(text))

def green_print(text):
    print('\033[1;32m{}\033[0m'.format(text))

def flash_print(text):
    print('\033[5;32m{}\033[0m'.format(text))


def get_list(li, start, end):
    if start is not None and start < 0:
        start = 0

    if end is not None:
        if end > len(li):
            end = len(li)

    if start is None and end is None:
        return li
    if start is None and end is not None:
        return li[:end]
    
    if start is not None and end is None:
        return li[start:]

    if start is not None and end is not None:
        return li[start:end]
    

def exec_cmd(*,li_cmd, start, end, name, debug=False):
    print("开始执行 {} 命令".format(name))
    l = get_list(li_cmd, start, end)

    _start = start
    if _start is None:
        _start = 0

    if debug:
        print('l', l)
        for i, cmd in enumerate(l):
            print(cmd)
            ran = random.randint(0, len(l)-1)
            if i == ran:
                red_print("第 {} 条{}命令错误, {}".format(i+_start, name, cmd))
                sys.exit(-1)
            green_print("命令执行成功: {}".format(cmd))    
        return

    for i, cmd in enumerate(l):
        p = subprocess.Popen(cmd, shell=True, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
        p.wait()
        if p.returncode != 0:
            red_print("第 {} 条{}命令错误, {}".format(i+_start, name, cmd))
            print("解决错误之后从错误命令开始执行： start.py {} {}:".format(name, i+start))
            sys.exit(-1)
        green_print("命令执行成功: {}".format(cmd))


def init(start, end):
    exec_cmd(li_cmd=l_init, start=start, end=end, name="init")

def download(start, end):
    exec_cmd(li_cmd=l_download, start=start, end=end, name="download")

def install(start, end):
   exec_cmd(li_cmd=l_install, start=start, end=end, name="install")


def get_arg()->[]:
    li = [None, None]

    if len(sys.argv)>=3 and sys.argv[2] is not None:
        arr = sys.argv[2].split(':')
        try:
            li[0] = int(arr[0])
            li[1] = int(arr[1])
        except Exception as e:
            pass

    return li

if __name__ == "__main__":
    if len(sys.argv) <=1:
        print("Usage: start.py init/install/download/print [start:end]")
        sys.exit(-1)
    arg = get_arg()
    if sys.argv[1] == "init":   
        init(arg[0], arg[1])

    if sys.argv[1] == "install":
        install(arg[0], arg[1])

    if sys.argv[1] == "download":  # 包前不包后
        download(arg[0], arg[1])

    if sys.argv[1] == "test":
        print(get_list(l_install, arg[0], arg[1]))
        print(len(get_list(l_install, arg[0], arg[1])))

    if sys.argv[1] == "print":
        flash_print("init列表命令：")
        for i, k in enumerate(l_init):
            print("init[{}]: {}".format(i, k))

        flash_print("download列表命令：")
        for i, k in enumerate(l_download):
            print("download[{}]: {}".format(i, k))
        
        flash_print("install列表命令：")
        for i, k in enumerate(l_install):
            print("install[{}]: {}".format(i, k))
        