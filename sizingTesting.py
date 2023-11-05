from cmu_graphics import *
from PIL import Image
def onAppStart(app):
    app.gameOver = False
    app.level = 0
    app.blueX = 100
    app.blueY = 400
    app.redX = 700
    app.redY = 400
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
    app.width = 886
    app.height = 512
    app.steps = 0
    ### Jumping Animations
    app.variations = [0] + list(range(50, -55, -5)) 

    app.cyRed = 400
    app.jumpRed = False
    app.variationsYRed = 1

    app.cyBlue = 400
    app.jumpBlue = False
    app.variationsYBlue = 1
    #Images
    app.backgroundPic = Image.open("background.jpg")
    app.backgroundPic = CMUImage(app.backgroundPic)
    app.mike1Pic = Image.open("mike1.png")
    app.mike1Pic = CMUImage(app.mike1Pic)
    app.mike2Pic = Image.open("mike2.png")
    app.mike2Pic = CMUImage(app.mike2Pic)
    app.mike3Pic = Image.open("mike3.png")
    app.mike3Pic = CMUImage(app.mike3Pic)
    app.mike4Pic = Image.open("mike4.png")
    app.mike4Pic = CMUImage(app.mike4Pic)
    app.mike5Pic = Image.open("mike5.png")
    app.mike5Pic = CMUImage(app.mike5Pic)
    app.mike6Pic = Image.open("mike6.png")
    app.mike6Pic = CMUImage(app.mike6Pic)
    ###Animations
    app.runningBlue = {1: 'runningImage1', 2: 'runningImage2', 3: 'runningImage3', 4: 'runningImage4'}
    app.runIndxBlue = 1
    app.runAnimationBlue = False

    app.restingBlue = {1: 'restingImage1', 2: 'restingImage2', 3: 'restingImage3', 4: 'restingImage4'}
    app.restIndxBlue = 1
    app.restAnimationBlue = True
    app.stepsAnimation = 0
    

    app.runningRed = {1: 'runningImage1', 2: 'runningImage2', 3: 'runningImage3', 4: 'runningImage4'}
    app.runIndxRed = 1
    app.runAnimationRed = False

    app.restingRed = {1: 'restingImage1', 2: 'restingImage2', 3: 'restingImage3', 4: 'restingImage4'}
    app.restIndxRed = 1
    app.restAnimationRed = True

    


def onKeyPress(app, key):
    if app.gameOver != True:
        if key == "e":
            if not app.blueKick:
                app.blueKick = True
                app.blueKickCounter = 0
            if app.blueKickCounter == 0:
                if distance(app, app.redX, app.blueX, app.redY, app.blueY) < app.redHeight + app.blueWidth and app.healthRed > 10:
                    app.healthRed -= 10
                elif distance(app, app.redX, app.blueX, app.redY, app.blueY) < app.redHeight + app.blueWidth and app.healthRed == 10:
                    app.healthRed -= 9
                    app.gameOver = True 
                    app.WinnerBlue = True

        if key == '/':
            if not app.redKick:
                app.redKick = True
                app.redKickCounter = 0
            if app.redKickCounter == 0:
                if distance(app, app.redX, app.blueX, app.redY, app.blueY) < app.redWidth + app.blueHeight and app.healthBlue > 10:
                    app.healthBlue -= 10
                elif distance(app, app.redX, app.blueX, app.redY, app.blueY) < app.redWidth + app.blueHeight and app.healthBlue == 10:
                    app.healthBlue -= 9
                    app.gameOver = True
                    app.winnerRed = True

        ###Jumping Animations:
        if key == 'up':
            app.jumpRed = True
            app.restAnimationBlue = False
        if key == 'w':
            app.jumpBlue = True
            app.restAnimationRed = False


def onKeyHold(app, keys):
    if app.gameOver != True:
        if "a" in keys:
            app.blueMoving = True
            app.blueDX = -10
            app.runAnimationBlue = True
            app.restAnimationBlue = False
            
        if "d" in keys: 
            app.blueMoving = True    
            app.blueDX = 10
            app.runAnimationBlue = True
            app.restAnimationBlue = False

        if "right" in keys:
            app.redMoving = True
            app.redDX = 10
            app.runAnimationRed = True
            app.restAnimationRed = False

        if "left" in keys:
            app.redDX = -10
            app.redMoving = True
            app.runAnimationRed = True
            app.restAnimationRed = False
        



