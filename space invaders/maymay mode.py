import pgzrun
from random import randint
WIDTH = 600
HEIGHT = 800
TITLE = 'Space Invaders -normal-'
buggys = []
dont_know = []
bug_bullet = []
mini_buggys = []
ship = Actor('galaga')
ship.x = 300
ship.y = 750
score = 0
game_on = True
death_message = 0
type_of_bug = 1
upgrade = 1
level = 1
m = 0

def make_bugs():
    global type_of_bug

    if type_of_bug == 1:
        for i in range(randint(1,6)):
            for j in range(5):
                bug = Actor('bug')
                bug.x = 80*j + 135
                bug.y = 200 + (-70*i) 
                bug.hp = 1
                bug.move = 0
                bug.pts = 1
                bug.spd = 0.9
                bug.shoot = False
                bug.bullet = 1
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)

    elif type_of_bug == 2:
        for i in range(randint(1,4)):
            for j in range(5):
                bug = Actor('bug')
                bug.x = 80*j + 135
                bug.y = 200 + (-70*i) 
                bug.hp = 1
                bug.move = randint(-2,2)
                bug.pts = 2
                bug.spd = 1.5
                bug.shoot = False
                bug.bullet = 1
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)

    elif type_of_bug == 3:
        for i in range(randint(2,6)):
            for j in range(6):
                bug = Actor('bug')
                bug.x = 100*j
                bug.y = 200 + (-70*i) 
                bug.hp = 1
                bug.move = 1
                bug.pts = 2
                bug.spd = 0.9
                bug.shoot = False
                bug.bullet = 1                
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)

    elif type_of_bug == 4:
        for i in range(randint(1,6)):
            for j in range(6):
                bug = Actor('bug')
                bug.x = 100*j
                bug.y = 200 + (-70*i) 
                bug.hp = 1
                bug.move = 2
                bug.pts = 2
                bug.spd = 0.9
                bug.shoot = False
                bug.bullet = 1                
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)  

    elif type_of_bug == 6:
        for i in range(randint(1,6)):
            for j in range(6):
                bug = Actor('bug')
                bug.x = 100*j
                bug.y = 200 + (-70*i) 
                bug.hp = 1
                bug.move = -2
                bug.pts = 2
                bug.spd = 0.9
                bug.shoot = False
                bug.bullet = 1
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)

    elif type_of_bug == 7:
        for i in range(randint(2,6)):
            for j in range(6):
                bug = Actor('bug')
                bug.x = 100*j
                bug.y = 200 + (-70*i) 
                bug.hp = 1
                bug.move = -1
                bug.pts = 2
                bug.spd = 0.9
                bug.shoot = False
                bug.bullet = 1
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)

    elif type_of_bug == 5:
        for i in range(2):
            for j in range(2):
                bug = Actor('ufo bug')
                bug.x = 150+(j*300)
                bug.y = 200 + (-200*i) 
                bug.hp = 20
                bug.move = 0
                bug.pts = 2
                bug.spd = 0.5
                bug.shoot = True
                bug.bullet = 2
                bug.boss = False
                bug.ufo = True
                bug.asteroid = False
                buggys.append(bug)  
    
    elif type_of_bug == 8:
        for i in range(1):
            for j in range(8):
                bug = Actor('bug')
                bug.x = 100*j
                bug.y = 50
                bug.hp = 5
                bug.move = -1
                bug.pts = 2
                bug.spd = 0
                bug.shoot = True
                bug.bullet = 1
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)

    elif type_of_bug == 9:
        for i in range(1):
            for j in range(8):
                bug = Actor('bug')
                bug.x = 100*j
                bug.y = 50
                bug.hp = 5
                bug.move = 1
                bug.pts = 2
                bug.spd = 0
                bug.shoot = True
                bug.bullet = 1
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)

    elif type_of_bug == 10:
        for i in range(6):
            for j in range(5):
                bug = Actor('bug')
                bug.x = 80*j + 135
                bug.y = 420 - (70*i) 
                bug.hp = 1
                bug.move = 0
                bug.pts = 1
                bug.spd = 0
                bug.shoot = True
                bug.bullet = 1
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)

    elif type_of_bug == 11:
        for i in range(5):
            for j in range(5):
                bug = Actor('bug')
                bug.x = 80*j + 135
                bug.y = 200 + (-70*i) 
                bug.hp = 1
                bug.move = -2 + j
                bug.pts = 2
                bug.spd = 0.9
                bug.shoot = False
                bug.bullet = 1
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)
    
    elif type_of_bug == 12:
        for i in range(4):
            for j in range(6):
                bug = Actor('bug')
                bug.x = 100*j + 50
                bug.y = 200 - (70*i) 
                bug.hp = 1
                bug.move = (2.5 - j)*(i/2)
                bug.pts = 2
                bug.spd = 0.9
                bug.shoot = False
                bug.bullet = 1
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)
    
    elif type_of_bug == 13:
        for i in range(20):
            for j in range(5):
                k = randint(1,2)
                if k == 1:
                    bug = Actor('bug')
                    bug.x = 80*j + 135
                    bug.y = 200 + (-70*i) 
                    bug.hp = 1
                    bug.move = 0
                    bug.pts = 1
                    bug.spd = 2
                    bug.shoot = False
                    bug.bullet = 1
                    bug.boss = False
                    bug.ufo = False
                    bug.asteroid = False
                    buggys.append(bug)

    elif type_of_bug == 14:
        for i in range(20):
            l = randint(1,2)
            if l == 1:
                bug = Actor('asteroid')
            elif l == 2:
                bug = Actor('asteroid_2')
            bug.x = randint(60,540)
            bug.y = -200*i 
            bug.hp = 7
            bug.move = 0
            bug.pts = 1
            bug.spd = 2
            bug.shoot = False
            bug.bullet = 1
            bug.boss = False
            bug.ufo = False
            bug.asteroid = True
            buggys.append(bug)

    elif type_of_bug == 15:
        for i in range(20):
            l = randint(1,2)
            if l == 1:
                bug = Actor('asteroid')
            elif l == 2:
                bug = Actor('asteroid_2')
            bug.x = randint(60,540)
            bug.y = -200*i 
            bug.hp = 7
            bug.move = 3
            bug.pts = 1
            bug.spd = 2
            bug.shoot = False
            bug.bullet = 1
            bug.boss = False
            bug.ufo = False
            bug.asteroid = True
            buggys.append(bug)

    elif type_of_bug == 16:
        for i in range(20):
            for j in range(2):
                l = randint(1,2)
                bug = Actor('bug')
                bug.x = randint(60,540)
                bug.y = -200*i 
                bug.hp = 1
                bug.move = randint(-3,3)
                bug.pts = 1
                bug.spd = 2
                bug.shoot = False
                bug.bullet = 1
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)

    elif type_of_bug == 17:
        for i in range(20):
            l = randint(1,3)
            if l == 1:
                bug = Actor('asteroid')
                bug.hp = 7
                bug.move = 0
                bug.spd = 2
                bug.asteroid = True

            elif l == 2:
                bug = Actor('asteroid_2')
                bug.hp = 7
                bug.move = 0
                bug.spd = 2
                bug.asteroid = True

            else:
                bug = Actor('bug')
                bug.hp = 1
                bug.move = randint(-2,2)
                bug.spd = 1
                bug.asteroid = False

            bug.x = randint(60,540)
            bug.y = -100*i 
            bug.pts = 1
            bug.spd = 2
            bug.shoot = False
            bug.bullet = 1
            bug.boss = False
            bug.ufo = False
            buggys.append(bug)


    elif type_of_bug == 18:
        bug = Actor('big asteroid')
        bug.x = 300
        bug.y = -550
        bug.hp = 30
        bug.move = 0
        bug.pts = 20
        bug.spd = 2
        bug.shoot = False
        bug.bullet = 1
        bug.boss = True
        bug.ufo = False
        bug.asteroid = True
        buggys.append(bug)

    elif type_of_bug == 19:
        bug = Actor('ufo boss')
        bug.x = 300
        bug.y = 0
        bug.hp = 150
        bug.move = 0
        bug.pts = 20
        bug.spd = 0.3
        bug.shoot = True
        bug.bullet = 1
        bug.boss = True
        bug.ufo = True
        bug.asteroid = False
        buggys.append(bug)

    else:
        bug = Actor('boss bug')
        bug.x = 300
        bug.y = 0
        bug.hp = 70
        bug.move = 0
        bug.pts = 20
        bug.spd = 0.5
        bug.shoot = False
        bug.bullet = 1
        bug.boss = True
        bug.ufo = False
        bug.asteroid = False
        buggys.append(bug)
        for i in range(1):
            for j in range(8):
                bug = Actor('bug')
                bug.x = 100*j
                bug.y = 50
                bug.hp = 5
                bug.move = -1
                bug.pts = 2
                bug.spd = 0
                bug.shoot = True
                bug.bullet = 1
                bug.boss = False
                bug.ufo = False
                bug.asteroid = False
                buggys.append(bug)
        for i in range(1):
            for j in range(2):
                bug = Actor('ufo bug')
                bug.x = 100 + 400*j
                bug.y = 200
                bug.hp = 20
                bug.move = 0
                bug.pts = 2
                bug.spd = 0
                bug.shoot = True
                bug.bullet = 2
                bug.boss = False
                bug.ufo = True
                bug.asteroid = False
                buggys.append(bug)
    type_of_bug = randint(1,20)

    

