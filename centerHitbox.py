from cmu_graphics import *

def onAppStart(app):
    app.level = 0
    app.blueX = 120
    app.blueY = 300
    app.redX = 280
    app.redY = 300
    app.stepsPerSecond = 24
    app.redMoving = False
    app.healthRed = 100
    app.healthBlue = 100
    app.blueDX = 0
    app.redDX = 0
    app.blueMoving = False
    app.redWidth, app.redHeight = (60, 100)
    app.blueWidth, app.blueHeight = (60, 100)
    app.redKick = False
    app.blueKick = False
    app.redKickCounter = 0
    app.blueKickCounter = 0
    app.winnerRed = False
    app.winnerBlue = False
    app.GameOver = False

def onKeyPress(app, key):
    if key == "r":
        if not app.redKick:
            app.redKick = True
            app.redKickCounter = 0
        if distance(app, app.redX, app.blueX, app.redY, app.blueY) < app.redHeight + app.blueWidth and app.healthBlue > 10:
            app.healthBlue -= 10
        elif distance(app, app.redX, app.blueX, app.redY, app.blueY) < app.redHeight + app.blueWidth and app.healthRed == 10:
            app.healthBlue -= 9
            app.gameOver = True 
            app.WinnerRed = True

    if key == '/':
        if not app.blueKick:
            app.blueKick = True
            app.blueKickCounter = 0
        if distance(app, app.redX, app.blueX, app.redY, app.blueY) < app.redWidth + app.blueHeight and app.healthRed > 10:
            app.healthRed -= 10
        elif distance(app, app.redX, app.blueX, app.redY, app.blueY) < app.redWidth + app.blueHeight and app.healthRed == 10:
            app.healthRed -= 9
            app.gameOver = True
            app.winnerBlue = True

def onKeyHold(app, keys):
    if "a" in keys:
        app.blueMoving = True
        app.blueDX = -10
    if "d" in keys:
        #if app.blueX + app.blueWidth < app.redX - app.redWidth: 
        app.blueMoving = True    
        app.blueDX = 10
    if "right" in keys:
        #if app.redX > app.blueX:
        app.redMoving = True
        app.redDX = 10
    if "left" in keys:
        #if app.redX - app.redWidth > app.blueX + app.blueWidth:
        app.redDX = -10
        app.redMoving = True

def onKeyRelease(app, key):
    if key == "a" or key == "d":
        app.blueMoving = False
        app.blueDX = 0
    if key == "right" or key == "left":
        app.redMoving = False
        app.redDX = 0

# def isValidPosition(app):
#     if (app.blueX + app.blueWidth + app.blueDX > app.redX- app.redWidth or 
#         app.redX - app.redWidth + app.redDX < app.blueX + app.blueWidth):
#         return False
#     return True

def onStep(app):
    if app.blueMoving:
        app.blueX += app.blueDX
        if not isValidPos(app):
            app.blueX -= app.blueDX
            app.blueDX = 0
    if app.redMoving:
        app.redX += app.redDX
        if not isValidPos(app):
            app.redX -= app.redDX
            app.redDX = 0
    if app.redKick:
        app.redKickCounter += 1
        if app.redKickCounter == 1:
            app.redWidth, app.redHeight = (app.redHeight, app.redWidth)
        if app.redKickCounter >= 20:
            app.redKickCounter = 0
            app.redKick = False
            app.redWidth, app.redHeight = (60, 100)
    if app.blueKick:
        app.blueKickCounter += 1
        if app.blueKickCounter == 1:
            app.blueWidth, app.blueHeight = (app.blueHeight, app.blueWidth)
        if app.blueKickCounter >= 20:
            app.blueKickCounter = 0
            app.blueKick = False
            app.blueWidth, app.blueHeight = (60, 100)

def redrawAll(app):
    
    if app.winnerRed == True:
        drawLabel("Red Wins", 200, 230)
    elif app.winnerBlue == True:
        drawLabel("BlueWins", 200, 230)

    drawRect(app.blueX, app.blueY, app.blueWidth, app.blueHeight, fill="blue",
             align = 'center')
    drawRect(app.redX, app.redY, app.redWidth, app.redHeight, fill="red",
             align = 'center')
    
    ##BlueHealth
    drawRect(app.width/10, app.height/10, 100, 10, fill = 'red', border = 'black')
    drawRect(app.width/10, app.height/10, app.healthBlue, 10, fill = 'green', border = 'black')
    
    ##RedHealth
    drawRect(app.width - app.width/10 - 100, app.height/10, 100, 10, fill = 'red', border = 'black')
    drawRect(app.width - app.width/10 - 100, app.height/10, app.healthRed, 10, fill = 'green', border = 'black')

def isValidPos(app):
    if app.blueWidth/2 + app.redWidth/2 > app.redX - app.blueX:
        return False
    return True

    
    # if (app.blueX <= app.redX - app.redWidth <= app.blueX + app.blueWidth or 
    #     app.blueX <= app.redX<= app.blueX + app.blueWidth or
    #     app.redX - app.redWidth <= app.blueX <= app.redX or 
    #     app.redX - app.redWidth <= app.blueX + app.blueWidth <= app.redX):
    #           return False
    # else:
    #      return True
    
def distance(app, x1, x2, y1, y2):
    return((x1 - x2)**2+(y1-y2)**2)**0.5

def main():
    runApp()

main()
