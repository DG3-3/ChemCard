import pygame
def scinit():
    # Initialize the game
    pygame.init()

    # Set up the display
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Chemistry Card")
    icon = pygame.image.load("../assets/images/tuji.ico")
    pygame.display.set_icon(icon)
    return screen

def main():
    screen = scinit()

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color (RGB)
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.update()

    # Quit the game
    pygame.quit()

main()
