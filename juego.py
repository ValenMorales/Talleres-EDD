import pygame
import pygame_gui
import sys

pygame.init()

WIDTH, HEIGHT = 800, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jueguito")

manager = pygame_gui.UIManager((WIDTH, HEIGHT))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 100), (150, 50)), manager=manager,
                                               object_id='#main_text_entry')

clock = pygame.time.Clock()
corde_y = 230
radio = 30

def show_nodes(number):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for i in range(100,(int(number)+1)*100, 100):
                pygame.draw.circle (SCREEN, "black", (i+radio,corde_y),radio, 5)

        pygame.display.update()
        clock.tick(60)

def input_data():
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                 show_nodes(event.text)

            manager.process_events(event)

        manager.update(UI_REFRESH_RATE)

        SCREEN.fill("white")

        manager.draw_ui(SCREEN)

        pygame.display.update()
    

input_data()