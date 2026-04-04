from pyfiglet import figlet_format
from pystyle import Colorate,Colors

def Log():
  #smmono12 font i us 
  text = figlet_format("Z-ROCK",font="smmono12")
  print(Colorate.Horizontal(Colors.green_to_blue,text))