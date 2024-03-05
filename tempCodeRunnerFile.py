import os
import eel
from engine.features import playAssistantSound
from engine.command import *

# Initialize Eel with the 'www' directory
eel.init("www")

def start():
    # Play the assistant sound (assuming playAssistantSound is correctly defined in features)
    playAssistantSound()

    # Open the web application using Microsoft Edge
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    # Start the Eel application
    eel.start('index.html', mode=None, host='localhost', block=True)

if __name__ == "__main__":
    # Start the application when the script is run
    start()
