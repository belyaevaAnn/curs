from .models import *


def get_material():
    materials = Material.objects.all()
    return materials


def get_services():
    services = Service.objects.all()
    return services


def get_review():
    reviews = Review.objects.all()
    return reviews

