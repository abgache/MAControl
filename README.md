# MAControl  
## Change your MAC adress in a single command.  

### Version : ``1.0.0`` 

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/) 

# What is it?
It is just a simple MAC adress spoofer made in pyhon.  

# How to use it?  
## Linux:
**Download:**  
```bash  
sudo cd /usr/share  
sudo git clone https://github.com/abgache/macontrol.git  
sudo cd macontrol  
sudo pip install -r requirements.txt  
sudo chmod 555 /usr/share/macontrol/main.py
sudo cp /usr/share/macontrol/bin/macontrol /bin/macontrol
sudo cp /usr/share/macontrol/bin/macontrol-update /bin/macontrol-update  
```  
**Usage:**  
```bash  
macontrol [-h] [-i INTERFACE] [-m MAC] [--no-root]
```  
**Update:**  
```bash  
sudo /usr/share/macontrol/bin/macontrol-update  
```  
> [!WARNING]
> If you get errors after updating, please re-run the updater and install pip dependencies.  

---

## License  
### MAControl License (MC-1.0)  
> Copyright (c) 2026 Abgache  

Permission is hereby granted to use, copy, modify, and distribute this software for personal, educational, and security research purposes, subject to the following conditions:  
1. Do not use this software for illegal activities.  
2. Do not claim it as your own work without credit.  
3. If you break it, you fix it yourself.  

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.**  