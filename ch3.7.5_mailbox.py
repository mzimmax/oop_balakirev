class MailBox:
    def __init__(self):
        self.inbox_list = []

    def recive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_list = [MailItem(*i.split("; ")) for i in lst_in]


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False


    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


mail.recive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[3].set_read(True)
inbox_list_filtered = [i for i in mail.inbox_list if i]
