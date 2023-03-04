import pygame

(width, height) = (1000, 500)
background_colour = (255, 255, 255)

color = (0,0,0)
center_point = (50,50)

pygame.display.set_caption('Achtung die Kurve')
screen = pygame.display.set_mode((width, height))

screen.fill(background_colour)

pygame.display.flip()

clock = pygame.time.Clock()

pygame.draw.circle(screen, color, center_point,20)
pygame.display.update()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
                



    pygame.display.update()
    clock.tick(60)








"""

# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
