from gamelib import *


def randLocate(objects):
    for i in range(len(objects)):
        x=randint(-20000,20000)
        y=randint(100,1200)
        objects[i].moveTo(x,-y)




game = Game(1500,1000,"Soulseeker")

soulOG = Animation ("images/soul.png",4,game,196/2,196/2,3)
soul = Animation ("images/soul.png",4,game,196/2,196/2,3)
soul.resizeBy(-10)
soulOG.resizeBy(-10)
selfctrl = Animation ("images/selfctrl.png",1, game,17,16)
goodness = Animation ("images/goodness.png",1,game,96,96)
pat = Animation ("images/patience.png",1,game,34,34)
kind = Animation ("images/kindness.png",1,game,34,34)
gent = Animation ("images/gentleness.png",1,game,34,34)
bk = Image ("images/backround.png",game)
lose = Image ("images/GameOver.png",game)
win = Image ("images/victory.png",game)
lose.resizeTo(game.width,game.height)
win.resizeTo(game.width,game.height)
joe=[]
for i in range(100):
    jo = Image ("images/Joe.png",game)
    jo.resizeBy(110)
    joe.append(jo)
randLocate(joe)

sammy=[]
for i in range(75):
    sam = Image ("images/aaron.png",game)
    sammy.append(sam)
randLocate(sammy)

dav=[]
for i in range(50):    
    dave = Image ("images/panagioti.png",game)
    dave.resizeBy(-20)
    dav.append(dave)
randLocate(dav)

gdbullets=[]




kind.resizeBy(450)
selfctrl.resizeBy(450)
goodness.resizeBy(50)
pat.resizeBy(450)
gent.resizeBy(120)
bk.resizeTo(1500,1000)

selfctrl.visible = False
goodness.visible = False
pat.visible = False
kind.visible = False
gent.visible = False


