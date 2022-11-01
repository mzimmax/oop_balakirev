class Graph:
    def __init__(self, data):
        self.data = data
        self.is_show = True

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        print("Графическое отображение данных:", end=" ")
        self.show_table()

    def show_bar(self):
        print("Столбчатая диаграмма:", end=" ")
        self.show_table()

    def set_show(self, fl_show: bool):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_graph()
gr.show_table()