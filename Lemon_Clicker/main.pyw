import pygame
import os
import random
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((600, 450)) #Original resolution 450 x 450
pygame.display.set_caption("Lemon Clicker v0.36a") #Alpha 0.36
clock = pygame.time.Clock()
timer = 0
global_timer = 0
minute_timer = 60
wait_time = 0
waiting = False
autoclick_clicked = False
autoclick_timer = 0
extra_clicks = 0
click_power = 1
click_power_timer = 0

lemon_img = pygame.image.load("Assets/lemon.png").convert_alpha()
pygame.display.set_icon(pygame.transform.scale(lemon_img, (32, 32)))
AutoClick_img = pygame.image.load("Assets/Auto_Clicker_Button.png").convert_alpha()
Lemonade_img = pygame.image.load("Assets/Lemonade_Button.png").convert_alpha()
Double_img = pygame.image.load("Assets/Double_Button.png").convert_alpha()

def ra():
    return random.randint(0, 450)

#Gets player score
if not os.path.exists("Assets/save_data.lemon"):
    open("Assets/save_data.lemon", "w+").write("0 0")

try:
    save_file = open("Assets/save_data.lemon", "r").read()
    save_file = save_file.split(" ")
    PLAYERSCORE = int(save_file[0])
    extra_clicks = int(save_file[1])
except Exception as e:
    open("Assets/save_data.lemon", "w").truncate(0)
    open("Assets/save_data.lemon", "w").write("0 0")

def disp_text(window, x, y, text):
    font = pygame.font.SysFont("Comic Sans MS", 20)
    surface = font.render(text, False, (0, 0, 0))
    window.blit(surface, (x, y))

def disp_fake_button(window, texture):
    button = pygame.transform.scale(texture, (100, 100))
    window.blit(button, (475, 25))

def disp_autoclick(window):
    global PLAYERSCORE
    global AutoClick_img
    global extra_clicks
    button = AutoClick_img
    window.blit(button, (450, 0))
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > 450 and mouse_pos[0] < 600 and mouse_pos[1] > 0 and mouse_pos[1] < 150 and pygame.mouse.get_pressed()[0] == True:
        if PLAYERSCORE >= 100:
            PLAYERSCORE -= 100
            extra_clicks += 1
        return True
    return False

def disp_lemonade(window):
    global PLAYERSCORE
    global Lemonade_img
    global minute_timer
    global click_power
    if minute_timer <= 0:
        window.blit(Lemonade_img, (450, 150))
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > 450 and mouse_pos[0] < 600 and mouse_pos[1] > 150 and mouse_pos[1] < 300 and pygame.mouse.get_pressed()[0] == True:
            PLAYERSCORE += (200 * click_power)
            minute_timer = 60

def disp_double(window):
    global Double_img
    global minute_timer
    global click_power
    global click_power_timer
    if minute_timer <= 0:
        window.blit(Double_img, (450, 300))
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > 450 and mouse_pos[0] < 600 and mouse_pos[1] > 300 and mouse_pos[1] < 450 and pygame.mouse.get_pressed()[0] == True:
            click_power = 2
            click_power_timer = 20
            minute_timer = 60

def disp_lemon(window):
    global PLAYERSCORE
    global lemon_img
    global timer
    global click_power
    lemon = lemon_img
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > 25 and mouse_pos[0] < 425 and mouse_pos[1] > 75 and mouse_pos[1] < 375 and pygame.mouse.get_pressed()[0] == True:
        print(f"Lemon Clicked!!!! Score = {PLAYERSCORE + 1}")
        PLAYERSCORE += click_power
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
        #Debug Keys: Up arrow sets the minute timer to 1
        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_UP:
        #        minute_timer = 1

    ''' Falling Lemons Background '''
    #Fast background lemons
    for lemon in fast_lemons:
        window.blit(pygame.transform.scale(lemon_img, (25, 20)), tuple(fast_lemons[lemon]))
        fast_lemons[lemon][1] += 7
        if fast_lemons[lemon][1] > 450:
            fast_lemons[lemon][1] = 0
    #medium background lemons
    for lemon in medium_lemons:
        window.blit(pygame.transform.scale(lemon_img, (25, 20)), tuple(medium_lemons[lemon]))
        medium_lemons[lemon][1] += 5
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
    if wait_time >= 5:
        wait_time = 0
        waiting = False

    #minute timer script
    if global_timer % 30 == 0 and minute_timer > 0:
        minute_timer -= 1
    if minute_timer <= 0:
        pass

    #Auto Click Button Script
    if not autoclick_clicked:
        autoclick_clicked = disp_autoclick(window)
    if autoclick_clicked:
        disp_fake_button(window, AutoClick_img)
        autoclick_timer += 1
    if autoclick_timer >= 5:
        autoclick_clicked = False
        autoclick_timer = 0
    
    #Auto Click Script
    if global_timer % 30 == 0:
        PLAYERSCORE += (extra_clicks * click_power)

    #Double Click Timer Script
    if click_power_timer > 0:
        if global_timer % 30 == 0:
            click_power_timer -= 1
    elif click_power_timer <= 0:
        click_power = 1

    disp_text(window, 0, 0, f"Score: {PLAYERSCORE} | AutoClicks: {extra_clicks} | Timer: {minute_timer} {'| READY' if minute_timer <=0 else ''}")
    disp_text(window, 0, 22, 'Double Points Time Left: '+str(click_power_timer) if click_power_timer > 0 else '')
    disp_lemonade(window)
    disp_double(window)
    timer += 1
    global_timer += 1
    pygame.display.update()
    clock.tick(30)
    window.fill((255, 255, 0))


with open("Assets/save_data.lemon", "w") as savedata:
    savedata.truncate(0)
    savedata.write(f"{str(PLAYERSCORE)} {str(extra_clicks)}")
    savedata.close()
pygame.quit()
quit(0)
