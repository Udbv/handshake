import pyric
import pyric.pyw as pyw

class Interfaces(object):
    def __init__(self):
        self.wifi_interfaces=''
        self.attack_interface=''
        self.scan_interface=''

    def get_wifi_interfaces(self):
        try:
            self.wifi_interfaces = pyw.winterfaces()
            print(self.wifi_interfaces)
            if self.wifi_interfaces.__len__()>=2:
                self.attack_interface = self.wifi_interfaces[1]
                self.scan_interface = self.wifi_interfaces[0]
            elif self.wifi_interfaces.__len__()==1:
                self.attack_interface = self.wifi_interfaces[0]
                self.scan_interface = self.wifi_interfaces[0]
            else :
                exit("No wifi interfaces available")
            #print(self.scan_interface,self.attack_interface)
        except pyric.error as e:
            print("Error {}".format(e))
        return self

    def start_interface(self):
        pyw.up(self)
