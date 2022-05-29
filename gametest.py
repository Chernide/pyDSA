import pygame

def main():
    pygame.init()

    sub = pygame.image.load("./resources/submarine.png")
    pygame.display.set_icon(sub)
    pygame.display.set_caption("pyDSA")

    screen = pygame.display.set_mode((800,800))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()