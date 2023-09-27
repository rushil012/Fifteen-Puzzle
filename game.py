# author: Rushil Nagpal
# date: May 26, 2023
# file: game.py , GUI for the fifteen puzzle 
# input: the name of button clicked 
# output: the result of the button 
from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
import numpy as np
def clickButton(name):
    t = name.cget("text")
    if t == " ":                                        #do nothing if empty space is selected
        pass
    elif t == "shuffle":            
        tiles.shuffle(50)
        index = 0
        for i in tiles.tiles:                               #matching tiles order with button after shuffling
            if i == 0:
                labels[index].set(" ")
                index += 1
            else:
                labels[index].set(str(i))
                index += 1
    elif tiles.is_valid_move(int(t)):
        move_index = np.where(tiles.tiles ==int(t))[0][0]
        empty_index = np.where(tiles.tiles == 0)[0][0]
        tiles.transpose(move_index,empty_index)
        labels[empty_index].set(str(t))                     # Update the button labels based on the new game state
        labels[move_index].set(" ")                         # Update the game state with the selected move
    
if __name__ == '__main__':
# make tiles
    tiles = Fifteen()
# make a window
    gui = Tk()
    gui.title("Fifteen")
    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')
    # make buttons
    text1 = StringVar()
    text1.set('1')                                                      #button 1 with string "1" 
    name1 = 1
    button1 = Button(gui, textvariable=text1, name=str(name1),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button1))
    button1.configure(bg='coral')
    
    text2 = StringVar()
    text2.set('2')
    name2 = 2
    button2 = Button(gui, textvariable=text2, name=str(name2),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button2))
    button2.configure(bg='coral')

    text3 = StringVar()
    text3.set('3')
    name3 = 3
    button3 = Button(gui, textvariable=text3, name=str(name3),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button3))
    button3.configure(bg='coral')

    text4 = StringVar()
    text4.set('4')
    name4 = 4
    button4 = Button(gui, textvariable=text4, name=str(name4),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button4))
    button4.configure(bg='coral')

    text5 = StringVar()
    text5.set('5')
    name5 = 5
    button5 = Button(gui, textvariable=text5, name=str(name5),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button5))
    button5.configure(bg='coral')

    text6 = StringVar()
    text6.set('6')
    name6 = 6
    button6 = Button(gui, textvariable=text6, name=str(name6),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button6))
    button6.configure(bg='coral')


    text7 = StringVar()
    text7.set('7')
    name7 = 7
    button7 = Button(gui, textvariable=text7, name=str(name7),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button7))
    button7.configure(bg='coral')

    text8 = StringVar()
    text8.set('8')
    name8 = 8
    button8 = Button(gui, textvariable=text8, name=str(name8),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button8))
    button8.configure(bg='coral')


    text9 = StringVar()
    text9.set('9')
    name9 = 9
    button9 = Button(gui, textvariable=text9, name=str(name9),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button9))
    button9.configure(bg='coral')

    text10 = StringVar()
    text10.set('10')
    name10 = 10
    button10 = Button(gui, textvariable=text10, name=str(name10),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button10))
    button10.configure(bg='coral')


    text11 = StringVar()
    text11.set('11')
    name11 = 11
    button11 = Button(gui, textvariable=text11, name=str(name11),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button11))
    button11.configure(bg='coral')


    text12 = StringVar()
    text12.set('12')
    name12 = 12
    button12 = Button(gui, textvariable=text12, name=str(name12),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button12))
    button12.configure(bg='coral')

    text13 = StringVar()
    text13.set('13')
    name13 = 13
    button13 = Button(gui, textvariable=text13, name=str(name13),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button13))
    button13.configure(bg='coral')

    text14 = StringVar()
    text14.set('14')
    name14 = 14
    button14 = Button(gui, textvariable=text14, name=str(name14),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button14))
    button14.configure(bg='coral')

    text15 = StringVar()
    text15.set('15')
    name15 = 15
    button15 = Button(gui, textvariable=text15, name=str(name15),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button15))
    button15.configure(bg='coral')

    text0 = StringVar()
    text0.set(' ')
    name0 = 0
    button0 = Button(gui, textvariable=text0, name=str(name0),
    bg='white', fg='black', font=font, height=2, width=5,
    command = lambda : clickButton(button0))
    button0.configure(bg='coral')

    shuffle_text = StringVar()
    shuffle_text.set("shuffle")
    nameshuffle = "shuffle"
    shuffle_button = Button(gui, textvariable=shuffle_text, name="shuffle",
                            bg='white', fg='black', font=font, height=1, width=12,
                            command=lambda: clickButton(shuffle_button))
    shuffle_button.configure(bg='coral')
    labels = [text1, text2, text3, text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15,text0,shuffle_text]
    # the key argument name is used to identify the button
    gui.nametowidget(name1).configure(bg='white')
    gui.nametowidget(name2).configure(bg='white')
    gui.nametowidget(name3).configure(bg='white')
    gui.nametowidget(name4).configure(bg='white')
    gui.nametowidget(name5).configure(bg='white')
    gui.nametowidget(name6).configure(bg='white')
    gui.nametowidget(name7).configure(bg='white')
    gui.nametowidget(name8).configure(bg='white')
    gui.nametowidget(name9).configure(bg='white')
    gui.nametowidget(name10).configure(bg='white')
    gui.nametowidget(name11).configure(bg='white')
    gui.nametowidget(name12).configure(bg='white')
    gui.nametowidget(name13).configure(bg='white')
    gui.nametowidget(name14).configure(bg='white')
    gui.nametowidget(name15).configure(bg='white')
    gui.nametowidget(name0).configure(bg='white')
    gui.nametowidget(shuffle_button).configure(bg='white')
    # add buttons to the window
    # use .grid() or .pack() methods
    val = 0
    buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15,button0,shuffle_button ]
    for button in buttons:
        if button == shuffle_button:
            button.grid(row = val//4, columnspan=5)             #making grid of buttons using for loop
        button.grid(row=val//4, column = val%4)
        val +=1
    
    # update the window
    gui.mainloop()
