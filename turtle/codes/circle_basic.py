import turtle as t

colors = ["#490a3d", "#bd1550", "#e97f02", "#f8ca00"]
n = 50

t.speed("fastest")
for i in range(n):
    t.pencolor(colors[i % len(colors)])
    t.circle(120)
    t.right(360/n)
