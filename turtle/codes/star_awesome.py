import turtle as t

colors = ["#490a3d", "#bd1550", "#e97f02", "#f8ca00"]
n = 50

t.speed("fastest")
for i in range(n*2):
    t.pencolor(colors[i % len(colors)])
    for j in range(5):
        t.forward(90+i)
        t.right(144)
        t.forward(90+i)
        t.left(72)
    t.right(360/n)
