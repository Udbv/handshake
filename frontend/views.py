from django.shortcuts import render
from wifi import Cell
# Create your views here.
from django.http import HttpResponse
import backend.handshaker
import backend.networks_list as networks
from django.views import generic
def index(request):
    handshaker = backend.handshaker.Handshaker()

    networks_map = networks.get_networks_list(handshaker.scan_interface)
    #networks_map = ['1',2,3]
    for network in networks_map:
        print("netoworks {} ".format(network))
    return render(
        request,
        'networks.html',
        context={'scan_interface': handshaker.scan_interface, 'networks_map':Cell.all(handshaker.scan_interface).values()},
    )

class NetworkListView(generic.ListView):
    template_name = 'networks.html'
    context_object_name = 'networks_map'
    # def get_queryset(self):
        # handshaker = backend.handshaker.Handshaker()
        #
        # networks_map = networks.get_networks_list(handshaker.scan_interface)
        # for network in networks_map:
        #     print("netowrks {} ".format(network.ssid))
        # return networks_map,handshaker.scan_interface