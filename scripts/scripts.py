import platform
import os
import random

def is_admin():
    if platform.system() == "Windows":
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        return os.geteuid() == 0

def generate_mac(): # ty ChatGPT for this
    # 6 bytes
    mac = [0x00] * 6

    # premier byte: unicast + locally administered
    mac[0] = (random.randint(0x00, 0xFF) & 0xFE) | 0x02

    # reste random
    for i in range(1, 6):
        mac[i] = random.randint(0x00, 0xFF)

    return ":".join(f"{b:02x}" for b in mac)