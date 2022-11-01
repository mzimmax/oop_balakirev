class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        del self.modules[indx - 1]


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        del self.lessons[indx - 1]


class LessonItem:
    """ lesson = LessonItem(название урока, число практических занятий, общая длительность урока)"""

    valid_types = {
        "title": str,
        "practices": int,
        "duration": int
    }

    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if not isinstance(value, (self.valid_types[key])):
            raise TypeError("Неверный тип присваиваемых данных.")
        if type(value) == int and value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item not in self.valid_types.keys():
            object.__delattr__(self, item)

    def __getattr__(self, item):
        return False


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.remove_lesson(1)
course.add_module(module_2)
print(module_1.__dict__)




