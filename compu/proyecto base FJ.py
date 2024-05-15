# Import necessary libraries
import turtle
import random
from time import * 

# Initialize variables  
name = input("Ingresa el nombre: ")
age = int(input("Ingrese su edad: "))
favorite_color = input("Enter the favorite color of the child (red, green, blue, yellow, purple): ")
def clear_screen():
    sleep(5)
    turtle.clearscreen()

def marcos(): #Margenes para todos paneles de con diseño poligonal con medidas de 1050 de ancho y 650 de alto
    turtle.hideturtle()
    turtle.speed(50)
    turtle.penup()
    turtle.setpos(-525,325) 
    turtle.pendown()
    turtle.width(3)
    for i in range(2):
        turtle.forward(1050)
        turtle.right(90)
        turtle.forward(650)
        turtle.right(90)
    turtle.penup()
    turtle.setpos(-525,325) 
    turtle.pendown()
    for i in range(2):
        turtle.forward(1050)
        turtle.right(90)
        turtle.forward(75)
        turtle.right(90)
    turtle.penup()
    turtle.setpos(-525,-150) 
    turtle.pendown()
    for i in range(2):
        turtle.forward(1050)
        turtle.right(90)
        turtle.forward(175)
        turtle.right(90)
        turtle.speed(10)
    turtle.penup()
    turtle.goto(0,275)
    turtle.pendown()
    turtle.write(f"El Roble y la Ardilla: Una Amistad en el Bosque la aventura de {name}", False, "center", ("comic sans", 20))

# Function to display a sequence


def panel1():
    turtle.begin_fill()
    t = turtle.Pen()
    turtle.speed(0)
    turtle.setup(1200, 800)
    turtle.bgcolor('white')
    turtle.clear()
    turtle.reset()
   
    turtle.fillcolor("white")
    marcos()
    def arbol():
        def dibujar_arbol(t, longitud, angulo):
            if longitud < 10:
                return
            else:
                t.forward(longitud)
                t.left(angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.right(2 * angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.left(angulo)
                t.backward(longitud)

        t = turtle.Turtle()
        t.color("green")
        t.width(2)
        t.speed(0)  # Máxima velocidad de dibujo

        t.left(90)
        t.penup()
        t.goto(200, -150)
        t.pendown()

        dibujar_arbol(t, 100, 30)
    def ardilla():
        t = turtle.Turtle()
        t.speed(0)
        t.width(3)

        # Cuerpo de la ardilla
        t.penup()
        t.fillcolor("#8B4513")  # Marrón oscuro
        t.begin_fill()
        t.goto(-250,-140)
        t.pendown()
        t.circle(50)
        t.end_fill()

        # Bloque chiquito encima
        t.penup()
        t.fillcolor("#8B4513")
        t.begin_fill()
        t.goto(-190, -100)  # Posicionar el bloque encima del cuerpo
        t.pendown()
        t.circle(35)
        t.end_fill()
        
        # Cola de la ardilla
        t.penup()
        t.fillcolor("#8B4513")  # Marrón oscuro
        t.begin_fill()
        t.goto(-310, -30)  # Posicionando la cola
        t.pendown()
        for _ in range(2):
            t.forward(15)
            t.right(90)
            t.forward(70)
            t.right(90)
        t.end_fill()
        
        # Orejas
        t.penup()
        t.goto(-210, -25)  # Posicionar el ojo derecho
        t.pendown()
        t.fillcolor("#8B4513")
        t.begin_fill()
        for _ in range(4):
            t.forward(15)
            t.right(90)
        t.end_fill()

        t.penup()
        t.goto(-180, -25)  # Posicionar el ojo izquierdo
        t.pendown()
        t.fillcolor("#8B4513")
        t.begin_fill()
        for _ in range(4):
            t.forward(15)
            t.right(90)
        t.end_fill()
        
        #dientes
        
        # Cola de la ardilla
        t.penup()
        t.fillcolor("white")  # Marrón oscuro
        t.begin_fill()
        t.goto(-195, -70)  # Posicionando la cola
        t.pendown()
        for _ in range(2):
            t.forward(15)
            t.right(90)
            t.forward(10)
            t.right(90)
        t.end_fill()
        
        

        # Ojos negros
        t.penup()
        t.goto(-200, -55)  # Posicionar el ojo derecho
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):
            t.forward(5)
            t.right(90)
        t.end_fill()

        t.penup()
        t.goto(-180, -55)  # Posicionar el ojo izquierdo
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):
            t.forward(5)
            t.right(90)
        t.end_fill()

        t.hideturtle()
    turtle.end_fill()
    arbol()
    ardilla()
    turtle.penup()
    turtle.goto(0,-275)
    turtle.pendown()
    turtle.speed(10)
    turtle.write(f"En un bosque, había un árbol llamado Roble que quería hacer amigos.\nUn día, conoció a una ardilla llamada {name} que buscaba su hogar perfecto. ", align='center', font=('Arial', 16, 'normal'))
    clear_screen()
