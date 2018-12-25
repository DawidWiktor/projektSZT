from .models import Navbar, Footer

def add_variable_to_context(request):
    navbar = Navbar.objects.first()
    footer = Footer.objects.first()
    return {
        'nav': navbar,
        'footer': footer
    }