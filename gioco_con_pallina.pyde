x=80
y=80
XR=0
XR2=0
HR=375
HR2=0
Verx=1
Very=1
raggio=50
PuntiG1=0
PuntiG2=0
def setup ():
     size(600,400)
     
def draw():
    global Verx,Very,raggio,x,y,XR,XR2,HR,PuntiG1,PuntiG2,Verx, Very
    background(0, 0, 0)
    fill(255,255,255)
    ellipse (x,y,20,20)
    x=x+(3*Verx)
    y=y+(3*Very)
    if y>=HR-(20/2) and (x+(20/2)>XR and x-(20/2)<XR+80): 
        Very*=-1
    if y<=HR2+35 and (x+(20/2)>XR2 and x-(20/2)<XR2+80):
       Very*=-1
    if x>width or x<=0:
        Verx*=-1
    if y>height or y<=0:
        Very*=-1
    if y<0:
        PuntiG1=PuntiG1+10
    if y>=height:
        PuntiG2=PuntiG2+10
    if XR2>=width-50:
        XR2=XR2-50
    if XR>=width-50:
        XR=XR-50
    if XR<0:
        XR*=-1
    if XR2<0:
        XR2*=-1
    if PuntiG1>=100:
        textSize(50)
        fill(255,0,0)
        text("Giocatore 1 vince", 100,200)
        delay(1000)
    if PuntiG2>=100:
         textSize(50)
         fill(0,0,255)
         text("Giocatore 2 vince", 100,200)
         delay(1000)
    fill (255 )
    textSize ( 30 )
    fill(0,120,255)
    text ( PuntiG2, 0,50 )
    fill (255 )
    textSize ( 30 )
    fill(255,120,0)
    text ( PuntiG1, 10,375 )
    fill(255,120,0)
    rect(XR,HR,80,25)
    fill(0,120,255)
    rect(XR2,HR2,80,25)

def keyPressed():
    global XR, Verx,XR2
    if keyCode == LEFT:
        XR=XR-25
    if keyCode == RIGHT:
        XR=XR+25
    if key == "a":
        XR2=XR2-25
    if key == "d":
           XR2=XR2+25
