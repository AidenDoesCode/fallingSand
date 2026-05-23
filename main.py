import pygame
import sand
import random
import button
import sys

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# set initial sand value to sand color
rainbowSand = False
# Initialize the manager
manager = sand.SandManager()

def getRandRGB():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

# --- 1. Define the Button Actions ---
def clearScreen():
    manager.clear_all()

def setRainbowColor():
    global rainbowSand  
    rainbowSand = True

def switchToSandMode():
    global rainbowSand
    rainbowSand = False

def getSandColor():
    return (194, 178, 128)

# --- Created Clear Button Instance ---
clearButton = button.Button(
    x=1160, 
    y=20, 
    width=100, 
    height=25, 
    text="Clear",       
    color=(50, 50, 50), 
    hover_color=(100, 100, 100), 
    action=clearScreen
)

# --- Created Rainbow Button Instance ---
rainbowButton = button.Button(
    x=1160, 
    y=55, 
    width=100, 
    height=25, 
    text="Rainbow",       
    color=(50, 50, 50), 
    hover_color=(100, 100, 100), 
    action=setRainbowColor  
)

sandColorButton = button.Button(
    x=1160, 
    y=90, 
    width=100, 
    height=25, 
    text="Sand Color",       
    color=(50, 50, 50), 
    hover_color=(100, 100, 100), 
    action=switchToSandMode  
)

while running:
    # 1. Event Handling Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # --- 3. Check Button Clicks ---
        clearButton.check_click(event)
        rainbowButton.check_click(event)
        sandColorButton.check_click(event)

    # 2. Input Handling (Spawning Sand)
    mouse_buttons = pygame.mouse.get_pressed()
    
    # Check if mouse is over the Buttons to prevent spawning sand behind it
    mouse_pos = pygame.mouse.get_pos()
    if mouse_buttons[0] and not (clearButton.rect.collidepoint(mouse_pos) or rainbowButton.rect.collidepoint(mouse_pos) or sandColorButton.rect.collidepoint(mouse_pos)):
        x, y = mouse_pos
        if rainbowSand:
            manager.add_rect(getRandRGB(), x, y)
        else: 
            manager.add_rect(getSandColor(), x, y)

    # 3. Frame Engine & Physics Triggers
    manager.frame_count += 1
    
    # Run the physics engine update step every 2 frames
    if manager.frame_count % 2 == 0:
        manager.update_physics()

    # 4. Rendering / Drawing Stage
    screen.fill((20, 24, 30)) # Dark night sky background
    
    # --- 4. Draw the Buttons ---
    clearButton.draw(screen)
    rainbowButton.draw(screen)
    sandColorButton.draw(screen)

    manager.draw_all(screen)  # Render current grid state
    pygame.display.flip()     # Swap graphics buffer to display

    # 5. Framerate Cap
    clock.tick(60)

pygame.quit()