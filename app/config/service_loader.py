from collections import namedtuple

from app.services.BookingService import BookingService


def init_services():
    services_dict = {
        "booking_service": BookingService()
    }
    return namedtuple('Services', services_dict.keys())(*services_dict.values())
