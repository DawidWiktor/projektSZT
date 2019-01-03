from .models import Navbar, Footer, BasePage
from django.conf import settings

def add_variable_to_context(request):
    navbar = Navbar.objects.first()
    footer = Footer.objects.first()
    base = BasePage.objects.first()
    data = {
        "user": request.user
    }
    return {
        'data': data,
        'nav': navbar,
        'footer': footer,
        'base' : base
    }