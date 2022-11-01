class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []
        self.names = []

    def add_app(self, app):
        if app.name not in self.names:
            self.apps.append(app)
            self.names.append(app.name)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory_max=1024):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list


app_1 = AppVK() # name = "ВКонтакте"
app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024
ph = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}) # name = "Phone", phone_list = словарь с контактами
sm = SmartPhone("Honor 1.0")
sm.add_app(app_1)
sm.add_app(app_2)
sm.add_app(ph)
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
sm.remove_app(ph)
for a in sm.apps:
    print(a.name)