def panel2():
    
    t = turtle.Pen()
    turtle.speed(0)
    turtle.setup(1200, 800)
    turtle.bgcolor('white')
    turtle.bgcolor("white")
    marcos()
    
    def copa():
        t = turtle.Turtle()
        t.speed(0)
        t.width(3)

        # Tronco del árbol
        t.penup()
        t.goto(-20, -200)
        t.pendown()
        t.fillcolor("#8B4513")  # Marrón oscuro
        t.begin_fill()
        for _ in range(2):
            t.forward(40)
            t.right(90)
            t.forward(200)
            t.right(90)
        t.end_fill()

        # Definir la forma de la hoja
        hoja = turtle.Shape("compound")
        t.reset()
        t.begin_poly()
        t.forward(80)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(80)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.end_poly()
        hoja.addcomponent(t.get_poly(), "green", "dark green")

        # Registrar la forma de la hoja
        turtle.register_shape("hoja", hoja)

        # Copa del árbol con hojas de formas aleatorias y colores variados
        colores = ["green", "dark green", "yellow", "orange", "red"]
        for _ in range(100):
            x = random.randint(-150, 100)
            y = random.randint(0, 200)
            color = random.choice(colores)
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.setheading(random.randint(0, 360))  # Rotar la hoja aleatoriamente
            t.shape("hoja")
            t.color(color)
            t.stamp()

        t.hideturtle()
    def sol():
        t = turtle.Turtle()
        t.speed(0)
        t.color("yellow")
        t.penup()
        t.goto(300, 150)  # Posición del sol en la esquina superior derecha
        t.pendown()
        t.begin_fill()
        for _ in range(36):
            t.forward(150)
            t.right(170)
        t.end_fill()
        t.hideturtle()
    
    sol()
    turtle.penup()
    turtle.goto(0,-275)
    turtle.pendown()
    turtle.speed(10)
    turtle.write(f"Juntos, decidieron buscar un lugar donde Roble pudiera tener\nmuchas hojas para ofrecer sombra y {name} pudiera almacenar muchas nueces.", align='center', font=('Arial', 16, 'normal'))
    copa()
    clear_screen()
    
