import sys
import ac
import acsys
import sim_info

#variabili globali poiche ci servono sia un acMain che in acUpdate
l_lapcount=0
lapcount=0
b_benzina=0
benzina=0

def acMain(ac_version): # acMain si occupa esclusivamente del setup dell'app
    global l_lapcount, b_benzina


    appWindow = ac.newApp("benza") #finestra effettiva dell'app
    ac.setSize(appWindow, 200, 200)

    ac.log("Hello, Assetto Corsa application world!")
    ac.console("Hello, Assetto Corsa console!")

    l_lapcount = ac.addLabel(appWindow, "Laps: 0");
    b_benzina  = ac.addLabel(appWindow, "Fuel: 0");

    ac.setPosition(l_lapcount, 3, 30) #il label sara settato a 30 verticali (poiche in alto c'e l'header) e 3 orizzontali per separarlo dal bordo
    ac.setPosition(b_benzina, 3, 50 )

    return "benza"

def acUpdate(deltaT):
    global l_lapcount, lapcount, b_benzina, benzina

    laps = ac.getCarState(0, acsys.CS.LapCount)
    info = sim_info.SimInfo()
    remaining = info.physics.fuel

    if laps > lapcount:
        lapcount = laps
        ac.setText(l_lapcount, "Laps: {}".format(lapcount))

    if remaining < benzina:
        benzina = remaining
        ac.setText(b_benzina, "Fuel: {}".format(benzina))

def acShutdown():
    ac.log("app benz chiusa")
    ac.console("app benza chiusa")
