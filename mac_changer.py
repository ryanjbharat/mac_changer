#!/usr/bin/env python3

import subprocess
import argparse
import re


def get_arguments():
    """ Creates parser object, adds arguments, and returns """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    args = parser.parse_args()
    if not args.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not args.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return args


def change_mac(interface, new_mac):
    """ Changes the MAC address """
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])


def get_current_mac(interface):
    """ Returns current MAC address """
    ifconfig_result = subprocess.getoutput("ifconfig " + interface)
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


args = get_arguments()

current_mac = get_current_mac(args.interface)
print("Current MAC = " + str(current_mac))

change_mac(args.interface, args.new_mac)

current_mac = get_current_mac(args.interface)
if current_mac == args.new_mac:
    print("[+] MAC address was changed successfully to " + current_mac)
else:
    print("[-] MAC address was not changed.")
