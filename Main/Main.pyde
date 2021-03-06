from random import randint

###Global Data
#screensize:
screen_xSize = 1200
screen_ySize = 800

#btn_size
buttonWidth = 12.5
buttonHeight = 5

## instruction font size, height, box radius.
textsize = 24
firstLine = 400
radius = 25

#Menu data
tabs = [0, 1, 2, 3, 4]
tabNames = ['Spel overzicht', 'Duelleren', 'Shortcut', 'Kaartregels', 'Namen']
activeTab = 0

# Initial data of Dueleren
# amount of dices Attacker have
diceCount = 4

#Dice images
dice = []

#2 seperate List of Dice Result
diceRes= []
diceResV=[]

#Dice BTN names
choices= ['3 dobbelstenen','4 dobbelstenen']


# Loaded images of Kaart into kaart.
kaart = []

# Initial Data for Namen
spelerNamen = {"speler1":"", "speler2":"", "speler3":"", "speler4":""}
selected_field = None

#Switch on/off
blinkTime = millis()
blinkOn = True
blinkLine = ""

#Spinning Wheel
rad = []
Rad_number = 0


# Initial Data for GegevensOverzicht
Rood_tegen_Groen = 0
Rood_tegen_Blauw = 0
Rood_tegen_Geel = 0
Groen_tegen_Rood = 0
Groen_tegen_Blauw = 0
Groen_tegen_Geel = 0
Blauw_tegen_Rood = 0
Blauw_tegen_Groen = 0
Blauw_tegen_Geel = 0
Geel_tegen_Rood = 0
Geel_tegen_Groen = 0
Geel_tegen_Blauw = 0
Rood_Gevangenis = 0
Groen_Gevangenis = 0
Blauw_Gevangenis = 0
Geel_Gevangenis = 0
Rood_Boer = 0
Groen_Boer = 0
Blauw_Boer = 0
Geel_Boer = 0
Rood_Reeks = 0
Groen_Reeks = 0
Blauw_Reeks = 0
Geel_Reeks = 0

def setup():
    global screen_xSize, screen_ySize
    global kaart, rad
    global bg_img, plus, minus, resetknop, dice
    size(screen_xSize, screen_ySize)
    bg_img = loadImage("background_img.png")
    plus = loadImage("Pluse.jpg")
    minus = loadImage("min.jpg")
    rad.append(loadImage("rad_default.jpg"))
    dice.append(loadImage( "dice_wit.jpg"))
    resetknop =  loadImage('resetknop.png')
    resetknop.resize(50,50)
    noStroke()
    
    # Kaart photo saved to kaart list
    for i in range (1,14):
        kaart.append(loadImage(str(i)+".jpg"))    
        
    # Rad photo's save to rad list.
    for i in range(1, 3):
        rad.append(loadImage("rad"+str(i)+".jpg"))

    # Dueleren Dice photo save variable
    for i in range(1,7):
       dice.append(loadImage("dice_"+str(i)+".png")) 

def menuButton():
    global screen_xSize, screen_ySize
    global tabs
    for tab in tabs:
        fill(150)
        stroke(150)
        rect(20+(tabs[tab]*200), 10, 180, 50, 10)
        noStroke()
        noFill()
    noStroke()
    fill(200)    
    button(0, 70, screen_xSize, 30)
    noFill()
def menuText():
    global tabNames
    for x in range(len(tabNames)):   
        fill(0,0,0)
        fonts("Arial Bold Italic", 20, True)
        textAlign(CENTER,CENTER)
        text(tabNames[x], 20+(x*200), 10, 180, 50)
        noFill()

def draw_bg(x, screen_xSize, screen_ySize):
    redraw()
    x.resize(screen_xSize, screen_ySize)
    x = background(x)
    return x

def active(type):
    if type == 'menu':
        return fill(255,255,0)
    
    if type == 'diceChoiceBtn':
        return fill(255,200,0)
    
    if type == 'instruction':
        return fill(100,0,100)
    
def button(x1,y1,x2,y2,radius = 0):
    stroke(150)
    rect(x1,y1,x2,y2,radius)
    noStroke()
        
def fonts(font_type,font_size, state):
    return textFont(createFont(font_type,font_size, state))

def field_colors(field):
    if field == 1: return fill(255,0,0)
    if field == 2: return fill(0,255,0)
    if field == 3: return fill(50,70,255)
    if field == 4: return fill(255,255,0)

