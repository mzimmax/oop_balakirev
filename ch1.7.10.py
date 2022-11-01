class AppStore:
    aplications = []

    def add_application(self, app):
        self.aplications.append(app)
        """- добавление нового приложения app в магазин;"""

    def remove_application(self, app):
        """- удаление приложения app из магазина;"""
        self.aplications.remove(app)

    def block_application(self, app):
        """- блокировка приложения app
        (устанавливает локальное свойство blocked
        объекта app в значение True);"""
        app.blocked = True

    def total_apps(self):
        """- возвращает общее число приложений в магазине."""
        return len(self.aplications)


class Application:

    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)

# 111
app_whatsup = Application("WhatsUp")
store.add_application(app_whatsup)
store.block_application(app_whatsup)
print(store.total_apps())
