from cmu_graphics import *
def loadFighter(app):
    class Fighter():
        def __init__(self, name, x, health):
            self.name = name
            self.health = health
            self.x = x
            self.alive = True
def onAppStart(app):
    loadFighter(app)
    app.width = 1000
    app.height = 500
    pat = Fighter('PAT', 100, 100)
    mike = Fighter('MIKE', 900, 100)

def redrawAll(app):
    drawRect(pat.x, 500, 100, 100, fill = 'red')
    drawRect(mike.x, 500, 100, 100, fill = 'blue')

def onStep(app):
    pass

def onKeyPress(app, key):
    pass

def main():
    runApp()

main()