def OverzichtGegevens():
    global spelerNamen, plus, minus
    global textsize, firstLine, radius
    textAlign(CENTER)
    stroke(0,0,0)
    for x in range(0,3):
        fill(0,0,0)
        rect(90,120+(x*20),858,20)
    fill(255,255,255)
    fonts("Arial Bold", 20, True)
    text("Gegevens overzicht van het spel", 200, 120, 700,25)
    
    fill(255,255,255)
    fonts("Arial Bold", 17, True)
    text('Verslagen kleur', 250, 140, 398, 25)
    textAlign(CENTER)
    text('Gevangenis', 650, 160, 100, 180)
    text('Boer', 750, 160, 100, 180)
    text('Reeks', 850, 160, 100, 180)
    noFill()
    noStroke()
    
    #Reset button
    fill(200,200,200)
    button(screen_xSize/100*8, screen_ySize/100*35, 100, 35, 15)
    fill(0,0,0)
    textAlign(CENTER,CENTER)
    text('RESET',screen_xSize/100*8, screen_ySize/100*35, 100,35)
    noFill() 
    
    
    fonts("Arial", 19, True)
    for x in range(len(spelerNamen)):
        stroke(0,0,0)
        field_colors(x+1)
        rect(90, 180+(x*20), 158, 20)  #column 1
        fill(255,255,255)
        rect(248, 180+(x*20), 700, 20) #column 2
        noFill()
        noStroke()
    
    for x in range(len(spelerNamen)):#horizontale kolom1
        fill(0,0,0)
        textAlign(LEFT)
        if len(spelerNamen["speler"+str(x+1)]) > 0:
            text(str(spelerNamen["speler"+str(x+1)]), 100, 195+(x*20))
        else:
            text("speler"+str(x+1), 100, 195+(x*20))
        noFill()
    for x in range(4):
        fill(155,155,155)
        stroke(0)
        rect(248+(x*100), 180+(x*20), 100, 20)
        noStroke()
        noFill()

    for x in range(5):#tabel
        if x < 4:
            stroke(0,0,0)
            field_colors(x+1)
            rect(248+(x*100), 160, 100, 20)
            noFill()
        stroke(0,0,0)
        line(248+(x*100),180,248+(x*100),260)
        noStroke()
        
    for x in range(3):#tabel2
        stroke(255,255,255)
        line(648+(x*100), 160, 648+(x*100), 180)
        stroke(0,0,0)
        line(648+(x*100), 180, 648+(x*100), 260)
        noStroke()
    
    fill(0,0,0)    
    #kolom 1
    image(minus,250,201,18,18)
    image(minus,250,222,18,18)
    image(minus,250,242,18,18)
    image(minus,250,242,18,18)
    
    image(plus,330,201,18,18)
    image(plus,330,222,18,18)
    image(plus,330,242,18,18)
    
    text(str(Groen_tegen_Rood),295,201,313,219)
    text(str(Blauw_tegen_Rood),295,222,313,219)
    text(str(Geel_tegen_Rood),295,242,313,219)
    
    #kolom 2
    image(minus,350,181,18,18)
    image(minus,350,222,18,18)    
    image(minus,350,242,18,18)
    
    image(plus,430,181,18,18)
    image(plus,430,222,18,18)
    image(plus,430,242,18,18)
    
    text(str(Rood_tegen_Groen),395,181,413,219)
    text(str(Blauw_tegen_Groen),395,222,413,219)
    text(str(Geel_tegen_Groen),395,242,413,219)
    
    #kolom 3
    image(minus,450,181,18,18)
    image(minus,450,202,18,18)
    image(minus,450,242,18,18)
    
    image(plus,530,181,18,18)
    image(plus,530,202,18,18)
    image(plus,530,242,18,18)
    
    text(str(Rood_tegen_Blauw),495,181,413,219)
    text(str(Groen_tegen_Blauw),495,202,413,219)
    text(str(Geel_tegen_Blauw),495,242,413,219)
    
    #kolom 4
    image(minus,550,181,18,18)
    image(minus,550,202,18,18)
    image(minus,550,222,18,18)
    
    image(plus,630,181,18,18)
    image(plus,630,202,18,18)
    image(plus,630,222,18,18)
    
    text(str(Rood_tegen_Geel),595,181,413,219)
    text(str(Groen_tegen_Geel),595,202,413,219)
    text(str(Blauw_tegen_Geel),595,222,413,219)
    
    #kolom 5
    image(minus,650,181,18,18)
    image(minus,650,202,18,18)
    image(minus,650,222,18,18)
    image(minus,650,242,18,18)
    
    image(plus,730,181,18,18)
    image(plus,730,202,18,18)
    image(plus,730,222,18,18)
    image(plus,730,242,18,18)
    
    text(str(Rood_Gevangenis),695,181,413,219)
    text(str(Groen_Gevangenis),695,202,413,219)
    text(str(Blauw_Gevangenis),695,222,413,219)
    text(str(Geel_Gevangenis),695,242,413,219)
    
    #kolom 6
    image(minus,750,181,18,18)
    image(minus,750,202,18,18)
    image(minus,750,222,18,18)
    image(minus,750,242,18,18)
    
    image(plus,830,181,18,18)
    image(plus,830,202,18,18)
    image(plus,830,222,18,18)
    image(plus,830,242,18,18)
    
    text(str(Rood_Boer),795,181,413,219)
    text(str(Groen_Boer),795,202,413,219)
    text(str(Blauw_Boer),795,222,413,219)
    text(str(Geel_Boer),795,242,413,219)
    
    #kolom 7
    image(minus,850,181,18,18)
    image(minus,850,202,18,18)
    image(minus,850,222,18,18)
    image(minus,850,242,18,18)
    
    image(plus,930,181,18,18)
    image(plus,930,202,18,18)
    image(plus,930,222,18,18)
    image(plus,930,242,18,18)
    
    text(str(Rood_Reeks),895,181,413,219)
    text(str(Groen_Reeks),895,202,413,219)
    text(str(Blauw_Reeks),895,222,413,219)
    text(str(Geel_Reeks),895,242,413,219)    
    noFill()
    
    ## Instruction box bg color
    fill(200,200,200,150)
    rect(screen_xSize/100*5, 390, screen_xSize/100*90, 328, radius)
    noFill()
    ## Instruction text
    active('instruction')
    fonts("Ariel", textsize, False)
    textAlign(LEFT)
    text('Instructies:', screen_xSize/100*5+10, firstLine, screen_xSize/100*90,textsize*1.5)
    fonts("Ariel", textsize-4, False)
    margin = textsize*2
    text("Vul eerst uw naam in bij de tab \"Namen\".", screen_xSize/100*5+10, firstLine+(margin), screen_xSize/100*90,textsize*1.5)
    text("Gebruik dit overzicht om alles bij te houden gedurende spelronde.", screen_xSize/100*5+10, firstLine+(margin*2), screen_xSize/100*80,textsize*1.5)
    text("Wanneer een winnaar bekend is van het spel, druk op de \"RESET\" knop om alles terug te zetten naar 0.", screen_xSize/100*5+10, firstLine+(margin*3), screen_xSize/100*90,textsize*1.5)
    text('Gebruik de tab \"Dueleren\" wanneer je iemand aanvalt.', screen_xSize/100*5+10, firstLine+(margin*4), screen_xSize/100*90,textsize*1.5)
    text('Gebruik de tab \"Shortcut\" wanneer je op het kruisingspunt zit voor de shortcut.', screen_xSize/100*5+10, firstLine+(margin*5), screen_xSize/100*90,textsize*1.5)
    text('Gebruik de tab \"Kaartregels\" als je de regels wilt weten van elke kaart.', screen_xSize/100*5+10, firstLine+(margin*6), screen_xSize/100*90,textsize*1.5)
    noFill()
    