def panel3():
    turtle.begin_fill()
    t = turtle.Pen()
    turtle.speed(0)
    turtle.setup(1200, 800)
    turtle.bgcolor('white')
    turtle.clear()
    turtle.reset()
    turtle.fillcolor("white")
    marcos()
    
    def arbol1():
        def dibujar_arbol(t, longitud, angulo):
            if longitud < 10:
                return
            else:
                t.forward(longitud)
                t.left(angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.right(2 * angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.left(angulo)
                t.backward(longitud)

        t = turtle.Turtle()
        t.color("green")
        t.width(2)
        t.speed(0)  # Máxima velocidad de dibujo

        t.left(90)
        t.penup()
        t.goto(200, -150)
        t.pendown()

        dibujar_arbol(t, 100, 30)
    def arbol2():
        def dibujar_arbol(t, longitud, angulo):
            if longitud < 10:
                return
            else:
                t.forward(longitud)
                t.left(angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.right(2 * angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.left(angulo)
                t.backward(longitud)

        t = turtle.Turtle()
        t.color("green")
        t.width(2)
        t.speed(0)  # Máxima velocidad de dibujo

        t.left(90)
        t.penup()
        t.goto(100, -150)
        t.pendown()

        dibujar_arbol(t, 100, 30)
    def arbol3():
        def dibujar_arbol(t, longitud, angulo):
            if longitud < 10:
                return
            else:
                t.forward(longitud)
                t.left(angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.right(2 * angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.left(angulo)
                t.backward(longitud)

        t = turtle.Turtle()
        t.color("green")
        t.width(2)
        t.speed(0)  # Máxima velocidad de dibujo

        t.left(90)
        t.penup()
        t.goto(0, -150)
        t.pendown()

        dibujar_arbol(t, 100, 30)   
    def arbol4():
        def dibujar_arbol(t, longitud, angulo):
            if longitud < 10:
                return
            else:
                t.forward(longitud)
                t.left(angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.right(2 * angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.left(angulo)
                t.backward(longitud)

        t = turtle.Turtle()
        t.color("green")
        t.width(2)
        t.speed(0)  # Máxima velocidad de dibujo

        t.left(90)
        t.penup()
        t.goto(-100, -150)
        t.pendown()

        dibujar_arbol(t, 100, 30)
    def arbol5():
        def dibujar_arbol(t, longitud, angulo):
            if longitud < 10:
                return
            else:
                t.forward(longitud)
                t.left(angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.right(2 * angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.left(angulo)
                t.backward(longitud)

        t = turtle.Turtle()
        t.color("green")
        t.width(2)
        t.speed(0)  # Máxima velocidad de dibujo

        t.left(90)
        t.penup()
        t.goto(-200, -150)
        t.pendown()

        dibujar_arbol(t, 100, 30)
    def sol():
        t = turtle.Turtle()
        t.speed(0)
        t.color("yellow")
        t.penup()
        t.goto(300, 150)  # Posición del sol en la esquina superior derecha
        t.pendown()
        t.begin_fill()
        for _ in range(36):
            t.forward(150)
            t.right(170)
        t.end_fill()
        t.hideturtle()
    def ardilla():
        t = turtle.Turtle()
        t.speed(0)
        t.width(3)

        # Cuerpo de la ardilla
        t.penup()
        t.fillcolor("#8B4513")  # Marrón oscuro
        t.begin_fill()
        t.goto(-250,-140)
        t.pendown()
        t.circle(50)
        t.end_fill()

        # Bloque chiquito encima
        t.penup()
        t.fillcolor("#8B4513")
        t.begin_fill()
        t.goto(-190, -100)  # Posicionar el bloque encima del cuerpo
        t.pendown()
        t.circle(35)
        t.end_fill()
        
        # Cola de la ardilla
        t.penup()
        t.fillcolor("#8B4513")  # Marrón oscuro
        t.begin_fill()
        t.goto(-310, -30)  # Posicionando la cola
        t.pendown()
        for _ in range(2):
            t.forward(15)
            t.right(90)
            t.forward(70)
            t.right(90)
        t.end_fill()
        
        # Orejas
        t.penup()
        t.goto(-210, -25)  # Posicionar el ojo derecho
        t.pendown()
        t.fillcolor("#8B4513")
        t.begin_fill()
        for _ in range(4):
            t.forward(15)
            t.right(90)
        t.end_fill()

        t.penup()
        t.goto(-180, -25)  # Posicionar el ojo izquierdo
        t.pendown()
        t.fillcolor("#8B4513")
        t.begin_fill()
        for _ in range(4):
            t.forward(15)
            t.right(90)
        t.end_fill()
        
        #dientes
        
        # Cola de la ardilla
        t.penup()
        t.fillcolor("white")  # Marrón oscuro
        t.begin_fill()
        t.goto(-195, -70)  # Posicionando la cola
        t.pendown()
        for _ in range(2):
            t.forward(15)
            t.right(90)
            t.forward(10)
            t.right(90)
        t.end_fill()
        
        

        # Ojos negros
        t.penup()
        t.goto(-200, -55)  # Posicionar el ojo derecho
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):
            t.forward(5)
            t.right(90)
        t.end_fill()

        t.penup()
        t.goto(-180, -55)  # Posicionar el ojo izquierdo
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):
            t.forward(5)
            t.right(90)
        t.end_fill()

        t.hideturtle()
    turtle.end_fill()
    
    sol()
    
    turtle.penup()
    turtle.goto(0,-275)
    turtle.pendown()
    turtle.speed(10)
    turtle.write(f"Después de buscar un poco, encontraron un claro soleado donde\nRoble podía crecer fuerte y {name} podía tener muchos árboles para esconder sus nueces. ", align='center', font=('Arial', 16, 'normal'))
    arbol1()
    arbol2()
    arbol3()
    arbol4()
    arbol5()
    ardilla()
    clear_screen()

def panel4():
    t = turtle.Pen()
    turtle.speed(0)
    turtle.setup(1200, 800)
    turtle.bgcolor('white')
    turtle.reset()
    turtle.bgcolor("white")
    marcos()
    def arbol():
        def dibujar_arbol(t, longitud, angulo):
            if longitud < 10:
                return
            else:
                t.forward(longitud)
                t.left(angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.right(2 * angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.left(angulo)
                t.backward(longitud)

        t = turtle.Turtle()
        t.color("green")
        t.width(2)
        t.speed(0)  # Máxima velocidad de dibujo

        t.left(90)
        t.penup()
        t.goto(0, -150)
        t.pendown()

        dibujar_arbol(t, 100, 30)   
    def ardilla():
        t = turtle.Turtle()
        t.speed(0)
        t.width(3)

        # Cuerpo de la ardilla
        t.penup()
        t.fillcolor("#8B4513")  # Marrón oscuro
        t.begin_fill()
        t.goto(-250,-140)
        t.pendown()
        t.circle(50)
        t.end_fill()

        # Bloque chiquito encima
        t.penup()
        t.fillcolor("#8B4513")
        t.begin_fill()
        t.goto(-190, -100)  # Posicionar el bloque encima del cuerpo
        t.pendown()
        t.circle(35)
        t.end_fill()
        
        # Cola de la ardilla
        t.penup()
        t.fillcolor("#8B4513")  # Marrón oscuro
        t.begin_fill()
        t.goto(-310, -30)  # Posicionando la cola
        t.pendown()
        for _ in range(2):
            t.forward(15)
            t.right(90)
            t.forward(70)
            t.right(90)
        t.end_fill()
        
        # Orejas
        t.penup()
        t.goto(-210, -25)  # Posicionar el ojo derecho
        t.pendown()
        t.fillcolor("#8B4513")
        t.begin_fill()
        for _ in range(4):
            t.forward(15)
            t.right(90)
        t.end_fill()

        t.penup()
        t.goto(-180, -25)  # Posicionar el ojo izquierdo
        t.pendown()
        t.fillcolor("#8B4513")
        t.begin_fill()
        for _ in range(4):
            t.forward(15)
            t.right(90)
        t.end_fill()
        
        #dientes
        
        # Cola de la ardilla
        t.penup()
        t.fillcolor("white")  # Marrón oscuro
        t.begin_fill()
        t.goto(-195, -70)  # Posicionando la cola
        t.pendown()
        for _ in range(2):
            t.forward(15)
            t.right(90)
            t.forward(10)
            t.right(90)
        t.end_fill()
        
        

        # Ojos negros
        t.penup()
        t.goto(-200, -55)  # Posicionar el ojo derecho
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):
            t.forward(5)
            t.right(90)
        t.end_fill()

        t.penup()
        t.goto(-180, -55)  # Posicionar el ojo izquierdo
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):
            t.forward(5)
            t.right(90)
        t.end_fill()

        t.hideturtle()
    def sol():
        t = turtle.Turtle()
        t.speed(0)
        t.color("yellow")
        t.penup()
        t.goto(300, 150)  # Posición del sol en la esquina superior derecha
        t.pendown()
        t.begin_fill()
        for _ in range(36):
            t.forward(150)
            t.right(170)
        t.end_fill()
        t.hideturtle()
        
    arbol()
    ardilla()
    sol()
    
    turtle.penup()
    turtle.goto(0,-275)
    turtle.pendown()
    turtle.speed(10)
    turtle.write(f" Se convirtieron en grandes amigos y pasaban sus días felices juntos,\ndisfrutando del sol y compartiendo historias.", align='center', font=('Arial', 16, 'normal'))
    clear_screen()

def panel5():
    t = turtle.Pen()
    turtle.speed(0)
    turtle.setup(1200, 800)
    turtle.bgcolor('white')
    turtle.reset()
    turtle.bgcolor("white")
    marcos()

    def arbol():
        def dibujar_arbol(t, longitud, angulo):
            if longitud < 10:
                return
            else:
                t.forward(longitud)
                t.left(angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.right(2 * angulo)
                dibujar_arbol(t, longitud * 0.7, angulo)
                t.left(angulo)
                t.backward(longitud)

        t = turtle.Turtle()
        t.color("green")
        t.width(2)
        t.speed(0)  # Máxima velocidad de dibujo

        t.left(90)
        t.penup()
        t.goto(0, -150)
        t.pendown()

        dibujar_arbol(t, 100, 30)   
    def ardilla():
        t = turtle.Turtle()
        t.speed(0)
        t.width(3)

        # Cuerpo de la ardilla
        t.penup()
        t.fillcolor("#8B4513")  # Marrón oscuro
        t.begin_fill()
        t.goto(-250,-140)
        t.pendown()
        t.circle(50)
        t.end_fill()

        # Bloque chiquito encima
        t.penup()
        t.fillcolor("#8B4513")
        t.begin_fill()
        t.goto(-190, -100)  # Posicionar el bloque encima del cuerpo
        t.pendown()
        t.circle(35)
        t.end_fill()
        
        # Cola de la ardilla
        t.penup()
        t.fillcolor("#8B4513")  # Marrón oscuro
        t.begin_fill()
        t.goto(-310, -30)  # Posicionando la cola
        t.pendown()
        for _ in range(2):
            t.forward(15)
            t.right(90)
            t.forward(70)
            t.right(90)
        t.end_fill()
        
        # Orejas
        t.penup()
        t.goto(-210, -25)  # Posicionar el ojo derecho
        t.pendown()
        t.fillcolor("#8B4513")
        t.begin_fill()
        for _ in range(4):
            t.forward(15)
            t.right(90)
        t.end_fill()

        t.penup()
        t.goto(-180, -25)  # Posicionar el ojo izquierdo
        t.pendown()
        t.fillcolor("#8B4513")
        t.begin_fill()
        for _ in range(4):
            t.forward(15)
            t.right(90)
        t.end_fill()
        
        #dientes
        
        # Cola de la ardilla
        t.penup()
        t.fillcolor("white")  # Marrón oscuro
        t.begin_fill()
        t.goto(-195, -70)  # Posicionando la cola
        t.pendown()
        for _ in range(2):
            t.forward(15)
            t.right(90)
            t.forward(10)
            t.right(90)
        t.end_fill()
        
        

        # Ojos negros
        t.penup()
        t.goto(-200, -55)  # Posicionar el ojo derecho
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):
            t.forward(5)
            t.right(90)
        t.end_fill()

        t.penup()
        t.goto(-180, -55)  # Posicionar el ojo izquierdo
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):
            t.forward(5)
            t.right(90)
        t.end_fill()

        t.hideturtle()
    
    
    arbol()
    ardilla()
    turtle.penup()
    turtle.goto(0, -275)
    turtle.pendown()
    turtle.speed(10)
    turtle.write(f"Y así, el árbol Roble y la ardilla {name} vivieron felices para siempre en su bosque encantado.", align='center', font=('Arial', 16, 'normal'))
    clear_screen()
       
menu = """
Menú:
1. Secuencia 1
2. Secuencia 2
3. Secuencia 3
4. Secuencia 4
5. Secuencia 5
6. Salir
"""

variable = True


while True:
    print(menu)
    opcion = input("Seleccione una secuencia del 1 al 5 o Salir 6: ")
    if opcion == "1":
        panel1()
    elif opcion == "2":
        panel2()
    elif opcion == "3":
        panel3()
    elif opcion == "4":
        panel4()
    elif opcion == "5":
        panel5()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Solo elija un numero del menu.")

turtle.done()