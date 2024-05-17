from db.models import Page, SubPage, News
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
    url = ''

    news_found = False

    for part in path_parts:
        if not part:
            continue
        if url:
            url += '/'  # Добавляем слэш перед каждой частью пути, кроме первой
        url += part

        if part == 'news':
            title = 'Новости'
            breadcrumbs_list.append({'title': title, 'slug': url})
            if len(path_parts) > path_parts.index(part) + 1:
                next_part = path_parts[path_parts.index(part) + 1]
                if next_part.isdigit():
                    try:
                        news_item = News.objects.get(pk=next_part)
                        title = news_item.title
                        url += '/' + next_part
                        breadcrumbs_list.append({'title': title, 'slug': url})
                    except News.DoesNotExist:
                        title = "Статья"
                    break
                break
            else:
                break

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
        breadcrumbs_list.append({'title': title, 'slug': url})

    return {'breadcrumbs': breadcrumbs_list}