def draw():
    global buggys, bug, pew_pew, score, game_on, death_message,dont_know,bug_bullet,mini_buggys,type_of_bug,level
    screen.clear()
    for i in dont_know:
        i.draw()
    for i in bug_bullet:
        i.draw()
    for i in mini_buggys:
        i.draw()
    ship.draw()
    for bug in buggys:
        bug.draw()

    screen.draw.text(f'score = {score}\nLevel: {level}',(50,10),fontsize = 30)

    if game_on == False:
        screen.fill('black')
        buggys = []
        dont_know = []
        bug_bullet = []
        mini_buggys = []
        if death_message == 1:
            screen.draw.text('Game Over!\nyou have been served as dinner',center = (300,400),fontsize = 50)
        elif death_message == 2:
            screen.draw.text('Game Over!\nyou have been blown to bits',center = (300,400),fontsize = 50)
        elif death_message == 3:
            screen.draw.text('Game Over!\nthe earth has been\nabliterated by a tiny bug',center = (300,400),fontsize = 50)
        elif death_message == 4:
            screen.draw.text('Game Over!\nyou have been squashed by a bug',center = (300,400),fontsize = 50)
        elif death_message == 5:
            screen.draw.text('Game Over!\nyou have been abducted by a ufo',center = (300,400),fontsize = 50)
        elif death_message == 6:
            screen.draw.text('Game Over!\nyou have been smashed by a big ufo',center = (300,400),fontsize = 50)
        elif death_message == 7:
            screen.draw.text('Game Over!\nyou have been hit by a asteroid',center = (300,400),fontsize = 50)
        elif death_message == 8:
            screen.draw.text('Game Over!\nyou have exploded when coming\ninto contact with a comically\nlarge asteroid',center = (300,400),fontsize = 50)        


        screen.draw.text(f'score = {score}\npress R',center = (300,500),fontsize = 30)
    

