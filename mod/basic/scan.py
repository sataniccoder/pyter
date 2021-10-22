from scapy.all import *

def atk():
    rang = input("[+] enter ip range (eg: 192.168.0.1/24): ")
    print("[TIME] time : 5+ seconds")  
    print("[+] running...")

    target_ip = rang
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []

    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    print("\n\n=====================================")
    print("available devices in the network:")
    print("")
    print("IP" + " "*18+"MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))
    print("\n=====================================")