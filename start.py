import os,sys
import subprocess
from cmd_config import l_init, l_download, l_install

def red_print(text):
    print('\033[5;31m{}\033[0m'.format(text))

def green_print(text):
    print('\033[1;32m{}\033[0m'.format(text))

def init():
    print("开始执行初始化命令>>>>")

    for i, cmd in enumerate(l_init):
        print("开始执行指令:{}".format(cmd))
        p = subprocess.Popen(cmd, shell=True, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
        p.wait()
        if p.returncode != 0:
            red_print("第{}条init指令出错，忽略: {} ".format(i, cmd))
        green_print("指令执行成功: {}".format(cmd))

def download(start, end):
    print("开始执行下载命令")
    for i, cmd in enumerate(l_download[start:end]):
        print("开始执行指令:{}".format(cmd))
        p = subprocess.Popen(cmd, shell=True, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
        p.wait()
        if p.returncode != 0:
            red_print("错误的download指令: {}, 第{}条命令错误".format(cmd, i))
            sys.exit(-1)
        green_print("指令执行成功: {}".format(cmd))



def install(start, end):
    print("开始执行安装命令")
    for i, cmd in enumerate(l_install[start:end]):
        print("开始执行指令:{}".format(cmd))
        p = subprocess.Popen(cmd, shell=True, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
        p.wait()
        if p.returncode != 0:
            red_print("错误的download指令: {}, 第{}条命令错误".format(cmd, i))
            sys.exit(-1)
        green_print("指令执行成功: {}".format(cmd))



if __name__ == "__main__":
    green_print("开始执行")
    if sys.argv[1] == "init":
        init()
    if sys.argv[1] == "install":
        start = 0
        end = len(l_install) - 1
        try:
            if sys.argv[2] is not None:
                arr = sys.argv[2].split(':')
                start = int(arr[0])
                end = int(arr[1])
        except Exception as e:
            pass
        install(start, end)
    if sys.argv[1] == "download":  # 包前不包后
        start = 0
        end = len(l_download) - 1
        try:
            if sys.argv[2] is not None:
                arr = sys.argv[2].split(':')
                start = int(arr[0])
                end = int(arr[1])
        except Exception as e:
            pass
        download(start, end)