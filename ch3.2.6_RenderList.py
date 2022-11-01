class RenderList:
    def __init__(self, type_list="ul"):
        self.type_list = type_list

    def __call__(self, *args, **kwargs):
        tag = "ul"
        if self.type_list == "ol":
            tag = "ol"
        text = "\n".join(["<li>" + str(i) + "</li>" for i in args[0]])
        return f"<{tag}>\n{text}\n</{tag}>"


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)