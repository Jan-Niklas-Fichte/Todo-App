from django.apps import AppConfig


class TodosConfig(AppConfig):
    name = 'todos'

    def ready(self):
        from todos import reoccurence_scheduler
        reoccurence_scheduler.start()