def Reset(What2Reset):
    if What2Reset == 'OverzichtGegevens':
        global Rood_tegen_Groen,Rood_tegen_Blauw, Rood_tegen_Geel
        global Groen_tegen_Rood, Groen_tegen_Blauw,Groen_tegen_Geel
        global Blauw_tegen_Rood,Blauw_tegen_Groen,Blauw_tegen_Geel
        global Geel_tegen_Rood,Geel_tegen_Groen,Geel_tegen_Blauw
        global Rood_Gevangenis,Groen_Gevangenis,Blauw_Gevangenis,Geel_Gevangenis
        global Rood_Boer,Groen_Boer,Blauw_Boer,Geel_Boer 
        global Rood_Reeks, Groen_Reeks, Blauw_Reeks,Geel_Reeks
        Rood_tegen_Groen = 0
        Rood_tegen_Blauw = 0
        Rood_tegen_Geel = 0
        Groen_tegen_Rood = 0
        Groen_tegen_Blauw = 0
        Groen_tegen_Geel = 0
        Blauw_tegen_Rood = 0
        Blauw_tegen_Groen = 0
        Blauw_tegen_Geel = 0
        Geel_tegen_Rood = 0
        Geel_tegen_Groen = 0
        Geel_tegen_Blauw = 0
        Rood_Gevangenis = 0
        Groen_Gevangenis = 0
        Blauw_Gevangenis = 0
        Geel_Gevangenis = 0
        Rood_Boer = 0
        Groen_Boer = 0
        Blauw_Boer = 0
        Geel_Boer = 0
        Rood_Reeks = 0
        Groen_Reeks = 0
        Blauw_Reeks = 0
        Geel_Reeks = 0
    
    if What2Reset == 'Dices':
        global diceRes
        global diceResV
        diceRes= []
        diceResV=[]
                                                                                    
