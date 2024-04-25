from django.db.models import Exists, OuterRef
from db.models import Page, NavMenu


def get_table(request):
    pages = list(Page.objects.all())

    pages_subquery = Page.objects.filter(item_id=OuterRef('pk')).values('id')
    nav_menu_items = list(
        NavMenu.objects.annotate(has_pages=Exists(pages_subquery)).values('id', 'slug', 'has_pages', 'value'))

    return {
        'nav_menu_items': nav_menu_items,
        'pages': pages
    }


def get_breadcrumbs(request):
    current_path = request.get_full_path()
    path_parts = current_path.strip('/').split('/')

    path_with_values = []

    for slug in path_parts:
        try:
            nav_menu_item = NavMenu.objects.get(slug=slug)
            path_with_values.append({
                'slug': slug,
                'value': nav_menu_item.value
            })
        except NavMenu.DoesNotExist:
            path_with_values.append({
                'slug': slug,
                'value': None
            })

    return {'current_path': path_with_values}
