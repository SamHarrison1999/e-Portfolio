import turtle

t = turtle.Turtle()
t.lt(90)
t.penup()
t.backward(150)
t.pendown()
t.speed(10)


def recursive_tree(branch_length, angle, t):
    """Draw a tree recursively"""
    if branch_length > 1:
        t.forward(branch_length)
        t.right(angle)
        recursive_tree(branch_length - 7, angle, t)
        t.left(angle * 2)
        recursive_tree(branch_length - 7, angle, t)
        t.right(angle)
        t.backward(branch_length)


recursive_tree(60, 20, t)
turtle.mainloop()