speed(1000)
penup()

beadCount=36
beadRadius=10
bracletDiameter=200
bracletRadius=100


def bead_draw():
    pendown()
    begin_fill()
    circle(beadRadius)
    end_fill()
    penup()
    goto(0,0)   
   
for i in range(36):
    print(i%3)
    loopColor=i%3
    forward(bracletRadius)
    if loopColor==2:
        color("purple")
    if loopColor==1:
        color("blue")
    if loopColor==0:
        color("red")    
            
    bead_draw()
    left(10)

#for bead braclet
