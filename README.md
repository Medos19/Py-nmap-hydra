## Python call nmap and hydra

A tool for parsing Nmap Scan Result and send command to Hydra, automated the password exploit!

If you need an email warning, configure the sendmail.

 * hydra:https://github.com/vanhauser-thc/thc-hydra
 * nmap:https://github.com/nmap/nmap

```bash
#ubuntu
sudo apt-get -y install nmap hydra
pip install libnmap
```

## setup
 * configure target

```bash
sudo su
mkdir /root/scans
cd /root
git clone https://github.com/origingod/Py-nmap-hydra scans
```

 * add scan to crontab

```bash
0 22 * * * /bin/sh /root/scans/scan_per.sh
```

 * if you want to sendmail , uncomment the line in scan_per.sh and configure your email in sendmail.py
