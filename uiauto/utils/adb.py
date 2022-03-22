import os
import sys


def install(file: str, path=sys.path[0], device=None, replace_old=False, allow_test=False):
    shell = 'adb install '
    if device is not None:
        shell += ' -s ' + device
    if replace_old:
        shell += ' -r '
    if allow_test:
        shell += ' -t '
    shell += path + file
    os.system(shell)
    print("执行了————————————————————————" + shell)


def uninstall(pachage_name, deivce=None):
    shell = 'adb uninstall '
    if deivce is not None:
        shell += ' -s ' + deivce
    shell += pachage_name
    os.system(shell)
    print("执行了————————————————————————" + shell)
