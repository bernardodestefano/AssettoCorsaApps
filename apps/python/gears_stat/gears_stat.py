################################################################################
# Gears Stat
# Assetto Corsa MOD, V1.0, 26.02.2013 V1.0
# Bernardo De Stefano
#
# This app shows statistics for gears usage during each lap.
# First column is total time for a particular gear in seconds.
# Second column is latest time of gear usage before change a gear.
# Third column is % to total of gear usage during the lap.
# This app might be useful for gears rate tuning,
# it allows you to understand utilization of each gear.
################################################################################

import time
import ac
import acsys

curr_gear1_time=0
curr_gear2_time=0
curr_gear3_time=0
curr_gear4_time=0
curr_gear5_time=0
curr_gear6_time=0
curr_gear7_time=0

last_gear1_time=0
last_gear2_time=0
last_gear3_time=0
last_gear4_time=0
last_gear5_time=0
last_gear6_time=0
last_gear7_time=0

curr_gear1_percent=0
curr_gear2_percent=0
curr_gear3_percent=0
curr_gear4_percent=0
curr_gear5_percent=0
curr_gear6_percent=0
curr_gear7_percent=0

start_time=0
curr_gear=-1
prev_gear=-2

x_app_size = 215
y_app_size = 190

x_label1 = 10
x_label2_delta = 70
y_label1 = 40
y_label_delta = 20

gear1_label=0
gear2_label=0
gear3_label=0
gear4_label=0
gear5_label=0
gear6_label=0
gear7_label=0

gear1_last_label=0
gear2_last_label=0
gear3_last_label=0
gear4_last_label=0
gear5_last_label=0
gear6_last_label=0
gear7_last_label=0

gear1_percent_label=0
gear2_percent_label=0
gear3_percent_label=0
gear4_percent_label=0
gear5_percent_label=0
gear6_percent_label=0
gear7_percent_label=0

current_lap_time = -1
is_lap_started = False

def newLap():
    clearCurrTimes();

def clearCurrTimes():
    global curr_gear1_time, curr_gear2_time, curr_gear3_time, curr_gear4_time
    global curr_gear5_time, curr_gear6_time, curr_gear7_time, total_lap_time
    global last_gear1_time, last_gear2_time, last_gear3_time, last_gear4_time, last_gear5_time, last_gear6_time, last_gear7_time

    curr_gear1_time=0
    curr_gear2_time=0
    curr_gear3_time=0
    curr_gear4_time=0
    curr_gear5_time=0
    curr_gear6_time=0
    curr_gear7_time=0

    last_gear1_time=0
    last_gear2_time=0
    last_gear3_time=0
    last_gear4_time=0
    last_gear5_time=0
    last_gear6_time=0
    last_gear7_time=0

    total_lap_time = 0
    curr_gear = -1
    prev_gear = -2

def onUpdate(game_gear):

    global start_time, curr_gear, prev_gear, curr_gear1_time, curr_gear2_time, curr_gear3_time, curr_gear4_time
    global curr_gear5_time, curr_gear6_time, curr_gear7_time
    global curr_gear1_percent, curr_gear2_percent, curr_gear3_percent, curr_gear4_percent, curr_gear5_percent
    global curr_gear6_percent, curr_gear7_percent
    global last_gear1_time, last_gear2_time, last_gear3_time, last_gear4_time, last_gear5_time, last_gear6_time, last_gear7_time

    if curr_gear == game_gear:
        delta = time.time() - start_time

        if curr_gear == 2:
            curr_gear1_time += delta
            if curr_gear == prev_gear:
                last_gear1_time += delta
            else:
                prev_gear = curr_gear
                last_gear1_time = delta

        if curr_gear == 3:
            curr_gear2_time += delta
            if curr_gear == prev_gear:
                last_gear2_time += delta
            else:
                prev_gear = curr_gear
                last_gear2_time = delta


        if curr_gear == 4:
            curr_gear3_time += delta
            if curr_gear == prev_gear:
                last_gear3_time += delta
            else:
                prev_gear = curr_gear
                last_gear3_time = delta

        if curr_gear == 5:
            curr_gear4_time += delta
            if curr_gear == prev_gear:
                last_gear4_time += delta
            else:
                prev_gear = curr_gear
                last_gear4_time = delta

        if curr_gear == 6:
            curr_gear5_time += delta
            if curr_gear == prev_gear:
                last_gear5_time += delta
            else:
                prev_gear = curr_gear
                last_gear5_time = delta


        if curr_gear == 7:
            curr_gear6_time += delta
            if curr_gear == prev_gear:
                last_gear6_time += delta
            else:
                prev_gear = curr_gear
                last_gear6_time = delta


        if curr_gear == 8:
            curr_gear7_time += delta
            if curr_gear == prev_gear:
                last_gear7_time += delta
            else:
                prev_gear = curr_gear
                last_gear7_time = delta


        start_time = time.time()
    else:
        curr_gear = game_gear
        start_time = time.time()

    total_lap_time = curr_gear1_time + curr_gear2_time + curr_gear3_time + curr_gear4_time + curr_gear5_time + curr_gear6_time + curr_gear7_time

    if total_lap_time != 0:
        curr_gear1_percent = round((curr_gear1_time * 100) / total_lap_time)
        curr_gear2_percent = round((curr_gear2_time * 100) / total_lap_time)
        curr_gear3_percent = round((curr_gear3_time * 100) / total_lap_time)
        curr_gear4_percent = round((curr_gear4_time * 100) / total_lap_time)
        curr_gear5_percent = round((curr_gear5_time * 100) / total_lap_time)
        curr_gear6_percent = round((curr_gear6_time * 100) / total_lap_time)
        curr_gear7_percent = round((curr_gear7_time * 100) / total_lap_time)