def Duel():
    global resetknop, diceCount, dice, diceRes, diceResV 
    global sumA,sumB
    
    fill(255,255,240) 
    rect(0,250,screen_xSize/100 * 80,50)# White Bar 1 
    rect(0,550,screen_xSize/100 * 80,50)# White Bar 2 
    
    textSize(30)
    textAlign(LEFT,CENTER)
    fill(50,50,50)
    text('Aanvaller',40,250,200,50)
    text('Verdediger',40,550,200,50)
    
    textAlign(CENTER,CENTER)
    
    # Dice 3 and 4 buttons
    fill(255,0,0)
    button(300,110,200,50, radius =50)
    button(550,110,200,50, radius =50)
    active('diceChoiceBtn')
    for x in range(2):
        if diceCount == 4:
            button(550,110,200,50, radius =50)
            noFill()
        elif diceCount == 3:
            button(300,110,200,50, radius =50)
            noFill()
        textSize(20)
        fill(0,0,0)
        text(choices[x],300+(x*250), 110, 200, 50)
        noFill()

        #Roll & Reset buttons
        for i in range (2):
            fill(255,0,0)
            stroke(255,0,0)
            rect(300+(i*500), 175, 130, 50, 150)
            noStroke()
            noFill()
    
    textAlign(CENTER)
    textSize(20)
    fill(255,0,0,170)
    rect(10,110,250,90,25) #red bubble instructions
    fill(255,255,255)
    text('Kies het aantal dobbelsten en rol daarna de dobbelstenen.',10,110,250,200)    
    
    textSize(23)
    textAlign(CENTER,CENTER)
    fill(255,255,255)
    text('Rol',300,175,130,50)
    noFill()
    image(resetknop,845,175)

    win()
    
    if sumA  == 0:
        for x in range(diceCount):
            image(dice[0], 20+(x*200), 320)
    else:   
        y1 = 0   
        for a in diceRes:
            image(dice[a], 20+(y1*200),320)
            y1 += 1
    
    if sumB == 0:
        for x in range(3):
            image(dice[0], 20+(x*200),620)
    else:
        y2 = 0       
        for a in diceResV:
            image(dice[a],20+(y2*200),620)
            y2 += 1
    
    
    
def win():
    global diceRes, diceResV
    global sumA,sumB
    sumA = sum(diceRes)
    sumB = sum(diceResV)
    
    # show total points by default
    fill(255,0,0)
    textSize(30)
    textAlign(CENTER,CENTER)
    text('Totaal: '+str(sumA),((screen_xSize/100) * 75) - 150,250,200,50)
    text('Totaal: '+str(sumB),((screen_xSize/100) * 75) - 150,550,200,50)
    
    textAlign(LEFT,CENTER)
    if sumA >= 3 and sumB >= 3:
        if  sumA > sumB:
            text('wint!', 245,250,700,50) # display text in the White Bar 1
        elif sumA < sumB:
            text('wint!', 245,550,700,50) # display text in the White Bar 2
        elif sumA == sumB:
            text('Gelijkspel, gooi nog een keer!', 245,250,700,50) # display text in the input field box
            text('Gelijkspel, gooi nog een keer!', 245,550,700,50) # display text in the input field box

    noFill()
    textSize(18)   

def roll_dice():
    global diceCount
    global diceRes, diceResV
    
    x = 0
    y = 0
    while x < diceCount:
        diceRes.append(randint(1,6))
        x+=1
    
    while y < 3:
        diceResV.append(randint(1,6))
        y+=1
    
    
         
def Spin_rad():
    global Rad_number
    Rad_number = randint(1,2)

def RadPage():
    global Rad_number
    
    fill(255,255,255)
    button(400, 250, 200, 40, 50)

    fill(0,0,0)
    fonts('Ariel',18, True)
    textAlign(CENTER, CENTER)
    text("Rol het rad!", 400, 250, 200, 40) 
    noFill()
    
    if Rad_number == 0:
        image(rad[0],300,300)
    else:
        image(rad[Rad_number],300,300)
    

    
