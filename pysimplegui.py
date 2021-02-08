# Music player in python
import PySimpleGUI as sg
sg.theme("DarkPurple4")

from demo import get_file
#file = get_file()
from pygame import mixer

import os
file = get_file()
filename = os.path.basename(file)
print(filename)


layout = [
        [sg.Button("Play", size=["30", "2"], key='-PLAY-')],
        [sg.Button("Pause", size=["30", "2"], key='-PAUSE-')],
        [sg.Button("UnPause", size=["30", "2"], key='-UNPAUSE-')],
        [sg.Button("Reset", size=['30', '2'], key="-RESET-")],
        [sg.Text("Volume :-"),sg.Slider(range=(0, 10),default_value= 5,
        orientation='horizontal', key='-VOLUME-', enable_events=True)],
        [sg.Button("Exit Player", size=['30', '2'], key="-EXIT_PLAYER-")]
]


window = sg.Window(filename, layout)




while True:
    events, values = window.read()
    if events in ('-EXIT_PLAYER-', None):
        mixer.music.stop()
        exit()

    elif events in ("-PLAY-"):
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()


    elif events in ("-PAUSE-"):
        mixer.music.pause()

    elif events in ('-UNPAUSE-'):
        mixer.music.unpause()

    #elif events in ('-PLAY'):
        #mixer.music.play()

    elif events in ('-RESET-'):
        mixer.music.stop()
        mixer.music.play()

    elif events in ('-VOLUME-'):
        volume = values['-VOLUME-']
        actual_volume = volume / 10
        mixer.music.set_volume(actual_volume)

    else:
        sg.popup("event not recognised")

