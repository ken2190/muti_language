import os
import subprocess
import sys


def install(file: str, path=sys.path[0], device=None, replace_old=False, allow_test=False):
    shell = 'adb'
    if device is not None:
        shell += ' -s ' + device.serial + ' install '
    else:
        shell = 'adb install '
    if replace_old:
        shell += ' -r '
    if allow_test:
        shell += ' -t '
    shell += path + file
    os.system(shell)
    print("执行了————————————————————————" + shell)


def uninstall(pachage_name, device=None):
    shell = 'adb'
    if device is not None:
        shell += ' -s ' + device.serial + ' uninstall '
    shell += pachage_name
    os.system(shell)
    print("执行了————————————————————————" + shell)


def get_devices_list():
    cmd = "adb devices"
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    pr.wait()
    out = pr.stdout.readlines()
    devices = []
    for i in out[1:-1]:
        # if str(i).__contains__("."):  # 只获取wifi连接的手机
        device = str(i).split("\\")[0].split("'")[-1]
        #     devices.append(device)     只取wifi连接的
        devices.append(device)
    return devices


def connect_devices(ips_):
    # os.system("adb tcpip 5555")
    if isinstance(ips_, (list, tuple)):
        for ip in ips_:
            os.system("adb connect " + ip)
    elif isinstance(ips_, str):
        os.system("adb connect " + ips_)


def disconnect_device(no):
    # no is serial or wlan_ip
    os.system("adb disconnect " + no)
