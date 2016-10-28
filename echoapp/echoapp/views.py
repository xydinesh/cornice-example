""" Cornice services.
"""
from cornice import Service


hello = Service(name='hello', path='/', description="Simplest app")
name = Service(name='name', path='/names', description="Name app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}


@name.get()
def get_names(request):
    """Returns Name"""
    return {'Name': 'Dinesh'}
