#!/bin/python
import argparse
import platform
import os
import random
from colorama import init, Fore, Style, just_fix_windows_console
from scripts.mac import mac as mac_spoofer_class
import scripts.scripts as utilities

version = "1.0.0"

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

    # gerer l'interface
    if not args.interface:
        print(f"{Fore.YELLOW}[*]{Style.RESET_ALL} No interface given, defaulting to {'Wi-Fi 1' if platform.system() == 'Windows' else 'wlan0'}")
        interface = 'Wi-Fi 1' if platform.system() == 'Windows' else "wlan0"
    else:
        interface = str(args.interface)
    
    # init la classe
    mac_spoofer = mac_spoofer_class(interface=interface)
    mac_spoofer.get_current_mac()

    print(f"{Fore.CYAN}[/]{Style.RESET_ALL} Actual MAC adress : {mac_spoofer}")

    # warn parce trop la flemme de rendre windows stable
    if platform.system() == "Windows":
        print(f"\033[38;5;208m[!]{Style.RESET_ALL} Windows is not fully supported, you may encounter problems.")
    
    # check si le programme est launch en tant qu'admin
    if not utilities.is_admin() and not args.no_root:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} Please run the program with {'admin privileges' if platform.system() == 'Windows' else 'root privileges'}.")
        exit(1)

    if not args.mac: # utilities.generate_mac
        mac2spoof = utilities.generate_mac()
        print(f"{Fore.YELLOW}[*]{Style.RESET_ALL} No MAC adress given, spoofing to random mac.")
    else:
        mac2spoof = str(args.mac)
    
    print(f"{Fore.CYAN}[/]{Style.RESET_ALL} New mac adress : {mac2spoof}")

    mac_spoofer.spoof(mac2spoof)

if __name__ == "__main__":
    if platform.system() == "Windows":
        just_fix_windows_console()
    banner()
    main()
