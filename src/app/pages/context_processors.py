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
    path_parts = [part for part in request.get_full_path().strip('/').split('/') if part]
    breadcrumbs = []
    for part in path_parts:
        # Query the database to find the matching NavMenu or Page by slug
        try:
            nav_menu_item = NavMenu.objects.get(slug=part)
            breadcrumbs.append({'slug': nav_menu_item.slug, 'value': nav_menu_item.value})
        except NavMenu.DoesNotExist:
            try:
                page_item = Page.objects.get(slug=part)
                breadcrumbs.append({'slug': page_item.slug, 'value': page_item.value})
            except Page.DoesNotExist:
                # If no matching slug found, append a placeholder or handle accordingly
                breadcrumbs.append({'slug': part, 'value': part})  # Используйте part как значение, если не найдено в БД
    return {'breadcrumbs': breadcrumbs}
