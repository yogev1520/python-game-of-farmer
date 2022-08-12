import signal
import threading
from PIL import ImageGrab
import os
import time
import webbrowser
from win32 import win32api
import win32.lib.win32con as win32con
import PySimpleGUI as sg
import _thread


#
#
#>>>>>>>>> import module section <<<<<<<<<<<<
#re liealnk ="https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117"
#commant import webbq numpy .The Python Imaging Library.PyWin
#src tutorrowser set urlsrc open broser
def WabWin():
    srcUrl1 ="https://poki.com/en/g/game-of-farmers"
    google=webbrowser.open(srcUrl1)

#All coordinates assume a screen resolution of 1280x1024, and Chrome 
#maximized with the Bookmarks Toolbar enabled.
#Down key has been hit 4 times to center play area in browser.

#159,119,995,588 game screen box

#Play area =  x_pad+1, y_pad+1, 995, 588   
    #game window cordinate
x_pad = 158#left top corner of game play area
y_pad = 118#right top corner
def screenGrab():   
    box = (x_pad+1,y_pad+1,x_pad+796,y_pad+469)
    img = ImageGrab.grab(box)
    img.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
    '.png', 'PNG')
#mouse Events
#onClick laft mouse button
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
  #  print ("Click.") #completely optional. But nice for debugging purposes.

#on hold down  button
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
#mouse movment cordination
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     
def get_cords():
    time.sleep(1)
    x,y = win32api.GetCursorPos()#create 2 vars x and y and set it to mouse position!!!
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def startGame():  
    print("startScript")
    time.sleep(3)
    #location of 1 box
    gardian1() #>>>>>>>>>>pic gardan 1<<<<<<<<<<<
    leftClick()
    print(">>>>>>>>>>pic gardan 1<<<<<<<<<<<")
    time.sleep(1)
    picfruits1() #>>>>>>>>>>>>>>pic fruits<<<<<<<<<<<
    print(">>>>>pic fruits<<<<<")
    time.sleep(1)
    collectReword()# collect from box1 reworded 
    collectReword() 
    collectReword()
    print(">>>>>>collectReword<<<<<<<")
    lackWill()# go to lucky whill screen
    print(">>>>>>luckywillbtn<<<<<<<")
    clickOnLuckyWill()
    print(">>>>>>clickOnLuckywill<<<<<<<")
    clickOnLuckyWill()
    print(">>>>>>clickOnLuckywill<<<<<<<")
    finishLevel()#>>>>>finishLevel(1)<<<<<<<
    print(">>>>>finishLevel(1)<<<<<<<")
    time.sleep(7)
#def level_2():  
    Pan()#select pan
    gardian1()#select gardian1 of 9
    print(">>>>gardian1 selected!!<<<<<<")
    time.sleep(1)
    Bloon()
    print(">>>>>>>>>>baloon pic up<<<<<<<<<")
    time.sleep(5)
    lackWill()
    print(">>>>>>lucky whill pic<<<<<<<<")
    clickOnLuckyWill()
    print("lucky whill clickd")
    clickOnLuckyWill()
    print("lucky whill clickd")
    clickOnLuckyWill()
    print("lucky whill clickd")
    print("-------------------")
    picfruits2()
    print(">>>>>>pic fruits 2<<<<<")
    Bloon()
    print("baloon")
    time.sleep(1)
    lackWill()
    print("lucky whill")
    clickOnLuckyWill()
    print("lucky whill click")
    clickOnLuckyWill()
    print("lucky whill click")
    clickOnLuckyWill()
    print("lucky whill click")
    clickOnLuckyWill()
    print("lucky whill click")
    clickOnLuckyWill()
    print("lucky whill click")
    time.sleep(3)
    mousePos((416,335))#complite level 3
    print(">>>>>>LEVEL (3)<<<<<<")
    leftClick()
    time.sleep(3) 
