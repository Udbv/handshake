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
        i=0
        def byQuality_key(network):
            return network.quality
        sorted_quality = sorted(self.networks_list, key=byQuality_key,reverse=True)
        for network in sorted_quality:#self.networks_list:
            if network.channel is None:
                network.channel = 0
            if network.ssid is "":
                network.ssid="Hidden"
            res = [i+1,
                 network.address,
                 network.ssid ,
                 network.channel,
                 network.quality]
            print(
                "{0[0]:2d}) bssid {0[1]:16s} ssid {0[2]:23s} channel {0[3]} quality {0[4]:>5s}".format(res

                )
            )
            i+=1

        network_number = input("Choose network №:")
        print("Deauth #{} {}".format(network_number,sorted_quality[int(network_number)].ssid))
if __name__ == "__main__":
    print ("Starting handshake capture")
    api = Handshaker()