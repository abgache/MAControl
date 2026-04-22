from colorama import init, Fore, Style
import subprocess
import re
import os
import platform

class mac():
    def __init__(self, interface="wlan0"):
        self.interface=interface
        self.os = platform.system()
        self.base_mac = None
        self.spoofed_mac = None
        self.spoofed = False # Mac spoofing status

    def __str__(self): # renvoie l'adresse mac actuelle
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

    def spoof(self, new_mac, interface=None):
        if interface == None:
            interface = self.interface
        new_mac = new_mac.replace('-', ':')
        print(f"{Fore.YELLOW}[*]{Style.RESET_ALL} Attempting to change MAC address to {new_mac}")
        try:
            if self.os == "Windows":
                new_mac_clean = new_mac.replace(':', '')
                print(f"{Fore.RED}[-]{Style.RESET_ALL} Windows is still not supported yet.")
                exit(0)
            else:
                subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
                subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac], check=True)
                subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} MAC address changed.")
            self.spoofed = True
        except Exception as e:
            self.spoofed = False
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Spoof failed : {e}")
            print(f"{Fore.CYAN}[/]{Style.RESET_ALL} Actual MAC adress : {self.get_current_mac()}")
            exit(2)