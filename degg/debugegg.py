import inspect
import colorama
colorama.init(autoreset=True)
def debug_egg(txt,col="RED"):
    frame=inspect.stack()[1]
    print("[Line: "+str(frame.lineno)+"]   "+getattr(colorama.Fore,col.upper(),"")+str(txt))
    return"[Line: "+str(frame.lineno)+"]   "+getattr(colorama.Fore,col.upper(),"")+str(txt)
degg=debug_egg
