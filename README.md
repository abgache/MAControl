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
sudo chmod 555 /usr/share/macontrol/bin/macontrol  
sudo chmod 555 /usr/share/macontrol/bin/macontrol-update  
sudo echo 'export PATH="$PATH:/usr/share/macontrol/bin"' >> ~/.profile  
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
