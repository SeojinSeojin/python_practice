import turtle as t

colors = ["#490a3d", "#bd1550", "#e97f02", "#f8ca00"]
n = 200
lent = 20

t.speed("fastest")
for i in range(n):
    t.pencolor(colors[i % len(colors)])
    t.forward(lent)
    t.left(92)
    lent += 2
