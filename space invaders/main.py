import pgzrun
WIDTH = 600
HEIGHT = 800
TITLE = 'Space Invaders -normal mode-'
buggys = []
dont_know = []
ship = Actor('galaga')
ship.x = 300
ship.y = 750
score = 0
game_on = True

def make_bugs():
    for i in range(5):
        for j in range(5):
            bug = Actor('bug')
            bug.x = 80*j +135
            bug.y = 70*i +100
            buggys.append(bug)


    

def draw():
    global buggys, bug, pew_pew, score, game_on
    screen.clear()
    for i in dont_know:
        i.draw()
    ship.draw()
    for bug in buggys:
        bug.draw()

    screen.draw.text(f'score = {score}',(50,10),fontsize = 30)
    if game_on == False:
        screen.fill('black')
        screen.draw.text('You Win',center = (300,400),fontsize = 70)
        screen.draw.text(f'score = {score}\npress r to play again',center = (300,450),fontsize = 30)

    if game_on == 'lost':
        screen.fill('black')
        screen.draw.text('you have been served as dinner',center = (300,400),fontsize = 50)
        screen.draw.text(f'score = {score}\npress r to play again',center = (300,450),fontsize = 30)
    

def update():
    global buggys,bug,score,game_on
    if keyboard.left:
        ship.x = ship.x - 10
    if keyboard.right:
        ship.x = ship.x + 10
    for i in dont_know:
        i.y =i.y-10
    for bug in buggys:
        bug.y = bug.y+0.5
        for i in dont_know:
            if bug.colliderect(i):
                dont_know.remove(i)
                buggys.remove(bug)
                score = score + 1  
        if bug.y > 700:
            game_on = 'lost'
        if buggys == []:
            game_on = False

def on_key_down(key):
    global pew_pew, buggys, score, game_on
    if key == keys.SPACE:
        pew_pew = Actor('bullet')
        pew_pew.x = ship.x
        pew_pew.y = ship.y
        dont_know.append(pew_pew)

    if game_on == 'lost':
        if key == keys.R:
            game_on = True
            pew_pew = []
            buggys = []
            score = 0
            make_bugs()

    if game_on == False:
        if key == keys.R:
            game_on = True
            pew_pew = []
            buggys = []
            make_bugs()

def game_lost():
    screen.fill('black')
make_bugs()
pgzrun.go()