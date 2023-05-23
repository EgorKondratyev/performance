class BaseMixin:
    sidebar = [
        {'title': 'Главная страница', 'name_url': 'main_page'},
        {'title': 'Успеваемость', 'name_url': 'main_page'},
        {'title': 'Отработки', 'name_url': 'main_page'},
        {'title': 'Обратная связь', 'name_url': 'main_page'},
        {'title': 'Выход', 'name_url': 'logout'}
    ]
    additional_sidebar = [
        {'title': 'Добавить специальность', 'url': 'http://127.0.0.1:8000/admin/academic_performance/speciality/add/'},
        {'title': 'Добавить предмет', 'url': 'http://127.0.0.1:8000/admin/academic_performance/subjects/add/'},
        {'title': 'Добавить группу', 'url': 'http://127.0.0.1:8000/admin/academic_performance/groups/add/'},
        {'title': 'Добавить студента', 'url': 'http://127.0.0.1:8000/admin/academic_performance/students/add/'},
    ]

    def get_base_context_data(self, **kwargs):
        context = kwargs
        context['sidebar'] = self.sidebar
        context['additional_sidebar'] = self.additional_sidebar
        if not context.get('title'):
            context['title'] = 'Главная страница'
        return context