def acMain(ac_version):
    global gear1_label, gear2_label, gear3_label, gear4_label, gear5_label, gear6_label, gear7_label
    global gear1_percent_label, gear2_percent_label, gear3_percent_label, gear4_percent_label, gear5_percent_label, gear6_percent_label, gear7_percent_label
    global gear1_last_label, gear2_last_label, gear3_last_label, gear4_last_label, gear5_last_label, gear6_last_label, gear7_last_label
    appWindow = ac.newApp("Gears Stat")
    ac.setSize(appWindow, x_app_size, y_app_size)

    x_delta = 10
    y_label = y_label1
    gear1_label = ac.addLabel(appWindow, "gear1_label")
    ac.setPosition(gear1_label, x_label1, y_label)
    gear1_last_label = ac.addLabel(appWindow, "gear1_last_label")
    ac.setPosition(gear1_last_label, x_label1 + x_label2_delta + x_delta, y_label)
    gear1_percent_label = ac.addLabel(appWindow, "gear1_percent_label")
    ac.setPosition(gear1_percent_label, x_label1 + 2*x_label2_delta, y_label)

    y_label += y_label_delta
    gear2_label = ac.addLabel(appWindow, "gear2_label")
    ac.setPosition(gear2_label, x_label1, y_label)
    gear2_last_label = ac.addLabel(appWindow, "gear2_last_label")
    ac.setPosition(gear2_last_label, x_label1 + x_label2_delta + x_delta, y_label)
    gear2_percent_label = ac.addLabel(appWindow, "gear2_percent_label")
    ac.setPosition(gear2_percent_label, x_label1 + 2*x_label2_delta, y_label)

    y_label += y_label_delta
    gear3_label = ac.addLabel(appWindow, "gear3_label")
    ac.setPosition(gear3_label, x_label1, y_label)
    gear3_last_label = ac.addLabel(appWindow, "gear3_last_label")
    ac.setPosition(gear3_last_label, x_label1 + x_label2_delta + x_delta, y_label)
    gear3_percent_label = ac.addLabel(appWindow, "gear3_percent_label")
    ac.setPosition(gear3_percent_label, x_label1 + 2*x_label2_delta, y_label)

    y_label += y_label_delta
    gear4_label = ac.addLabel(appWindow, "gear4_label")
    ac.setPosition(gear4_label, x_label1, y_label)
    gear4_last_label = ac.addLabel(appWindow, "gear4_last_label")
    ac.setPosition(gear4_last_label, x_label1 + x_label2_delta + x_delta, y_label)
    gear4_percent_label = ac.addLabel(appWindow, "gear4_percent_label")
    ac.setPosition(gear4_percent_label, x_label1 + 2*x_label2_delta, y_label)

    y_label += y_label_delta
    gear5_label = ac.addLabel(appWindow, "gear5_label")
    ac.setPosition(gear5_label, x_label1, y_label)
    gear5_last_label = ac.addLabel(appWindow, "gear5_last_label")
    ac.setPosition(gear5_last_label, x_label1 + x_label2_delta + x_delta, y_label)
    gear5_percent_label = ac.addLabel(appWindow, "gear5_percent_label")
    ac.setPosition(gear5_percent_label, x_label1 + 2*x_label2_delta, y_label)

    y_label += y_label_delta
    gear6_label = ac.addLabel(appWindow, "gear6_label")
    ac.setPosition(gear6_label, x_label1, y_label)
    gear6_last_label = ac.addLabel(appWindow, "gear6_last_label")
    ac.setPosition(gear6_last_label, x_label1 + x_label2_delta + x_delta, y_label)
    gear6_percent_label = ac.addLabel(appWindow, "gear6_percent_label")
    ac.setPosition(gear6_percent_label, x_label1 + 2*x_label2_delta, y_label)

    y_label += y_label_delta
    gear7_label = ac.addLabel(appWindow, "gear7_label")
    ac.setPosition(gear7_label, x_label1, y_label)
    gear7_last_label = ac.addLabel(appWindow, "gear7_last_label")
    ac.setPosition(gear7_last_label, x_label1 + x_label2_delta + x_delta, y_label)
    gear7_percent_label = ac.addLabel(appWindow, "gear7_percent_label")
    ac.setPosition(gear7_percent_label, x_label1 + 2*x_label2_delta, y_label)

    updateGearsInfo(True)
    newLap()

