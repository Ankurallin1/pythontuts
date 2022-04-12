#l=[ ["ankur",1],["yug",2],
    #["comeon",3],["discord",4] ]
#print(l)
#di=dict(l)
#for i,j in di.items():
#for i,j in l:
  #  print(i, "roll no is", j)
"""f=[7,9,0,9,5,8,23,65,90,12,54]
for i in f:
      if str(i).isnumeric() and i>9:
          print(i)
"""
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)