import math
import copy
import turtle


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other[0], self.y + other[1])


class Rectangle:
    height = None
    width = None
    corner = None


class Circle:
    center = None
    radius = None


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


def distance_between_points(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx ** 2 + dy ** 2)
    return dist


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


def move_rectangle_copy(rect, dx, dy):
    new = copy.deepcopy(rect)
    new.move_rectangle(dx, dy)
    return new


def point_in_circle(point, circle):
    d = distance_between_points(point, circle.center)
    print(d)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    p = copy.copy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False


def draw_circle(t, circle):
    t.pu()
    t.goto(circle.center.x, circle.center.x - circle.radius)  # Position pen to draw rim of circle
    t.pd()  # Place pen to draw
    t.circle(circle.radius)  # Draw the circle
    t.pu()  # Lift pen


def draw_rect(t, rect):
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.setheading(0)
    t.pd()

    for length in rect.width, rect.height, rect.width, rect.height:
        t.fd(length)
        t.rt(90)


if __name__ == '__main__':
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))
    t = turtle.Turtle()

    # draw the axes
    length = 400
    t.fd(length)
    t.bk(length)
    t.lt(90)
    t.fd(length)
    t.bk(length)

    # draw a rectangle
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    draw_rect(t, box)

    # draw a circle
    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    draw_circle(t, circle)

    # wait for the user to close the window
    turtle.mainloop()
