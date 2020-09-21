import pygame
import os
import random
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Lemon Clicker v0.21a") #Alpha 0.20
clock = pygame.time.Clock()
timer = 0
wait_time = 0
waiting = False

lemon_img = pygame.image.load("lemon.png").convert_alpha()

def ra():
    return random.randint(0, 450)

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
    global lemon_img
    global timer
    lemon = lemon_img
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > 25 and mouse_pos[0] < 425 and mouse_pos[1] > 75 and mouse_pos[1] < 375 and pygame.mouse.get_pressed()[0] == True:
        print(f"Lemon Clicked!!!! Score = {PLAYERSCORE + 1}")
        PLAYERSCORE += 1
        lemon_resized = pygame.transform.scale(lemon, (300, 200))
        window.blit(lemon_resized, (75, 135))
        return True
    else:
        lemon_resized = pygame.transform.scale(lemon, (400, 300))
        window.blit(lemon_resized, (25, 75))
        return False

def disp_fake_lemon(window):
    global lemon_img
    lemon_resized = pygame.transform.scale(lemon_img, (300, 200))
    window.blit(lemon_resized, (75, 135))

# window.blit(pygame.transform.scale(pygame.image.load("lemon.png"), (x_scale, y_scale)), (x_pos, y_pos))
fast_lemons = {"L0":[ra(), 0], "L1":[ra(), 0], "L2":[ra(), 0], "L3":[ra(), 0], "L4":[ra(), 0], "L5":[ra(), 0], "L6":[ra(), 0], "L7":[ra(), 0], "L8":[ra(), 0], "L9":[ra(), 0]}
medium_lemons = {"L0":[ra(), 0], "L1":[ra(), 0], "L2":[ra(), 0], "L3":[ra(), 0], "L4":[ra(), 0], "L5":[ra(), 0], "L6":[ra(), 0], "L7":[ra(), 0], "L8":[ra(), 0], "L9":[ra(), 0]}
slow_lemons = {"L0":[ra(), 0], "L1":[ra(), 0], "L2":[ra(), 0], "L3":[ra(), 0], "L4":[ra(), 0], "L5":[ra(), 0], "L6":[ra(), 0], "L7":[ra(), 0], "L8":[ra(), 0], "L9":[ra(), 0]}
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fast background lemons
    for lemon in fast_lemons:
        window.blit(pygame.transform.scale(lemon_img, (25, 20)), tuple(fast_lemons[lemon]))
        fast_lemons[lemon][1] += 10
        if fast_lemons[lemon][1] > 450:
            fast_lemons[lemon][1] = 0
    #medium background lemons
    for lemon in medium_lemons:
        window.blit(pygame.transform.scale(lemon_img, (25, 20)), tuple(medium_lemons[lemon]))
        medium_lemons[lemon][1] += 6
        if medium_lemons[lemon][1] > 450:
            medium_lemons[lemon][1] = 0
    #slow background lemons
    for lemon in slow_lemons:
        window.blit(pygame.transform.scale(lemon_img, (25, 20)), tuple(slow_lemons[lemon]))
        slow_lemons[lemon][1] += 3
        if slow_lemons[lemon][1] > 450:
            slow_lemons[lemon][1] = 0

        
    #Anti lemon click script    
    if not waiting:
        waiting = disp_lemon(window)
    if waiting:
        wait_time += 1
        disp_fake_lemon(window)
    if wait_time > 15:
        wait_time = 0
        waiting = False
    
    disp_text(window, f"Score: {PLAYERSCORE}")
    timer += 1
    pygame.display.update()
    clock.tick(30)
    window.fill((255, 255, 0))


with open("save_data.lemon", "w") as savedata:
    savedata.truncate(0)
    savedata.write(str(PLAYERSCORE))
    savedata.close()
pygame.quit()
quit(0)
