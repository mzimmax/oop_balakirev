class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        res = []
        for i in range(len(self.data)):
            if self.LIMIT_Y[0] <= self.data[i] <= self.LIMIT_Y[1]:
                res.append(self.data[i])
        print(*res)


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
