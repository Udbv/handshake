import pyric
import pyric.pyw as pyw

class Interfaces(object):
    def __init__(self):
        print("as")
        self.wifi_interfaces=''
        self.attack_interface=''
        self.scan_interface=''

    def get_wifi_interfaces(self):
        try:
            self.wifi_interfaces = pyw.winterfaces()
            self.attack_interface = self.wifi_interfaces[0]
            self.scan_interface = self.wifi_interfaces[1]
            #print(self.scan_interface,self.attack_interface)
        except pyric.error as e:
            print("Error {}".format(e))
        return self