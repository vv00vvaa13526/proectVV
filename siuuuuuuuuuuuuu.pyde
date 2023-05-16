a = 910
b = 980
g = 255
h = 1080
t = 1010
w = 1035
m = 935
j = 1080
f = 0
x = 1
s = 0
#level1
fer=[910,480,100,600]
fer1=[310,480,700,100]
fer2=[310,190,100,390]
fer3=[310,190,500,100]
fer4=[710,190,100,500]
fer5=[110,590,700,100]

def setup():
    fullScreen()
    background(242,202,39)
def draw():
    global a, b, g, j, m, w, t, h, f, x, s
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
        if b == fer[x] and a == fer[f]:
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
        if b == fer1[x] and a == fer1[f]:
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
        if b == fer2[x] and a == fer2[f]:
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
        if b == fer3[x] and a == fer3[0]+fer3[2]-fer3[3]:
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
