import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0);

def main():
    window = initWindow()
    start(window)

def initWindow():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Git - Branching")
    return window

def start(window):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(BLACK)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