def onKeyRelease(app, key):
    if app.gameOver != True:
        if key == "a" or key == "d":
            app.blueMoving = False
            app.blueDX = 0
        if key == "right" or key == "left":
            app.redMoving = False
            app.redDX = 0
        
        ###Animations
        if 'a' in key or 'd' in key:
            app.runAnimationBlue = False
            app.restAnimationBlue = True

        if 'left' in key or 'right' in key:
            app.runAnimationRed = False
            app.restAnimationRed = True


def onStep(app):
    if app.gameOver != True:
        if app.blueMoving:
            app.blueX += app.blueDX
        if app.redMoving:
            app.redX += app.redDX
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
        
        ### Jumping Animations
        if app.jumpRed == True:
            if app.variationsYRed < len(app.variations):
                app.variationsYRed += 1
            if app.variationsYRed >= len(app.variations):
                app.jumpRed = False
                app.variationsYRed = 1
        else:
            app.variationsYRed = 0
        
        if app.jumpBlue == True:
            if app.variationsYBlue < len(app.variations):
                app.variationsYBlue += 1
            if app.variationsYBlue >= len(app.variations):
                app.jumpBlue = False
                app.variationsYBlue = 1
        else:
            app.variationsYBlue = 0

        ###Animations
        app.stepsAnimation += 1
        if app.stepsAnimation % 7 == 0:
            if app.runAnimationBlue == True:
                if app.runIndxBlue < 5:
                    app.runIndxBlue += 1
                if app.runIndxBlue >= 5:
                    app.runIndxBlue = 1
                print(app.runningBlue[app.runIndxBlue])
            
            if app.restAnimationBlue == True:
                if app.restIndxBlue < 5:
                    app.restIndxBlue += 1
                if app.restIndxBlue >= 5:
                    app.restIndxBlue = 1
                print(app.restingBlue[app.restIndxBlue])

        if app.stepsAnimation % 7 == 0:
            if app.runAnimationRed == True:
                if app.runIndxRed < 5:
                    app.runIndxRed += 1
                if app.runIndxRed >= 5:
                    app.runIndxRed = 1
                print(app.runningRed[app.runIndxRed])
            
            if app.restAnimationRed == True:
                if app.restIndxRed < 5:
                    app.restIndxRed += 1
                if app.restIndxRed >= 5:
                    app.restIndxRed = 1
                print(app.restingRed[app.restIndxRed])


        
    
def onMousePress(app, mx, my):
    print(mx, my)

def redrawAll(app):
    #Draw BG
    drawImage(app.backgroundPic, 400, 200, align = "center")
    drawImage(app.mike1Pic, 200, 200)
    if app.winnerRed == True:
        drawLabel("Mike Wins!", app.width/2, app.height/2, font = 'orbitron', size = 150, fill = 'red', bold = True, border = 'black', borderWidth = 5)
    elif app.winnerBlue == True:
        drawLabel("Pat Wins!", app.width/2, app.height/2, font = 'orbitron', size = 150, fill = 'blue', bold = True, border = 'black', borderWidth = 5)

    drawRect(app.blueX, app.blueY - sum(app.variations[:app.variationsYBlue - 1]) - app.variations[app.variationsYBlue], app.blueWidth, app.blueHeight, fill="blue")
    drawRect(app.redX, app.redY - sum(app.variations[:app.variationsYRed - 1]) - app.variations[app.variationsYRed], app.redWidth, app.redHeight, fill="red",
             align = 'top-right')
    
    ##BlueHealth
    drawRect(app.width/10, app.height/10, 100, 10, fill = 'red', border = 'black')
    drawRect(app.width/10, app.height/10, app.healthBlue, 10, fill = 'green', border = 'black')
    
    ##RedHealth
    drawRect(app.width - app.width/10 - 100, app.height/10, 100, 10, fill = 'red', border = 'black')
    drawRect(app.width - app.width/10 - 100, app.height/10, app.healthRed, 10, fill = 'green', border = 'black')

def isValidPos(app):
    if (app.blueX <= app.redX - app.redWidth <= app.blueX + app.blueWidth or 
        app.blueX <= app.redX<= app.blueX + app.blueWidth or
        app.redX - app.redWidth <= app.blueX <= app.redX or 
        app.redX - app.redWidth <= app.blueX + app.blueWidth <= app.redX):
              return False
    else:
         return True
    
def distance(app, x1, x2, y1, y2):
    return((x1 - x2)**2+(y1-y2)**2)**0.5

def main():
    runApp()

main()
