#!/usr/bin/python
import turtle

def draw_square(square_turtle):
	for i in range(4):
		square_turtle.forward(100)
		square_turtle.right(90)


def draw_circle(circle_turtle) :
	circle_turtle.circle(100)


def draw_triangle(tri_turtle):

	tri_turtle.right(30)
	tri_turtle.forward(100)
	tri_turtle.right(60)
	tri_turtle.forward(100)
	tri_turtle.left(30)
	tri_turtle.backward(200)


def draw_rhombus(go_turtle):
	for i in range(2):
		go_turtle.forward(100)
		go_turtle.left(45)
		go_turtle.forward(100)
		go_turtle.left(135)


def main():
	window = turtle.Screen()
	window.bgcolor("#FFFAF0")

	myTurtle = turtle.Turtle()
	myTurtle.shape("turtle")
	myTurtle.color("#9ACD32")

	for i in range(13):
		draw_circle(myTurtle)
		myTurtle.right(30)

	window.clear()
	myTurtle.reset()


	for i in range(19):
		draw_square(myTurtle)
		myTurtle.right(20)

	window.clear()
	myTurtle.reset()

	window.bgcolor("#FFFAF0")
	myTurtle.shape("turtle")
	myTurtle.color("#48D1CC")
	for i in range(39):
		draw_rhombus(myTurtle)
		myTurtle.right(10)


#	draw_circle(myTurtle)
#	draw_triangle(myTurtle)

	window.exitonclick()


if __name__ == '__main__':
  main()


