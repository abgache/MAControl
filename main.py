import re, uuid, argparse

version = "0.0.1"

class mac():
    def __init__(self):
        self.base_mac = None
    
    def get_current_mac(self):
        self.base_mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

def banner():
    pass

def main():
    pass

if __name__ == "__main__":
