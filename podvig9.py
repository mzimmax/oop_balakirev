class Figure:
    type: str = 'ellipse'
    color: str = 'red'


fig1: Figure = Figure()

fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

del fig1.color

print(*(fig1.__dict__))

