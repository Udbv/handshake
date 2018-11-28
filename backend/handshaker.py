import os
import backend.networks_list as networks

from backend.interface_manager import Interfaces


class Handshaker(object):
    def __init__(self):
        self.interface_manager = Interfaces()
        self.interfaces = self.interface_manager.get_wifi_interfaces()
        self.attack_interface = self.interfaces.attack_interface
        self.scan_interface = self.interfaces.scan_interface
        #print(self.interfaces)

        print("scan interaface {}".format(self.interfaces.scan_interface))
        self.networks_list=networks.get_networks_list(self.interfaces.scan_interface)
        for network in self.networks_list:
            print("bssid {} ssid {} channel {}".format(network.address, network.ssid, network.channel))

if __name__ == "__main__":
    print ("Starting handshake capture")
    api = Handshaker()