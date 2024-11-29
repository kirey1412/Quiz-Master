import pgzrun

TITLE="Quiz Master"
WIDTH=870
HEIGHT=650

questionfilename="questions.txt"

marqueebox=Rect(0,0,870,80)
questionbox=Rect(0,0,650,150)
timerbox=Rect(0,0,150,150)
skipbox=Rect(0,0,150,330)
option1=Rect(0,0,300,150)
option2=Rect(0,0,300,150)
option3=Rect(0,0,300,150)
option4=Rect(0,0,300,150)
options=[option1,option2,option3,option4]

marquemessage=""

marqueebox.move_ip(0,0)
questionbox.move_ip(20,100)
timerbox.move_ip(700,100)
skipbox.move_ip(700,270)
option1.move_ip(20,270)
option2.move_ip(370,270)
option3.move_ip(20,450)
option4.move_ip(370,450)

questions=[]
questioncount=0

questionindex=0

def readquestion():
    qfile=open(questionfilename, "r")
    for question in qfile:
        questions.append(question)
        questioncount+=1
    qfile.close()

def nextquestion():
    questionindex+=1
    return questions.pop(0).split(",")

def draw():
    screen.fill("black")
    screen.draw.filled_rect(marqueebox,"black")
    screen.draw.filled_rect(questionbox,"red")
    screen.draw.filled_rect(timerbox,"green")
    screen.draw.filled_rect(skipbox,"white")
    for option in options:
        screen.draw.filled_rect(option,"yellow")
    marquemessage="Welcome to the Quiz Master!"
    screen.draw.textbox(marquemessage,marqueebox,color="red",shadow=(0.5,0.5),scolor="dimgray")

def movemarquee():
    marqueebox.x-=2
    if marqueebox.right<0:
        marqueebox.left=WIDTH


def update():
    movemarquee()

pgzrun.go()