p=30
t = 0
wait = 0
game.score=0
g = 0
waitg=0
#__Main Game________________________________________________________________________________________________________________________________________________
while not game.over:
    game.processInput()
    bk.draw()
    t+=1
    p+=1
    wait+=1
    g+=1
    waitg+=1


    soul.draw()
    selfctrl.moveTo(soul.x-5,soul.y+15)
    goodness.moveTo(soul.x-5,soul.y+15)
    pat.moveTo(soul.x-5,soul.y+15)
    kind.moveTo(soul.x-5,soul.y+15)
    gent.moveTo(soul.x-5,soul.y+15)

    


    
    
    #          CHARACTERS!!!!!!!!!!!!!!!!!!!!

    if soul.isOffScreen() or selfctrl.isOffScreen() or goodness.isOffScreen() or pat.isOffScreen() or kind.isOffScreen() or gent.isOffScreen():
        soul.health-=0.05
    
    if keys.Pressed[K_0]:
        selfctrl.visible = False
        soul.visible = True
        goodness.visible = False
        pat.visible = False
        kind.visible = False
        gent.visible = False

    #self control

    if keys.Pressed[K_1]:
        selfctrl.visible = True
        soul.visible = False
        goodness.visible = False
        pat.visible = False
        kind.visible = False
        gent.visible = False
        
    if selfctrl.visible == True:
        if keys.Pressed[K_UP]:
            soul.y-=5
        if keys.Pressed[K_DOWN]:
            soul.y+=5
        if keys.Pressed[K_LEFT]:
            soul.x-=5
        if keys.Pressed[K_RIGHT]:
            soul.x+=5
    #goodness

    if keys.Pressed[K_2]:
        goodness.visible = True
        soul.visible = False
        selfctrl.visible = False
        pat.visible = False
        kind.visible = False
        gent.visible = False

    if goodness.visible == True:
        if keys.Pressed[K_UP]:
            soul.y+=3
        if keys.Pressed[K_DOWN]:
            soul.y-=3
        if keys.Pressed[K_LEFT]:
            soul.x+=3
        if keys.Pressed[K_RIGHT]:
            soul.x-=3


    for i in range(len(gdbullets)):
        gdbullets[i].move()
        if gdbullets[i].isOffScreen():
            gdbullets[i].visible = False
            

    if goodness.visible == True and t > 25 and (keys.Pressed[K_UP] or keys.Pressed[K_DOWN] or keys.Pressed[K_LEFT] or keys.Pressed[K_RIGHT]) :
            bullet = Image ("images/bullet.png",game)
            bullet.moveTo(soul.x-5,soul.y+15)
            if keys.Pressed[K_UP] :
                t = 0
                bullet.move()
                bullet.setSpeed(10,0)
                
                    
                    

            if keys.Pressed[K_DOWN] :
                t = 0
                bullet.move()
                bullet.setSpeed(10,180)
                

            if keys.Pressed[K_LEFT] :
                t = 0
                bullet.move()
                bullet.setSpeed(10,90)
                

            if keys.Pressed[K_RIGHT]:
                t = 0
                bullet.move()
                bullet.setSpeed(10,270)
                

                
            gdbullets.append(bullet)                

            

    #patience
    

    if keys.Pressed[K_3] and wait > 300 and pat.visible == False:
        p = 0
        pat.visible = True
        soul.visible = False
        goodness.visible = False
        selfctrl.visible = False
        kind.visible = False
        gent.visible = False

    if p<=100 and (keys.Pressed[K_1] or keys.Pressed[K_2] or keys.Pressed[K_4] or keys.Pressed[K_5]):
        p=0
        wait = 0
        
    
        
    if pat.visible == True and p>=100:
        p=0
        wait = 0
        pat.visible = False
        soul.visible = True


    
        
            
            
        
    if pat.visible == True:
        if keys.Pressed[K_UP]:
            soul.y+=2
        if keys.Pressed[K_DOWN]:
            soul.y-=2
        if keys.Pressed[K_LEFT]:
            soul.x+=2
        if keys.Pressed[K_RIGHT]:
            soul.x-=2

    #kindess
    

    if keys.Pressed[K_4]:
        kind.visible = True
        pat.visible = False
        soul.visible = False
        goodness.visible = False
        selfctrl.visible = False
        gent.visible = False
        
    if kind.visible == True:
        soul.health+=0.05
        if keys.Pressed[K_UP]:
            soul.y+=3
        if keys.Pressed[K_DOWN]:
            soul.y-=3
        if keys.Pressed[K_LEFT]:
            soul.x+=3
        if keys.Pressed[K_RIGHT]:
            soul.x-=3
    if soul.health>200:
        soul.health-=0.05

    #gent

    if keys.Pressed[K_5] and waitg > 300 and gent.visible == False:
        g = 0
        pat.visible = False
        soul.visible = False
        goodness.visible = False
        selfctrl.visible = False
        kind.visible = False
        gent.visible = True
    if g<=100 and (keys.Pressed[K_1] or keys.Pressed[K_2] or keys.Pressed[K_4] or keys.Pressed[K_3]):
        g=0
        waitg = 0

    if gent.visible == True and g==400:
        g=0
        waitg=0
        gent.visible = False
        soul.visible = True
        
    
    if keys.Pressed[K_UP]:
        soul.y-=3
    if keys.Pressed[K_DOWN]:
        soul.y+=3
    if keys.Pressed[K_LEFT]:
        soul.x-=3
    if keys.Pressed[K_RIGHT]:
        soul.x+=3

    #          ENEMIES!!!!!!!!!!!!!!!!!!!!  


    
    for i in range (len(joe)):
        
        
        if joe[i].visible == True and gent.visible == True:
            joe[i].moveTowards(soul,-5)
        else:
            joe[i].moveTowards(soul,3)
            
        if joe[i].visible == True and joe[i].collidedWith(pat):
            joe[i].visible = False
            game.score +=1
    
        if joe[i].visible == True and (joe[i].collidedWith(soul) or joe[i].collidedWith(goodness) or joe[i].collidedWith(selfctrl) or joe[i].collidedWith(kind) or joe[i].collidedWith(gent)):
            soul.health-=7
            joe[i].visible = False
            game.score +=1
        if joe[i].health<=0:
            joe[i].visible = False
        '''

        if game.score == 100:
            if joe[i].visible == True and gent.visible == True:
                joe[i].moveTowards(soul,-3)
            else:
                joe[i].moveTowards(soul,5)
        '''
            
    
        

    for i in range (len(dav)):
        if dav[i].visible == True and gent.visible == True:
            dav[i].moveTowards(soul,-5)
        else:
            dav[i].moveTowards(soul,5)
        
        if dav[i].visible == True and dav[i].collidedWith(pat):            
            dav[i].visible = False
            game.score+=1

        if dav[i].visible == True and (dav[i].collidedWith(soul) or dav[i].collidedWith(goodness) or dav[i].collidedWith(selfctrl) or dav[i].collidedWith(kind) or dav[i].collidedWith(gent)):            
            dav[i].visible = False
            soul.health-=7
            game.score+=1

        if dav[i].health<=0:
            dav[i].visible = False
        '''
        if game.score == 100:
            if dav[i].visible == True and gent.visible == True:
                dav[i].moveTowards(soul,-3)
            else:
                dav[i].moveTowards(soul,8)
          
        ''' 
    for i in range (len(sammy)):
        if sammy[i].visible == True and gent.visible == True:
            sammy[i].moveTowards(soul,-5)
        else:
            sammy[i].moveTowards(soul,2)
        if sammy[i].visible == True and sammy[i].collidedWith(pat):            
            sammy[i].visible = False
            
        if sammy[i].visible == True and (sammy[i].collidedWith(soul) or sammy[i].collidedWith(goodness) or sammy[i].collidedWith(selfctrl) or sammy[i].collidedWith(kind) or sammy[i].collidedWith(gent)):
            sammy[i].visible = False
            soul.health-=13
        if sammy[i].health<=0:
            sammy[i].visible = False
        '''
        if game.score == 100:
            if sammy[i].visible == True and gent.visible == True:
                sammy[i].moveTowards(soul,-3)
            else:
                sammy[i].moveTowards(soul,5)
        '''
            
            
               
                
        

    for gd in gdbullets:
        
        for j in joe:
            if gd.collidedWith(j):
                j.health-=100
                game.score+=1
        
        for d in dav:
            if gd.collidedWith(d):
                d.health-=100
                game.score+=1
        
        for s in sammy:
            if gd.collidedWith(s):
                s.health-=3

        

             
    



    game.displayScore()
    game.drawText("Health:" + str(soul.health),400,10)
    if soul.health < 0 or game.score >= 150:
        game.over=True

    game.update(60)


#Game Overs___________________________________________________________________________________________________________________________________________________________________________
game.over=False
while not game.over:
    game.processInput()
    if soul.health > 0:
        win.draw()
        game.update(60)
    else:
        lose.draw()
        game.update(60)

        
        
    game.update(60)
game.quit()
    
