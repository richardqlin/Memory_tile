from tkinter import messagebox
from tkinter import *
import random

import time



#### GLOBAL VARIABLES ######

#data list contains the data in the cards


from PIL import Image


#initialize or initiate our root(window)
root = Tk()
root.resizable(False,False)
root.title("Memory Game")

s = IntVar()
mark=Image.open(r'C:/Users/richardlin/Downloads/mark.png')
mark1= mark.resize((100,100))
mark1 = mark1.save('C:/Users/richardlin/Downloads/mark1.png')
mark_img=PhotoImage(file='C:/Users/richardlin/Downloads/mark1.png')

apple=Image.open(r'C:/Users/richardlin/Downloads/apple.png')
apple1= apple.resize((100,100))
apple1 = apple1.save('C:/Users/richardlin/Downloads/apple1.png')
apple_img=PhotoImage(file='C:/Users/richardlin/Downloads/apple1.png')

cherry=Image.open(r'C:/Users/richardlin/Downloads/cherry.png')
cherry1= cherry.resize((100,100))
cherry1 = cherry1.save('C:/Users/richardlin/Downloads/cherry1.png')
cherry_img=PhotoImage(file='C:/Users/richardlin/Downloads/cherry1.png')

strawberry=Image.open(r'C:/Users/richardlin/Downloads/strawberry.png')
strawberry1= strawberry.resize((100,100))
strawberry1 = strawberry1.save('C:/Users/richardlin/Downloads/strawberry1.png')
strawberry_img=PhotoImage(file='C:/Users/richardlin/Downloads/strawberry1.png')

watermelon=Image.open(r'C:/Users/richardlin/Downloads/watermelon.png')
watermelon1= watermelon.resize((100,100))
watermelon1 = watermelon1.save('C:/Users/richardlin/Downloads/watermelon1.png')
watermelon_img = PhotoImage(file='C:/Users/richardlin/Downloads/watermelon1.png')

pear=Image.open(r'C:/Users/richardlin/Downloads/pear.png')
pear1= pear.resize((100,100))
pear1 = pear1.save('C:/Users/richardlin/Downloads/pear1.png')
pear_img=PhotoImage(file='C:/Users/richardlin/Downloads/pear1.png')

orange=Image.open(r'C:/Users/richardlin/Downloads/orange.png')
orange1= orange.resize((100,100))
orange1 = orange1.save('C:/Users/richardlin/Downloads/orange1.png')
orange_img=PhotoImage(file='C:/Users/richardlin/Downloads/orange1.png')

banana=Image.open(r'C:/Users/richardlin/Downloads/banana.png')
banana1= banana.resize((100,100))
banana1 = banana1.save('C:/Users/richardlin/Downloads/banana1.png')
banana_img=PhotoImage(file='C:/Users/richardlin/Downloads/banana1.png')

pineapple=Image.open(r'C:/Users/richardlin/Downloads/pineapple.png')
pineapple1= pineapple.resize((100,100))
pineapple1 = pineapple1.save('C:/Users/richardlin/Downloads/pineapple1.png')
pineapple_img=PhotoImage(file='C:/Users/richardlin/Downloads/pineapple1.png')

num ='1122334455667788'

d={'1':apple_img,'2':pear_img,'3':orange_img,'4':banana_img,'5':pineapple_img,'6':cherry_img,'7':strawberry_img,'8':watermelon_img}
num = list(num)
random.shuffle(num)

score = 0

track=[]

timer = IntVar()
duration=0

start = time.time()
class Tile:
    def __init__(self):
        self.state = NORMAL
        self.button_clicked = True
        self.button = [Button(image=mark_img, text='', command = lambda i=i: self.button_click(i), state = self.state) for i in range(16)]
        # self.button=[]
        # for i in range(16):
        #    b=Button(image=mark_img, command = lambda i=i: self.button_click(i), state = self.state) for i in range(16)
        #    self.button.append(b)
        
    def show_question_mark(self):
        for i in range(16):
            self.button[i].grid(row= i//4+1, column= i%4)
        

    def button_click(self,i):
        global score, track,start, duration
        self.button[i].config(image= d[num[i]],state = self.state)
        if self.button[i]['text'] == '':
            track.append(i)
            self.button[i]['text']= 'x'
            
        print(track)
        root.update()
        root.after(1000)
        
        if len(track)==2:
            if num[track[0]]==num[track[1]]:
                self.button[track[0]].config(state=DISABLED)
                self.button[track[1]].config(state=DISABLED)
                score += 1
            else:     
                self.button[track[0]].config(image=mark_img, state=self.state)
                self.button[track[1]].config(image=mark_img, state =self.state)
                self.button[track[0]].config(state=NORMAL)
                self.button[track[1]].config(state=NORMAL)
                self.button[track[0]]['text']=''
                self.button[track[1]]['text']=''
            track=[]
        if score == 8:
            messagebox.showinfo('score','Taken time:'+str(duration))
        duration = round(time.time() - start,2)
        print(duration)
        timer.set(duration)
       
        
tile= Tile()
label1=Label(root,text= ' Taken Time: ')
label1.grid(row = 0 ,column=2)
label= Label(root,textvariable =  timer)
label.grid(row = 0, column=3)
button_quit= Button(root,text='Quit', command=quit)
button_quit.grid(row=0, column=0)
tile.show_question_mark()
