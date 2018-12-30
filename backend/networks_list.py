from wifi import Cell,scheme
from .interface_manager import Interfaces
def get_networks_list(interface):
    print(interface)
    try:
        networks_list=Cell.all(interface)
    except Exception:
        Interfaces.start_interface(interface)
    return networks_list
