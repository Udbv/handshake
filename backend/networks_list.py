from wifi import Cell,scheme

def get_networks_list(interface):
    #print(interface)
    networks_list=Cell.all(interface)
    return networks_list
