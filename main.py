#!/bin/python
import argparse
import platform
import subprocess
import re
import os
from colorama import init, Fore, Back, Style

version = "0.0.2"

class mac():
    def __init__(self, interface="wlan0"):
        self.interface=interface
        self.os = platform.system()
        self.base_mac = None
        self.spoofed = False
        self.spoofed_mac = None

    def __str__(self):
        # Check si l'adresse a deja ete spoof
        if not self.spoofed:
            if self.base_mac:
                return str(self.base_mac)
            else:
                print(f"{Fore.RED}[-]{Style.RESET_ALL} Please spoof your mac adress or get it before trying to see it.")
                return ""
        else:
            if self.spoofed_mac:
                return str(self.spoofed_mac)
            else:
                print(f"{Fore.RED}[-]{Style.RESET_ALL} The mac adress has been spoofed but no adress is registered.")
                return ""

    def get_current_mac(self, interface=None):
        if interface == None:
            interface = self.interface
        # jst check l'os pr lancer une commande et parse la commande pr chopper le mac
        try:
            if self.os == "Windows":
                result = subprocess.check_output(f"getmac /v /fo list", shell=True).decode()
                # Parse Windows output to find MAC for interface
                lines = result.split('\n')
                for i, line in enumerate(lines):
                    if interface.lower() in line.lower():
                        # Look for MAC in nearby lines
                        for j in range(i, min(i+10, len(lines))):
                            mac_match = re.search(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", lines[j])
                            if mac_match:
                                self.base_mac = mac_match.group(0).replace("-", ":")
            else:
                result = subprocess.check_output(f"ifconfig {interface}", shell=True).decode()
                mac_search = re.search(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", result)
                if mac_search:
                    self.base_mac = mac_search.group(0).replace("-", ":")
        except Exception as e:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Error getting MAC address: {e}")
            exit(1)
        
        if not self.base_mac:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} No mac adress found for this interface, please check your interface.")
            exit(1)
        return self.base_mac

def is_admin():
    if platform.system() == "Windows":
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:  # Linux / macOS
        return os.geteuid() == 0

def banner():
    global version
    banner="""  __  __          _____            _             _ 
 |  \/  |   /\   / ____|          | |           | |
 | \  / |  /  \ | |     ___  _ __ | |_ _ __ ___ | |
 | |\/| | / /\ \| |    / _ \| '_ \| __| '__/ _ \| |
 | |  | |/ ____ \ |___| (_) | | | | |_| | | (_) | |
 |_|  |_/_/    \_\_____\___/|_| |_|\__|_|  \___/|_|"""
    credit = f"{' ' * 34}By {Fore.BLUE}Abgache{Style.RESET_ALL}\n{' ' * 34}Version: {Fore.GREEN}{version}{Style.RESET_ALL}\n"
    print(banner)
    print(credit)

def main():
    parser = argparse.ArgumentParser(description="MAC Address Spoofer")
    parser.add_argument("-i", "--interface", help="Network interface to modify")
    parser.add_argument("-m", "--mac", help="Specify the new MAC adress (random if not specified)")
    parser.add_argument("--no-root",help=f"Disable the check for {'admin' if platform.system() == 'Windows' else 'root'} privileges",action="store_true")

    args = parser.parse_args()

    if not args.interface:
        if platform.system() == "Windows":
            print(f"{Fore.YELLOW}[*]{Style.RESET_ALL} No interface given defaulting to Wi-Fi 1")
            interface = "Wi-Fi 1"
        else:
            print(f"{Fore.YELLOW}[*]{Style.RESET_ALL} No interface given defaulting to wlan0")
            interface = "wlan0"
    else:
        interface = str(args.interface)
    
    mac_spoofer = mac(interface=interface)
    mac_spoofer.get_current_mac()

    print(f"{Fore.CYAN}[/]{Style.RESET_ALL} Actual MAC adress : {mac_spoofer}")

    if platform.system() == "Windows":
        print(f"\033[38;5;208m[!]{Style.RESET_ALL} Windows is not fully supported, you may encounter problems.")
    
    if not is_admin() and not args.no_root:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} Please run the program with {'admin privileges' if platform.system() == 'Windows' else 'root privileges'}.")
        exit(1)

if __name__ == "__main__":
    banner()
    main()