def update():
    global buggys,bug,score,game_on,pew_pew,death_message,upgrade,level,m
    m = m + 1
    if level > 1:
        upgrade = 2
        if level > 2:
            upgrade = 3
            if level > 5:
                upgrade = 4
                if level > 6:
                    upgrade = 5
                    if level > 7:
                        upgrade = 6
                        if level > 8:
                            upgrade = 7
                            if level > 10:
                                upgrade = 8
                                if level > 11:
                                    upgrade = 9
                                    if level > 13:
                                        upgrade = 10
                                        if level > 14:
                                            upgrade = 11
    if m == 10:
        for i in range((upgrade)):
            pew_pew = Actor('medbullet')
            pew_pew.x = ship.x
            pew_pew.y = ship.y
            pew_pew.move = ((upgrade/2)-i)-0.5
            dont_know.append(pew_pew)
            m = 0

    else:
        upgrade = 1
    if game_on == True:
        mini_bug = randint(1,200) 
        if mini_bug == 1:
            bug = Actor('mini bug')
            bug.x = randint(50,550)
            bug.y = 0 
            bug.hp = 1
            bug.move = randint(-1,1)       
            mini_buggys.append(bug)   
    if keyboard.left:
        ship.x = ship.x - 10
    if keyboard.right:
        ship.x = ship.x + 10
    if ship.x > 600:
        ship.x = 0
    if ship.x < 0:
        ship.x = 600
    for i in dont_know:
        i.y =i.y - 10
        i.x =i.x +i.move
    for i in bug_bullet:
        i.y = i.y + 5
    for bug in buggys:
        if bug.hp <1:
            if bug.boss == False:
                buggys.remove(bug)
                score = score + bug.pts
            else:
                buggys.remove(bug)
                score = score + bug.pts
                level = level + 1
        bug.y = bug.y+bug.spd
        bug.x = bug.x+bug.move
        if bug.x < 0:
            bug.x = 600
        elif bug.x > 600:
            bug.x = 0
        if bug.y > 700:
            if bug.boss == True and bug.ufo == True:
                death_message == 6
            if bug.boss == True:
                game_on = False
                death_message = 4
            elif bug.ufo == True:
                game_on = False
                death_message = 5
            elif bug.asteroid == True:
                game_on = False
                death_message = 7
            else:
                game_on = False
                death_message = 1     

        elif bug.boss == True and bug.asteroid == True:
            if bug.y > 200:
                game_on = False
                death_message = 8                


        if bug.shoot == True:
            if bug.boss == True and bug.ufo == True:
                i = randint(1,50)
                if i == 1:
                    bugbullet = Actor('bigbullet')
                    bugbullet.x = randint(20,580)
                    bugbullet.y = bug.y - 100
                    bug_bullet.append(bugbullet)
            else:
                i = randint(1,500)
                if i == 1:
                    if bug.bullet == 1:
                        bugbullet = Actor('bullet')
                    if bug.bullet == 2:
                        bugbullet = Actor('bigbullet')
                    bugbullet.x = bug.x
                    bugbullet.y = bug.y
                    bug_bullet.append(bugbullet)

        for i in bug_bullet:
            if ship.colliderect(i):
                bug_bullet.remove(i)
                game_on = False
                death_message = 2
            elif i.y > 800:
                bug_bullet.remove(i)


        for i in dont_know:
            if bug.colliderect(i): 
                bug.hp = bug.hp - 1
                dont_know.remove(i)
            elif i.y < 0:
                dont_know.remove(i)
    
    for bug in mini_buggys:
        if bug.hp <1:
            mini_buggys.remove(bug)
            score = score + 2
        bug.y = bug.y+1
        bug.x = bug.x+bug.move
        if bug.x < 0:
            bug.x = 600

        elif bug.x > 600:
            bug.x = 0

        if bug.y > 800:
            death_message = 3
            game_on = False

        if bug.colliderect(ship): 
            bug.hp = bug.hp - 1

        for i in dont_know:
            if bug.colliderect(i): 
                bug.hp = bug.hp - 1
                dont_know.remove(i)


    if game_on == True and buggys == []:
        pew_pew = []
        buggys = []
        score = score + 10
        make_bugs()


def on_key_down(key):
    global pew_pew,buggys,score,game_on,type_of_bug,upgrade,level

    if key == keys.R:
        if game_on == False:
            upgrade = 0
            level = 0
            game_on = True
            score = 0
            type_of_bug = 1




make_bugs()
pgzrun.go()