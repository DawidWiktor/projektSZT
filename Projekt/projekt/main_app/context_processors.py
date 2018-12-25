from .models import Navbar, Footer, BasePage

def add_variable_to_context(request):
    navbar = Navbar.objects.first()
    footer = Footer.objects.first()
    base = BasePage.objects.first()
    print('foot')
    print(base.headerImage)
    data = {
        "user": request.user
    }
    
    return {
        'data': data,
        'nav': navbar,
        'footer': footer,
        'base' : base
    }