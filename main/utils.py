class BaseMixin:
    def get_base_context_data(self, **kwargs):
        context = kwargs
        context['sidebar'] = self.get_sidebar()
        context['additional_sidebar'] = self.get_additional_sidebar()
        if not context.get('title'):
            context['title'] = 'Главная страница'
        return context

    @staticmethod
    def get_sidebar():
        sidebar = [
            {'title': 'Главная страница', 'name_url': 'main_page'},
            {'title': 'Успеваемость', 'name_url': 'groups'},
            {'title': 'Отработки', 'name_url': 'main_page'},
            {'title': 'Обратная связь', 'name_url': 'main_page'},
            {'title': 'Выход', 'name_url': 'logout'}
        ]
        return sidebar

    @staticmethod
    def get_additional_sidebar():
        additional_sidebar = [
            {
                'title': 'Добавить специальность',
                'url': 'http://127.0.0.1:8000/admin/main/speciality/add/'
            },
            {
                'title': 'Добавить предмет',
                'url': 'http://127.0.0.1:8000/admin/main/subjects/add/'
            },
            {
                'title': 'Добавить группу',
                'url': 'http://127.0.0.1:8000/admin/main/groups/add/'
            },
            {
                'title': 'Добавить студента',
                'url': 'http://127.0.0.1:8000/admin/main/students/add/'
            },
            {
                'title': 'Добавить отработку',
                'url': 'http://127.0.0.1:8000/admin/working_out/workingout/add/'
            }
        ]
        return additional_sidebar
