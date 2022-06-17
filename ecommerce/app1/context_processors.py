from . models import category

def menu_links(request):
    links=category.objects.all()
    return dict(link_key=links)