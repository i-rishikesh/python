import turtle

#create a turtle object
a = turtle.Turtle()

#create a screen object for title and background
sc = turtle.Screen()
sc.title('YE FOOL APKE LIYE')
sc.bgcolor('light blue')

a.color("black", "pink")
a.speed(6)  # 0 - fast speed,,,, 1--slow speed,,,,,,  5--average
a.fd(-150)

a.begin_fill()

for i in range(90):
    a.forward(300)
    a.left(170)

a.end_fill()
turtle.mainloop()