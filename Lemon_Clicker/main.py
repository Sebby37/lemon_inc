import pygame
import os
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Lemon Clicker v0.01")

#Gets player score
if not os.path.exists("save_data.lemon"):
    open("save_data.lemon", "w+").write("0")

try:
    PLAYERSCORE = int(open("save_data.lemon", "r").read())
except Exception as e:
    open("save_data.lemon", "w").truncate(0)
    open("save_data.lemon", "w").write("0")

def disp_text(window, text):
    font = pygame.font.SysFont("Comic Sans MS", 30)
    surface = font.render(text, False, (0, 0, 0))
    window.blit(surface, (0, 0))

def disp_lemon(window):
    global PLAYERSCORE
    lemon = pygame.image.load("lemon.png")
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > 25 and mouse_pos[0] < 425 and mouse_pos[1] > 75 and mouse_pos[1] < 375 and pygame.mouse.get_pressed()[0] == True:
        print("Lemon Clicked!!!!")
        PLAYERSCORE += 1
        lemon_resized = pygame.transform.scale(lemon, (300, 200))
        window.blit(lemon_resized, (75, 135))
    else:
        lemon_resized = pygame.transform.scale(lemon, (400, 300))
        window.blit(lemon_resized, (25, 75))

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("save_data.lemon", "w") as savedata:
                savedata.truncate(0)
                savedata.write(str(PLAYERSCORE))
                savedata.close()
            pygame.quit()
            quit(0)

    disp_lemon(window)
    disp_text(window, f"Score: {PLAYERSCORE}")
    
    pygame.display.update()
    clock.tick(60)
    window.fill((255, 255, 255))
