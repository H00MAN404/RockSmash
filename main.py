from tkinter import *
from random import randint
from time import time, sleep
from math import sqrt
import sys

width = 1345
height = 710

#global collisions
points = 0

S_spd = 10

wn = Tk()

wn.title('bubble blaster')
c = Canvas(wn, width = width, height = height, bg = "black")
c.pack()

player = c.create_oval(0, 0, 30, 30, outline = "black")
player1 = c.create_polygon(5, 5, 5, 25, 30, 15, fill="white")
Prad = 15
midx = width / 2
midy = height / 2
c.move(player, midx, midy)
c.move(player1, midx, midy)

objectid = list()
objectrad = list()
objectspd = list()
maxr = 30
minr = 10
maxspd = 10
offset = 100

x = True

def update_x():
      global x
      x = False

wn.protocol("WM_DELETE_WINDOW", update_x)

def movePlayer(event):
  #print('input')
  if event.keysym == 'Up':
    c.move(player, 0, -S_spd)
    c.move(player1, 0, -S_spd)
  elif event.keysym == 'Down':
    c.move(player, 0, S_spd)
    c.move(player1, 0, S_spd)
  elif event.keysym == 'Right':
    c.move(player, S_spd, 0)
    c.move(player1, S_spd, 0)
  elif event.keysym == 'Left':
    c.move(player, -S_spd, 0)
    c.move(player1, -S_spd, 0)
  elif event.keysym == 'esc':
    wn.destroy()

c.bind_all('<Key>', movePlayer)

def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y

def createObj():
  x = width + offset
  y = randint(0, height)
  r = randint(minr, maxr)
  id1 = c.create_oval(x - r, y - r, x + r, y + r, outline = 'white')
  objectid.append(id1)
  objectrad.append(r)
  objectspd.append(randint(5, maxspd))

def moveObj():
  for i in range(len(objectid)):
    c.move(objectid[i], -objectspd[i], 0)

def delObj(i):
  del objectspd[i]
  del objectrad[i]
  c.delete(objectid[i])
  del objectid[i]

def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def collision():
    points = 0
    for o in range(len(objectid) -1, -1, -1):
        if distance(player, objectid[o]) < (Prad + objectrad[o]):
            points += (objectrad[o] + objectspd[o])
            delObj(o)
    return points        


time = 150

def countdown():
  sleep(2)
  destroyWin()
  #wn.destroy()
    
def destroyWin():
  wn.destroy()
  sleep(1)
  print('your final score:', points)
  sleep(2)
  print('thanks for playing')
  sleep(2)

#c.create_text(50, 10, text = 'your score is >', fill="white")
st = c.create_text(90, 15, fill="white", font = 1)
#stt = c.create_text(150, 15, fill="white", font = 1)
def show(score):
    c.itemconfig(st, text = 'your score is > ' + str(points))
'''
def time(time):
    c.itemconfig(st, text = str(time))
'''
#GAME LOOP
while True:
  if(randint(1, 10) == 1):
    createObj()
  moveObj()
  points += collision()
  wn.update_idletasks()
  sleep(0.02)
  #print(points)
  show(points)
  #time(time)
  if time > -1:
    time -= 1
  elif time < 0:
    sleep(1)
    countdown()
  #print(time)
  try:
    wn.update()
  except:
    print('  ')
  #print(collisions)
  
    