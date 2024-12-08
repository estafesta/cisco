#!/usr/bin/env python

def telnet():
    print("line vty 0 4")
    print("password cisco")
    print("login")
    print("transport input telnet")

def ssh():
    print("hostname Router0")
    print("ip domain-name router0.local")
    print("crypto key generate rsa")
    print("ip ssh version 2")
    print("username admin password cisco")
    print("line vty 0 4")
    print("login local")
    print("transport input ssh")

def configure_interfaces():
    interfaceList = ['GigabitEthernet0/0', 'GigabitEthernet0/1']
    addressList = ['192.168.10.1', '192.168.11.1']
    maskList = ['255.255.255.0', '255.255.255.0']

    for index, interface in enumerate(interfaceList):
        print(f"interface {interface}")
        print(f"ip address {addressList[index]} {maskList[index]}")
        print("no shutdown")
        print("!")

if __name__ == "__main__":
    import sys

    protocol = "telnet"  # Standardprotokoll
    if len(sys.argv) > 1:
        protocol = sys.argv[1].lower()

    configure_interfaces()

    if protocol == "telnet":
        print("! Konfiguration für Telnet:")
        telnet()
    elif protocol == "ssh":
        print("! Konfiguration für SSH:")
        ssh()
    else:
        print(f"Unbekanntes Protokoll: {protocol}")
        print("Verwenden Sie 'telnet' oder 'ssh'.")
