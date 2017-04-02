#function file

def goto(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def instructions(t):
    t.right(10)
    t.forward(100)
    t.right(10)
    t.forward(50)
    t.left(99)
    t.forward(30)
    t.left(80)
    t.forward(3)
    t.left(-3)
    t.forward(30)
    t.left(20)
    t.forward(15)
    t.left(10)
    t.forward(5)
    for times in range(6):
        t.right(14)
        t.forward(7)
    t.left(4)
    t.forward(5)
    t.right(110)
    t.forward(55)
    t.left(10)
    t.forward(25)
    t.left(84)
    t.forward(40)
    t.right(120)
    t.forward(57)
    t.left(126)
    t.forward(75)
    t.left(48)
    t.forward(50)
    t.right(54)
    t.forward(35)
    t.left(110)
    t.forward(188)
    t.left(80)
    t.forward(128)

def Grayson(t):
    t.begin_fill()
    t.color('bisque')
    instructions(t)
    t.end_fill()

    t.color('black')
    goto(t,120,150)
    t.right(50)
    t.forward(35)
    t.left(90)
    t.forward(35)

    t.begin_fill()
    t.color('skyblue')
    goto(t,110,136)
    t.right(70)
    t.forward(12)
    t.left(40)
    t.forward(13)
    t.left(34)
    t.forward(12)
    t.left(100)
    t.forward(16)
    t.left(30)
    t.forward(10)
    t.left(30)
    t.forward(18)
    t.left(109)
    t.forward(12)
    t.end_fill()

    t.begin_fill()
    t.color('black')
    goto(t,121,136)
    t.forward(5)
    t.left(30)
    t.forward(15)
    t.left(42)
    t.forward(10)
    t.left(100)
    t.forward(3)
    t.left(30)
    t.forward(13)
    t.left(12)
    t.left(20)
    t.forward(10)
    t.forward(4)
    t.end_fill()

    t.color('white')
    goto(t,123,130)
    t.circle(1)
    
    t.color('black')
    goto(t,123,36)
    t.right(198)
    t.forward(29)
    t.right(100)
    t.forward(8)
    t.left(5)
    t.forward(21)
    for times in range(4):
        t.right(17)
        t.forward(8)
    t.right(117)
    t.forward(20)
    t.left(8)
    t.forward(20)
    t.left(8)
    t.forward(10)
    t.left(91)
    t.forward(7)
    t.left(92)
    t.forward(10)
    t.right(15)
    t.forward(22)
    t.right(2)
    t.forward(17)
    t.left(107)
    t.forward(15)
    for times in range(3):
        t.left(20)
        t.forward(3)
    t.left(15)
    t.forward(40)

    goto(t,83,47)
    t.left(190)
    for times in range(6):
        t.left(13)
        t.forward(4)
    
    goto(t,105,57)
    t.circle(.5)
    goto(t,124,60)
    t.circle(.5)
    goto(t,140,66)
    t.circle(.5)
    goto(t,140,48)
    t.circle(.5)
    goto(t,118,48)
    t.circle(.5)
    goto(t,65,17)
    t.circle(.5)
    goto(t,80,8)
    t.circle(.5)
    goto(t,95,3)
    t.circle(.5)
    goto(t,101,-1)
    t.circle(.5)
    goto(t,127,-3)
    t.circle(.5)
    goto(t,142,-8)
    t.circle(.5)
    goto(t,140,-25)
    t.circle(.5)
    goto(t,124,-17)
    t.circle(.5)
    goto(t,100,-11)
    t.circle(.5)
    goto(t,90,-5)
    t.circle(.5)
    goto(t,84,-3)
    t.circle(.5)
    goto(t,74,2)
    t.circle(.5)
    goto(t,63,-5)
    t.circle(.5)

    goto(t,48,119)
    t.right(114)
    t.forward(8)
    for times in range(11):
        t.left(9)
        t.forward(3)
    t.left(20)
    t.forward(18)
    t.left(40)
    t.forward(16)
    t.right(39)
    t.forward(3)
    t.left(45)
    t.forward(20)
    t.left(50)
    t.forward(7)
    t.left(50)
    t.forward(15)
    goto(t,49,42)
    t.begin_fill()
    t.color('gold')
    t.circle(14)
    t.end_fill()
    t.color('black')
    goto(t,45,88)
    t.left(95)
    t.forward(3)
    for times in range(9):
        t.right(9)
        t.forward(1)
    t.forward(5)
    for times in range(3):
        t.right(6)
        t.forward(3)
    t.left(101)
    t.forward(10)
    for times in range(9):
        t.left(11)
        t.forward(3)
    t.left(40)
    t.forward(20)
    goto(t,38,95)
    t.left(180)
    for times in range(6):
        t.left(5)
        t.forward(3)

def Nate(t):
    t.begin_fill()
    t.color('navajowhite')
    instructions(t)
    t.end_fill()

def Joyce(t):
    t.begin_fill()
    t.color('wheat')
    instructions(t)
    t.end_fill()
    
def Judy(t):
    t.begin_fill()
    t.color('BurlyWood')
    instructions(t)
    t.end_fill()    

def Susan(t):
    t.begin_fill()
    t.color('Tan')
    instructions(t)
    t.end_fill()

def Ethan(t):
    t.begin_fill()
    t.color('BlanchedAlmond')
    instructions(t)
    t.end_fill()

def Hailee(t):
    t.begin_fill()
    t.color('OldLace')
    instructions(t)
    t.end_fill()

def Stephan(t):
    t.begin_fill()
    t.color('Seashell')
    instructions(t)
    t.end_fill()

def Zain(t):
    t.begin_fill()
    t.color('FloralWhite')
    instructions(t)
    t.end_fill()

def Ally(t):
    t.begin_fill()
    t.color('Azure')
    instructions(t)
    t.end_fill()

def Jack(t):
    t.begin_fill()
    t.color('LightCyan')
    instructions(t)
    t.end_fill()    

def Stephanie(t):
    t.begin_fill()
    t.color('paleturquoise')
    instructions(t)
    t.end_fill()    
    
def Bryan(t):
    t.begin_fill()
    t.color('Powderblue')
    instructions(t)
    t.end_fill()    
        
def Albert(t):
    t.begin_fill()
    t.color('lightSkyblue')
    instructions(t)
    t.end_fill()    
        
def Mike(t):
    t.begin_fill()
    t.color('skyblue')
    instructions(t)
    t.end_fill()       
    
def Sharon(t):
    t.begin_fill()
    t.color('cornflowerblue')
    instructions(t)
    t.end_fill()       

def Jorge(t):
    t.begin_fill()
    t.color('dodgerblue')
    instructions(t)
    t.end_fill()       
        
def Tess(t):
    t.begin_fill()
    t.color('royalblue')
    instructions(t)
    t.end_fill()

def Maliya(t):
    t.begin_fill()
    t.color('lightgreen')
    instructions(t)
    t.end_fill()  

def Dimitri(t):
    t.begin_fill()
    t.color('mediumspringgreen')
    instructions(t)
    t.end_fill() 

def Shawn(t):
    t.begin_fill()
    t.color('springgreen')
    instructions(t)
    t.end_fill() 

def Andrew(t):
    t.begin_fill()
    t.color('lime')
    instructions(t)
    t.end_fill() 

def Shaima(t):
    t.begin_fill()
    t.color('limegreen')
    instructions(t)
    t.end_fill() 

def Kelsey(t):
    t.begin_fill()
    t.color('mediumseagreen')
    instructions(t)
    t.end_fill() 

def Tasha(t):
    t.begin_fill()
    t.color('seagreen')
    instructions(t)
    t.end_fill()
    
def George(t):
    t.begin_fill()
    t.color('forestgreen')
    instructions(t)
    t.end_fill() 

def Lolla(t):
    t.begin_fill()
    t.color('Green')
    instructions(t)
    t.end_fill() 

def Halsey(t):
    t.begin_fill()
    t.color('gainsboro')
    instructions(t)
    t.end_fill() 

def Ari(t):
    t.begin_fill()
    t.color('lightgrey')
    instructions(t)
    t.end_fill() 

def Emily(t):
    t.begin_fill()
    t.color('silver')
    instructions(t)
    t.end_fill() 

def Briana(t):
    t.begin_fill()
    t.color('darkgray')
    instructions(t)
    t.end_fill()     

def Juan(t):
    t.begin_fill()
    t.color('gray')
    instructions(t)
    t.end_fill()

def Malloy(t):
    t.begin_fill()
    t.color('DimGray')
    instructions(t)
    t.end_fill()
    
def Teala(t):
    t.begin_fill()
    t.color('lightslategray')
    instructions(t)
    t.end_fill() 

def Miana(t):
    t.begin_fill()
    t.color('slategray')
    instructions(t)
    t.end_fill()
    
def Kiara(t):
    t.begin_fill()
    t.color('darkslategray')
    instructions(t)
    t.end_fill() 

def Joanna(t):
    t.begin_fill()
    t.color('Thistle')
    instructions(t)
    t.end_fill()

def Zoe(t):
    t.begin_fill()
    t.color('plum')
    instructions(t)
    t.end_fill() 

def Lilly(t):
    t.begin_fill()
    t.color('violet')
    instructions(t)
    t.end_fill() 

def Daisy(t):
    t.begin_fill()
    t.color('orchid')
    instructions(t)
    t.end_fill() 

def William(t):
    t.begin_fill()
    t.color('mediumorchid')
    instructions(t)
    t.end_fill() 

def Jeff(t):
    t.begin_fill()
    t.color('Mediumpurple')
    instructions(t)
    t.end_fill() 

def Titus(t):
    t.begin_fill()
    t.color('blueviolet')
    instructions(t)
    t.end_fill() 

def Flora(t):
    t.begin_fill()
    t.color('darkviolet')
    instructions(t)
    t.end_fill() 

def Olivia(t):
    t.begin_fill()
    t.color('darkorchid')
    instructions(t)
    t.end_fill() 

def Hanna(t):
    t.begin_fill()
    t.color('Lightcoral')
    instructions(t)
    t.end_fill() 

def Eva(t):
    t.begin_fill()
    t.color('salmon')
    instructions(t)
    t.end_fill() 

def Charlie(t):
    t.begin_fill()
    t.color('Indianred')
    instructions(t)
    t.end_fill() 
    
def Quisha(t):
    t.begin_fill()
    t.color('Crimson')
    instructions(t)
    t.end_fill()

def Willy(t):
    t.begin_fill()
    t.color('red')
    instructions(t)
    t.end_fill() 

def Meredith(t):
    t.begin_fill()
    t.color('firebrick')
    instructions(t)
    t.end_fill() 

def Sierra(t):
    t.begin_fill()
    t.color('darkred')
    instructions(t)
    t.end_fill() 

def Alexa(t):
    t.begin_fill()
    t.color('maroon')
    instructions(t)
    t.end_fill() 

def Polly(t):
    t.begin_fill()
    t.color('rosybrown')
    instructions(t)
    t.end_fill()     