#def level_3_4():  
    time.sleep(3) 
    bayItams()
    print(">>>>>>bayItamBtn<<<<<<<")
    time.sleep(3)
    mousePos((416,335))#complite level 4 
    leftClick()
    print(">>>>>>>>>>level (4)<<<<<<<<<<<<")#>>>>>>>>>>level (4)<<<<<<<<<<<<<<
    time.sleep(5)
    clowd() #2x gold clowd
    print(">>>>>>clowd+adds<<<<<<<<")
    time.sleep(3)
    Bloon()
    print("<<<<baloon>>>>>")
    time.sleep(1)
    lackWill()
    print("lucky whill inter")
    clickOnLuckyWill()
    print(">>>>>lucky whill clickd<<<<<")
    ExitluckyWill()
    print(">>>>>>>lucky whill exit<<<<<<<<")
    time.sleep(3)
    Pan()
    mousePos((363,270))#gardian2Pic
    leftClick()
    print(">>>>>pan<<<<<")
    exitPan()
    print("exit pan")
    time.sleep(7)
    lackWill()
    print(">>>>>lucky whill inter<<<<<")
    clickOnLuckyWill()
    print("lucky whill clickd")
    ExitluckyWill()
    print("lucky whill exit")
    bayItams()
    print(">>>>>>>>bay itam<<<<<<")
    ExitbayItam()
    print("skipAdds")
    SkipAdds()
    print("exit bay itam")
    lackWill()
    print("<<<<open lucky whill>>>>>")
    clickOnLuckyWill()
    print("klickd on lucky whill")
    clickOnLuckyWill()
    print("klickd on lucky whill")
    clickOnLuckyWill()
    print("klickd on lucky whill")
    ExitluckyWill()
    print("exit lucky whill")
    time.sleep(3)
    gardian3()
    print(">>>>>>pick gardian (3)<<<<<")
    picfruits1()
    print(">>>>>pic fruit 1<<<<<<<")
    time.sleep(1)
    lackWill()
    print("open lucky whill")
    clickOnLuckyWill()
    print("klickd on lucky whill")
    clickOnLuckyWill()
    print("klickd on lucky whill")
    clickOnLuckyWill()
    print("klickd on lucky whill")
    ExitluckyWill()
    print("Exit lucky whill")
    time.sleep(5)
    SkipAdds()
    time.sleep(1)#
    collectReword()
    print(">>>>>colect reword from gardian1<<<<<")
    time.sleep(2)
    collectReword2()
    print("collect reworded from gardian2")
    time.sleep(2)
    collectReword()
    print("collect reword gardian1")
    time.sleep(2)
    collectReword2()
    print("colect reword gardian2")
    time.sleep(2)
    gardian4()
    print(">>>>>pick gardian4")
    time.sleep(1)
    picfruits1()
    print("<<<<pick fruits>>> (1)")
    finishLevel()#>>>>>>>>>>>level(5)<<<<<<<<<<<<<<
    print("<<<<<level (5) >>>>>>>")
    #swich to level 5 to and game mode
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #level5toendGame()
    #>>>>>>>>>>>>End Game tutoreal<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def level5toendGame():
    time.sleep(2)
    Bloon()
    time.sleep(1)
    LuckyWhillx10()
    time.sleep(2)
    bayItams()
    time.sleep(2)
    ExitbayItam()
    SkipAdds()
    time.sleep(7)
    Bloon()
    time.sleep(2)
    LuckyWhillx10()
    time.sleep(2)
    bayItams()
    time.sleep(2)
    ExitbayItam()
    time.sleep(2)
    SkipAdds()
    time.sleep(2)
    Bloon()
    time.sleep(2)
    LuckyWhillx10()
    time.sleep(1)
    

def skip30Min():
    time.sleep(3)
    mousePos((109,107))# inter button
    leftClick()
    time.sleep(1)
    mousePos((413,353))
    leftClick()
    time.sleep(11)
    print("end")

def grdianAddVal():
    time.sleep(2)
    Pan()
    mousePos((462,435))# scale pan position
    leftClick()
    time.sleep(1)
####################################
    mousePos((396,318))#gardian 1
    leftClick()
    time.sleep(10)
    mousePos((364,263))#gardian 2
    leftClick()
    time.sleep(10)
    mousePos((334, 219))#gardian 3
    leftClick()
    time.sleep(10)
    mousePos((457 ,280))#gardian 4
    leftClick()
    time.sleep(10)
    mousePos((423, 235))#gardian 5
    leftClick()
    time.sleep(10)
    mousePos((383, 187))#gardian 6
    leftClick()
    time.sleep(10)
    mousePos((509 ,252))#gardian 7
    leftClick()
    time.sleep(10)
    mousePos((478, 215))#gardian 8
    leftClick()
    time.sleep(10)
    mousePos((440 ,161))#gardian 9
    leftClick()
    time.sleep(10)

