from collections import namedtuple

from services.HelloService import HelloService


def init_services():
    services_dict = {
        "hello_service": HelloService()
    }
    return namedtuple('Services', services_dict.keys())(*services_dict.values())
