import json
import os
from colorama import init, Fore, Style

class backup():
    def __init__(self, filename="backup.json"):
        self.filename = filename
        self.data = {}
        if not os.path.exists(self.filename):
            print(f"{Fore.YELLOW}[*]{Style.RESET_ALL} No backup file found, creating new one.")
            with open(self.filename, "w") as f:
                json.dump(self.data, f)
        else:
            with open(self.filename, "r") as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    print(f"{Fore.RED}[-]{Style.RESET_ALL} Failed to load backup file, exiting for safety.")
                    exit(3)
                except Exception as e:
                    print(f"{Fore.RED}[-]{Style.RESET_ALL} Error loading backup file: {e}")
                    exit(3)
    
    def __str__(self):
        return self.filename

    def save(self, interface, mac):
        mac = mac.replace("-", ":").replace(" ", "")
        # e.g : {"wlan0": "00:11:22:33:44:55"}
        # Check if the interface is already in the backup, if not add it, if yes update it
        if interface in self.data:
            if self.data[interface] == mac:
                print(f"{Fore.YELLOW}[*]{Style.RESET_ALL} Interface {interface} already in backup with the same MAC.")
                return
            print(f"{Fore.YELLOW}[*]{Style.RESET_ALL} Interface {interface} already in backup, updating MAC address...")
        else:
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Adding interface {interface} to backup.")

        self.data[interface] = mac
        try:            
            with open(self.filename, "w") as f:
                json.dump(self.data, f, indent=4)
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Backup saved successfully.")
        except Exception as e:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Failed to save backup: {e}")
    
    def get(self, interface):
        return self.data.get(interface, None)