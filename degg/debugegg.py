import inspect
import colorama
import time
colorama.init(autoreset=True)
degg_msg=True
def debug_egg(txt,col="RED"):
    frame=inspect.stack()[1]
    print("[Line: "+str(frame.lineno)+"]   "+getattr(colorama.Fore,col.upper(),"")+str(txt))
    return"[Line: "+str(frame.lineno)+"]   "+getattr(colorama.Fore,col.upper(),"")+str(txt)
degg=debug_egg
time.sleep(0.5)
if degg_msg==True:
    debug_egg("Hello! It seems you have imported my package 'debug_egg' or 'degg'. I hope you enjoy! \n degg('YOUR_TEXT', 'YOUR_COLOR') \n          -Egglord \n \n","blue")