def Kaartregels():
    global kaart, screen_xSize, screen_ySize
    card_width =  150 #150 px width card
    card_height = 250 #250 px height card
    cardText_width =  133 #5 px margin from x start x position ,card 133px
    cardText_height = 195 #40 px margin from y position,card 195px
    left_margin= screen_xSize/100*25 #margin from left 25%
    card = 0
    for yRow in range(4):
        for xRow in range(5):
            if card < 13:
                # left_margin/2 = 150px
                image(kaart[card],left_margin/2 + (xRow*card_width), 100 +(card_height*yRow))
                card+=1

    fill(140,0,0)
    fonts("Arial Bold Italic", 14, True)
    textAlign (LEFT)
    # text box with auto wrap (x,y, from x, from y)
    Aas = "Een pion uit het startveld op eigen startpositie (vlag icoontje) zetten of een pion 1 plaats vooruit zetten." 
    text(Aas, left_margin/2 + 5 + (cardText_width*0), 100 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Twee = "Bij deze kaart moet je je pion twee stappen vooruit zetten."
    text(Twee, left_margin/2 + 22 + (cardText_width*1), 100 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Drie = "Bij deze kaart moet je je pion drie stappen vooruit zetten."
    text(Drie, left_margin/2 + 22 + (cardText_width*2+20), 100 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Vier = "Bij deze kaart moet je je pion vier stappen achteruit zetten." 
    text(Vier,left_margin/2 +22+ (cardText_width*3+35),100 + ( cardText_height*0)+40, cardText_width-11,cardText_height-40)
    Vijf = "Bij deze kaart moet je je pion vijf stappen vooruit zetten."
    text(Vijf,left_margin/2 +22+ (cardText_width*4+50),100 + (cardText_height*0)+40, cardText_width-11,cardText_height-40)
    Zes = "Bij deze kaart moet je je pion zes stappen vooruit zetten."
    text(Zes, left_margin/2 + 5 + (cardText_width*0), 350+ (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Zeven = "Bij deze kaart kan je je pion zeven stappen vooruit zetten of splietsen over twee pionnen."
    text(Zeven, left_margin/2 + 22 + (cardText_width*1), 350+ (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Acht = "Bij deze kaart moet je je pion acht stappen vooruit zetten."
    text(Acht, left_margin/2 + 22 + (cardText_width*2+20),350+ (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Negen = "Bij deze kaart moet je je pion negen stappen vooruit zetten."
    text(Negen,left_margin/2 +22+ (cardText_width*3+35),350 + ( cardText_height*0)+40, cardText_width-11,cardText_height-40)
    Tien = "Bij deze kaart moet je je pion tien stappen vooruit zetten."
    text(Tien,left_margin/2 +22+ (cardText_width*4+50),350+ (cardText_height*0)+40, cardText_width-11,cardText_height-40)
    Boer = "Een eigen pion met een pion van een andere speler omruilen."
    text(Boer, left_margin/2 + 5 + (cardText_width*0), 600+ (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Vrouw = "Een pion twaalf plaatsen vooruit zetten."
    text(Vrouw, left_margin/2 + 22 + (cardText_width*1), 600 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Heer = "Een pion uit het startveld op eigen startpositie(vlag icoontje) zetten."
    text(Heer, left_margin/2 + 22 + (cardText_width*2+20), 600 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)

    noFill()


def Names():
    global spelerNamen
    global blinkTime, blinkOn, blinkLine
    
    # Table name    
    textAlign(CENTER)
    stroke(0,0,0)
    fill(0,0,0)
    rect(90,120,508,20)
    fill(255,255,255)
    fonts("Arial Bold", 18, True)
    text("Vul uw naam hier onder in:", 200, 120, 398,25)
    noFill()
    noStroke()
    
    
    fonts("Arial", 16, True)
    for x in range(len(spelerNamen)):
        stroke(0,0,0)
        field_colors(x+1)
        rect(90, 140+(x*20), 108, 20)  #column 1
        
        fill(0,0,0)# Text color
        textAlign(LEFT) # text alignment
        text("speler" + str(x+1), 100, 155+(x*20)) #player1-4 column 1
        
        noFill()
        
        # highlight selected field upon click or Tab.
        if (x+1) == selected_field:
            fill(255,255,160)
            rect(198, 140+(x*20), 400, 20) #column 2
            fill(0,0,0)
            text(str(spelerNamen["speler"+str(x+1)])+blinkLine, 200, 155+(x*20)) # display text in the input field box
        else:
            fill(255,255,255)
            rect(198, 140+(x*20), 400, 20) #column 2
            fill(0,0,0)
            text(str(spelerNamen["speler"+str(x+1)]), 200, 155+(x*20))
        noFill()
        noStroke()
        
    if blinkOn:
        fill(0,0,0)
        blinkLine = "|"
        noFill()
    else:
        blinkLine = ""
        
    if (millis() - 250 > blinkTime):
        blinkTime = millis()
        blinkOn = not blinkOn

def mousePressed():
    global Rood_tegen_Groen,Rood_tegen_Blauw, Rood_tegen_Geel
    global Groen_tegen_Rood, Groen_tegen_Blauw,Groen_tegen_Geel
    global Blauw_tegen_Rood,Blauw_tegen_Groen,Blauw_tegen_Geel
    global Geel_tegen_Rood,Geel_tegen_Groen,Geel_tegen_Blauw
    global Rood_Gevangenis,Groen_Gevangenis,Blauw_Gevangenis,Geel_Gevangenis
    global Rood_Boer,Groen_Boer,Blauw_Boer,Geel_Boer 
    global Rood_Reeks, Groen_Reeks, Blauw_Reeks,Geel_Reeks
    global diceCount
    global activeTab
    global selected_field
    
    if mouseButton == LEFT:
        if mouseX > 20 and mouseX < 200 and mouseY > 10 and mouseY < 60:
            activeTab = 0
        if mouseX > 220 and mouseX < 400 and mouseY > 10 and mouseY < 60:
            activeTab = 1
        if mouseX > 420 and mouseX < 600 and mouseY > 10 and mouseY < 60:
            activeTab = 2
        if mouseX > 620 and mouseX < 800 and mouseY > 10 and mouseY < 60:   
            activeTab = 3
        if mouseX > 820 and mouseX < 1000 and mouseY > 10 and mouseY < 60: 
            activeTab = 4
        
        #OverzichtGegevens page
        if activeTab == 0:
            #kolom 1
            if mouseX > 250 and mouseX < 268  and mouseY > 201 and mouseY < 219:
                if Groen_tegen_Rood > 0:
                    Groen_tegen_Rood = Groen_tegen_Rood - 1    
            elif mouseX > 330 and mouseX < 348  and mouseY > 201 and mouseY < 219:
                Groen_tegen_Rood = Groen_tegen_Rood + 1
            elif mouseX > 250 and mouseX < 268  and mouseY > 222 and mouseY < 240:
                if Blauw_tegen_Rood > 0:
                    Blauw_tegen_Rood = Blauw_tegen_Rood - 1
            elif mouseX > 330 and mouseX < 348  and mouseY > 222 and mouseY < 240:
                Blauw_tegen_Rood = Blauw_tegen_Rood + 1
            elif mouseX > 250 and mouseX < 268  and mouseY > 242 and mouseY < 260:
                if Geel_tegen_Rood > 0:
                    Geel_tegen_Rood = Geel_tegen_Rood - 1
            elif mouseX > 330 and mouseX < 348  and mouseY > 242 and mouseY < 260:
                Geel_tegen_Rood = Geel_tegen_Rood + 1
            #kolom 2
            elif mouseX > 350 and mouseX < 368  and mouseY > 182 and mouseY < 200:
                if Rood_tegen_Groen > 0:
                    Rood_tegen_Groen = Rood_tegen_Groen - 1
            elif mouseX > 430 and mouseX < 448  and mouseY > 182 and mouseY < 200:
                Rood_tegen_Groen = Rood_tegen_Groen + 1
            elif mouseX > 350 and mouseX < 368  and mouseY > 222 and mouseY < 240:
                if Blauw_tegen_Groen > 0:
                    Blauw_tegen_Groen = Blauw_tegen_Groen - 1
            elif mouseX > 430 and mouseX < 448  and mouseY > 222 and mouseY < 240:
                Blauw_tegen_Groen = Blauw_tegen_Groen + 1
            elif mouseX > 350 and mouseX < 368  and mouseY > 242 and mouseY < 260:
                if Geel_tegen_Groen > 0:
                    Geel_tegen_Groen = Geel_tegen_Groen - 1
            elif mouseX > 430 and mouseX < 448  and mouseY > 242 and mouseY < 260:
                Geel_tegen_Groen = Geel_tegen_Groen + 1
            #kolom 3
            elif mouseX > 450 and mouseX < 468  and mouseY > 181 and mouseY < 199:
                if Rood_tegen_Blauw > 0:
                    Rood_tegen_Blauw = Rood_tegen_Blauw - 1
            elif mouseX > 530 and mouseX < 548  and mouseY > 181 and mouseY < 191:
                Rood_tegen_Blauw = Rood_tegen_Blauw + 1
            elif mouseX > 450 and mouseX < 468  and mouseY > 202 and mouseY < 220:
                if Groen_tegen_Blauw > 0:
                    Groen_tegen_Blauw = Groen_tegen_Blauw - 1
            elif mouseX > 530 and mouseX < 548  and mouseY > 202 and mouseY < 220:
                Groen_tegen_Blauw = Groen_tegen_Blauw + 1
            elif mouseX > 450 and mouseX < 468  and mouseY > 242 and mouseY < 260:
                if Geel_tegen_Blauw > 0:
                    Geel_tegen_Blauw = Geel_tegen_Blauw - 1
            elif mouseX > 530 and mouseX < 548  and mouseY > 242 and mouseY < 260:
                Geel_tegen_Blauw = Geel_tegen_Blauw + 1
            #kolom 4
            elif mouseX > 550 and mouseX < 568  and mouseY > 181 and mouseY < 199:
                if Rood_tegen_Geel > 0:
                    Rood_tegen_Geel = Rood_tegen_Geel - 1
            elif mouseX > 630 and mouseX < 648  and mouseY > 181 and mouseY < 199:
                Rood_tegen_Geel = Rood_tegen_Geel + 1
            elif mouseX > 550 and mouseX < 568  and mouseY > 202 and mouseY < 220:
                if Groen_tegen_Geel > 0:
                    Groen_tegen_Geel = Groen_tegen_Geel - 1
            elif mouseX > 630 and mouseX < 648  and mouseY > 202 and mouseY < 220:
                Groen_tegen_Geel = Groen_tegen_Geel + 1
            elif mouseX > 550 and mouseX < 568  and mouseY > 222 and mouseY < 240:
                if Blauw_tegen_Geel > 0:
                    Blauw_tegen_Geel = Blauw_tegen_Geel - 1
            elif mouseX > 630 and mouseX < 648  and mouseY > 222 and mouseY < 240:
                Blauw_tegen_Geel = Blauw_tegen_Geel + 1
            #kolom 5
            elif mouseX > 650 and mouseX < 668  and mouseY > 181 and mouseY < 199:
                if Rood_Gevangenis > 0:
                    Rood_Gevangenis = Rood_Gevangenis - 1
            elif mouseX > 730 and mouseX < 748  and mouseY > 181 and mouseY < 199:
                Rood_Gevangenis = Rood_Gevangenis + 1
            elif mouseX > 650 and mouseX < 668  and mouseY > 202 and mouseY < 220:
                if Groen_Gevangenis > 0:
                    Groen_Gevangenis = Groen_Gevangenis - 1
            elif mouseX > 730 and mouseX < 748  and mouseY > 202 and mouseY < 220:
                Groen_Gevangenis = Groen_Gevangenis + 1
            elif mouseX > 650 and mouseX < 668  and mouseY > 222 and mouseY < 240:
                if Blauw_Gevangenis > 0:
                    Blauw_Gevangenis = Blauw_Gevangenis - 1
            elif mouseX > 730 and mouseX < 748  and mouseY > 222 and mouseY < 240:
                Blauw_Gevangenis = Blauw_Gevangenis + 1
            elif mouseX > 650 and mouseX < 668  and mouseY > 242 and mouseY < 260:
                if Geel_Gevangenis > 0:
                    Geel_Gevangenis = Geel_Gevangenis - 1
            elif mouseX > 730 and mouseX < 748  and mouseY > 242 and mouseY < 260:
                Geel_Gevangenis = Geel_Gevangenis + 1
            #kolom 6
            elif mouseX > 750 and mouseX < 768  and mouseY > 181 and mouseY < 199:
                if Rood_Boer > 0:
                    Rood_Boer = Rood_Boer - 1
            elif mouseX > 830 and mouseX < 848  and mouseY > 181 and mouseY < 199:
                Rood_Boer = Rood_Boer + 1
            elif mouseX > 750 and mouseX < 768  and mouseY > 202 and mouseY < 220:
                if Groen_Boer > 0:
                    Groen_Boer = Groen_Boer - 1
            elif mouseX > 830 and mouseX < 848  and mouseY > 202 and mouseY < 220:
                Groen_Boer = Groen_Boer + 1
            elif mouseX > 750 and mouseX < 768  and mouseY > 222 and mouseY < 240:
                if Blauw_Boer > 0:
                    Blauw_Boer = Blauw_Boer - 1
            elif mouseX > 830 and mouseX < 848  and mouseY > 222 and mouseY < 240:
                Blauw_Boer = Blauw_Boer + 1
            elif mouseX > 750 and mouseX < 768  and mouseY > 242 and mouseY < 260:
                if Geel_Boer > 0:
                    Geel_Boer = Geel_Boer - 1
            elif mouseX > 830 and mouseX < 848  and mouseY > 242 and mouseY < 260:
                Geel_Boer = Geel_Boer + 1
            #kolom 7
            elif mouseX > 850 and mouseX < 868  and mouseY > 181 and mouseY < 199:
                if Rood_Reeks > 0:
                    Rood_Reeks = Rood_Reeks - 1
            elif mouseX > 930 and mouseX < 948  and mouseY > 181 and mouseY < 199:
                Rood_Reeks = Rood_Reeks + 1
            elif mouseX > 850 and mouseX < 868  and mouseY > 202 and mouseY < 220:
                if Groen_Reeks > 0:
                    Groen_Reeks = Groen_Reeks - 1
            elif mouseX > 930 and mouseX < 948  and mouseY > 202 and mouseY < 220:
                Groen_Reeks = Groen_Reeks + 1
            elif mouseX > 850 and mouseX < 868  and mouseY > 222 and mouseY < 240:
                if Blauw_Reeks > 0:
                    Blauw_Reeks = Blauw_Reeks - 1
            elif mouseX > 930 and mouseX < 948  and mouseY > 222 and mouseY < 240:
                Blauw_Reeks = Blauw_Reeks + 1
            elif mouseX > 850 and mouseX < 868  and mouseY > 242 and mouseY < 260:
                if Geel_Reeks > 0:
                    Geel_Reeks = Geel_Reeks - 1
            elif mouseX > 930 and mouseX < 948  and mouseY > 242 and mouseY < 260:
                Geel_Reeks = Geel_Reeks + 1
            elif mouseX > screen_xSize/100*7 and  mouseY > screen_ySize/100*35 and mouseX < screen_xSize/100*7 + 100 and mouseY < screen_ySize/100*35 +35 :
                Reset('OverzichtGegevens')
        
        # if activeTab == 2:
        #     if (mouseX > 400) and (mouseX <600) and (mouseY >250) and (mouseY < 290):
        #         Spin_rad()
        
        #Dueleren Tab
        if activeTab == 1:
            if mouseX > 300 and mouseX < 500 and mouseY > 110 and mouseY < 160:
                Reset('Dices')
                diceCount = 3    
                
            if mouseX > 550 and mouseX < 750 and mouseY > 110 and mouseY < 160:
                Reset('Dices')
                diceCount= 4
            
            if mouseX > 300 and mouseX < 430 and mouseY > 175 and mouseY < 225:
                Reset('Dices')
                roll_dice()
                win()
            #reset button click area
            if mouseX > 800 and mouseX < 930 and mouseY > 175 and mouseY < 225:
                Reset('Dices')
        
        #Namen Tab        
        if activeTab == 4:
            if mouseX >198 and mouseY > 140 and mouseX <598 and mouseY < 160:
                selected_field = 1
                return selected_field
            
            if mouseX >198 and mouseY > 160 and mouseX <598 and mouseY < 180:
                selected_field = 2
                return selected_field
            
            if mouseX >198 and mouseY > 180 and mouseX <598 and mouseY < 200:
                selected_field = 3
                return selected_field
            
            if mouseX >198 and mouseY > 200 and mouseX <598 and mouseY < 220:
                selected_field = 4
                return selected_field
        else:
            selected_field = None
        
        ## mouse position debugger
        # if mousePressed == True:
        #     frameRate(12)
        #     stroke(155)
        #     fill (0)
        #     ellipse(mouseX, mouseY,5,5)
        #     print(str(mouseX)+":"+str(mouseY))
                            
def keyPressed():
    global spelerNamen
    global selected_field
    global activeTab
    
    if activeTab == 4 and selected_field != None:
        # SHIFT keyCode = 16;
        # keyCode 17 = CONTROL, 18 = ALT pressed
        # keyCode 9 = TAB
        if key == TAB:
            if selected_field >= len(spelerNamen):
                selected_field = 1
            else:
                selected_field = selected_field +1
        elif key==BACKSPACE:
            if len(spelerNamen["speler"+str(selected_field)]) > 0:
                spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)][:len(spelerNamen["speler"+str(selected_field)])-1]
        elif key==ENTER or key==RETURN:
            # Enter new line, not used in this program.
            # spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)] + "\n"
            selected_field = None
        elif (key >= 'A' and key <='Z') or (key >='a' and key <= 'z') or keyCode == 32 or key == SHIFT:
            if len(spelerNamen["speler"+str(selected_field)]) < 10:
                spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)] + str(key)
        
                                    
def draw():    
    draw_bg(bg_img, screen_xSize, screen_ySize)
    menuButton()
    active('menu')
    button(20+(activeTab*200), 10, 180, 50, radius = 10)
    menuText()

    if activeTab == 0:
        OverzichtGegevens()
    elif activeTab == 1:
        Duel()
    elif activeTab == 2:
        RadPage()
        if mousePressed and mouseButton == LEFT and (mouseX > 400) and (mouseX <600) and (mouseY >250) and (mouseY < 290):
            Spin_rad()
    elif activeTab == 3:
        Kaartregels()
    elif activeTab == 4:
        Names()