def clickOnluckyBtn():
    mousePos((414,385))#button of lucky will 
    leftClick()
    time.sleep(1)
    clickOnluckyBtn()

def LuckyWhillx10():
    print("lucky whill")
    lackWill()
    clickOnLuckyWill()
    clickOnLuckyWill()
    clickOnLuckyWill()
    clickOnLuckyWill()
    clickOnLuckyWill()
    clickOnLuckyWill()
    clickOnLuckyWill()
    clickOnLuckyWill()
    clickOnLuckyWill()
    clickOnLuckyWill()
    ExitluckyWill()
    SkipAdds()
   
def exitPan():
    mousePos((534,436))#Exit pan button
    leftClick()

def bayItams():
    time.sleep(3)
    mousePos((799,425))#bay button
    leftClick()
    time.sleep(3)
    mousePos((425,211))#slot 1
    leftClick()
    time.sleep(3)
    mousePos((426,269))#slot 2
    leftClick()
    time.sleep(3)
    mousePos((417,319))#slot 3
    leftClick()
    time.sleep(3)
    print("bayItams")

def ExitbayItam():
    print("ExitBayItam")
    mousePos((532,444))#exit button bay itam
    leftClick()

def SkipAdds():
    print("SkipAdds")
    time.sleep(8)
    mousePos((722,406))#skip adds
    leftClick()
    
def clowd():
    print("clowd")
    mousePos((789,128))
    leftClick()
    mousePos((420,365))#make it rain
    time.sleep(1)
    leftClick()
    time.sleep(15)

def picfruits1():
    mousePos((346, 256))#pic froth1
    leftClick()
    time.sleep(1)

def picfruits2():
    mousePos((365, 282))#pic froth1
    leftClick()
    time.sleep(2)
    mousePos((341,250)) 
    leftClick()
    time.sleep(1)

def collectReword():
    time.sleep(1)
    mousePos((360, 346))
    time.sleep(1)
    mousePos((380, 322))
    time.sleep(1)
    mousePos((392, 322))
    leftClick()
    print("click 3 get froth")
    time.sleep(1)

def collectReword2():
    time.sleep(3)
    mousePos((295 ,311))
    leftClick()
    mousePos((336,295))
    leftClick()
    mousePos((362, 271))
    leftClick()
    time.sleep(1)

def Pan():
    mousePos((417,427))  #pan
    leftClick()
    time.sleep(5)
    
def lackWill():
    mousePos((38, 364))#enter the luckywill
    leftClick()
    print("in lucky will")
    time.sleep(1)

def clickOnLuckyWill():
    mousePos((414,385))#button of lucky will 
    leftClick()
    time.sleep(7)

def ExitluckyWill():
    mousePos((531,437))
    leftClick()
    print("exit lucky will ")

def gardian1():
    mousePos((394,324))
    leftClick()

def gardian2():    
    #location of 2 box
    mousePos((362 ,275))
    leftClick()
    time.sleep(5)

def gardian3():    
    #location of 3 box  
    mousePos((333,228))
    leftClick()
    time.sleep(5)

def gardian4():
    #location of 4 box
    time.sleep(3)
    mousePos((448,294))
    leftClick()
    time.sleep(5)

def gardian5():
    #location of 5 box
    mousePos((421,243))
    leftClick()
    time.sleep(5)

def gardian6():
    #location of 6 box
    mousePos((388 ,199))
    leftClick()
    time.sleep(5)

def gardian7():
    #location of 7 box
    mousePos((502 ,260))
    leftClick()

    time.sleep(5)

def gardian8():
    #location of 8 box
    mousePos((470 ,206 ))
    leftClick()
    time.sleep(5)

def gardian9():
    #location of 9 box
    mousePos((445, 166))
    leftClick()
    time.sleep(5)

def main():    
    gui()
   # WabWin()#open broweser
   # time.sleep(5)#delay 5 sec
   # startGame()
   # time.sleep(1)

