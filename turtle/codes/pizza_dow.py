import turtle as t

colors = ["#490a3d", "#bd1550", "#e97f02", "#f8ca00"]
n = 60

t.speed("fastest")
for i in range(n*8):
    t.pencolor(colors[i % len(colors)])
    t.circle(20)
    if (i//15) % 2 == 0:
        t.right(360/n)
    else:
        t.left(270/n)
        t.forward(5)
