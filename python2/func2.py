# create a function that returns both the area and circumference of a circle given its radius

# also we use math function in the place of 3.14 which is math.pi
def circle(r):
    area = 3.14*(r**2)
    circum = 2*3.14*r
    print(f"area of circle is {area:.2f}")
    print(f"circumferrence of circle is {circum:.2f}")
    return area, circum


circle(10)


def argum(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


argum(name="saqib", age="22")