def Bloon():
    print("baloon")
    mousePos((361,290))   #baloon1
    print("bloon1Presst")
    leftClick() 
    time.sleep(1)

    mousePos((499,122))  #baloon2
    leftClick()
    print("bloon2Presst")
    time.sleep(1)

    mousePos((503,196))  #baloon3
    leftClick()
    time.sleep(1)
    print("bloon3Presst")
    
    
    mousePos((338,155))  #baloon4
    leftClick() 
    print("bloon4Presst")
    time.sleep(1) 

    mousePos((333,193))  #baloon5
    leftClick()
    print("bloon5Presst") 
    time.sleep(1)

    mousePos((502,161))  #baloon6
    leftClick()
    print("bloon6Presst")
    time.sleep(1)

    mousePos((397,169))  #baloon3
    leftClick()
    print("bloon7Presst")
    time.sleep(1)

    mousePos((494,252))#baloon4
    leftClick()
    mousePos((342,275))#baloon5
    leftClick()
    mousePos((496,256))#baloon6
    leftClick()
    mousePos((432,298))#baloon7
    leftClick()
    mousePos((488,108))#baloon8
    leftClick()

def finishLevel():
    time.sleep(1)
    mousePos((416,335))#complite level 2 
    leftClick()

#create event
stopThreading = threading.Event()
#set the event of thread you make above to True  so we can set the event stopThreding.is_set  to =True
def signal_handler(sigNum,frame):
    stopThreading.set()
#  # # 
signal.signal(signal.SIGINT,signal_handler)

############## GUI GUI GUI GUI  GUI GUI GUI GUI  GUI GUI GUI GUI GUI GUI GUI GUI GUI GUI GUI GUI GUI GUI GUI GUI GUI GUI    

#margins=( 1,310) my needed set screen <<<< here >>>>> 
## 995,120 ,1280,720,
#visual studio code timps list short cats >>>>
#alt laft_mouse_click on target will make you Wirth 2 or more lines together#
#my screen 1280,720
#sg.theme("DarkPurple6")


#thet commend is set the signal thread Event thet we creat above to True ech signal need is on hendler func?



StartGame = threading.Thread(target=startGame)#frame ? 
Level5ToEnd = threading.Thread(target=level5toendGame)

#StartGame.daemon = True
#Level5ToEnd.daemon = True
##### ELEMENTS ######
layout1 =[
[sg.Text("game of farmer Bot")],#set text
[sg.Text("made by yogev shushan IL worior")],
[sg.Button("openViewGame"),sg.Button("closeBot")],
[sg.Button("StopBot"),sg.Button("startBot"),sg.Button("LeveL5above")],
[sg.Button("screenGrab"),sg.Button("get_cords"),sg.Button("leftClick") ],

[sg.Button("skip30Min")],  
]
def gui():
    window = sg.Window('Multithreaded Window',size=(230,500),location=(1035,70),
    keep_on_top=True, element_padding=(1,1)).Layout(layout1)

    while True:    
    #event, Values = Window.read(timeout=(1000)) # make 2 vars  and loop true the event and values
        event, values = window.Read(timeout=100)
        if event == "closeBot" or event == sg.WIN_CLOSED :# if event (topBot) or (window close) brake
                break          
                print(f'{event}clean brake Good job')
        elif event == "StopBot" or stopThreading.is_set() :
                print (f'{stopThreading.is_set(),{StartGame.name}}event is set true =loop break')
                
                print(f'thread<>identity { _thread.get_ident()}')

                
                _thread.exit()
                print(f'{StartGame}print after the break')      
        elif event == "startBot":
             StartGame.start()
             StartGame.join()
              

             if StartGame.is_alive():
                StartGame_id =StartGame.native_id
                print(f'{StartGame.is_alive()}is_alive{StartGame_id}<< id >>')
                print("StartGame<<< is on >>>")  
        elif event == "openViewGame" :
              WabWin()
        
        elif event == "screenGrab":    
            screenGrab()
            print("screenGrab")

        elif event == "get_cords":
            get_cords()
            print("Cords")
        elif event == "LeveL5above":
            
            Level5ToEnd.start()
            print("END event level5ToEnd")
            
               
        elif event == "skip30Min":
            skip30Min()
        else: window.refresh()
    print("loop bake end Line befor window Close")    
    window.close()# dont forget to close at the end !!!!
    
   

#layout <element contents>
#window sattings 
#Window=sg.Window("title",layout,size=(150,550),location=(1110,100),keep_on_top=True, element_padding=(1,1),)# set the win title and display
# events , values 
    
if __name__ == '__main__':
    main()

 


