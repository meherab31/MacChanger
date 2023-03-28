
import re
from random import choice, randint
import subprocess

print("0>Current Mac\n1>Manual MacChanger \n2> Auto MacChanger")
inp = int(input("Choose Any Number: "))
interface = input("Enter net interface name: ").strip()


def main():
    if inp == 0:
        CurrentMac()

    elif inp == 1:
        new_mac = input("Enter the new mac address: ").strip()
        ChangeMac(interface, new_mac)

    elif inp == 2:
        random = RandMac()
        print(random)
        ChangeMac(interface, random)


def RandMac():
    cisco = ["00", "40", "96"]
    dell = ["00", "14", "22"]
    mac_address = choice([cisco, dell])
    for i in range(3):
        one = choice(str(randint(0, 9)))
        two = choice(str(randint(0, 9)))
        three = (str(one + two))
        mac_address.append(three)
    return ":".join(mac_address)


def ChangeMac(interface, new_mac):
    subprocess.call(["ifconfig " + str(interface) + " down"], shell=True)
    subprocess.call(["ifconfig " + str(interface) + " hw ether " + str(new_mac) + " "], shell=True)
    subprocess.call(["ifconfig " + str(interface) + " up"], shell=True)


def CurrentMac():
    output = subprocess.check_output(["ifconfig " + "wlan0"], shell=True)
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    print("Old Mac Address {}", format(current_mac))



if __name__ == "__main__":
    main()