def acUpdate(deltaT):
    global current_lap_time, is_lap_started

    # logic to detect starting of new lap
    current_lap_time = ac.getCarState(0, acsys.CS.LapTime)
    if (current_lap_time < 300) and (is_lap_started == False):
        is_lap_started = True
        newLap()
    if current_lap_time > 2000:
        is_lap_started = False

    onUpdate(ac.getCarState(0, acsys.CS.Gear))
    updateGearsInfo(False)

def updateGearsInfo(force_update):
    if(is_lap_started == False or force_update == True):
        ac.setText(gear1_label, "1: {0}".format(round(curr_gear1_time, 1)))
        ac.setText(gear2_label, "2: {0}".format(round(curr_gear2_time, 1)))
        ac.setText(gear3_label, "3: {0}".format(round(curr_gear3_time, 1)))
        ac.setText(gear4_label, "4: {0}".format(round(curr_gear4_time, 1)))
        ac.setText(gear5_label, "5: {0}".format(round(curr_gear5_time, 1)))
        ac.setText(gear6_label, "6: {0}".format(round(curr_gear6_time, 1)))
        ac.setText(gear7_label, "7: {0}".format(round(curr_gear7_time, 1)))

        ac.setText(gear1_last_label, "{0}".format(round(last_gear1_time, 1)))
        ac.setText(gear2_last_label, "{0}".format(round(last_gear2_time, 1)))
        ac.setText(gear3_last_label, "{0}".format(round(last_gear3_time, 1)))
        ac.setText(gear4_last_label, "{0}".format(round(last_gear4_time, 1)))
        ac.setText(gear5_last_label, "{0}".format(round(last_gear5_time, 1)))
        ac.setText(gear6_last_label, "{0}".format(round(last_gear6_time, 1)))
        ac.setText(gear7_last_label, "{0}".format(round(last_gear7_time, 1)))

        ac.setText(gear1_percent_label, "{0} %".format(round(curr_gear1_percent, 1)))
        ac.setText(gear2_percent_label, "{0} %".format(round(curr_gear2_percent, 1)))
        ac.setText(gear3_percent_label, "{0} %".format(round(curr_gear3_percent, 1)))
        ac.setText(gear4_percent_label, "{0} %".format(round(curr_gear4_percent, 1)))
        ac.setText(gear5_percent_label, "{0} %".format(round(curr_gear5_percent, 1)))
        ac.setText(gear6_percent_label, "{0} %".format(round(curr_gear6_percent, 1)))
        ac.setText(gear7_percent_label, "{0} %".format(round(curr_gear7_percent, 1)))

def testRun():
    global curr_gear1_time, curr_gear2_time, curr_gear1_percent, curr_gear2_percent, total_lap_time
    newLap()
    onUpdate(1)
    time.sleep(0.017)
    onUpdate(1)
    onUpdate(2)
    time.sleep(0.025)
    onUpdate(2)
    onUpdate(1)
    time.sleep(0.019)
    onUpdate(1)
    print(curr_gear1_time)
    print(curr_gear2_time)
    print(total_lap_time)
    print(curr_gear1_percent)
    print(curr_gear2_percent)
