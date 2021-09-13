import numpy as np
import pygame
from scipy.integrate import odeint

#  ode int part

g=9.81                                         # Change this for Gravitational Constant
l=200                                          # Change this for Length of Pendulum
k=0.01                                         # Change this for Dampening Coefficient

# HEre we define our function with arguments fun(Y' vector, function w.r.t intrgrate, args)
def fun(y,x,k,g,l):

    theta,omega=y    #  here theta' = omega so omega'=theta"
    dydt=[omega,-k*omega-(g/l)*np.sin(theta)]
    
    return dydt

# here We define initial conditions yinitial=[x0,y0]

initialcondition=[np.pi/2-0.1,0]

tarray=[0]
Point=[]
# //////////Pendulum Loop/////////

def Pendulum(L,theta,Pos=[]):
    theta+=np.pi/2
    pygame.draw.line(gameDisplay,Black,(Pos[0],Pos[1]),(L*np.cos(theta)+Pos[0],L*np.sin(theta)+Pos[1]),3)
    pygame.draw.circle(gameDisplay,Black,(L*np.cos(theta)+Pos[0],L*np.sin(theta)+Pos[1]),20)
    return (L*np.cos(theta)+Pos[0],L*np.sin(theta)+Pos[1])

# //////////////////////////////

def drawpoint(k):

    Point.insert(0,k)

    if len(Point)>=5000:
        Point.pop(-1)

    for i in range(len(Point)):
        pygame.draw.circle(gameDisplay,Black,((int(Point[i][0]),int(Point[i][1]+0.1*i))),1)

# //////////////////////////

White=(255,255,255)
Black=(0,0,0)
Green=(0,255,0)
width,height=850,850

xlim=[-1,10]
ylim=[-1,10]
scalex=width/(xlim[1]-xlim[0])
scaley=height/(ylim[1]-ylim[0])
time=0
gameDisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption("Damped Pendulum")         # Setting window title
pygame.font.init()                                      # initialising font for further use
font=pygame.font.Font('freesansbold.ttf',15)
pygame.display.flip()

def T(x,y):
	return(int(scalex*(x+1.0)),int(height-scaley*(y+1.0)))

A=False
while True:

# /////////////////////////////////////////////////// Display Grid Setup ////////////////////////////
    
    gameDisplay.fill(White)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                A=True
    pygame.draw.line(gameDisplay,Black,(scalex*(-xlim[0]),0),(scalex*(-xlim[0]),height),2)
    pygame.draw.line(gameDisplay,Black,(0,height-scaley*(-ylim[0])),(width,height-scaley*(-ylim[0])),2)

    for i in range(int(width/scalex)):
    	pygame.draw.line(gameDisplay,Black,(i*scalex,0),(i*scalex,height),1)
    for i in range(int(height/scaley)):
    	pygame.draw.line(gameDisplay,Black,(0,i*scaley),(width,i*scaley),1)
    


# ///////////////////////////////////////////////////////////////////////////////////////////////////
    if A==True:
        time+=1
        tarray.append(0.00006*time) 
        
        Ps = odeint(fun,initialcondition,tarray,args=(g,l,k))
        initialcondition=Ps[-1]
        initialomega=Ps[0]
        theta=initialcondition[0]
        Omega=initialomega[0]
        j=Pendulum(l,theta=theta,Pos=T(5,10))
        drawpoint(j)
        tarray.pop(0)
    # ////////////
        text=font.render("Theta="+str(round(float(180*theta/np.pi),3))+' Degrees',True,Black,White)
        textrect=text.get_rect()
        textrect.center=(T(2,9)[0]-75,T(2,9)[1]-40)
        gameDisplay.blit(text,textrect)
    # ////////////
        text1=font.render("Dapmening Coefficient ="+str(k),True,Black,White)
        textrect1=text1.get_rect()
        textrect1.center=(T(2,8)[0]-75,T(2,8)[1]-40)
        gameDisplay.blit(text1,textrect1)
    # ////////////
        text2=font.render("Omega ="+str(round(float(Omega),3))+' radian/s',True,Black,White)
        textrect2=text2.get_rect()
        textrect2.center=(T(2,8.5)[0]-75,T(2,8.5)[1]-40)
        gameDisplay.blit(text2,textrect2)
    # ///////////
    pygame.display.update()


#Created by Harsh Maurya with 💖 ............ :)

