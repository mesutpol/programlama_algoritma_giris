import turtle
# Ekranı hazırla
ekran=turtle.Screen()
ekran.title("ekrana çizgi çizdiren program ")
ekran.bgcolor("white")
# Turtle nesnesini oluştur
pen=turtle.Turtle()
pen.speed(50)  # Çizgi çizme hızı

# Yön tuşlarına basıldığında çağrılacak fonksiyonlar
def yukarı():
    pen.setheading(90)  # Yukarı yönde hareket et
    pen.forward(5)       # 5 birim ileri git
def asagı():
    pen.setheading(270) # Aşağı yönde hareket et
    pen.forward(5)       # 5 birim ileri git
def geri():
    pen.setheading(180)  # Sola doğru hareket et
    pen.forward(5)       # 5 birim ileri git
def ileri():
    pen.setheading(0)  # Sağa doğru hareket et
    pen.forward(5)     # 5 birim ileri git

# Yön tuşlarına basıldığında ilgili fonksiyonları bağla
ekran.listen()
ekran.onkey(yukarı,"Up")
ekran.onkey(asagı,"Down")
ekran.onkey(ileri,"Right")
ekran.onkey(geri,"Left")

# Programı çalıştır
turtle.done()