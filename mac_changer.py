#!/usr/bin/env python3

import subprocess
import argparse


def get_arguments():
    """Creates parser object, adds arguments, and returns"""
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
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])


args = get_arguments()
change_mac(args.interface, args.new_mac)
