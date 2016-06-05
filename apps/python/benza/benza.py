import sys
import ac
import acsys
import sim_info

l_lapcount=0
lapcount=0
b_benzina=0
benzina=0

def acMain(ac_version):
    global l_lapcount, b_benzina


    appWindow = ac.newApp("benza")
    ac.setSize(appWindow, 200, 200)

    ac.log("Benza Start")
    ac.console("Benza is running")

    l_lapcount = ac.addLabel(appWindow, "Laps: 0");
    b_benzina  = ac.addLabel(appWindow, "Fuel: 0");

    ac.setPosition(l_lapcount, 3, 30)

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
    ac.log("Benza exit")
    ac.console("Benza exit")
