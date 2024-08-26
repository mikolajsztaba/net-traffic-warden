import subprocess
import atexit
from scapy.all import *

def start_sniffing(blocked_hosts):
    TRAFFIC_THRESHOLD = 10
    traffic_counter = {}
    added_rules = []

    def check_traffic(pkt):
        if IP in pkt:
            src_ip = pkt[IP].src
            print("Packet from:", src_ip)
            if src_ip not in traffic_counter:
                traffic_counter[src_ip] = 0
            traffic_counter[src_ip] += 1
            if traffic_counter[src_ip] >= TRAFFIC_THRESHOLD and src_ip in blocked_hosts:
                print("Blocking traffic from:", src_ip)
                rule = ["iptables", "-A", "INPUT", "-s", src_ip, "-j", "DROP"]
                subprocess.run(rule)
                added_rules.append(rule)

    def cleanup():
        for rule in added_rules:
            remove_rule = rule.copy()
            remove_rule[1] = '-D'
            subprocess.run(remove_rule)
        print("All added iptables rules have been removed.")

    print("Starting packet sniffing...")
    try:
        sniff(prn=check_traffic, filter="tcp or icmp", store=0)
    finally:
        cleanup()
