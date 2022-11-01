class Model:
    def __init__(self):
        self.records: dict = {}

    def query(self, **kwargs):
        self.records = kwargs

    def __str__(self):
        answer = ", ".join(["=".join((i[0], str(i[1]))) for i in self.records.items()])
        return [f"Model: {answer}", "Model"][len(self.records) == 0]


model = Model()
model.query(id=1, fio='Sergey', old=33)
# model.query()

print(model)
