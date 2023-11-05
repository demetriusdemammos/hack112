
from cmu_graphics import *

def onAppStart(app):
    app.Health1 = 100
    app.Health2 = 100

def redrawAll(app):
    drawRect(app.width/10, app.height/10, app.width/10 + 100, app.height/10 + 10, fill = None, border = 'black')

def main():
    runApp()

main()
