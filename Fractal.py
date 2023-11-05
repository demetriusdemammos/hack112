from cmu_graphics import *

def onAppStart(app):
    app.level = 0

def drawFractal(level, cx, cy, w):
    if level == 0:
        drawRect(cx, cy, w, w/5, align = 'center', fill = 'white')
        drawRect(cx, cy-10, w-2, w/5, align = 'center', fill = 'white')
        drawRect(cx, cy-20, w-4, w/5, align = 'center', fill = 'white')
        drawRect(cx, cy-30, w-6, w/5, align = 'center', fill = 'white')
    else:
        drawRect(cx, cy, w, w/5, align = 'center', fill = 'white')
        drawRect(cx, cy-10, w-2, w/5, align = 'center', fill = 'white')
        drawRect(cx, cy-20, w-4, w/5, align = 'center', fill = 'white')
        drawRect(cx, cy-30, w-6, w/5, align = 'center', fill = 'white')
        drawRect(cx, cy-40, w-8, w/5, align = 'center', fill = 'white')
        drawFractal(level-1, cx, cy - 10*level, w-2*level)
        if level == 5:
            drawPolygon(168, 113, cx, 75, 232, 113, fill ='white')
            drawRect(185, 108, 10, 4, fill = 'red')
            drawRect(205, 108, 10, 4, fill = 'red')
        #drawFractal(level, -r/2, r*2/3, r/3)
        #drawCircle()
    
    pass

def onKeyPress(app, key):
    if (key in ['up', 'right']) and (app.level < 5):
        app.level += 1
    elif (key in ['down', 'left']) and (app.level > 0):
        app.level -= 1

def redrawAll(app):
    colorList = ['lightCyan', 'lightBlue', 'lightSteelBlue', 'steelBlue', 'midnightBlue', 'black']
    drawRect(0, 0, app.width, app.height, fill = colorList[app.level])
    drawCircle(app.width/2, app.height+600, 700, fill = 'green')
    drawCircle(app.width/2 - 60*app.level, 30 + 40*app.level**1.3, 50, fill = 'gold')
    drawFractal(app.level, 200, 300, 100)
    
    drawLabel(f'Level {app.level} Fractal',
              app.width/2, 30, size=16, bold=True)
    drawLabel('Use arrows to change level',
              app.width/2, 50, size=12, bold=True)

def main():
    runApp()

main()