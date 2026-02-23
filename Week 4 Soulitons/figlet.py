import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
    figlet.setFont(font=f)

elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in fonts):
        f = sys.argv[2]
        figlet.setFont(font=f)
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))
