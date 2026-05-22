import pygame
import sand

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Initialize the manager
manager = sand.SandManager()

while running:
    # 1. Event Handling Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Input Handling (Spawning Sand)
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # Held left mouse button
        x, y = pygame.mouse.get_pos()
        manager.add_rect((234, 182, 88), x, y)  # Spawns a sand-colored grain

    # 3. Frame Engine & Physics Triggers
    manager.frame_count += 1
    
    # Run the physics engine update step every 2 frames
    if manager.frame_count % 2 == 0:
        manager.update_physics()

    # 4. Rendering / Drawing Stage
    screen.fill((20, 24, 30)) # Dark night sky background
    manager.draw_all(screen)  # Render current grid state
    pygame.display.flip()     # Swap graphics buffer to display

    # 5. Framerate Cap
    clock.tick(60)

pygame.quit()