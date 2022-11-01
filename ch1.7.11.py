class Viber:
    messages = []

    @classmethod
    def add_message(cls, msgs):
        """- добавление нового сообщения в список сообщений;"""
        cls.messages.append(msgs)

    @classmethod
    def remove_message(cls, msgs):
        """- удаление сообщения из списка;"""
        cls.messages.remove(msgs)

    def set_like(msgs):
        """- поставить/убрать лайк для сообщения msg
        (если лайка нет то он ставится, если уже есть, то убирается);"""
        msgs.fl_like = not msgs.fl_like

    @classmethod
    def show_last_message(cls, tail):
        """- отображение последних сообщений;"""
        if tail > len(cls.messages):
            print([(i.text, i.fl_like) for i in cls.messages[::-1]])
        else:
            print([(i.text, i.fl_like) for i in cls.messages[:-(tail + 1):-1]])


    @classmethod
    def total_messages(cls):
        """- возвращает общее число сообщений."""
        return len(cls.messages)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like



# end
msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
#Viber.remove_message(msg)

Viber.add_message(Message("Что вы о нем думаете???"))
Viber.add_message(Message("вы думаете?"))
print(Viber.total_messages())
Viber.show_last_message(10)