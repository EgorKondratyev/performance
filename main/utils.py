sidebar = [
    {'title': 'Главная страница', 'name_url': 'main_page'},
    {'title': 'Успеваемость', 'name_url': 'main_page'},
    {'title': 'Отработки', 'name_url': 'main_page'},
    {'title': 'Обратная связь', 'name_url': 'main_page'},
    {'title': 'Выход', 'name_url': 'logout'}
]


class BaseMixin:
    @staticmethod
    def get_base_context_data(**kwargs):
        context = kwargs
        context['sidebar'] = sidebar
        if not context.get('title'):
            context['title'] = 'Главная страница'
        return context

