from db.models import Page, SubPage
from django.db.models import Exists, OuterRef

def navmenu(request):
    pages = Page.objects.annotate(has_subpages=Exists(SubPage.objects.filter(page=OuterRef('pk'))))

    pages_with_subpages = []
    for page in pages:
        page_data = {
            'id': page.id,
            'title': page.title,
            'slug': page.slug,
            'has_subpages': page.has_subpages,
            'has_pages': []
        }

        if page.has_subpages:
            subpages = SubPage.objects.filter(page=page)
            page_data['has_pages'] = list(subpages.values('id', 'title', 'slug'))

        pages_with_subpages.append(page_data)

    return {'pages': pages_with_subpages}


def breadcrumbs(request):
    path = request.path_info.strip('/')
    path_parts = path.split('/')
    breadcrumbs_list = []
    url = '/'

    for part in path_parts:
        if not part:
            continue
        url += f'{part}/'

        try:
            page = Page.objects.filter(slug=part).first()
            if page:
                title = page.title
            else:
                subpage = SubPage.objects.filter(slug=part).first()
                if subpage:
                    title = subpage.title
                else:
                    title = part.capitalize()
        except (Page.DoesNotExist, SubPage.DoesNotExist):
            title = part.capitalize()
        breadcrumbs_list.append({'title': title, 'url': url})

    return {'breadcrumbs': breadcrumbs_list}