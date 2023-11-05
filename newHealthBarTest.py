from cmu_graphics import *

def onAppStart(app):
    app.health1 = 100  # Percentage of health for player 1
    app.health2 = 100  # Percentage of health for player 2
    app.healthBarWidthPercent = 20  # Width of the health bar as a percentage of screen width
    app.healthBarHeight = 20  # Height of the health bar
    app.testHealthReduction = True  # Flag to test health bar reduction

def redrawAll(app):
    # Calculate the width of the health bar based on the percentage of the screen width
    healthBarFullWidth = app.width * (app.healthBarWidthPercent / 100)
    
    # Outer rectangle (border for the health bar) for player 1
    drawRect(app.width * 0.1, app.height * 0.1, healthBarFullWidth, app.healthBarHeight, fill=None, border='black')
    
    # Filled health bar for player 1 based on current health
    healthBarCurrentWidth = max(1.0, healthBarFullWidth * (app.health1 / 100))
    drawRect(app.width * 0.1, app.height * 0.1, healthBarCurrentWidth, app.healthBarHeight, fill='green')

    # Repeat the process for player 2 below player 1's health bar
    drawRect(app.width * 0.1, app.height * 0.1 + 30, healthBarFullWidth, app.healthBarHeight, fill=None, border='black')
    healthBarCurrentWidth2 = max(1.0, healthBarFullWidth * (app.health2 / 100))
    drawRect(app.width * 0.1, app.height * 0.1 + 30, healthBarCurrentWidth2, app.healthBarHeight, fill='blue')

def onStep(app):
    # This is just for testing purposes to simulate health reduction over time
    if app.testHealthReduction:
        app.health1 -= 0.1  # Decrease player 1's health
        app.health2 -= 0.2  # Decrease player 2's health
        
        # Clamp the health values to be no less than 0
        app.health1 = max(app.health1, 0)
        app.health2 = max(app.health2, 0)
        
        # Stop the test once health is depleted
        if app.health1 <= 0 and app.health2 <= 0:
            app.testHealthReduction = False

def main():
    runApp()

main()
