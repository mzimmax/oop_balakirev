class WindowDlg:
    def __init__(self, title, height, width):
        self.__title = title
        self.__height = self.__width = None
        self.height = height
        self.width = width
        self.show_flag = False

    def show(self):
        if  self.show_flag:
            print(f'{self.__title}: {self.__width}, {self.__height}')
            self.show_flag = False

    @staticmethod
    def check_value(value):
        if type(value) == int and 0 <= value <= 10000:
            return True

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if WindowDlg.check_value(value):
            if value != self.__height:
                self.show_flag = True
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if WindowDlg.check_value(value):
            if value != self.__width:
                self.show_flag = True
            self.__width = value


wnd = WindowDlg("dlg1", 100, 200)
wnd.width = 230
wnd.height = 20
wnd.show()
