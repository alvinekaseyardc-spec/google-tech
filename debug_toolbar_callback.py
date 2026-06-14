# googleTech/debug_toolbar_callback.py
def show_toolbar(request):
    from django.conf import settings
    if not settings.DEBUG:
        return False
    # Ne pas afficher sur l'accueil
    if request.path == '/':
        return False
    return True