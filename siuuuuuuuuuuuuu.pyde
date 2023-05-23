a = 910
b = 980
s = 0
#level1
fer=[910,480,100,600]
fer1=[310,480,700,100]
fer2=[310,190,100,390]
fer3=[310,190,500,100]
fer4=[710,190,100,500]
fer5=[110,590,700,100]
fer6=[110,340,100,350]
fer7=[110,340,1500,100]
fer8=[1510,340,100,600]
fer9=[1210,840,400,100]
fer10=[1210,0,100,940]
fer11=[1210,0,710,100]
fer12=[1820,0,100,700]
fer13=[1320,600,600,100]
def setup():
    fullScreen()
    background(242,202,39)
def draw():
    global a, b, s
    fill(255)
    rect(a,b,100,100)
    if keyPressed:
        if key == 'd':
            a = a + 5 
    if keyPressed:
        if key == 'a':
            a = a - 5
    if keyPressed:
        if key == 'w':
            b = b - 5
    if keyPressed:
        if key == 's':
            b = b + 5
    if b >= 981:
        b = 980
    if b <= -1:
        b = 0
    if a >= 1821:
        a = 1820
    if a <= -1:
        a = 0
    if s == 0:
        fill(0)
        rect(fer[0],fer[1],fer[2],fer[3])
        fill(255,0,0)
        rect(fer[0],fer[1],fer[2],fer[2])
        fill(255)
        rect(a,b,100,100)
        if a <= fer[0]:
            a = fer[0]
        if a >= fer[0]:
            a = fer[0]
        if b >= fer[1]+fer[3]-fer[2]:
            b = fer[1]+fer[3]-fer[2]
        if b <= fer[1]:
            b = fer[1]
        if b == fer[1] and a == fer[0]:
            s = 1
    if s == 1:
        fill(0)
        rect(fer1[0],fer1[1],fer1[2],fer1[3])
        fill(255,0,0)
        rect(fer1[0],fer1[1],fer1[3],fer1[3])
        fill(255)
        rect(a,b,100,100)
        if b <= fer1[1]:
            b = fer[1]
        if b >= fer[1]:
            b = fer[1]
        if a >= fer1[0]+fer1[2]-fer1[3]:
            a = fer1[0]+fer1[2]-fer1[3]
        if a <= fer1[0]:
            a = fer1[0]
        if b == fer1[1] and a == fer1[0]:
            s = 2
    if s == 2:
        fill(0)
        rect(fer2[0],fer2[1],fer2[2],fer2[3])
        fill(255,0,0)
        rect(fer2[0],fer2[1],fer2[2],fer2[2])
        fill(255)
        rect(a,b,100,100)
        if b >= fer2[1]+fer2[3]-fer2[2]:
            b = fer2[1]+fer2[3]-fer2[2]
        if b <= fer2[1]:
            b = fer2[1]
        if a >= fer2[0]:
            a = fer2[0]
        if a <= fer2[0]:
            a = fer2[0]
        if b == fer2[1] and a == fer2[0]:
            s = 3
    if s == 3:
        fill(0)
        rect(fer3[0],fer3[1],fer3[2],fer3[3])
        fill(255,0,0)
        rect(fer3[0]+fer3[2]-fer3[3],fer3[1],fer3[3],fer3[3])
        fill(255)
        rect(a,b,100,100)
        if b >= fer3[1]:
            b = fer3[1]
        if b <= fer3[1]:
            b = fer3[1]
        if a >= fer3[0]+fer3[2]-fer3[3]:
            a = fer3[0]+fer3[2]-fer3[3]
        if a <= fer3[0]:
            a = fer3[0]
        if b == fer3[1] and a == fer3[0]+fer3[2]-fer3[3]:
            s = 4
    if s == 4:
        fill(0)
        rect(fer4[0],fer4[1],fer4[2],fer4[3])
        fill(255,0,0)
        rect(fer4[0],fer4[1]+fer4[3]-fer4[2],fer4[2],fer4[2])
        fill(255)
        rect(a,b,100,100)
        if b >= fer4[1]+fer4[3]-fer4[2]:
            b = fer4[1]+fer4[3]-fer4[2]
        if b <= fer4[1]:
            b = fer4[1]
        if a >= fer4[0]:
            a = fer4[0]
        if a <= fer4[0]:
            a = fer4[0]
        if b == fer4[1]+fer4[3]-fer[2] and a == fer4[0]:
            s = 5
    
    if s == 5:
        fill(0)
        rect(fer5[0],fer5[1],fer5[2],fer5[3])
        fill(255,0,0)
        rect(fer5[0],fer5[1],fer5[3],fer5[3])
        fill(255)
        rect(a,b,100,100)
        if b >= fer5[1]:
            b = fer5[1]
        if b <= fer5[1]:
            b = fer5[1]
        if a >= fer5[0]+fer5[2]-fer5[3]:
            a = fer5[0]+fer5[2]-fer5[3]
        if a <= fer5[0]:
            a = fer5[0]
        if b == fer5[1] and a == fer5[0]:
            s = 6
            
    if s == 6:
        fill(0)
        rect(fer6[0],fer6[1],fer6[2],fer6[3])
        fill(255,0,0)
        rect(fer6[0],fer6[1],fer6[2],fer6[2])
        fill(255)
        rect(a,b,100,100)
        if b <= fer6[1]:
            b = fer6[1]
        if b >= fer6[1]+fer6[3]-fer6[2]:
            b = fer6[1]+fer6[3]-fer6[2]
        if a >= fer6[0]:
            a = fer6[0]
        if a <= fer6[0]:
            a = fer6[0]
        if b == fer6[1] and a == fer6[0]:
            s = 7
            
    if s == 7:
        fill(0)
        rect(fer7[0],fer7[1],fer7[2],fer7[3])
        fill(255,0,0)
        rect(fer7[0]+fer7[2]-fer7[3],fer7[1],fer7[3],fer7[3])
        fill(255)
        rect(a,b,100,100)
        if b <= fer7[1]:
            b = fer7[1]
        if b >= fer7[1]:
            b = fer7[1]
        if a >= fer7[0]+fer7[2]-fer7[3]:
            a = fer7[0]+fer7[2]-fer7[3]
        if a <= fer7[0]:
            a = fer7[0]
        if b == fer7[1] and a == fer7[0]+fer7[2]-fer7[3]:
            s = 8
            
    if s == 8:
        fill(0)
        rect(fer8[0],fer8[1],fer8[2],fer8[3])
        fill(255,0,0)
        rect(fer8[0],fer8[1]+fer8[3]-fer8[2],fer8[2],fer8[2])
        fill(255)
        rect(a,b,100,100)
        if b <= fer8[1]:
            b = fer8[1]
        if b >= fer8[1]+fer8[3]-fer8[2]:
            b = fer8[1]+fer8[3]-fer8[2]
        if a >= fer8[0]:
            a = fer8[0]
        if a <= fer8[0]:
            a = fer8[0]
        if b == fer8[1]+fer8[3]-fer8[2] and a == fer8[0]:
            s = 9
            
    if s == 9:
        fill(0)
        rect(fer9[0],fer9[1],fer9[2],fer9[3])
        fill(255,0,0)
        rect(fer9[0],fer9[1],fer9[3],fer9[3])
        fill(255)
        rect(a,b,100,100)
        if b <= fer9[1]:
            b = fer9[1]
        if b >= fer9[1]:
            b = fer9[1]
        if a >= fer9[0]+fer9[2]-fer9[3]:
            a = fer9[0]+fer9[2]-fer9[3]
        if a <= fer9[0]:
            a = fer9[0]
        if b == fer9[1] and a == fer9[0]:
            s = 10
            
    if s == 10:
        fill(0)
        rect(fer10[0],fer10[1],fer10[2],fer10[3])
        fill(255,0,0)
        rect(fer10[0],fer10[1],fer10[2],fer10[2])
        fill(255)
        rect(a,b,100,100)
        if b <= fer10[1]:
            b = fer10[1]
        if b >= fer10[1]+fer10[3]-fer10[2]:
            b = fer10[1]+fer10[3]-fer10[2]
        if a >= fer10[0]:
            a = fer10[0]
        if a <= fer10[0]:
            a = fer10[0]
        if b == fer10[1] and a == fer10[0]:
            s = 11
            
    if s == 11:
        fill(0)
        rect(fer11[0],fer11[1],fer11[2],fer11[3])
        fill(255,0,0)
        rect(fer11[0]+fer11[2]-fer11[3],fer11[1],fer11[3],fer11[3])
        fill(255)
        rect(a,b,100,100)
        if b <= fer11[1]:
            b = fer11[1]
        if b >= fer11[1]:
            b = fer11[1]
        if a >= fer11[0]+fer11[2]-fer11[3]:
            a = fer11[0]+fer11[2]-fer11[3]
        if a <= fer11[0]:
            a = fer11[0]
        if b == fer11[1] and a == fer11[0]+fer11[2]-fer11[3]:
            s = 12
            
    if s == 12:
        fill(0)
        rect(fer12[0],fer12[1],fer12[2],fer12[3])
        fill(255,0,0)
        rect(fer12[0],fer12[1]+fer12[3]-fer12[2],fer12[2],fer12[2])
        fill(255)
        rect(a,b,100,100)
        if b <= fer12[1]:
            b = fer12[1]
        if b >= fer12[1]+fer12[3]-fer12[2]:
            b = fer12[1]+fer12[3]-fer12[2]
        if a >= fer12[0]:
            a = fer12[0]
        if a <= fer12[0]:
            a = fer12[0]
        if b == fer12[1]+fer12[3]-fer12[2] and a == fer12[0]:
            s = 13
            
    if s == 13:
        fill(0)
        rect(fer13[0],fer13[1],fer13[2],fer13[3])
        fill(0,255,0)
        rect(fer13[0],fer13[1],fer13[3],fer13[3])
        fill(255)
        rect(a,b,100,100)
        if b <= fer13[1]:
            b = fer13[1]
        if b >= fer13[1]:
            b = fer13[1]
        if a >= fer13[0]+fer13[2]-fer13[3]:
            a = fer13[0]+fer13[2]-fer13[3]
        if a <= fer13[0]:
            a = fer13[0]
        if b == fer13[1] and a == fer13[0]:
            s = 14
            
    if s == 14:
        background(3,255,236)
        textSize(200)
        fill(255)
        text("YOU WIN",490,710)
