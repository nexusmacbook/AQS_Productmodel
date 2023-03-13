import pyttsx3,traceback
from module import LineNotify

try:
    def soundENG(soundstr,soundAct):
        if soundAct == 1:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty("voice", voices[0].id)
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate-40)
            engine.say(soundstr)
            engine.runAndWait()
        else:
            pass
    
except BaseException as be:

    traceerror = traceback.print_exc()
    LineNotify.LINE(f"\n例外発生:{be}\n{str(traceerror)}")