import pygame
import os
import time
import random
import json
pygame.font.init()
pygame.mixer.init()
pygame.init()

screen_width = 1280
screen_height = 720
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FNAF PY")

#colours
WHITE = (255, 255, 255)

#fonts
Small_Font = pygame.font.SysFont('comicsans', 30)
Medium_Font = pygame.font.SysFont('comicsans', 35)
Big_Font = pygame.font.SysFont('comicsans', 40)

#loading images
office_bg_image = pygame.image.load(os.path.join('Images', 'office.png'))

mainmenu_image = pygame.image.load(os.path.join('Images', 'mainmenu.png'))

continue_image = pygame.image.load(os.path.join('Images', 'continue.png'))

newgame_image = pygame.image.load(os.path.join('Images', 'newgame.png'))

arrow_image = pygame.image.load(os.path.join('Images', 'arrow.png'))

night_6_image = pygame.image.load(os.path.join('Images', '6th_night.png'))
custom_night_image = pygame.image.load(os.path.join('Images', 'custom_night.png'))

camera_button_image = pygame.image.load(os.path.join('Images', 'camera_button.png'))
camera_button_image = pygame.transform.scale(camera_button_image, (500, 50))

green_bar_image = pygame.image.load(os.path.join('Images', 'usage_bar', 'green_bar.png'))
yellow_bar_image = pygame.image.load(os.path.join('Images', 'usage_bar', 'yellow_bar.png'))
red_bar_image = pygame.image.load(os.path.join('Images', 'usage_bar', 'red_bar.png'))

door_button_on_image = pygame.image.load(os.path.join('Images', 'door', 'door_button_on.png'))
door_button_on_image = pygame.transform.scale(door_button_on_image, (100, 100))

door_button_image = pygame.image.load(os.path.join('Images', 'door', 'door_button.png'))
door_button_image = pygame.transform.scale(door_button_image, (100, 100))

light_button_on_image = pygame.image.load(os.path.join('Images', 'light', 'light_button_on.png'))
light_button_on_image = pygame.transform.scale(light_button_on_image, (100, 100))

light_button_image = pygame.image.load(os.path.join('Images', 'light', 'light_button.png'))
light_button_image = pygame.transform.scale(light_button_image, (100, 100))

left_light_image = pygame.image.load(os.path.join('Images', 'light', 'left_light.png'))
right_light_image = pygame.image.load(os.path.join('Images', 'light', 'left_light.png'))

left_door_image = pygame.image.load(os.path.join('Images', 'door', 'door.png'))
right_door_image = pygame.image.load(os.path.join('Images', 'door', 'door.png'))

bon_image = pygame.image.load(os.path.join('Images', 'animatronics', 'bon.png'))
chic_image = pygame.image.load(os.path.join('Images', 'animatronics', 'chic.png'))
fox_image = pygame.image.load(os.path.join('Images', 'animatronics', 'fox.png'))
fred_image = pygame.image.load(os.path.join('Images', 'animatronics', 'fred.png'))
fred_power_out_image = pygame.image.load(os.path.join('Images', 'animatronics', 'power_out_fred.png'))

map_image = pygame.image.load(os.path.join('Images', 'map.png'))
a1_image = pygame.image.load(os.path.join('Images', 'map', '1a.png'))
a1_on_image = pygame.image.load(os.path.join('Images', 'map', '1a_on.png'))

b1_image = pygame.image.load(os.path.join('Images', 'map', '1b.png'))
b1_on_image = pygame.image.load(os.path.join('Images', 'map', '1b_on.png'))

c1_image = pygame.image.load(os.path.join('Images', 'map', '1c.png'))
c1_on_image = pygame.image.load(os.path.join('Images', 'map', '1c_on.png'))

a2_image = pygame.image.load(os.path.join('Images', 'map', '2a.png'))
a2_on_image = pygame.image.load(os.path.join('Images', 'map', '2a_on.png'))

b2_image = pygame.image.load(os.path.join('Images', 'map', '2b.png'))
b2_on_image = pygame.image.load(os.path.join('Images', 'map', '2b_on.png'))

a3_image = pygame.image.load(os.path.join('Images', 'map', '3.png'))
a3_on_image = pygame.image.load(os.path.join('Images', 'map', '3_on.png'))

a4_image = pygame.image.load(os.path.join('Images', 'map', '4a.png'))
a4_on_image = pygame.image.load(os.path.join('Images', 'map', '4a_on.png'))

b4_image = pygame.image.load(os.path.join('Images', 'map', '4b.png'))
b4_on_image = pygame.image.load(os.path.join('Images', 'map', '4b_on.png'))

a5_image = pygame.image.load(os.path.join('Images', 'map', '5.png'))
a5_on_image = pygame.image.load(os.path.join('Images', 'map', '5_on.png'))

a6_image = pygame.image.load(os.path.join('Images', 'map', '6.png'))
a6_on_image = pygame.image.load(os.path.join('Images', 'map', '6_on.png'))

a7_image = pygame.image.load(os.path.join('Images', 'map', '7.png'))
a7_on_image = pygame.image.load(os.path.join('Images', 'map', '7_on.png'))

pirate_cove_image = pygame.image.load(os.path.join('Images', 'camera_area', 'pirate_cove', 'pirate_cove.png'))
pirate_cove_stage2_image = pygame.image.load(os.path.join('Images', 'camera_area', 'pirate_cove', 'pirate_cove_stage2.png'))
pirate_cove_stage3_image = pygame.image.load(os.path.join('Images', 'camera_area', 'pirate_cove', 'pirate_cove_stage3.png'))
pirate_cove_stage4_image = pygame.image.load(os.path.join('Images', 'camera_area', 'pirate_cove', 'pirate_cove_stage4.png'))

w_hall_corner_image = pygame.image.load(os.path.join('Images', 'camera_area', 'w_hall_corner', 'w_hall_corner.png'))
w_hall_corner_stage2_image = pygame.image.load(os.path.join('Images', 'camera_area', 'w_hall_corner', 'w_hall_corner_stage2.png'))

show_stage_image = pygame.image.load(os.path.join('Images', 'camera_area', 'show_stage', 'show_stage.png'))
show_stage_stage2_image = pygame.image.load(os.path.join('Images', 'camera_area', 'show_stage', 'show_stage_stage2.png'))
show_stage_stage3_image = pygame.image.load(os.path.join('Images', 'camera_area', 'show_stage', 'show_stage_stage3.png'))
show_stage_stage4_image = pygame.image.load(os.path.join('Images', 'camera_area', 'show_stage', 'show_stage_stage4.png'))

w_hall_image = pygame.image.load(os.path.join('Images', 'camera_area', 'w_hall', 'w_hall.png'))
w_hall_stage2_image = pygame.image.load(os.path.join('Images', 'camera_area', 'w_hall', 'w_hall_stage2.png'))

supply_closet_image = pygame.image.load(os.path.join('Images', 'camera_area', 'supply_closet', 'supply_closet.png'))
supply_closet_stage2_image = pygame.image.load(os.path.join('Images', 'camera_area', 'supply_closet', 'supply_closet_stage2.png'))

restrooms_image = pygame.image.load(os.path.join('Images', 'camera_area', 'restrooms', 'restrooms.png'))
restrooms_stage2_image = pygame.image.load(os.path.join('Images', 'camera_area', 'restrooms', 'restrooms_stage2.png'))

kitchen_image = pygame.image.load(os.path.join('Images', 'camera_area', 'kitchen.png'))

e_hall_image = pygame.image.load(os.path.join('Images', 'camera_area', 'e_hall', 'e_hall.png'))
e_hall_stage2_image = pygame.image.load(os.path.join('Images', 'camera_area', 'e_hall', 'e_hall_stage2.png'))

e_hall_corner_image = pygame.image.load(os.path.join('Images', 'camera_area', 'e_hall_corner', 'e_hall_corner.png'))
e_hall_corner_stage2_image = pygame.image.load(os.path.join('Images', 'camera_area', 'e_hall_corner', 'e_hall_corner_stage2.png'))
e_hall_corner_stage3_image = pygame.image.load(os.path.join('Images', 'camera_area', 'e_hall_corner', 'e_hall_corner_stage3.png'))

dining_area_image = pygame.image.load(os.path.join('Images', 'camera_area', 'dining_area', 'dining_area.png'))
dining_area_stage2_image = pygame.image.load(os.path.join('Images', 'camera_area', 'dining_area', 'dining_area_stage2.png'))
dining_area_stage3_image = pygame.image.load(os.path.join('Images', 'camera_area', 'dining_area', 'dining_area_stage3.png'))

backstage_image = pygame.image.load(os.path.join('Images', 'camera_area', 'backstage', 'backstage.png'))
backstage_stage2_image = pygame.image.load(os.path.join('Images', 'camera_area', 'backstage', 'backstage_stage2.png'))

win_image = pygame.image.load(os.path.join('Images', 'win.png'))
game_over_image = pygame.image.load(os.path.join('Images', 'game_over.png'))

boop_image = pygame.image.load(os.path.join('Images', 'boop.png'))
mute_call_image = pygame.image.load(os.path.join('Images', 'mute_call.png'))

customize_night_image = pygame.image.load(os.path.join('Images', 'customize_night.png'))
ready_image = pygame.image.load(os.path.join('Images', 'ready.png'))
left_arrow_image = pygame.image.load(os.path.join('Images', 'left_arrow.png'))
right_arrow_image = pygame.image.load(os.path.join('Images', 'right_arrow.png'))

pygame.display.set_icon(fred_image)

#sounds
phoneguy_night1 = pygame.mixer.Sound(os.path.join('Music', 'phoneguy_night1.mp3'))
phoneguy_night2 = pygame.mixer.Sound(os.path.join('Music', 'phoneguy_night2.mp3'))
phoneguy_night3 = pygame.mixer.Sound(os.path.join('Music', 'phoneguy_night3.mp3'))
phoneguy_night4 = pygame.mixer.Sound(os.path.join('Music', 'phoneguy_night4.mp3'))
quiet_footsteps_sound = pygame.mixer.Sound(os.path.join('Music', 'quiet_footsteps.mp3'))
loud_footsteps_sound = pygame.mixer.Sound(os.path.join('Music', 'loud_footsteps.mp3'))
light_on_sound = pygame.mixer.Sound(os.path.join('Music', 'light_on.mp3'))
light_off_sound = pygame.mixer.Sound(os.path.join('Music', 'light_off.mp3'))
door_open_sound = pygame.mixer.Sound(os.path.join('Music', 'door_open.mp3'))
door_close_sound = pygame.mixer.Sound(os.path.join('Music', 'door_close.mp3'))
foxy_run_sound = pygame.mixer.Sound(os.path.join('Music', 'foxy_run.mp3'))
foxy_banging_sound = pygame.mixer.Sound(os.path.join('Music', 'foxy_banging.mp3'))
jump_sound = pygame.mixer.Sound(os.path.join('Music', 'jump.mp3'))
jumpscare_sound = pygame.mixer.Sound(os.path.join('Music', 'jumpscare.mp3'))
boop_sound = pygame.mixer.Sound(os.path.join('Music', 'boop.mp3'))
music_box = pygame.mixer.Sound(os.path.join('Music', 'music_box.mp3'))
camera_sound = pygame.mixer.Sound(os.path.join('Music', 'camera.mp3'))
change_camera_sound = pygame.mixer.Sound(os.path.join('Music', 'change_camera.mp3'))

sound_queue = [foxy_run_sound, foxy_banging_sound]

#data
data_night = {
    'night_number': 1,
    'night_6_unlocked': False,
    'custom_night_unlocked': False,
    'night_6_on': False,
    'custom_night_on': False,
    'continue_pressed': False,
    'bon_ai': 0,
    'chic_ai': 0,
    'fox_ai': 0,
    'fred_ai': 0
}

#loading data
try:
    with open(os.path.join('data','night.json')) as night:
        data_night = json.load(night)
except:
    print("")

#class
class button:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

# Define a function to play the next sound in the queue
def play_next_sound():
    if sound_queue:
        next_sound = sound_queue.pop(0)
        next_sound.play()
        # Set a timer to generate an event when the sound finishes
        pygame.time.set_timer(pygame.USEREVENT, int(next_sound.get_length() * 1000))

def custom_mode():
    with open(os.path.join('data','night.json')) as night:
        data_night = json.load(night)
    ready_button = button(1000, 630, 195, 65, ready_image)
    left_arrow_button = button(100, 500, 35, 55, left_arrow_image)
    right_arrow_button = button(270, 500, 35, 55, right_arrow_image)
    left_arrow_button2 = button(420, 500, 35, 55, left_arrow_image)
    right_arrow_button2 = button(585, 500, 35, 55, right_arrow_image)
    left_arrow_button3 = button(705, 500, 35, 55, left_arrow_image)
    right_arrow_button3 = button(870, 500, 35, 55, right_arrow_image)
    left_arrow_button4 = button(980, 500, 35, 55, left_arrow_image)
    right_arrow_button4 = button(1145, 500, 35, 55, right_arrow_image)
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'night.json'),'w') as night:
                    json.dump(data_night, night)
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                ready_button_rect = pygame.Rect(ready_button.x, ready_button.y, ready_button.width, ready_button.height)
                left_arrow_button_rect = pygame.Rect(left_arrow_button.x, left_arrow_button.y, left_arrow_button.width, left_arrow_button.height)
                right_arrow_button_rect = pygame.Rect(right_arrow_button.x, right_arrow_button.y, right_arrow_button.width, right_arrow_button.height)
                left_arrow_button2_rect = pygame.Rect(left_arrow_button2.x, left_arrow_button2.y, left_arrow_button2.width, left_arrow_button2.height)
                right_arrow_button2_rect = pygame.Rect(right_arrow_button2.x, right_arrow_button2.y, right_arrow_button2.width, right_arrow_button2.height)
                left_arrow_button3_rect = pygame.Rect(left_arrow_button3.x, left_arrow_button3.y, left_arrow_button3.width, left_arrow_button3.height)
                right_arrow_button3_rect = pygame.Rect(right_arrow_button3.x, right_arrow_button3.y, right_arrow_button3.width, right_arrow_button3.height)
                left_arrow_button4_rect = pygame.Rect(left_arrow_button4.x, left_arrow_button4.y, left_arrow_button4.width, left_arrow_button4.height)
                right_arrow_button4_rect = pygame.Rect(right_arrow_button4.x, right_arrow_button4.y, right_arrow_button4.width, right_arrow_button4.height)
                if ready_button_rect.collidepoint(mousex, mousey):
                    data_night['continue_pressed'] = False
                    with open(os.path.join('data', 'night.json'),'w') as night:
                        json.dump(data_night, night)      
                    mainspot()
                if left_arrow_button_rect.collidepoint(mousex, mousey):
                    if data_night['fred_ai'] > 0:
                        data_night['fred_ai'] -= 1
                if right_arrow_button_rect.collidepoint(mousex, mousey):
                    if data_night['fred_ai'] < 20:
                        data_night['fred_ai'] += 1

                if left_arrow_button2_rect.collidepoint(mousex, mousey):
                    if data_night['bon_ai'] > 0:
                        data_night['bon_ai'] -= 1
                if right_arrow_button2_rect.collidepoint(mousex, mousey):
                    if data_night['bon_ai'] < 20:
                        data_night['bon_ai'] += 1
                
                if left_arrow_button3_rect.collidepoint(mousex, mousey):
                    if data_night['chic_ai'] > 0:
                        data_night['chic_ai'] -= 1
                if right_arrow_button3_rect.collidepoint(mousex, mousey):
                    if data_night['chic_ai'] < 20:
                        data_night['chic_ai'] += 1
                
                if left_arrow_button4_rect.collidepoint(mousex, mousey):
                    if data_night['fox_ai'] > 0:
                        data_night['fox_ai'] -= 1
                if right_arrow_button4_rect.collidepoint(mousex, mousey):
                    if data_night['fox_ai'] < 20:
                        data_night['fox_ai'] += 1
        fred_ai_text = Big_Font.render(str(data_night['fred_ai']), 1, WHITE)
        bon_ai_text = Big_Font.render(str(data_night['bon_ai']), 1, WHITE)
        chic_ai_text = Big_Font.render(str(data_night['chic_ai']), 1, WHITE)
        fox_ai_text = Big_Font.render(str(data_night['fox_ai']), 1, WHITE)
        window.blit(customize_night_image, (0, 0))
        window.blit(ready_button.image, (ready_button.x, ready_button.y))
        window.blit(left_arrow_button.image, (left_arrow_button.x, left_arrow_button.y))
        window.blit(right_arrow_button.image, (right_arrow_button.x, right_arrow_button.y))
        window.blit(left_arrow_button2.image, (left_arrow_button2.x, left_arrow_button2.y))
        window.blit(right_arrow_button2.image, (right_arrow_button2.x, right_arrow_button2.y))
        window.blit(left_arrow_button3.image, (left_arrow_button3.x, left_arrow_button3.y))
        window.blit(right_arrow_button3.image, (right_arrow_button3.x, right_arrow_button3.y))
        window.blit(left_arrow_button4.image, (left_arrow_button4.x, left_arrow_button4.y))
        window.blit(right_arrow_button4.image, (right_arrow_button4.x, right_arrow_button4.y))
        window.blit(fred_ai_text, (220, 500))
        window.blit(bon_ai_text, (535, 500))
        window.blit(chic_ai_text, (820, 500))
        window.blit(fox_ai_text, (1095, 500))
        pygame.display.update()

def win6am():
    win_image = pygame.image.load(os.path.join('Images', 'win.png'))
    sec = 0
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'night.json'),'w') as night:
                    json.dump(data_night, night)
                run = False
                pygame.quit()

        #timer
        sec += 1
        if sec >= 600:
            mainspot()
        win_image = pygame.transform.scale(win_image, (1280, 720))
        window.blit(win_image, (0, 0))
        pygame.display.update()

def mainspot():
    sec = 0
    night_num_text = ""
    run = True
    clock = pygame.time.Clock()
    # Load the night data
    with open(os.path.join('data', 'night.json'), 'r') as night:
        data_night = json.load(night)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'night.json'),'w') as night:
                    json.dump(data_night, night)
                run = False
                pygame.quit()
        if data_night['custom_night_on'] == True and data_night['continue_pressed'] == False:
            night_num_text = "7th"
        elif data_night['night_6_on'] == True and data_night['continue_pressed'] == False:
            night_num_text = "6th"
        elif data_night['night_number'] == 5:
            night_num_text = "5th"
        elif data_night['night_number'] == 4:
            night_num_text = "4th"
        elif data_night['night_number'] == 3:
            night_num_text = "3rd"
        elif data_night['night_number'] == 2:
            night_num_text = "2nd"
        elif data_night['night_number'] == 1:
            night_num_text = "1st"
        
        #timer
        sec += 1
        if sec >= 130:
            if data_night['custom_night_on'] == True and data_night['continue_pressed'] == False:
                custom_night()
            elif data_night['night_6_on'] == True and data_night['continue_pressed'] == False:
                night6()
            elif data_night['night_number'] == 5:
                night5()
            elif data_night['night_number'] == 4:
                night4()
            elif data_night['night_number'] == 3:
                night3()
            elif data_night['night_number'] == 2:
                night2()
            elif data_night['night_number'] == 1:
                main()
        
        Night_text = Big_Font.render(night_num_text + " Night", 1, WHITE)
        AM_text = Big_Font.render("12:00 AM", 1, WHITE)
        window.fill((0, 0, 0))
        window.blit(Night_text, (535, 270))
        window.blit(AM_text, (540, 200))
        pygame.display.update()

def mainmenu():
    # Load the night data
    with open(os.path.join('data', 'night.json'), 'r') as night:
        data_night = json.load(night)
    continue_text = button(100, 470, 250, 50, continue_image)
    newgame = button(100, 400, 250, 50, newgame_image)
    night_6 = button(100, 570, 250, 50, night_6_image)
    custom_night = button(100, 640, 250, 50, custom_night_image)
    show_6th_night = False
    show_custom_night = False
    show_arrow_night6 = False
    show_arrow_custom_night = False
    show_arrow_continue = False
    show_arrow_newgame = True
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'night.json'),'w') as night:
                    json.dump(data_night, night)
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                night_6_rect = pygame.Rect(night_6.x, night_6.y, night_6.width, night_6.height)
                custom_night_rect = pygame.Rect(custom_night.x, custom_night.y, custom_night.width, custom_night.height)
                continue_text_rect = pygame.Rect(continue_text.x, continue_text.y, continue_text.width, continue_text.height)
                newgame_rect = pygame.Rect(newgame.x, newgame.y, newgame.width, newgame.height)
                if continue_text_rect.collidepoint(mousex, mousey):
                    camera_sound.play()
                    data_night['continue_pressed'] = True
                    with open(os.path.join('data', 'night.json'),'w') as night:
                        json.dump(data_night, night)
                    mainspot()
                if newgame_rect.collidepoint(mousex, mousey):
                    data_night['continue_pressed'] = False
                    camera_sound.play()
                    data_night['night_number'] = 1
                    data_night['custom_night_on'] = False
                    data_night['night_6_on'] = False
                    with open(os.path.join('data', 'night.json'),'w') as night:
                        json.dump(data_night, night)
                    mainspot()
                if show_6th_night == True:
                    if night_6_rect.collidepoint(mousex, mousey):
                        data_night['continue_pressed'] = False
                        data_night['custom_night_on'] = False
                        data_night['night_6_on'] = True
                        with open(os.path.join('data', 'night.json'),'w') as night:
                            json.dump(data_night, night)
                        camera_sound.play()
                        mainspot()
                if show_custom_night == True:
                    if custom_night_rect.collidepoint(mousex, mousey):
                        data_night['continue_pressed'] = False
                        data_night['night_6_on'] = False
                        data_night['custom_night_on'] = True
                        with open(os.path.join('data', 'night.json'),'w') as night:
                            json.dump(data_night, night)
                        camera_sound.play()
                        custom_mode()
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
                night_6_rect = pygame.Rect(night_6.x, night_6.y, night_6.width, night_6.height)
                custom_night_rect = pygame.Rect(custom_night.x, custom_night.y, custom_night.width, custom_night.height)
                continue_text_rect = pygame.Rect(continue_text.x, continue_text.y, continue_text.width, continue_text.height)
                newgame_rect = pygame.Rect(newgame.x, newgame.y, newgame.width, newgame.height)
                if continue_text_rect.collidepoint(mousex, mousey):
                    change_camera_sound.stop()
                    change_camera_sound.play()
                    show_arrow_custom_night = False
                    show_arrow_night6 = False
                    show_arrow_newgame = False
                    show_arrow_continue = True
                if newgame_rect.collidepoint(mousex, mousey):
                    change_camera_sound.stop()
                    change_camera_sound.play()
                    show_arrow_continue = False
                    show_arrow_custom_night = False
                    show_arrow_night6 = False
                    show_arrow_newgame = True
                if show_6th_night == True:
                    if night_6_rect.collidepoint(mousex, mousey):
                        change_camera_sound.stop()
                        change_camera_sound.play()
                        show_arrow_continue = False
                        show_arrow_custom_night = False
                        show_arrow_newgame = False
                        show_arrow_night6 = True
                if show_custom_night == True:
                    if custom_night_rect.collidepoint(mousex, mousey):
                        change_camera_sound.stop()
                        change_camera_sound.play()
                        show_arrow_continue = False
                        show_arrow_newgame = False
                        show_arrow_night6 = False
                        show_arrow_custom_night = True

        if data_night['night_6_unlocked'] == True:
            show_6th_night = True
        if data_night['custom_night_unlocked'] == True:
            show_custom_night = True
        
        Night_text = Small_Font.render("Night " + str(int(data_night['night_number'])), 1, WHITE)
        window.blit(mainmenu_image, (0, 0))
        if show_arrow_newgame == True:
            window.blit(arrow_image, (0, 400))
        if show_arrow_continue == True:
            window.blit(arrow_image, (0, 470))
            window.blit(Night_text, (100, 520))
        if show_arrow_night6 == True:
            window.blit(arrow_image, (0, 570))
        if show_arrow_custom_night == True:
            window.blit(arrow_image, (0, 640))

        if show_6th_night == True:
            window.blit(night_6.image, (night_6.x, night_6.y))
        if show_custom_night == True:
            window.blit(custom_night.image, (custom_night.x, custom_night.y))
        window.blit(continue_text.image, (continue_text.x, continue_text.y))
        window.blit(newgame.image, (newgame.x, newgame.y))
        
        pygame.display.update()

def main():
    data_night['night_number'] = 1
    with open(os.path.join('data', 'night.json'),'w') as night:
        json.dump(data_night, night)
    phoneguy_night1.play()
    sec = 0
    sec_power = 0
    sec_chic = 0
    sec_fox = 0
    sec_fred = 0
    sec_call = 0
    camera_area_text1 = "W. Hall Corner"

    fred_image = pygame.image.load(os.path.join('Images', 'animatronics', 'fred.png'))

    pirate_cove_image2 = pirate_cove_image
    show_stage_image2 = show_stage_image
    w_hall_corner_image2 = w_hall_corner_image
    w_hall_image2 = w_hall_image
    supply_closet_image2 = supply_closet_image
    restrooms_image2 = restrooms_image
    e_hall_corner_image2 = e_hall_corner_image
    e_hall_image2 = e_hall_image
    dining_area_image2 = dining_area_image
    backstage_image2 = backstage_image

    bon_ai_number = 0
    fox_ai_number = 0
    chic_ai_number = 0

    move_delay = 250  # milliseconds
    move_delay_camera = 450  # milliseconds
    last_move_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    light_button = button(1850, 400, 100, 100, light_button_image)
    light_button2 = button(-250, 400, 100, 100, light_button_image)
    light_button_on = button(8150, 400, 100, 100, light_button_on_image)
    light_button_on2 = button(8150, 400, 100, 100, light_button_on_image)
    door_button = button(1850, 250, 100, 100, door_button_image)
    door_button2 = button(-250, 250, 100, 100, door_button_image)
    door_button_on = button(8150, 250, 100, 100, door_button_on_image)
    door_button_on2 = button(8150, 250, 100, 100, door_button_on_image)
    left_light = button(-100, 30, 200, 700, left_light_image)
    right_light = button(1600, 30, 200, 700, right_light_image)
    left_door = button(-100, 30, 200, 700, left_door_image)
    right_door = button(1600, 30, 200, 700, right_door_image)
    bon = button(-100, 30, 500, 700, bon_image)
    chic = button(1300, 10, 200, 550, chic_image)
    camera_button = button(300, 650, 500, 50, camera_button_image)
    camera_button2 = button(21500, 650, 500, 50, camera_button_image)
    a2_button = button(870, 550, 95, 65, a2_image)
    a2_on_button = button(11870, 550, 95, 65, a2_on_image)
    b2_button = button(870, 615, 95, 65, b2_image)
    b2_on_button = button(11870, 615, 95, 65, b2_on_image)
    a4_button = button(1030, 550, 95, 65, a4_image)
    a4_on_button = button(111030, 550, 95, 65, a4_on_image)
    b4_button = button(1030, 615, 95, 65, b4_image)
    b4_on_button = button(111030, 615, 95, 65, b4_on_image)
    a3_button = button(740, 500, 95, 65, a3_image)
    a3_on_button = button(11740, 500, 95, 65, a3_on_image)
    a5_button = button(730, 330, 95, 65, a5_image)
    a5_on_button = button(11730, 330, 95, 65, a5_on_image)
    a6_button = button(1130, 500, 95, 65, a6_image)
    a6_on_button = button(111130, 500, 95, 65, a6_on_image)
    a7_button = button(1140, 300, 95, 65, a7_image)
    a7_on_button = button(111140, 300, 95, 65, a7_on_image)
    a1_button = button(900, 200, 95, 65, a1_image)
    a1_on_button = button(11900, 200, 95, 65, a1_on_image)
    b1_button = button(890, 300, 95, 65, b1_image)
    b1_on_button = button(11890, 300, 95, 65, b1_on_image)
    c1_button = button(850, 400, 95, 65, c1_image)
    c1_on_button = button(11850, 400, 95, 65, c1_on_image)
    camera_area = button(-300, 0, 2250, 720, pirate_cove_image)
    boop_button = button(650, 150, 10, 10, boop_image)
    mute_call_button = button(0, 0, 300, 60, mute_call_image)
    
    officex = -300
    camerax = -300
    last_event_time = time.time()
    event_interval = 5  # Time interval in seconds

    flicker_interval = 500  # milliseconds
    last_flicker_time = pygame.time.get_ticks()
    show_power_out_fred = True

    update_pirate_cove = True
    update_backstage = True
    update_dining_area = True
    update_e_hall = True
    update_e_hall_corner = True
    update_restrooms = True
    update_show_stage = True
    update_supply_closet = True
    update_w_hall = True
    update_w_hall_corner = True

    stop_left = True
    stop_right = True
    show_left_light = False
    show_right_light = False
    show_left_door = False
    show_right_door = False
    show_bon = False
    show_chic = False
    show_camera = False
    jumpscare_end = False
    jumpscare_end_chic = False
    jumpscare_end_fox = False
    jumpscare_end_fred = False
    power_out = False
    power_out_fred_active = False
    cama2_active = False
    camb2_active = True
    cama4_active = False
    camb4_active = False
    cama3_active = False
    cama5_active = False
    cama6_active = False
    cama7_active = False
    cama1_active = False
    camb1_active = False
    camc1_active = False
    show_green_cama2_flicker = False
    show_green_camb2_flicker = False
    show_green_cama4_flicker = False
    show_green_camb4_flicker = False
    show_green_cama3_flicker = False
    show_green_cama5_flicker = False
    show_green_cama6_flicker = False
    show_green_cama7_flicker = False
    show_green_cama1_flicker = False
    show_green_camb1_flicker = False
    show_green_camc1_flicker = False
    mute_call = False


    night_number = 1
    am_number = 12
    power_number = 100
    sec_number = 0
    sec_number2 = 0
    sec_number3 = 0
    sec_number4 = 0
    sec_fox_move = 0

    pirate_cove_stage_number = 1
    bonnie_stage_number = 1
    chica_stage_number = 1
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'night.json'),'w') as night:
                    json.dump(data_night, night)
                run = False
                pygame.quit()
            current_time = pygame.time.get_ticks()

            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
                camera_button_rect = pygame.Rect(camera_button.x, camera_button.y, camera_button.width, camera_button.height)
                camera_button2_rect = pygame.Rect(camera_button2.x, camera_button2.y, camera_button2.width, camera_button2.height)
                if mousex < 400:
                    stop_left = False
                elif mousex > 900:
                    stop_right = False
                else:
                    stop_left = True
                    stop_right = True
                if power_out == False:
                    if camera_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 21500
                        camera_button2.x = 300
                        show_camera = True
                        last_move_time = current_time
                    if camera_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 300
                        camera_button2.x = 21500
                        show_camera = False
                        last_move_time = current_time
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                mute_call_button_rect = pygame.Rect(mute_call_button.x, mute_call_button.y, mute_call_button.width, mute_call_button.height)
                light_button_rect = pygame.Rect(light_button.x, light_button.y, light_button.width, light_button.height)
                light_button2_rect = pygame.Rect(light_button2.x, light_button2.y, light_button2.width, light_button2.height)
                light_button_on_rect = pygame.Rect(light_button_on.x, light_button_on.y, light_button_on.width, light_button_on.height)
                light_button_on2_rect = pygame.Rect(light_button_on2.x, light_button_on2.y, light_button_on2.width, light_button_on2.height)
                door_button_rect = pygame.Rect(door_button.x, door_button.y, door_button.width, door_button.height)
                door_button2_rect = pygame.Rect(door_button2.x, door_button2.y, door_button2.width, door_button2.height)
                door_button_on_rect = pygame.Rect(door_button_on.x, door_button_on.y, door_button_on.width, door_button_on.height)
                door_button_on2_rect = pygame.Rect(door_button_on2.x, door_button_on2.y, door_button_on2.width, door_button_on2.height)

                boop_button_rect = pygame.Rect(boop_button.x, boop_button.y, boop_button.width, boop_button.height)

                a2_button_rect = pygame.Rect(a2_button.x, a2_button.y, a2_button.width, a2_button.height)
                b2_button_rect = pygame.Rect(b2_button.x, b2_button.y, b2_button.width, b2_button.height)
                a4_button_rect = pygame.Rect(a4_button.x, a4_button.y, a4_button.width, a4_button.height)
                b4_button_rect = pygame.Rect(b4_button.x, b4_button.y, b4_button.width, b4_button.height)
                a3_button_rect = pygame.Rect(a3_button.x, a3_button.y, a3_button.width, a3_button.height)
                a5_button_rect = pygame.Rect(a5_button.x, a5_button.y, a5_button.width, a5_button.height)
                a6_button_rect = pygame.Rect(a6_button.x, a6_button.y, a6_button.width, a6_button.height)
                a7_button_rect = pygame.Rect(a7_button.x, a7_button.y, a7_button.width, a7_button.height)
                a1_button_rect = pygame.Rect(a1_button.x, a1_button.y, a1_button.width, a1_button.height)
                b1_button_rect = pygame.Rect(b1_button.x, b1_button.y, b1_button.width, b1_button.height)  
                c1_button_rect = pygame.Rect(c1_button.x, c1_button.y, c1_button.width, c1_button.height)
                

                if show_camera == False and power_out == False:

                    if mute_call_button_rect.collidepoint(mousex, mousey):
                        mute_call = True
                        mute_call_button.x = -1000000

                    if door_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_right_door = True
                        door_button_on.x = 1180
                        door_button.x = 8150
                        last_move_time = current_time
                    if door_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_left_door = True
                        door_button_on2.x = 50
                        door_button2.x = 8150
                        last_move_time = current_time
                    if door_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_right_door = False
                        door_button_on.x = 8150
                        door_button.x = 1180
                        last_move_time = current_time
                    if door_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_left_door = False
                        door_button_on2.x = 8150
                        door_button2.x = 50
                        last_move_time = current_time

                    if light_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_right_light = True
                        light_button_on.x = 1180
                        light_button.x = 8150
                        last_move_time = current_time
                    if light_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_left_light = True
                        light_button_on2.x = 50
                        light_button2.x = 8150
                        last_move_time = current_time
                    if light_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_right_light = False
                        light_button_on.x = 8150
                        light_button.x = 1180
                        last_move_time = current_time
                    if light_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_left_light = False
                        light_button_on2.x = 8150
                        light_button2.x = 50
                        last_move_time = current_time
                if show_camera == False:
                    if boop_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        boop_sound.play()
                        last_move_time = current_time

                if show_camera == True:
                    if a2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama2_active = True
                        camb2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "West Hall"
                        update_w_hall = True
                        update_pirate_cove = False
                        update_w_hall_corner = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_image2
                        last_move_time = current_time
                    if b2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb2_active = True
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "W. Hall Corner"
                        update_w_hall_corner = True
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_corner_image2
                        last_move_time = current_time
                    if a4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama4_active = True
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_e_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "East Hall"
                        update_e_hall = True
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_image2
                        last_move_time = current_time
                    if b4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb4_active = True
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_e_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "E. Hall Corner"
                        update_e_hall_corner = True
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_corner_image2
                        last_move_time = current_time
                    if a3_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama3_active = True
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_supply_closet == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Supply Closet"
                        update_supply_closet = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        camera_area.image = supply_closet_image2
                        last_move_time = current_time
                    if a5_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama5_active = True
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_backstage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Backstage"
                        update_backstage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = backstage_image2
                        last_move_time = current_time
                    if a6_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        if cama6_active == False:
                            change_camera_sound.play()
                        cama6_active = True
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        camera_area_text1 = "Kitchen"
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = kitchen_image
                        last_move_time = current_time
                    if a7_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama7_active = True
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_restrooms == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Restrooms"
                        update_restrooms = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = restrooms_image2
                        last_move_time = current_time
                    if a1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama1_active = True
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_show_stage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Show Stage"
                        update_show_stage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_supply_closet = False
                        camera_area.image = show_stage_image2
                        last_move_time = current_time
                    if b1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb1_active = True
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camc1_active = False
                        if update_dining_area == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Dining Area"
                        update_dining_area = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = dining_area_image2
                        last_move_time = current_time
                    if c1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camc1_active = True
                        camb1_active = False
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        if update_pirate_cove == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Pirates Cove"
                        update_pirate_cove = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = pirate_cove_image2
                        
                        last_move_time = current_time
        if power_out == True:
            sec_power += 1
        if sec_power == 420:
            music_box.play()
            power_out_fred_active = True
        if sec_power == 1320:
            power_out_fred_active = False
        if sec_power == 1500:
            jumpscare_sound.play() 
            jumpscare_end_fred = True
            stop_left = True
            stop_right = True
            show_camera = False

        sec_call += 1
        sec_fox_move += 1
        current_time3 = pygame.time.get_ticks()
        # Check if it's time to flicker
        if current_time3 - last_flicker_time >= flicker_interval and power_out_fred_active == True:
            show_power_out_fred = not show_power_out_fred  # Toggle visibility
            last_flicker_time = current_time3
        
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama2_active == True:
            show_green_cama2_flicker = not show_green_cama2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb2_active == True:
            show_green_camb2_flicker = not show_green_camb2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama4_active == True:
            show_green_cama4_flicker = not show_green_cama4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb4_active == True:
            show_green_camb4_flicker = not show_green_camb4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama3_active == True:
            show_green_cama3_flicker = not show_green_cama3_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama5_active == True:
            show_green_cama5_flicker = not show_green_cama5_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama6_active == True:
            show_green_cama6_flicker = not show_green_cama6_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama7_active == True:
            show_green_cama7_flicker = not show_green_cama7_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama1_active == True:
            show_green_cama1_flicker = not show_green_cama1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb1_active == True:
            show_green_camb1_flicker = not show_green_camb1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camc1_active == True:
            show_green_camc1_flicker = not show_green_camc1_flicker  # Toggle visibility
            last_flicker_time = current_time3

        current_time2 = time.time()
        if current_time2 - last_event_time >= event_interval and power_out == False:
            sec_number3 += 1   
            rng = random.randint(1, 20)
            print(rng)
                    
            #foxy
            if show_camera == False and sec_fox_move >= random.randint(50, 1000):
                sec_fox_move = 0
                if fox_ai_number >= rng:
                    pirate_cove_stage_number += 1
                    print("fox stage increased!")
                    if pirate_cove_stage_number == 1:
                        pirate_cove_image2 = pirate_cove_image
                        
                    if pirate_cove_image2 == pirate_cove_image and pirate_cove_stage_number == 2:
                        pirate_cove_image2 = pirate_cove_stage2_image    

                    if pirate_cove_image2 == pirate_cove_stage2_image and pirate_cove_stage_number == 3:
                        pirate_cove_image2 = pirate_cove_stage3_image
                        
                    if pirate_cove_image2 == pirate_cove_stage3_image and pirate_cove_stage_number == 4:
                        sec_number3 = 0
                        pirate_cove_image2 = pirate_cove_stage4_image
                    
            
            
            if fox_ai_number >= rng:   
                if sec_number3 == 5 and show_left_door == True or camera_area.image == w_hall_image2 and show_left_door == True:
                    play_next_sound()
                    power_number -= 1
                    pirate_cove_image2 = pirate_cove_image
                    sec_number3 = 0
                    pirate_cove_stage_number = 1
                if sec_number3 == 5 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image or camera_area.image == w_hall_image2 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image:
                    jumpscare_end_fox = True
                    jumpscare_sound.play()
                    stop_left = True
                    stop_right = True
                    show_camera = False
                
            #bonnie
            if bon_ai_number >= rng:
                bonnie_stage_number += 1
                print("bonnie stage increased!")
                if bonnie_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if bonnie_stage_number == 2:
                    show_stage_image2 = show_stage_stage2_image
                    dining_area_image2 = dining_area_stage2_image
                if bonnie_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    backstage_image2 = backstage_stage2_image
                if bonnie_stage_number == 4:
                    backstage_image2 = backstage_image
                    w_hall_image2 = w_hall_stage2_image
                if bonnie_stage_number == 5:
                    w_hall_image2 = w_hall_image
                    supply_closet_image2 = supply_closet_stage2_image
                if bonnie_stage_number == 6:
                    loud_footsteps_sound.play()
                    supply_closet_image2 = supply_closet_image
                    w_hall_corner_image2 = w_hall_corner_stage2_image
                if bonnie_stage_number >= 7:
                    w_hall_corner_image2 = w_hall_corner_image
                    show_bon = True

            if bon_ai_number >= rng and show_left_door == True and show_bon == True:
                show_bon = False
                quiet_footsteps_sound.play()
                bonnie_stage_number = 2
                sec_number2 = 0
            if bon_ai_number < rng:
                print("bonnie failed to move")
            if show_bon == True and show_left_light == True and show_camera == False:
                jump_sound.play()
            if show_bon == True and show_left_door == False:
                sec_number2 += 1
            if sec_number2 >= 2 and show_left_door == False and bon_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end = True
                show_bon = True
                show_left_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                bon.image = pygame.transform.scale(bon.image, (5000, 1000))
                
            #chica
            if chic_ai_number >= rng:
                chica_stage_number += 1
                print("Chica Stage Increased!!!")
                if chica_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if chica_stage_number == 2:
                    show_stage_image2 = show_stage_stage3_image
                    dining_area_image2 = dining_area_stage3_image
                if chica_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    restrooms_image2 = restrooms_stage2_image
                if chica_stage_number == 4:
                    restrooms_image2 = restrooms_image
                if chica_stage_number == 5:
                    e_hall_image2 = e_hall_stage2_image
                if chica_stage_number == 6:
                    loud_footsteps_sound.play()
                    e_hall_image2 = e_hall_image
                    e_hall_corner_image2 = e_hall_corner_stage2_image
                if chica_stage_number == 7:
                    e_hall_corner_image2 = e_hall_corner_image
                    show_chic = True

            if chic_ai_number >= rng and show_right_door == True and show_chic == True:
                show_chic = False
                quiet_footsteps_sound.play()
                chica_stage_number = 2
                sec_number4 = 0
            if chic_ai_number < rng:
                print("chica failed to move")
            if show_chic == True and show_right_light == True and show_camera == False:
                jump_sound.play()
            if show_chic == True and show_right_door == False:
                sec_number4 += 1
            if sec_number4 >= 2 and show_right_door == False and chic_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end_chic = True
                show_chic = True
                show_right_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                chic.image = pygame.transform.scale(chic.image, (2500, 1000))
                chic.x = bon.x

            last_event_time = current_time2

        if jumpscare_end == True:
            sec += 1
            phoneguy_night1.stop()
            show_bon = True
            show_left_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec >= 70:
            mainmenu()
        
        if jumpscare_end_chic == True:
            sec_chic += 1
            phoneguy_night1.stop()
            show_chic = True
            show_right_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_chic >= 70:
            mainmenu()
        
        if jumpscare_end_fox == True:
            sec_fox += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fox >= 140:
            mainmenu()
        
        if jumpscare_end_fred == True:
            sec_fred += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fred >= 70:
            mainmenu()

        if mute_call == True:
            phoneguy_night1.set_volume(0.00)

        if sec_call >= 1380:
            mute_call_button.x = -100000

        if show_camera == True and update_pirate_cove == True:
            camera_area.image = pirate_cove_image2

        if show_camera == True and update_backstage == True:
            camera_area.image = backstage_image2

        if show_camera == True and update_dining_area == True:
            camera_area.image = dining_area_image2

        if show_camera == True and update_e_hall == True:
            camera_area.image = e_hall_image2

        if show_camera == True and update_e_hall_corner == True:
            camera_area.image = e_hall_corner_image2

        if show_camera == True and update_restrooms == True:
            camera_area.image = restrooms_image2

        if show_camera == True and update_show_stage == True:
            camera_area.image = show_stage_image2

        if show_camera == True and update_supply_closet == True:
            camera_area.image = supply_closet_image2
        
        if show_camera == True and update_w_hall == True:
            camera_area.image = w_hall_image2
        
        if show_camera == True and update_w_hall_corner == True:
            camera_area.image = w_hall_corner_image2
            
        if stop_left == False and camerax < -100:
            camerax += 10
            
        if stop_right == False and camerax > -500:
            camerax -= 10

        if stop_left == False and officex < -5:
            officex += 10
            boop_button.x += 10
            left_light.x += 10
            right_light.x += 10
            left_door.x += 10
            right_door.x += 10
            bon.x += 10
            chic.x += 10
            light_button.x += 10
            light_button2.x += 10
            light_button_on.x += 10
            light_button_on2.x += 10
            door_button.x += 10
            door_button2.x += 10
            door_button_on.x += 10
            door_button_on2.x += 10
        if stop_right == False and officex > -970:
            officex -= 10
            boop_button.x -= 10
            left_light.x -= 10
            right_light.x -= 10
            left_door.x -= 10
            right_door.x -= 10
            bon.x -= 10
            chic.x -= 10
            light_button.x -= 10
            light_button2.x -= 10
            light_button_on.x -= 10
            light_button_on2.x -= 10
            door_button.x -= 10
            door_button2.x -= 10
            door_button_on.x -= 10
            door_button_on2.x -= 10
        
        sec_number+=1
        if sec_number == 5400:
            am_number = 1
        if sec_number == 10800:
            bon_ai_number += 1
            am_number = 2
        if sec_number == 16200:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 3
        if sec_number == 21600:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 4
        if sec_number == 27000:
            am_number = 5
        if sec_number == 32400:
            power_out = False
            data_night['night_number'] = 2
            with open(os.path.join('data', 'night.json'),'w') as night:
                json.dump(data_night, night)
            win6am()

        if power_number <= 0:
            power_out = True

        if power_out == False:
            Usage_text = Small_Font.render("Usage:", 1, WHITE)
            Power_left_text = Small_Font.render("Power left:", 1, WHITE)
            Night_text = Small_Font.render("Night " + str(int(night_number)), 1, WHITE)
            AM_text = Big_Font.render(str(int(am_number)) + " AM", 1, WHITE)
            Power_number_text = Big_Font.render(str(int(power_number)) + "%", 1, WHITE)
        Light_text = Small_Font.render("LIGHT", 1, WHITE)
        Door_text = Small_Font.render("DOOR", 1, WHITE)
        if power_out == False:
            camera_area_text = Big_Font.render(camera_area_text1, 1, WHITE)
        window.fill((0, 0, 0))
        if power_out == False:
            if show_right_light == True and show_chic == True and show_camera == False:
                window.blit(chic.image, (chic.x, chic.y))
        window.blit(office_bg_image, (officex, 0))
        window.blit(boop_button.image, (boop_button.x, boop_button.y))
        window.blit(mute_call_button.image, (mute_call_button.x, mute_call_button.y))
        if power_out == False:
            window.blit(camera_button.image, (camera_button.x, camera_button.y))
        if power_out == False:
            if jumpscare_end_chic == True:
                window.blit(chic.image, (chic.x, chic.y))
            if jumpscare_end_fox == True:
                window.blit(fox_image, (bon.x + 100, chic.y))
            if show_camera == True:
                power_number -= 0.0008
                window.blit(camera_area.image, (camerax, camera_area.y))
                window.blit(camera_area_text, (735, 130))
                window.blit(green_bar_image, (125, 670))
                window.blit(map_image, (750, 200))
                if show_green_cama1_flicker == False:
                    a1_button.x = 900
                    a1_on_button.x = 11900
                if show_green_cama2_flicker == False:
                    a2_button.x = 870
                    a2_on_button.x = 11870
                if show_green_camb2_flicker == False:
                    b2_button.x = 870
                    b2_on_button.x = 11870
                if show_green_camc1_flicker == False:
                    c1_button.x = 850
                    c1_on_button.x = 11850
                if show_green_camb1_flicker == False:
                    b1_button.x = 890
                    b1_on_button.x = 11890
                if show_green_cama7_flicker == False:
                    a7_button.x = 1140
                    a7_on_button.x = 111140
                if show_green_cama6_flicker == False:
                    a6_button.x = 1130
                    a6_on_button.x = 111130
                if show_green_cama5_flicker == False:
                    a5_button.x = 730
                    a5_on_button.x = 11730
                if show_green_cama3_flicker == False:
                    a3_button.x = 740
                    a3_on_button.x = 11740
                if show_green_camb4_flicker == False:
                    b4_button.x = 1030
                    b4_on_button.x = 111030
                if show_green_cama4_flicker == False:
                    a4_button.x = 1030
                    a4_on_button.x = 111030
                if show_green_cama2_flicker == True:
                    a2_button.x = 11870
                    a2_on_button.x = 870
                if cama2_active == False:
                    a2_button.x = 870
                if show_green_camb2_flicker == True:
                    b2_button.x = 11870
                    b2_on_button.x = 870
                if camb2_active == False:
                    b2_button.x = 870
                if show_green_camc1_flicker == True:
                    c1_button.x = 11850
                    c1_on_button.x = 850
                if camc1_active == False:
                    c1_button.x = 850
                if show_green_camb1_flicker == True:
                    b1_button.x = 11890
                    b1_on_button.x = 890
                if camb1_active == False:
                    b1_button.x = 890
                if show_green_cama1_flicker == True:
                    a1_button.x = 11900
                    a1_on_button.x = 900
                if cama1_active == False:
                    a1_button.x = 900
                if show_green_cama7_flicker == True:
                    a7_button.x = 111140
                    a7_on_button.x = 1140
                if cama7_active == False:
                    a7_button.x = 1140
                if show_green_cama6_flicker == True:
                    a6_button.x = 111130
                    a6_on_button.x = 1130
                if cama6_active == False:
                    a6_button.x = 1130
                if show_green_cama5_flicker == True:
                    a5_button.x = 11730
                    a5_on_button.x = 730
                if cama5_active == False:
                    a5_button.x = 730
                if show_green_cama3_flicker == True:
                    a3_button.x = 11740
                    a3_on_button.x = 740
                if cama3_active == False:
                    a3_button.x = 740
                if show_green_camb4_flicker == True:
                    b4_button.x = 111030
                    b4_on_button.x = 1030
                if camb4_active == False:
                    b4_button.x = 1030
                if show_green_cama4_flicker == True:
                    a4_button.x = 111030
                    a4_on_button.x = 1030
                if cama4_active == False:
                    a4_button.x = 1030
                window.blit(a2_on_button.image, (a2_on_button.x, a2_on_button.y))
                window.blit(b2_on_button.image, (b2_on_button.x, b2_on_button.y))
                window.blit(a4_on_button.image, (a4_on_button.x, a4_on_button.y))
                window.blit(b4_on_button.image, (b4_on_button.x, b4_on_button.y))
                window.blit(a3_on_button.image, (a3_on_button.x, a3_on_button.y))
                window.blit(a5_on_button.image, (a5_on_button.x, a5_on_button.y))
                window.blit(a6_on_button.image, (a6_on_button.x, a6_on_button.y))
                window.blit(a7_on_button.image, (a7_on_button.x, a7_on_button.y))
                window.blit(a1_on_button.image, (a1_on_button.x, a1_on_button.y))
                window.blit(b1_on_button.image, (b1_on_button.x, b1_on_button.y))
                window.blit(c1_on_button.image, (c1_on_button.x, c1_on_button.y))
                
                window.blit(a2_button.image, (a2_button.x, a2_button.y))           
                window.blit(b2_button.image, (b2_button.x, b2_button.y))             
                window.blit(a4_button.image, (a4_button.x, a4_button.y))              
                window.blit(b4_button.image, (b4_button.x, b4_button.y))              
                window.blit(a3_button.image, (a3_button.x, a3_button.y))  
                window.blit(a5_button.image, (a5_button.x, a5_button.y))               
                window.blit(a6_button.image, (a6_button.x, a6_button.y))    
                window.blit(a7_button.image, (a7_button.x, a7_button.y))             
                window.blit(a1_button.image, (a1_button.x, a1_button.y))             
                window.blit(b1_button.image, (b1_button.x, b1_button.y)) 
                window.blit(c1_button.image, (c1_button.x, c1_button.y))
                window.blit(camera_button2.image, (camera_button2.x, camera_button2.y))
            if show_left_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_left_light == True and show_camera == False:
                window.blit(left_light.image, (left_light.x, left_light.y))
            if show_left_light == True and show_bon == True and show_camera == False:
                window.blit(bon.image, (bon.x, bon.y))
            if show_right_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_right_light == True and show_camera == False:
                window.blit(right_light.image, (right_light.x, right_light.y))
            if show_left_door == True:
                power_number -= 0.002
                window.blit(yellow_bar_image, (150, 670))
            if show_left_door == True and show_camera == False:
                window.blit(left_door.image, (left_door.x, left_door.y))
            if show_right_door == True:
                power_number -= 0.002
                window.blit(red_bar_image, (175, 670))
            if show_right_door == True and show_camera == False:
                window.blit(right_door.image, (right_door.x, right_door.y))
            if show_right_door == False and show_left_door == False and show_right_light == False and show_left_light == False and show_camera == False:
                power_number -= 0
            window.blit(green_bar_image, (100, 670))
            power_number -= 0.0008
        if power_out == True and show_power_out_fred == True and power_out_fred_active == True:
            window.blit(fred_power_out_image, (bon.x, bon.y))

        if jumpscare_end_fred == True:
            fred_image = pygame.transform.scale(fred_image, (2500, 1000))
            window.blit(fred_image, (bon.x, chic.y))

        if show_camera == False:
            window.blit(door_button2.image, (door_button2.x, door_button2.y))
            window.blit(door_button.image, (door_button.x, door_button.y))
            window.blit(door_button_on2.image, (door_button_on2.x, door_button_on2.y))
            window.blit(door_button_on.image, (door_button_on.x, door_button_on.y))

            window.blit(light_button2.image, (light_button2.x, light_button2.y))
            window.blit(light_button.image, (light_button.x, light_button.y))
            window.blit(light_button_on2.image, (light_button_on2.x, light_button_on2.y))
            window.blit(light_button_on.image, (light_button_on.x, light_button_on.y))

            office_bg_image.blit(Light_text, (50, 500))
            office_bg_image.blit(Light_text, (2150, 500))
            office_bg_image.blit(Door_text, (50, 350))
            office_bg_image.blit(Door_text, (2150, 350))
        if power_out == False:
            window.blit(AM_text, (1150, 0))
            window.blit(Night_text, (1150, 50))
            window.blit(Usage_text, (0, 660))
            window.blit(Power_left_text, (0, 600))
            window.blit(Power_number_text, (160, 590))
        pygame.display.update()

def night2():
    data_night['custom_night_on'] = False
    
    phoneguy_night2.play()
    sec = 0
    sec_power = 0
    sec_chic = 0
    sec_fox = 0
    sec_fred = 0
    sec_call = 0
    camera_area_text1 = "W. Hall Corner"

    fred_image = pygame.image.load(os.path.join('Images', 'animatronics', 'fred.png'))

    pirate_cove_image2 = pirate_cove_image
    show_stage_image2 = show_stage_image
    w_hall_corner_image2 = w_hall_corner_image
    w_hall_image2 = w_hall_image
    supply_closet_image2 = supply_closet_image
    restrooms_image2 = restrooms_image
    e_hall_corner_image2 = e_hall_corner_image
    e_hall_image2 = e_hall_image
    dining_area_image2 = dining_area_image
    backstage_image2 = backstage_image

    bon_ai_number = 3
    fox_ai_number = 1 
    chic_ai_number = 1

    move_delay = 250  # milliseconds
    move_delay_camera = 450  # milliseconds
    last_move_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    light_button = button(1850, 400, 100, 100, light_button_image)
    light_button2 = button(-250, 400, 100, 100, light_button_image)
    light_button_on = button(8150, 400, 100, 100, light_button_on_image)
    light_button_on2 = button(8150, 400, 100, 100, light_button_on_image)
    door_button = button(1850, 250, 100, 100, door_button_image)
    door_button2 = button(-250, 250, 100, 100, door_button_image)
    door_button_on = button(8150, 250, 100, 100, door_button_on_image)
    door_button_on2 = button(8150, 250, 100, 100, door_button_on_image)
    left_light = button(-100, 30, 200, 700, left_light_image)
    right_light = button(1600, 30, 200, 700, right_light_image)
    left_door = button(-100, 30, 200, 700, left_door_image)
    right_door = button(1600, 30, 200, 700, right_door_image)
    bon = button(-100, 30, 500, 700, bon_image)
    chic = button(1300, 10, 200, 550, chic_image)
    camera_button = button(300, 650, 500, 50, camera_button_image)
    camera_button2 = button(21500, 650, 500, 50, camera_button_image)
    a2_button = button(870, 550, 95, 65, a2_image)
    a2_on_button = button(11870, 550, 95, 65, a2_on_image)
    b2_button = button(870, 615, 95, 65, b2_image)
    b2_on_button = button(11870, 615, 95, 65, b2_on_image)
    a4_button = button(1030, 550, 95, 65, a4_image)
    a4_on_button = button(111030, 550, 95, 65, a4_on_image)
    b4_button = button(1030, 615, 95, 65, b4_image)
    b4_on_button = button(111030, 615, 95, 65, b4_on_image)
    a3_button = button(740, 500, 95, 65, a3_image)
    a3_on_button = button(11740, 500, 95, 65, a3_on_image)
    a5_button = button(730, 330, 95, 65, a5_image)
    a5_on_button = button(11730, 330, 95, 65, a5_on_image)
    a6_button = button(1130, 500, 95, 65, a6_image)
    a6_on_button = button(111130, 500, 95, 65, a6_on_image)
    a7_button = button(1140, 300, 95, 65, a7_image)
    a7_on_button = button(111140, 300, 95, 65, a7_on_image)
    a1_button = button(900, 200, 95, 65, a1_image)
    a1_on_button = button(11900, 200, 95, 65, a1_on_image)
    b1_button = button(890, 300, 95, 65, b1_image)
    b1_on_button = button(11890, 300, 95, 65, b1_on_image)
    c1_button = button(850, 400, 95, 65, c1_image)
    c1_on_button = button(11850, 400, 95, 65, c1_on_image)
    camera_area = button(-300, 0, 2250, 720, pirate_cove_image)
    boop_button = button(650, 150, 10, 10, boop_image)
    mute_call_button = button(0, 0, 300, 60, mute_call_image)
    
    officex = -300
    camerax = -300
    last_event_time = time.time()
    event_interval = 5  # Time interval in seconds

    flicker_interval = 500  # milliseconds
    last_flicker_time = pygame.time.get_ticks()
    show_power_out_fred = True

    update_pirate_cove = True
    update_backstage = True
    update_dining_area = True
    update_e_hall = True
    update_e_hall_corner = True
    update_restrooms = True
    update_show_stage = True
    update_supply_closet = True
    update_w_hall = True
    update_w_hall_corner = True

    stop_left = True
    stop_right = True
    show_left_light = False
    show_right_light = False
    show_left_door = False
    show_right_door = False
    show_bon = False
    show_chic = False
    show_camera = False
    jumpscare_end = False
    jumpscare_end_chic = False
    jumpscare_end_fox = False
    jumpscare_end_fred = False
    power_out = False
    power_out_fred_active = False
    cama2_active = False
    camb2_active = True
    cama4_active = False
    camb4_active = False
    cama3_active = False
    cama5_active = False
    cama6_active = False
    cama7_active = False
    cama1_active = False
    camb1_active = False
    camc1_active = False
    show_green_cama2_flicker = False
    show_green_camb2_flicker = False
    show_green_cama4_flicker = False
    show_green_camb4_flicker = False
    show_green_cama3_flicker = False
    show_green_cama5_flicker = False
    show_green_cama6_flicker = False
    show_green_cama7_flicker = False
    show_green_cama1_flicker = False
    show_green_camb1_flicker = False
    show_green_camc1_flicker = False
    mute_call = False

    night_number = 2
    am_number = 12
    power_number = 100
    sec_number = 0
    sec_number2 = 0
    sec_number3 = 0
    sec_number4 = 0
    sec_number5 = 0
    sec_fox_move = 0

    pirate_cove_stage_number = 1
    bonnie_stage_number = 1
    chica_stage_number = 1
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'night.json'),'w') as night:
                    json.dump(data_night, night)
                run = False
                pygame.quit()
            current_time = pygame.time.get_ticks()

            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
                camera_button_rect = pygame.Rect(camera_button.x, camera_button.y, camera_button.width, camera_button.height)
                camera_button2_rect = pygame.Rect(camera_button2.x, camera_button2.y, camera_button2.width, camera_button2.height)
                if mousex < 400:
                    stop_left = False
                elif mousex > 900:
                    stop_right = False
                else:
                    stop_left = True
                    stop_right = True
                if power_out == False:
                    if camera_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 21500
                        camera_button2.x = 300
                        show_camera = True
                        last_move_time = current_time
                    if camera_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 300
                        camera_button2.x = 21500
                        show_camera = False
                        last_move_time = current_time
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                mute_call_button_rect = pygame.Rect(mute_call_button.x, mute_call_button.y, mute_call_button.width, mute_call_button.height)
                light_button_rect = pygame.Rect(light_button.x, light_button.y, light_button.width, light_button.height)
                light_button2_rect = pygame.Rect(light_button2.x, light_button2.y, light_button2.width, light_button2.height)
                light_button_on_rect = pygame.Rect(light_button_on.x, light_button_on.y, light_button_on.width, light_button_on.height)
                light_button_on2_rect = pygame.Rect(light_button_on2.x, light_button_on2.y, light_button_on2.width, light_button_on2.height)
                door_button_rect = pygame.Rect(door_button.x, door_button.y, door_button.width, door_button.height)
                door_button2_rect = pygame.Rect(door_button2.x, door_button2.y, door_button2.width, door_button2.height)
                door_button_on_rect = pygame.Rect(door_button_on.x, door_button_on.y, door_button_on.width, door_button_on.height)
                door_button_on2_rect = pygame.Rect(door_button_on2.x, door_button_on2.y, door_button_on2.width, door_button_on2.height)

                boop_button_rect = pygame.Rect(boop_button.x, boop_button.y, boop_button.width, boop_button.height)

                a2_button_rect = pygame.Rect(a2_button.x, a2_button.y, a2_button.width, a2_button.height)
                b2_button_rect = pygame.Rect(b2_button.x, b2_button.y, b2_button.width, b2_button.height)
                a4_button_rect = pygame.Rect(a4_button.x, a4_button.y, a4_button.width, a4_button.height)
                b4_button_rect = pygame.Rect(b4_button.x, b4_button.y, b4_button.width, b4_button.height)
                a3_button_rect = pygame.Rect(a3_button.x, a3_button.y, a3_button.width, a3_button.height)
                a5_button_rect = pygame.Rect(a5_button.x, a5_button.y, a5_button.width, a5_button.height)
                a6_button_rect = pygame.Rect(a6_button.x, a6_button.y, a6_button.width, a6_button.height)
                a7_button_rect = pygame.Rect(a7_button.x, a7_button.y, a7_button.width, a7_button.height)
                a1_button_rect = pygame.Rect(a1_button.x, a1_button.y, a1_button.width, a1_button.height)
                b1_button_rect = pygame.Rect(b1_button.x, b1_button.y, b1_button.width, b1_button.height)
                c1_button_rect = pygame.Rect(c1_button.x, c1_button.y, c1_button.width, c1_button.height)

                if show_camera == False and power_out == False:
                    if mute_call_button_rect.collidepoint(mousex, mousey):
                        mute_call = True
                        mute_call_button.x = -1000000

                    if door_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_right_door = True
                        door_button_on.x = 1180
                        door_button.x = 8150
                        last_move_time = current_time
                    if door_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_left_door = True
                        door_button_on2.x = 50
                        door_button2.x = 8150
                        last_move_time = current_time
                    if door_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_right_door = False
                        door_button_on.x = 8150
                        door_button.x = 1180
                        last_move_time = current_time
                    if door_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_left_door = False
                        door_button_on2.x = 8150
                        door_button2.x = 50
                        last_move_time = current_time

                    if light_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_right_light = True
                        light_button_on.x = 1180
                        light_button.x = 8150
                        last_move_time = current_time
                    if light_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_left_light = True
                        light_button_on2.x = 50
                        light_button2.x = 8150
                        last_move_time = current_time
                    if light_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_right_light = False
                        light_button_on.x = 8150
                        light_button.x = 1180
                        last_move_time = current_time
                    if light_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_left_light = False
                        light_button_on2.x = 8150
                        light_button2.x = 50
                        last_move_time = current_time
                if show_camera == False:
                    if boop_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        boop_sound.play()
                        last_move_time = current_time

                if show_camera == True:
                    if a2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama2_active = True
                        camb2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "West Hall"
                        update_w_hall = True
                        update_pirate_cove = False
                        update_w_hall_corner = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_image2
                        last_move_time = current_time
                    if b2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb2_active = True
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "W. Hall Corner"
                        update_w_hall_corner = True
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_corner_image2
                        last_move_time = current_time
                    if a4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama4_active = True
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_e_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "East Hall"
                        update_e_hall = True
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_image2
                        last_move_time = current_time
                    if b4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb4_active = True
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_e_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "E. Hall Corner"
                        update_e_hall_corner = True
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_corner_image2
                        last_move_time = current_time
                    if a3_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama3_active = True
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_supply_closet == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Supply Closet"
                        update_supply_closet = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        camera_area.image = supply_closet_image2
                        last_move_time = current_time
                    if a5_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama5_active = True
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_backstage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Backstage"
                        update_backstage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = backstage_image2
                        last_move_time = current_time
                    if a6_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        if cama6_active == False:
                            change_camera_sound.play()
                        cama6_active = True
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        camera_area_text1 = "Kitchen"
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = kitchen_image
                        last_move_time = current_time
                    if a7_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama7_active = True
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_restrooms == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Restrooms"
                        update_restrooms = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = restrooms_image2
                        last_move_time = current_time
                    if a1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama1_active = True
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_show_stage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Show Stage"
                        update_show_stage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_supply_closet = False
                        camera_area.image = show_stage_image2
                        last_move_time = current_time
                    if b1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb1_active = True
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camc1_active = False
                        if update_dining_area == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Dining Area"
                        update_dining_area = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = dining_area_image2
                        last_move_time = current_time
                    if c1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camc1_active = True
                        camb1_active = False
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        if update_pirate_cove == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Pirates Cove"
                        update_pirate_cove = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = pirate_cove_image2
                        
                        last_move_time = current_time

        if power_out == True:
            sec_power += 1
        if sec_power == 420:
            music_box.play()
            power_out_fred_active = True
        if sec_power == 1320:
            power_out_fred_active = False
        if sec_power == 1500:
            jumpscare_sound.play() 
            jumpscare_end_fred = True
            stop_left = True
            stop_right = True
            show_camera = False
        sec_call += 1
        sec_fox_move += 1
        current_time3 = pygame.time.get_ticks()
        # Check if it's time to flicker
        if current_time3 - last_flicker_time >= flicker_interval and power_out_fred_active == True:
            show_power_out_fred = not show_power_out_fred  # Toggle visibility
            last_flicker_time = current_time3
        
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama2_active == True:
            show_green_cama2_flicker = not show_green_cama2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb2_active == True:
            show_green_camb2_flicker = not show_green_camb2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama4_active == True:
            show_green_cama4_flicker = not show_green_cama4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb4_active == True:
            show_green_camb4_flicker = not show_green_camb4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama3_active == True:
            show_green_cama3_flicker = not show_green_cama3_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama5_active == True:
            show_green_cama5_flicker = not show_green_cama5_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama6_active == True:
            show_green_cama6_flicker = not show_green_cama6_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama7_active == True:
            show_green_cama7_flicker = not show_green_cama7_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama1_active == True:
            show_green_cama1_flicker = not show_green_cama1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb1_active == True:
            show_green_camb1_flicker = not show_green_camb1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camc1_active == True:
            show_green_camc1_flicker = not show_green_camc1_flicker  # Toggle visibility
            last_flicker_time = current_time3

        current_time2 = time.time()
        if current_time2 - last_event_time >= event_interval and power_out == False:
            sec_number3 += 1   
            rng = random.randint(1, 20)
            print(rng)
                    
            #foxy
            if show_camera == False and sec_fox_move >= random.randint(50, 1000):
                sec_fox_move = 0
                if fox_ai_number >= rng:
                    pirate_cove_stage_number += 1
                    print("fox stage increased!")
                    if pirate_cove_stage_number == 1:
                        pirate_cove_image2 = pirate_cove_image
                        
                    if pirate_cove_image2 == pirate_cove_image and pirate_cove_stage_number == 2:
                        pirate_cove_image2 = pirate_cove_stage2_image    

                    if pirate_cove_image2 == pirate_cove_stage2_image and pirate_cove_stage_number == 3:
                        pirate_cove_image2 = pirate_cove_stage3_image
                        
                    if pirate_cove_image2 == pirate_cove_stage3_image and pirate_cove_stage_number == 4:
                        sec_number3 = 0
                        pirate_cove_image2 = pirate_cove_stage4_image
                    
            
            
            if fox_ai_number >= rng:   
                if sec_number3 == 5 and show_left_door == True or camera_area.image == w_hall_image2 and show_left_door == True:
                    play_next_sound()
                    power_number -= 1
                    pirate_cove_image2 = pirate_cove_image
                    sec_number3 = 0
                    pirate_cove_stage_number = 1
                if sec_number3 == 5 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image or camera_area.image == w_hall_image2 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image:
                    jumpscare_end_fox = True
                    jumpscare_sound.play()
                    stop_left = True
                    stop_right = True
                    show_camera = False
                
            #bonnie
            if bon_ai_number >= rng:
                bonnie_stage_number += 1
                print("bonnie stage increased!")
                if bonnie_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if bonnie_stage_number == 2:
                    show_stage_image2 = show_stage_stage2_image
                    dining_area_image2 = dining_area_stage2_image
                if bonnie_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    backstage_image2 = backstage_stage2_image
                if bonnie_stage_number == 4:
                    backstage_image2 = backstage_image
                    w_hall_image2 = w_hall_stage2_image
                if bonnie_stage_number == 5:
                    w_hall_image2 = w_hall_image
                    supply_closet_image2 = supply_closet_stage2_image
                if bonnie_stage_number == 6:
                    loud_footsteps_sound.play()
                    supply_closet_image2 = supply_closet_image
                    w_hall_corner_image2 = w_hall_corner_stage2_image
                if bonnie_stage_number >= 7:
                    w_hall_corner_image2 = w_hall_corner_image
                    show_bon = True

            if bon_ai_number >= rng and show_left_door == True and show_bon == True:
                show_bon = False
                quiet_footsteps_sound.play()
                bonnie_stage_number = 2
                sec_number2 = 0
            if bon_ai_number < rng:
                print("bonnie failed to move")
            if show_bon == True and show_left_light == True and show_camera == False:
                jump_sound.play()
            if show_bon == True and show_left_door == False:
                sec_number2 += 1
            if sec_number2 >= 2 and show_left_door == False and bon_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end = True
                show_bon = True
                show_left_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                bon.image = pygame.transform.scale(bon.image, (5000, 1000))
                
            
            #chica
            if chic_ai_number >= rng:
                chica_stage_number += 1
                print("Chica Stage Increased!!!")
                if chica_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if chica_stage_number == 2:
                    show_stage_image2 = show_stage_stage3_image
                    dining_area_image2 = dining_area_stage3_image
                if chica_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    restrooms_image2 = restrooms_stage2_image
                if chica_stage_number == 4:
                    restrooms_image2 = restrooms_image
                if chica_stage_number == 5:
                    e_hall_image2 = e_hall_stage2_image
                if chica_stage_number == 6:
                    loud_footsteps_sound.play()
                    e_hall_image2 = e_hall_image
                    e_hall_corner_image2 = e_hall_corner_stage2_image
                if chica_stage_number == 7:
                    e_hall_corner_image2 = e_hall_corner_image
                    show_chic = True

            if chic_ai_number >= rng and show_right_door == True and show_chic == True:
                show_chic = False
                quiet_footsteps_sound.play()
                chica_stage_number = 2
                sec_number4 = 0
            if chic_ai_number < rng:
                print("chica failed to move")
            if show_chic == True and show_right_light == True and show_camera == False:
                jump_sound.play()
            if show_chic == True and show_right_door == False:
                sec_number4 += 1
            if sec_number4 >= 2 and show_right_door == False and chic_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end_chic = True
                show_chic = True
                show_right_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                chic.image = pygame.transform.scale(chic.image, (2500, 1000))
                chic.x = bon.x

            last_event_time = current_time2

        if jumpscare_end == True:
            sec += 1
            phoneguy_night1.stop()
            show_bon = True
            show_left_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec >= 70:
            mainmenu()
        
        if jumpscare_end_chic == True:
            sec_chic += 1
            phoneguy_night1.stop()
            show_chic = True
            show_right_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_chic >= 70:
            mainmenu()
        
        if jumpscare_end_fox == True:
            sec_fox += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fox >= 140:
            mainmenu()
        
        if jumpscare_end_fred == True:
            sec_fred += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fred >= 70:
            mainmenu()

        if mute_call == True:
            phoneguy_night2.set_volume(0.00)

        if sec_call >= 1380:
            mute_call_button.x = -100000

        if show_camera == True and update_pirate_cove == True:
            camera_area.image = pirate_cove_image2

        if show_camera == True and update_backstage == True:
            camera_area.image = backstage_image2

        if show_camera == True and update_dining_area == True:
            camera_area.image = dining_area_image2

        if show_camera == True and update_e_hall == True:
            camera_area.image = e_hall_image2

        if show_camera == True and update_e_hall_corner == True:
            camera_area.image = e_hall_corner_image2

        if show_camera == True and update_restrooms == True:
            camera_area.image = restrooms_image2

        if show_camera == True and update_show_stage == True:
            camera_area.image = show_stage_image2

        if show_camera == True and update_supply_closet == True:
            camera_area.image = supply_closet_image2
        
        if show_camera == True and update_w_hall == True:
            camera_area.image = w_hall_image2
        
        if show_camera == True and update_w_hall_corner == True:
            camera_area.image = w_hall_corner_image2
            

        if stop_left == False and camerax < -100:
            camerax += 10
            
        if stop_right == False and camerax > -500:
            camerax -= 10

        if stop_left == False and officex < -5:
            officex += 10
            boop_button.x += 10
            left_light.x += 10
            right_light.x += 10
            left_door.x += 10
            right_door.x += 10
            bon.x += 10
            chic.x += 10
            light_button.x += 10
            light_button2.x += 10
            light_button_on.x += 10
            light_button_on2.x += 10
            door_button.x += 10
            door_button2.x += 10
            door_button_on.x += 10
            door_button_on2.x += 10
        if stop_right == False and officex > -970:
            officex -= 10
            boop_button.x -= 10
            left_light.x -= 10
            right_light.x -= 10
            left_door.x -= 10
            right_door.x -= 10
            bon.x -= 10
            chic.x -= 10
            light_button.x -= 10
            light_button2.x -= 10
            light_button_on.x -= 10
            light_button_on2.x -= 10
            door_button.x -= 10
            door_button2.x -= 10
            door_button_on.x -= 10
            door_button_on2.x -= 10

        sec_number5 += 1
        if sec_number5 >= 360:
            power_number -= 1
            sec_number5 = 0

        sec_number+=1
        if sec_number == 5400:
            am_number = 1
        if sec_number == 10800:
            bon_ai_number += 1
            am_number = 2
        if sec_number == 16200:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 3
        if sec_number == 21600:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 4
        if sec_number == 27000:
            am_number = 5
        if sec_number == 32400:
            power_out = False
            data_night['night_number'] = 3
            with open(os.path.join('data', 'night.json'),'w') as night:
                json.dump(data_night, night)
            win6am()

        if power_number <= 0:
            power_out = True

        if power_out == False:
            Usage_text = Small_Font.render("Usage:", 1, WHITE)
            Power_left_text = Small_Font.render("Power left:", 1, WHITE)
            Night_text = Small_Font.render("Night " + str(int(night_number)), 1, WHITE)
            AM_text = Big_Font.render(str(int(am_number)) + " AM", 1, WHITE)
            Power_number_text = Big_Font.render(str(int(power_number)) + "%", 1, WHITE)
        Light_text = Small_Font.render("LIGHT", 1, WHITE)
        Door_text = Small_Font.render("DOOR", 1, WHITE)
        if power_out == False:
            camera_area_text = Big_Font.render(camera_area_text1, 1, WHITE)
        window.fill((0, 0, 0))
        if power_out == False:
            if show_right_light == True and show_chic == True and show_camera == False:
                window.blit(chic.image, (chic.x, chic.y))
        window.blit(office_bg_image, (officex, 0))
        window.blit(boop_button.image, (boop_button.x, boop_button.y))
        window.blit(mute_call_button.image, (mute_call_button.x, mute_call_button.y))
        if power_out == False:
            window.blit(camera_button.image, (camera_button.x, camera_button.y))
        if power_out == False:
            if jumpscare_end_chic == True:
                window.blit(chic.image, (chic.x, chic.y))
            if jumpscare_end_fox == True:
                window.blit(fox_image, (bon.x + 100, chic.y))
            if show_camera == True:
                power_number -= 0.0008
                window.blit(camera_area.image, (camerax, camera_area.y))
                window.blit(camera_area_text, (735, 130))
                window.blit(green_bar_image, (125, 670))
                window.blit(map_image, (750, 200))
                if show_green_cama1_flicker == False:
                    a1_button.x = 900
                    a1_on_button.x = 11900
                if show_green_cama2_flicker == False:
                    a2_button.x = 870
                    a2_on_button.x = 11870
                if show_green_camb2_flicker == False:
                    b2_button.x = 870
                    b2_on_button.x = 11870
                if show_green_camc1_flicker == False:
                    c1_button.x = 850
                    c1_on_button.x = 11850
                if show_green_camb1_flicker == False:
                    b1_button.x = 890
                    b1_on_button.x = 11890
                if show_green_cama7_flicker == False:
                    a7_button.x = 1140
                    a7_on_button.x = 111140
                if show_green_cama6_flicker == False:
                    a6_button.x = 1130
                    a6_on_button.x = 111130
                if show_green_cama5_flicker == False:
                    a5_button.x = 730
                    a5_on_button.x = 11730
                if show_green_cama3_flicker == False:
                    a3_button.x = 740
                    a3_on_button.x = 11740
                if show_green_camb4_flicker == False:
                    b4_button.x = 1030
                    b4_on_button.x = 111030
                if show_green_cama4_flicker == False:
                    a4_button.x = 1030
                    a4_on_button.x = 111030
                if show_green_cama2_flicker == True:
                    a2_button.x = 11870
                    a2_on_button.x = 870
                if cama2_active == False:
                    a2_button.x = 870
                if show_green_camb2_flicker == True:
                    b2_button.x = 11870
                    b2_on_button.x = 870
                if camb2_active == False:
                    b2_button.x = 870
                if show_green_camc1_flicker == True:
                    c1_button.x = 11850
                    c1_on_button.x = 850
                if camc1_active == False:
                    c1_button.x = 850
                if show_green_camb1_flicker == True:
                    b1_button.x = 11890
                    b1_on_button.x = 890
                if camb1_active == False:
                    b1_button.x = 890
                if show_green_cama1_flicker == True:
                    a1_button.x = 11900
                    a1_on_button.x = 900
                if cama1_active == False:
                    a1_button.x = 900
                if show_green_cama7_flicker == True:
                    a7_button.x = 111140
                    a7_on_button.x = 1140
                if cama7_active == False:
                    a7_button.x = 1140
                if show_green_cama6_flicker == True:
                    a6_button.x = 111130
                    a6_on_button.x = 1130
                if cama6_active == False:
                    a6_button.x = 1130
                if show_green_cama5_flicker == True:
                    a5_button.x = 11730
                    a5_on_button.x = 730
                if cama5_active == False:
                    a5_button.x = 730
                if show_green_cama3_flicker == True:
                    a3_button.x = 11740
                    a3_on_button.x = 740
                if cama3_active == False:
                    a3_button.x = 740
                if show_green_camb4_flicker == True:
                    b4_button.x = 111030
                    b4_on_button.x = 1030
                if camb4_active == False:
                    b4_button.x = 1030
                if show_green_cama4_flicker == True:
                    a4_button.x = 111030
                    a4_on_button.x = 1030
                if cama4_active == False:
                    a4_button.x = 1030
                window.blit(a2_on_button.image, (a2_on_button.x, a2_on_button.y))
                window.blit(b2_on_button.image, (b2_on_button.x, b2_on_button.y))
                window.blit(a4_on_button.image, (a4_on_button.x, a4_on_button.y))
                window.blit(b4_on_button.image, (b4_on_button.x, b4_on_button.y))
                window.blit(a3_on_button.image, (a3_on_button.x, a3_on_button.y))
                window.blit(a5_on_button.image, (a5_on_button.x, a5_on_button.y))
                window.blit(a6_on_button.image, (a6_on_button.x, a6_on_button.y))
                window.blit(a7_on_button.image, (a7_on_button.x, a7_on_button.y))
                window.blit(a1_on_button.image, (a1_on_button.x, a1_on_button.y))
                window.blit(b1_on_button.image, (b1_on_button.x, b1_on_button.y))
                window.blit(c1_on_button.image, (c1_on_button.x, c1_on_button.y))
                
                window.blit(a2_button.image, (a2_button.x, a2_button.y))           
                window.blit(b2_button.image, (b2_button.x, b2_button.y))             
                window.blit(a4_button.image, (a4_button.x, a4_button.y))              
                window.blit(b4_button.image, (b4_button.x, b4_button.y))              
                window.blit(a3_button.image, (a3_button.x, a3_button.y))  
                window.blit(a5_button.image, (a5_button.x, a5_button.y))               
                window.blit(a6_button.image, (a6_button.x, a6_button.y))    
                window.blit(a7_button.image, (a7_button.x, a7_button.y))             
                window.blit(a1_button.image, (a1_button.x, a1_button.y))             
                window.blit(b1_button.image, (b1_button.x, b1_button.y)) 
                window.blit(c1_button.image, (c1_button.x, c1_button.y))
                window.blit(camera_button2.image, (camera_button2.x, camera_button2.y))
            if show_left_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_left_light == True and show_camera == False:
                window.blit(left_light.image, (left_light.x, left_light.y))
            if show_left_light == True and show_bon == True and show_camera == False:
                window.blit(bon.image, (bon.x, bon.y))
            if show_right_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_right_light == True and show_camera == False:
                window.blit(right_light.image, (right_light.x, right_light.y))
            if show_left_door == True:
                power_number -= 0.002
                window.blit(yellow_bar_image, (150, 670))
            if show_left_door == True and show_camera == False:
                window.blit(left_door.image, (left_door.x, left_door.y))
            if show_right_door == True:
                power_number -= 0.002
                window.blit(red_bar_image, (175, 670))
            if show_right_door == True and show_camera == False:
                window.blit(right_door.image, (right_door.x, right_door.y))
            if show_right_door == False and show_left_door == False and show_right_light == False and show_left_light == False and show_camera == False:
                power_number -= 0
            window.blit(green_bar_image, (100, 670))
            power_number -= 0.0008
        if power_out == True and show_power_out_fred == True and power_out_fred_active == True:
            window.blit(fred_power_out_image, (bon.x, bon.y))
        
        if jumpscare_end_fred == True:
            fred_image = pygame.transform.scale(fred_image, (2500, 1000))
            window.blit(fred_image, (bon.x, chic.y))

        if show_camera == False:
            window.blit(door_button2.image, (door_button2.x, door_button2.y))
            window.blit(door_button.image, (door_button.x, door_button.y))
            window.blit(door_button_on2.image, (door_button_on2.x, door_button_on2.y))
            window.blit(door_button_on.image, (door_button_on.x, door_button_on.y))

            window.blit(light_button2.image, (light_button2.x, light_button2.y))
            window.blit(light_button.image, (light_button.x, light_button.y))
            window.blit(light_button_on2.image, (light_button_on2.x, light_button_on2.y))
            window.blit(light_button_on.image, (light_button_on.x, light_button_on.y))

            office_bg_image.blit(Light_text, (50, 500))
            office_bg_image.blit(Light_text, (2150, 500))
            office_bg_image.blit(Door_text, (50, 350))
            office_bg_image.blit(Door_text, (2150, 350))
        if power_out == False:
            window.blit(AM_text, (1150, 0))
            window.blit(Night_text, (1150, 50))
            window.blit(Usage_text, (0, 660))
            window.blit(Power_left_text, (0, 600))
            window.blit(Power_number_text, (160, 590))
        pygame.display.update()
def night3():
    
    phoneguy_night3.play()
    sec = 0
    sec_power = 0
    sec_chic = 0
    sec_fox = 0
    sec_fred = 0
    sec_call = 0
    camera_area_text1 = "W. Hall Corner"

    fred_image = pygame.image.load(os.path.join('Images', 'animatronics', 'fred.png'))

    pirate_cove_image2 = pirate_cove_image
    show_stage_image2 = show_stage_image
    w_hall_corner_image2 = w_hall_corner_image
    w_hall_image2 = w_hall_image
    supply_closet_image2 = supply_closet_image
    restrooms_image2 = restrooms_image
    e_hall_corner_image2 = e_hall_corner_image
    e_hall_image2 = e_hall_image
    dining_area_image2 = dining_area_image
    backstage_image2 = backstage_image

    bon_ai_number = 0
    fox_ai_number = 2 
    chic_ai_number = 5 
    fred_ai_number = 1 

    move_delay = 250  # milliseconds
    move_delay_camera = 450  # milliseconds
    last_move_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    light_button = button(1850, 400, 100, 100, light_button_image)
    light_button2 = button(-250, 400, 100, 100, light_button_image)
    light_button_on = button(8150, 400, 100, 100, light_button_on_image)
    light_button_on2 = button(8150, 400, 100, 100, light_button_on_image)
    door_button = button(1850, 250, 100, 100, door_button_image)
    door_button2 = button(-250, 250, 100, 100, door_button_image)
    door_button_on = button(8150, 250, 100, 100, door_button_on_image)
    door_button_on2 = button(8150, 250, 100, 100, door_button_on_image)
    left_light = button(-100, 30, 200, 700, left_light_image)
    right_light = button(1600, 30, 200, 700, right_light_image)
    left_door = button(-100, 30, 200, 700, left_door_image)
    right_door = button(1600, 30, 200, 700, right_door_image)
    bon = button(-100, 30, 500, 700, bon_image)
    chic = button(1300, 10, 200, 550, chic_image)
    camera_button = button(300, 650, 500, 50, camera_button_image)
    camera_button2 = button(21500, 650, 500, 50, camera_button_image)
    a2_button = button(870, 550, 95, 65, a2_image)
    a2_on_button = button(11870, 550, 95, 65, a2_on_image)
    b2_button = button(870, 615, 95, 65, b2_image)
    b2_on_button = button(11870, 615, 95, 65, b2_on_image)
    a4_button = button(1030, 550, 95, 65, a4_image)
    a4_on_button = button(111030, 550, 95, 65, a4_on_image)
    b4_button = button(1030, 615, 95, 65, b4_image)
    b4_on_button = button(111030, 615, 95, 65, b4_on_image)
    a3_button = button(740, 500, 95, 65, a3_image)
    a3_on_button = button(11740, 500, 95, 65, a3_on_image)
    a5_button = button(730, 330, 95, 65, a5_image)
    a5_on_button = button(11730, 330, 95, 65, a5_on_image)
    a6_button = button(1130, 500, 95, 65, a6_image)
    a6_on_button = button(111130, 500, 95, 65, a6_on_image)
    a7_button = button(1140, 300, 95, 65, a7_image)
    a7_on_button = button(111140, 300, 95, 65, a7_on_image)
    a1_button = button(900, 200, 95, 65, a1_image)
    a1_on_button = button(11900, 200, 95, 65, a1_on_image)
    b1_button = button(890, 300, 95, 65, b1_image)
    b1_on_button = button(11890, 300, 95, 65, b1_on_image)
    c1_button = button(850, 400, 95, 65, c1_image)
    c1_on_button = button(11850, 400, 95, 65, c1_on_image)
    camera_area = button(-300, 0, 2250, 720, pirate_cove_image)
    boop_button = button(650, 150, 10, 10, boop_image)
    mute_call_button = button(0, 0, 300, 60, mute_call_image)
    
    officex = -300
    camerax = -300
    last_event_time = time.time()
    event_interval = 5  # Time interval in seconds

    flicker_interval = 500  # milliseconds
    last_flicker_time = pygame.time.get_ticks()
    show_power_out_fred = True

    update_pirate_cove = True
    update_backstage = True
    update_dining_area = True
    update_e_hall = True
    update_e_hall_corner = True
    update_restrooms = True
    update_show_stage = True
    update_supply_closet = True
    update_w_hall = True
    update_w_hall_corner = True

    stop_left = True
    stop_right = True
    show_left_light = False
    show_right_light = False
    show_left_door = False
    show_right_door = False
    show_bon = False
    show_chic = False
    show_camera = False
    jumpscare_end = False
    jumpscare_end_chic = False
    jumpscare_end_fox = False
    jumpscare_end_fred = False
    power_out = False
    power_out_fred_active = False
    cama2_active = False
    camb2_active = True
    cama4_active = False
    camb4_active = False
    cama3_active = False
    cama5_active = False
    cama6_active = False
    cama7_active = False
    cama1_active = False
    camb1_active = False
    camc1_active = False
    show_green_cama2_flicker = False
    show_green_camb2_flicker = False
    show_green_cama4_flicker = False
    show_green_camb4_flicker = False
    show_green_cama3_flicker = False
    show_green_cama5_flicker = False
    show_green_cama6_flicker = False
    show_green_cama7_flicker = False
    show_green_cama1_flicker = False
    show_green_camb1_flicker = False
    show_green_camc1_flicker = False
    mute_call = False

    night_number = 3
    am_number = 12
    power_number = 100
    sec_number = 0
    sec_number2 = 0
    sec_number3 = 0
    sec_number4 = 0
    sec_number5 = 0
    sec_fred_move = 0
    sec_fox_move = 0

    pirate_cove_stage_number = 1
    bonnie_stage_number = 1
    chica_stage_number = 1
    fred_stage_number = 1
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'night.json'),'w') as night:
                    json.dump(data_night, night)
                run = False
                pygame.quit()
            current_time = pygame.time.get_ticks()

            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
                camera_button_rect = pygame.Rect(camera_button.x, camera_button.y, camera_button.width, camera_button.height)
                camera_button2_rect = pygame.Rect(camera_button2.x, camera_button2.y, camera_button2.width, camera_button2.height)
                if mousex < 400:
                    stop_left = False
                elif mousex > 900:
                    stop_right = False
                else:
                    stop_left = True
                    stop_right = True
                if power_out == False:
                    if camera_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 21500
                        camera_button2.x = 300
                        show_camera = True
                        last_move_time = current_time
                    if camera_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 300
                        camera_button2.x = 21500
                        show_camera = False
                        last_move_time = current_time
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                mute_call_button_rect = pygame.Rect(mute_call_button.x, mute_call_button.y, mute_call_button.width, mute_call_button.height)
                light_button_rect = pygame.Rect(light_button.x, light_button.y, light_button.width, light_button.height)
                light_button2_rect = pygame.Rect(light_button2.x, light_button2.y, light_button2.width, light_button2.height)
                light_button_on_rect = pygame.Rect(light_button_on.x, light_button_on.y, light_button_on.width, light_button_on.height)
                light_button_on2_rect = pygame.Rect(light_button_on2.x, light_button_on2.y, light_button_on2.width, light_button_on2.height)
                door_button_rect = pygame.Rect(door_button.x, door_button.y, door_button.width, door_button.height)
                door_button2_rect = pygame.Rect(door_button2.x, door_button2.y, door_button2.width, door_button2.height)
                door_button_on_rect = pygame.Rect(door_button_on.x, door_button_on.y, door_button_on.width, door_button_on.height)
                door_button_on2_rect = pygame.Rect(door_button_on2.x, door_button_on2.y, door_button_on2.width, door_button_on2.height)

                boop_button_rect = pygame.Rect(boop_button.x, boop_button.y, boop_button.width, boop_button.height)

                a2_button_rect = pygame.Rect(a2_button.x, a2_button.y, a2_button.width, a2_button.height)
                b2_button_rect = pygame.Rect(b2_button.x, b2_button.y, b2_button.width, b2_button.height)
                a4_button_rect = pygame.Rect(a4_button.x, a4_button.y, a4_button.width, a4_button.height)
                b4_button_rect = pygame.Rect(b4_button.x, b4_button.y, b4_button.width, b4_button.height)
                a3_button_rect = pygame.Rect(a3_button.x, a3_button.y, a3_button.width, a3_button.height)
                a5_button_rect = pygame.Rect(a5_button.x, a5_button.y, a5_button.width, a5_button.height)
                a6_button_rect = pygame.Rect(a6_button.x, a6_button.y, a6_button.width, a6_button.height)
                a7_button_rect = pygame.Rect(a7_button.x, a7_button.y, a7_button.width, a7_button.height)
                a1_button_rect = pygame.Rect(a1_button.x, a1_button.y, a1_button.width, a1_button.height)
                b1_button_rect = pygame.Rect(b1_button.x, b1_button.y, b1_button.width, b1_button.height)
                c1_button_rect = pygame.Rect(c1_button.x, c1_button.y, c1_button.width, c1_button.height)

                if show_camera == False and power_out == False:
                    if mute_call_button_rect.collidepoint(mousex, mousey):
                        mute_call = True
                        mute_call_button.x = -1000000

                    if door_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_right_door = True
                        door_button_on.x = 1180
                        door_button.x = 8150
                        last_move_time = current_time
                    if door_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_left_door = True
                        door_button_on2.x = 50
                        door_button2.x = 8150
                        last_move_time = current_time
                    if door_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_right_door = False
                        door_button_on.x = 8150
                        door_button.x = 1180
                        last_move_time = current_time
                    if door_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_left_door = False
                        door_button_on2.x = 8150
                        door_button2.x = 50
                        last_move_time = current_time

                    if light_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_right_light = True
                        light_button_on.x = 1180
                        light_button.x = 8150
                        last_move_time = current_time
                    if light_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_left_light = True
                        light_button_on2.x = 50
                        light_button2.x = 8150
                        last_move_time = current_time
                    if light_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_right_light = False
                        light_button_on.x = 8150
                        light_button.x = 1180
                        last_move_time = current_time
                    if light_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_left_light = False
                        light_button_on2.x = 8150
                        light_button2.x = 50
                        last_move_time = current_time
                if show_camera == False:
                    if boop_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        boop_sound.play()
                        last_move_time = current_time

                if show_camera == True:
                    if a2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama2_active = True
                        camb2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "West Hall"
                        update_w_hall = True
                        update_pirate_cove = False
                        update_w_hall_corner = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_image2
                        last_move_time = current_time
                    if b2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb2_active = True
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "W. Hall Corner"
                        update_w_hall_corner = True
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_corner_image2
                        last_move_time = current_time
                    if a4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama4_active = True
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_e_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "East Hall"
                        update_e_hall = True
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_image2
                        last_move_time = current_time
                    if b4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb4_active = True
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_e_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "E. Hall Corner"
                        update_e_hall_corner = True
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_corner_image2
                        last_move_time = current_time
                    if a3_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama3_active = True
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_supply_closet == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Supply Closet"
                        update_supply_closet = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        camera_area.image = supply_closet_image2
                        last_move_time = current_time
                    if a5_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama5_active = True
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_backstage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Backstage"
                        update_backstage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = backstage_image2
                        last_move_time = current_time
                    if a6_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        if cama6_active == False:
                            change_camera_sound.play()
                        cama6_active = True
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        camera_area_text1 = "Kitchen"
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = kitchen_image
                        last_move_time = current_time
                    if a7_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama7_active = True
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_restrooms == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Restrooms"
                        update_restrooms = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = restrooms_image2
                        last_move_time = current_time
                    if a1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama1_active = True
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_show_stage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Show Stage"
                        update_show_stage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_supply_closet = False
                        camera_area.image = show_stage_image2
                        last_move_time = current_time
                    if b1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb1_active = True
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camc1_active = False
                        if update_dining_area == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Dining Area"
                        update_dining_area = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = dining_area_image2
                        last_move_time = current_time
                    if c1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camc1_active = True
                        camb1_active = False
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        if update_pirate_cove == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Pirates Cove"
                        update_pirate_cove = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = pirate_cove_image2
                        
                        last_move_time = current_time
        if power_out == True:
            sec_power += 1
        if sec_power == 420:
            music_box.play()
            power_out_fred_active = True
        if sec_power == 1320:
            power_out_fred_active = False
        if sec_power == 1500:
            jumpscare_sound.play() 
            jumpscare_end_fred = True
            stop_left = True
            stop_right = True
            show_camera = False
        sec_call += 1
        sec_fred_move += 1
        sec_fox_move += 1
        current_time3 = pygame.time.get_ticks()
        # Check if it's time to flicker
        if current_time3 - last_flicker_time >= flicker_interval and power_out_fred_active == True:
            show_power_out_fred = not show_power_out_fred  # Toggle visibility
            last_flicker_time = current_time3

        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama2_active == True:
            show_green_cama2_flicker = not show_green_cama2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb2_active == True:
            show_green_camb2_flicker = not show_green_camb2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama4_active == True:
            show_green_cama4_flicker = not show_green_cama4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb4_active == True:
            show_green_camb4_flicker = not show_green_camb4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama3_active == True:
            show_green_cama3_flicker = not show_green_cama3_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama5_active == True:
            show_green_cama5_flicker = not show_green_cama5_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama6_active == True:
            show_green_cama6_flicker = not show_green_cama6_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama7_active == True:
            show_green_cama7_flicker = not show_green_cama7_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama1_active == True:
            show_green_cama1_flicker = not show_green_cama1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb1_active == True:
            show_green_camb1_flicker = not show_green_camb1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camc1_active == True:
            show_green_camc1_flicker = not show_green_camc1_flicker  # Toggle visibility
            last_flicker_time = current_time3

        current_time2 = time.time()
        if current_time2 - last_event_time >= event_interval and power_out == False:
            sec_number3 += 1   
            rng = random.randint(1, 20)
            print(rng)
            #freddy fazbear
            if show_camera == False:
                sec_fred_move = 0
                if fred_ai_number >= rng and sec_fred_move >= 1000 - 100 * fred_ai_number:
                    fred_stage_number += 1
                    print("Fred Stage INCREASED!!!!!!!")
                    if fred_stage_number == 1 and chica_stage_number == 1 and bonnie_stage_number == 1:
                        show_stage_image2 = show_stage_image
                    if fred_stage_number == 2:
                        show_stage_image2 = show_stage_stage4_image
                    if fred_stage_number >= 6:
                        e_hall_corner_image2 = e_hall_corner_stage3_image
            if camera_area.image != e_hall_corner_image2 and show_right_door == False and fred_stage_number >= 6:
                jumpscare_end_fred = True
                jumpscare_sound.play()
                stop_left = True
                stop_right = True
                show_camera = False
            if camera_area.image != e_hall_corner_image2 and show_right_door == True and fred_stage_number >= 6:
                e_hall_corner_image2 = e_hall_corner_image
                fred_stage_number = 5
                    
            #foxy
            if show_camera == False and sec_fox_move >= random.randint(50, 1000):
                sec_fox_move = 0
                if fox_ai_number >= rng:
                    pirate_cove_stage_number += 1
                    print("fox stage increased!")
                    if pirate_cove_stage_number == 1:
                        pirate_cove_image2 = pirate_cove_image
                        
                    if pirate_cove_image2 == pirate_cove_image and pirate_cove_stage_number == 2:
                        pirate_cove_image2 = pirate_cove_stage2_image    

                    if pirate_cove_image2 == pirate_cove_stage2_image and pirate_cove_stage_number == 3:
                        pirate_cove_image2 = pirate_cove_stage3_image
                        
                    if pirate_cove_image2 == pirate_cove_stage3_image and pirate_cove_stage_number == 4:
                        sec_number3 = 0
                        pirate_cove_image2 = pirate_cove_stage4_image
                    
            
            
            if fox_ai_number >= rng:   
                if sec_number3 == 5 and show_left_door == True or camera_area.image == w_hall_image2 and show_left_door == True:
                    play_next_sound()
                    power_number -= 1
                    pirate_cove_image2 = pirate_cove_image
                    sec_number3 = 0
                    pirate_cove_stage_number = 1
                if sec_number3 == 5 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image or camera_area.image == w_hall_image2 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image:
                    jumpscare_end_fox = True
                    jumpscare_sound.play()
                    stop_left = True
                    stop_right = True
                    show_camera = False
                
            #bonnie
            if bon_ai_number >= rng:
                bonnie_stage_number += 1
                print("bonnie stage increased!")
                if bonnie_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if bonnie_stage_number == 2:
                    show_stage_image2 = show_stage_stage2_image
                    dining_area_image2 = dining_area_stage2_image
                if bonnie_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    backstage_image2 = backstage_stage2_image
                if bonnie_stage_number == 4:
                    backstage_image2 = backstage_image
                    w_hall_image2 = w_hall_stage2_image
                if bonnie_stage_number == 5:
                    w_hall_image2 = w_hall_image
                    supply_closet_image2 = supply_closet_stage2_image
                if bonnie_stage_number == 6:
                    loud_footsteps_sound.play()
                    supply_closet_image2 = supply_closet_image
                    w_hall_corner_image2 = w_hall_corner_stage2_image
                if bonnie_stage_number >= 7:
                    w_hall_corner_image2 = w_hall_corner_image
                    show_bon = True

            if bon_ai_number >= rng and show_left_door == True and show_bon == True:
                show_bon = False
                quiet_footsteps_sound.play()
                bonnie_stage_number = 2
                sec_number2 = 0
            if bon_ai_number < rng:
                print("bonnie failed to move")
            if show_bon == True and show_left_light == True and show_camera == False:
                jump_sound.play()
            if show_bon == True and show_left_door == False:
                sec_number2 += 1
            if sec_number2 >= 2 and show_left_door == False and bon_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end = True
                show_bon = True
                show_left_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                bon.image = pygame.transform.scale(bon.image, (5000, 1000))
                
            
            #chica
            if chic_ai_number >= rng:
                chica_stage_number += 1
                print("Chica Stage Increased!!!")
                if chica_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if chica_stage_number == 2:
                    show_stage_image2 = show_stage_stage3_image
                    dining_area_image2 = dining_area_stage3_image
                if chica_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    restrooms_image2 = restrooms_stage2_image
                if chica_stage_number == 4:
                    restrooms_image2 = restrooms_image
                if chica_stage_number == 5:
                    e_hall_image2 = e_hall_stage2_image
                if chica_stage_number == 6:
                    loud_footsteps_sound.play()
                    e_hall_image2 = e_hall_image
                    e_hall_corner_image2 = e_hall_corner_stage2_image
                if chica_stage_number == 7:
                    e_hall_corner_image2 = e_hall_corner_image
                    show_chic = True

            if chic_ai_number >= rng and show_right_door == True and show_chic == True:
                show_chic = False
                quiet_footsteps_sound.play()
                chica_stage_number = 2
                sec_number4 = 0
            if chic_ai_number < rng:
                print("chica failed to move")
            if show_chic == True and show_right_light == True and show_camera == False:
                jump_sound.play()
            if show_chic == True and show_right_door == False:
                sec_number4 += 1
            if sec_number4 >= 2 and show_right_door == False and chic_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end_chic = True
                show_chic = True
                show_right_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                chic.image = pygame.transform.scale(chic.image, (2500, 1000))
                chic.x = bon.x

            last_event_time = current_time2

        if jumpscare_end == True:
            sec += 1
            phoneguy_night1.stop()
            show_bon = True
            show_left_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec >= 70:
            mainmenu()
        
        if jumpscare_end_chic == True:
            sec_chic += 1
            phoneguy_night1.stop()
            show_chic = True
            show_right_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_chic >= 70:
            mainmenu()
        
        if jumpscare_end_fox == True:
            sec_fox += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fox >= 140:
            mainmenu()

        if jumpscare_end_fred == True:
            sec_fred += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fred >= 70:
            mainmenu()

        if mute_call == True:
            phoneguy_night3.set_volume(0.00)

        if sec_call >= 1380:
            mute_call_button.x = -100000

        if show_camera == True and update_pirate_cove == True:
            camera_area.image = pirate_cove_image2

        if show_camera == True and update_backstage == True:
            camera_area.image = backstage_image2

        if show_camera == True and update_dining_area == True:
            camera_area.image = dining_area_image2

        if show_camera == True and update_e_hall == True:
            camera_area.image = e_hall_image2

        if show_camera == True and update_e_hall_corner == True:
            camera_area.image = e_hall_corner_image2

        if show_camera == True and update_restrooms == True:
            camera_area.image = restrooms_image2

        if show_camera == True and update_show_stage == True:
            camera_area.image = show_stage_image2

        if show_camera == True and update_supply_closet == True:
            camera_area.image = supply_closet_image2
        
        if show_camera == True and update_w_hall == True:
            camera_area.image = w_hall_image2
        
        if show_camera == True and update_w_hall_corner == True:
            camera_area.image = w_hall_corner_image2
            

        if stop_left == False and camerax < -100:
            camerax += 10
            
        if stop_right == False and camerax > -500:
            camerax -= 10

        if stop_left == False and officex < -5:
            officex += 10
            boop_button.x += 10
            left_light.x += 10
            right_light.x += 10
            left_door.x += 10
            right_door.x += 10
            bon.x += 10
            chic.x += 10
            light_button.x += 10
            light_button2.x += 10
            light_button_on.x += 10
            light_button_on2.x += 10
            door_button.x += 10
            door_button2.x += 10
            door_button_on.x += 10
            door_button_on2.x += 10
        if stop_right == False and officex > -970:
            officex -= 10
            boop_button.x -= 10
            left_light.x -= 10
            right_light.x -= 10
            left_door.x -= 10
            right_door.x -= 10
            bon.x -= 10
            chic.x -= 10
            light_button.x -= 10
            light_button2.x -= 10
            light_button_on.x -= 10
            light_button_on2.x -= 10
            door_button.x -= 10
            door_button2.x -= 10
            door_button_on.x -= 10
            door_button_on2.x -= 10

        sec_number5 += 1
        if sec_number5 >= 300:
            power_number -= 1
            sec_number5 = 0

        sec_number+=1
        if sec_number == 5400:
            am_number = 1
        if sec_number == 10800:
            bon_ai_number += 1
            am_number = 2
        if sec_number == 16200:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 3
        if sec_number == 21600:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 4
        if sec_number == 27000:
            am_number = 5
        if sec_number == 32400:
            power_out = False
            data_night['night_number'] = 4
            with open(os.path.join('data', 'night.json'),'w') as night:
                json.dump(data_night, night)
            win6am()

        if power_number <= 0:
            power_out = True

        if power_out == False:
            Usage_text = Small_Font.render("Usage:", 1, WHITE)
            Power_left_text = Small_Font.render("Power left:", 1, WHITE)
            Night_text = Small_Font.render("Night " + str(int(night_number)), 1, WHITE)
            AM_text = Big_Font.render(str(int(am_number)) + " AM", 1, WHITE)
            Power_number_text = Big_Font.render(str(int(power_number)) + "%", 1, WHITE)
        Light_text = Small_Font.render("LIGHT", 1, WHITE)
        Door_text = Small_Font.render("DOOR", 1, WHITE)
        if power_out == False:
            camera_area_text = Big_Font.render(camera_area_text1, 1, WHITE)
        window.fill((0, 0, 0))
        if power_out == False:
            if show_right_light == True and show_chic == True and show_camera == False:
                window.blit(chic.image, (chic.x, chic.y))
        window.blit(office_bg_image, (officex, 0))
        window.blit(boop_button.image, (boop_button.x, boop_button.y))
        window.blit(mute_call_button.image, (mute_call_button.x, mute_call_button.y))
        if power_out == False:
            window.blit(camera_button.image, (camera_button.x, camera_button.y))
        if power_out == False:
            if jumpscare_end_chic == True:
                window.blit(chic.image, (chic.x, chic.y))
            if jumpscare_end_fox == True:
                window.blit(fox_image, (bon.x + 100, chic.y))
            if show_camera == True:
                power_number -= 0.0008
                window.blit(camera_area.image, (camerax, camera_area.y))
                window.blit(camera_area_text, (735, 130))
                window.blit(green_bar_image, (125, 670))
                window.blit(map_image, (750, 200))
                if show_green_cama1_flicker == False:
                    a1_button.x = 900
                    a1_on_button.x = 11900
                if show_green_cama2_flicker == False:
                    a2_button.x = 870
                    a2_on_button.x = 11870
                if show_green_camb2_flicker == False:
                    b2_button.x = 870
                    b2_on_button.x = 11870
                if show_green_camc1_flicker == False:
                    c1_button.x = 850
                    c1_on_button.x = 11850
                if show_green_camb1_flicker == False:
                    b1_button.x = 890
                    b1_on_button.x = 11890
                if show_green_cama7_flicker == False:
                    a7_button.x = 1140
                    a7_on_button.x = 111140
                if show_green_cama6_flicker == False:
                    a6_button.x = 1130
                    a6_on_button.x = 111130
                if show_green_cama5_flicker == False:
                    a5_button.x = 730
                    a5_on_button.x = 11730
                if show_green_cama3_flicker == False:
                    a3_button.x = 740
                    a3_on_button.x = 11740
                if show_green_camb4_flicker == False:
                    b4_button.x = 1030
                    b4_on_button.x = 111030
                if show_green_cama4_flicker == False:
                    a4_button.x = 1030
                    a4_on_button.x = 111030
                if show_green_cama2_flicker == True:
                    a2_button.x = 11870
                    a2_on_button.x = 870
                if cama2_active == False:
                    a2_button.x = 870
                if show_green_camb2_flicker == True:
                    b2_button.x = 11870
                    b2_on_button.x = 870
                if camb2_active == False:
                    b2_button.x = 870
                if show_green_camc1_flicker == True:
                    c1_button.x = 11850
                    c1_on_button.x = 850
                if camc1_active == False:
                    c1_button.x = 850
                if show_green_camb1_flicker == True:
                    b1_button.x = 11890
                    b1_on_button.x = 890
                if camb1_active == False:
                    b1_button.x = 890
                if show_green_cama1_flicker == True:
                    a1_button.x = 11900
                    a1_on_button.x = 900
                if cama1_active == False:
                    a1_button.x = 900
                if show_green_cama7_flicker == True:
                    a7_button.x = 111140
                    a7_on_button.x = 1140
                if cama7_active == False:
                    a7_button.x = 1140
                if show_green_cama6_flicker == True:
                    a6_button.x = 111130
                    a6_on_button.x = 1130
                if cama6_active == False:
                    a6_button.x = 1130
                if show_green_cama5_flicker == True:
                    a5_button.x = 11730
                    a5_on_button.x = 730
                if cama5_active == False:
                    a5_button.x = 730
                if show_green_cama3_flicker == True:
                    a3_button.x = 11740
                    a3_on_button.x = 740
                if cama3_active == False:
                    a3_button.x = 740
                if show_green_camb4_flicker == True:
                    b4_button.x = 111030
                    b4_on_button.x = 1030
                if camb4_active == False:
                    b4_button.x = 1030
                if show_green_cama4_flicker == True:
                    a4_button.x = 111030
                    a4_on_button.x = 1030
                if cama4_active == False:
                    a4_button.x = 1030
                window.blit(a2_on_button.image, (a2_on_button.x, a2_on_button.y))
                window.blit(b2_on_button.image, (b2_on_button.x, b2_on_button.y))
                window.blit(a4_on_button.image, (a4_on_button.x, a4_on_button.y))
                window.blit(b4_on_button.image, (b4_on_button.x, b4_on_button.y))
                window.blit(a3_on_button.image, (a3_on_button.x, a3_on_button.y))
                window.blit(a5_on_button.image, (a5_on_button.x, a5_on_button.y))
                window.blit(a6_on_button.image, (a6_on_button.x, a6_on_button.y))
                window.blit(a7_on_button.image, (a7_on_button.x, a7_on_button.y))
                window.blit(a1_on_button.image, (a1_on_button.x, a1_on_button.y))
                window.blit(b1_on_button.image, (b1_on_button.x, b1_on_button.y))
                window.blit(c1_on_button.image, (c1_on_button.x, c1_on_button.y))
                
                window.blit(a2_button.image, (a2_button.x, a2_button.y))           
                window.blit(b2_button.image, (b2_button.x, b2_button.y))             
                window.blit(a4_button.image, (a4_button.x, a4_button.y))              
                window.blit(b4_button.image, (b4_button.x, b4_button.y))              
                window.blit(a3_button.image, (a3_button.x, a3_button.y))  
                window.blit(a5_button.image, (a5_button.x, a5_button.y))               
                window.blit(a6_button.image, (a6_button.x, a6_button.y))    
                window.blit(a7_button.image, (a7_button.x, a7_button.y))             
                window.blit(a1_button.image, (a1_button.x, a1_button.y))             
                window.blit(b1_button.image, (b1_button.x, b1_button.y)) 
                window.blit(c1_button.image, (c1_button.x, c1_button.y))
                window.blit(camera_button2.image, (camera_button2.x, camera_button2.y))
            if show_left_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_left_light == True and show_camera == False:
                window.blit(left_light.image, (left_light.x, left_light.y))
            if show_left_light == True and show_bon == True and show_camera == False:
                window.blit(bon.image, (bon.x, bon.y))
            if show_right_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_right_light == True and show_camera == False:
                window.blit(right_light.image, (right_light.x, right_light.y))
            if show_left_door == True:
                power_number -= 0.002
                window.blit(yellow_bar_image, (150, 670))
            if show_left_door == True and show_camera == False:
                window.blit(left_door.image, (left_door.x, left_door.y))
            if show_right_door == True:
                power_number -= 0.002
                window.blit(red_bar_image, (175, 670))
            if show_right_door == True and show_camera == False:
                window.blit(right_door.image, (right_door.x, right_door.y))
            if show_right_door == False and show_left_door == False and show_right_light == False and show_left_light == False and show_camera == False:
                power_number -= 0
            window.blit(green_bar_image, (100, 670))
            power_number -= 0.0008
        if power_out == True and show_power_out_fred == True and power_out_fred_active == True:
            window.blit(fred_power_out_image, (bon.x, bon.y))

        if jumpscare_end_fred == True:
            fred_image = pygame.transform.scale(fred_image, (2500, 1000))
            window.blit(fred_image, (bon.x, chic.y))

        if show_camera == False:
            window.blit(door_button2.image, (door_button2.x, door_button2.y))
            window.blit(door_button.image, (door_button.x, door_button.y))
            window.blit(door_button_on2.image, (door_button_on2.x, door_button_on2.y))
            window.blit(door_button_on.image, (door_button_on.x, door_button_on.y))

            window.blit(light_button2.image, (light_button2.x, light_button2.y))
            window.blit(light_button.image, (light_button.x, light_button.y))
            window.blit(light_button_on2.image, (light_button_on2.x, light_button_on2.y))
            window.blit(light_button_on.image, (light_button_on.x, light_button_on.y))

            office_bg_image.blit(Light_text, (50, 500))
            office_bg_image.blit(Light_text, (2150, 500))
            office_bg_image.blit(Door_text, (50, 350))
            office_bg_image.blit(Door_text, (2150, 350))
        if power_out == False:
            window.blit(AM_text, (1150, 0))
            window.blit(Night_text, (1150, 50))
            window.blit(Usage_text, (0, 660))
            window.blit(Power_left_text, (0, 600))
            window.blit(Power_number_text, (160, 590))
        pygame.display.update()

def night4():
    
    phoneguy_night4.play()
    sec = 0
    sec_power = 0
    sec_chic = 0
    sec_fox = 0
    sec_fred = 0
    sec_call = 0
    camera_area_text1 = "W. Hall Corner"

    fred_image = pygame.image.load(os.path.join('Images', 'animatronics', 'fred.png'))

    pirate_cove_image2 = pirate_cove_image
    show_stage_image2 = show_stage_image
    w_hall_corner_image2 = w_hall_corner_image
    w_hall_image2 = w_hall_image
    supply_closet_image2 = supply_closet_image
    restrooms_image2 = restrooms_image
    e_hall_corner_image2 = e_hall_corner_image
    e_hall_image2 = e_hall_image
    dining_area_image2 = dining_area_image
    backstage_image2 = backstage_image

    bon_ai_number = 2
    fox_ai_number = 6
    chic_ai_number = 4
    fred_ai_number = random.randint(1, 2)

    move_delay = 250  # milliseconds
    move_delay_camera = 450  # milliseconds
    last_move_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    light_button = button(1850, 400, 100, 100, light_button_image)
    light_button2 = button(-250, 400, 100, 100, light_button_image)
    light_button_on = button(8150, 400, 100, 100, light_button_on_image)
    light_button_on2 = button(8150, 400, 100, 100, light_button_on_image)
    door_button = button(1850, 250, 100, 100, door_button_image)
    door_button2 = button(-250, 250, 100, 100, door_button_image)
    door_button_on = button(8150, 250, 100, 100, door_button_on_image)
    door_button_on2 = button(8150, 250, 100, 100, door_button_on_image)
    left_light = button(-100, 30, 200, 700, left_light_image)
    right_light = button(1600, 30, 200, 700, right_light_image)
    left_door = button(-100, 30, 200, 700, left_door_image)
    right_door = button(1600, 30, 200, 700, right_door_image)
    bon = button(-100, 30, 500, 700, bon_image)
    chic = button(1300, 10, 200, 550, chic_image)
    camera_button = button(300, 650, 500, 50, camera_button_image)
    camera_button2 = button(21500, 650, 500, 50, camera_button_image)
    a2_button = button(870, 550, 95, 65, a2_image)
    a2_on_button = button(11870, 550, 95, 65, a2_on_image)
    b2_button = button(870, 615, 95, 65, b2_image)
    b2_on_button = button(11870, 615, 95, 65, b2_on_image)
    a4_button = button(1030, 550, 95, 65, a4_image)
    a4_on_button = button(111030, 550, 95, 65, a4_on_image)
    b4_button = button(1030, 615, 95, 65, b4_image)
    b4_on_button = button(111030, 615, 95, 65, b4_on_image)
    a3_button = button(740, 500, 95, 65, a3_image)
    a3_on_button = button(11740, 500, 95, 65, a3_on_image)
    a5_button = button(730, 330, 95, 65, a5_image)
    a5_on_button = button(11730, 330, 95, 65, a5_on_image)
    a6_button = button(1130, 500, 95, 65, a6_image)
    a6_on_button = button(111130, 500, 95, 65, a6_on_image)
    a7_button = button(1140, 300, 95, 65, a7_image)
    a7_on_button = button(111140, 300, 95, 65, a7_on_image)
    a1_button = button(900, 200, 95, 65, a1_image)
    a1_on_button = button(11900, 200, 95, 65, a1_on_image)
    b1_button = button(890, 300, 95, 65, b1_image)
    b1_on_button = button(11890, 300, 95, 65, b1_on_image)
    c1_button = button(850, 400, 95, 65, c1_image)
    c1_on_button = button(11850, 400, 95, 65, c1_on_image)
    camera_area = button(-300, 0, 2250, 720, pirate_cove_image)
    boop_button = button(650, 150, 10, 10, boop_image)
    mute_call_button = button(0, 0, 300, 60, mute_call_image)
    
    officex = -300
    camerax = -300
    last_event_time = time.time()
    event_interval = 5  # Time interval in seconds

    flicker_interval = 500  # milliseconds
    last_flicker_time = pygame.time.get_ticks()
    show_power_out_fred = True

    update_pirate_cove = True
    update_backstage = True
    update_dining_area = True
    update_e_hall = True
    update_e_hall_corner = True
    update_restrooms = True
    update_show_stage = True
    update_supply_closet = True
    update_w_hall = True
    update_w_hall_corner = True

    stop_left = True
    stop_right = True
    show_left_light = False
    show_right_light = False
    show_left_door = False
    show_right_door = False
    show_bon = False
    show_chic = False
    show_camera = False
    jumpscare_end = False
    jumpscare_end_chic = False
    jumpscare_end_fox = False
    jumpscare_end_fred = False
    power_out = False
    power_out_fred_active = False
    cama2_active = False
    camb2_active = True
    cama4_active = False
    camb4_active = False
    cama3_active = False
    cama5_active = False
    cama6_active = False
    cama7_active = False
    cama1_active = False
    camb1_active = False
    camc1_active = False
    show_green_cama2_flicker = False
    show_green_camb2_flicker = False
    show_green_cama4_flicker = False
    show_green_camb4_flicker = False
    show_green_cama3_flicker = False
    show_green_cama5_flicker = False
    show_green_cama6_flicker = False
    show_green_cama7_flicker = False
    show_green_cama1_flicker = False
    show_green_camb1_flicker = False
    show_green_camc1_flicker = False
    mute_call = False

    night_number = 4
    am_number = 12
    power_number = 100
    sec_number = 0
    sec_number2 = 0
    sec_number3 = 0
    sec_number4 = 0
    sec_number5 = 0
    sec_fred_move = 0
    sec_fox_move = 0

    pirate_cove_stage_number = 1
    bonnie_stage_number = 1
    chica_stage_number = 1
    fred_stage_number = 1
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'night.json'),'w') as night:
                    json.dump(data_night, night)
                run = False
                pygame.quit()
            current_time = pygame.time.get_ticks()

            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
                camera_button_rect = pygame.Rect(camera_button.x, camera_button.y, camera_button.width, camera_button.height)
                camera_button2_rect = pygame.Rect(camera_button2.x, camera_button2.y, camera_button2.width, camera_button2.height)
                if mousex < 400:
                    stop_left = False
                elif mousex > 900:
                    stop_right = False
                else:
                    stop_left = True
                    stop_right = True
                if power_out == False:
                    if camera_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 21500
                        camera_button2.x = 300
                        show_camera = True
                        last_move_time = current_time
                    if camera_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 300
                        camera_button2.x = 21500
                        show_camera = False
                        last_move_time = current_time
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                mute_call_button_rect = pygame.Rect(mute_call_button.x, mute_call_button.y, mute_call_button.width, mute_call_button.height)
                light_button_rect = pygame.Rect(light_button.x, light_button.y, light_button.width, light_button.height)
                light_button2_rect = pygame.Rect(light_button2.x, light_button2.y, light_button2.width, light_button2.height)
                light_button_on_rect = pygame.Rect(light_button_on.x, light_button_on.y, light_button_on.width, light_button_on.height)
                light_button_on2_rect = pygame.Rect(light_button_on2.x, light_button_on2.y, light_button_on2.width, light_button_on2.height)
                door_button_rect = pygame.Rect(door_button.x, door_button.y, door_button.width, door_button.height)
                door_button2_rect = pygame.Rect(door_button2.x, door_button2.y, door_button2.width, door_button2.height)
                door_button_on_rect = pygame.Rect(door_button_on.x, door_button_on.y, door_button_on.width, door_button_on.height)
                door_button_on2_rect = pygame.Rect(door_button_on2.x, door_button_on2.y, door_button_on2.width, door_button_on2.height)

                boop_button_rect = pygame.Rect(boop_button.x, boop_button.y, boop_button.width, boop_button.height)

                a2_button_rect = pygame.Rect(a2_button.x, a2_button.y, a2_button.width, a2_button.height)
                b2_button_rect = pygame.Rect(b2_button.x, b2_button.y, b2_button.width, b2_button.height)
                a4_button_rect = pygame.Rect(a4_button.x, a4_button.y, a4_button.width, a4_button.height)
                b4_button_rect = pygame.Rect(b4_button.x, b4_button.y, b4_button.width, b4_button.height)
                a3_button_rect = pygame.Rect(a3_button.x, a3_button.y, a3_button.width, a3_button.height)
                a5_button_rect = pygame.Rect(a5_button.x, a5_button.y, a5_button.width, a5_button.height)
                a6_button_rect = pygame.Rect(a6_button.x, a6_button.y, a6_button.width, a6_button.height)
                a7_button_rect = pygame.Rect(a7_button.x, a7_button.y, a7_button.width, a7_button.height)
                a1_button_rect = pygame.Rect(a1_button.x, a1_button.y, a1_button.width, a1_button.height)
                b1_button_rect = pygame.Rect(b1_button.x, b1_button.y, b1_button.width, b1_button.height)
                c1_button_rect = pygame.Rect(c1_button.x, c1_button.y, c1_button.width, c1_button.height)

                if show_camera == False and power_out == False:
                    if mute_call_button_rect.collidepoint(mousex, mousey):
                        mute_call = True
                        mute_call_button.x = -1000000

                    if door_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_right_door = True
                        door_button_on.x = 1180
                        door_button.x = 8150
                        last_move_time = current_time
                    if door_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_left_door = True
                        door_button_on2.x = 50
                        door_button2.x = 8150
                        last_move_time = current_time
                    if door_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_right_door = False
                        door_button_on.x = 8150
                        door_button.x = 1180
                        last_move_time = current_time
                    if door_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_left_door = False
                        door_button_on2.x = 8150
                        door_button2.x = 50
                        last_move_time = current_time

                    if light_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_right_light = True
                        light_button_on.x = 1180
                        light_button.x = 8150
                        last_move_time = current_time
                    if light_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_left_light = True
                        light_button_on2.x = 50
                        light_button2.x = 8150
                        last_move_time = current_time
                    if light_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_right_light = False
                        light_button_on.x = 8150
                        light_button.x = 1180
                        last_move_time = current_time
                    if light_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_left_light = False
                        light_button_on2.x = 8150
                        light_button2.x = 50
                        last_move_time = current_time
                if show_camera == False:
                    if boop_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        boop_sound.play()
                        last_move_time = current_time
                if show_camera == True:
                    if a2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama2_active = True
                        camb2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "West Hall"
                        update_w_hall = True
                        update_pirate_cove = False
                        update_w_hall_corner = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_image2
                        last_move_time = current_time
                    if b2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb2_active = True
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "W. Hall Corner"
                        update_w_hall_corner = True
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_corner_image2
                        last_move_time = current_time
                    if a4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama4_active = True
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_e_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "East Hall"
                        update_e_hall = True
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_image2
                        last_move_time = current_time
                    if b4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb4_active = True
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_e_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "E. Hall Corner"
                        update_e_hall_corner = True
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_corner_image2
                        last_move_time = current_time
                    if a3_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama3_active = True
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_supply_closet == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Supply Closet"
                        update_supply_closet = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        camera_area.image = supply_closet_image2
                        last_move_time = current_time
                    if a5_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama5_active = True
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_backstage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Backstage"
                        update_backstage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = backstage_image2
                        last_move_time = current_time
                    if a6_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        if cama6_active == False:
                            change_camera_sound.play()
                        cama6_active = True
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        camera_area_text1 = "Kitchen"
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = kitchen_image
                        last_move_time = current_time
                    if a7_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama7_active = True
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_restrooms == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Restrooms"
                        update_restrooms = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = restrooms_image2
                        last_move_time = current_time
                    if a1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama1_active = True
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_show_stage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Show Stage"
                        update_show_stage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_supply_closet = False
                        camera_area.image = show_stage_image2
                        last_move_time = current_time
                    if b1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb1_active = True
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camc1_active = False
                        if update_dining_area == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Dining Area"
                        update_dining_area = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = dining_area_image2
                        last_move_time = current_time
                    if c1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camc1_active = True
                        camb1_active = False
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        if update_pirate_cove == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Pirates Cove"
                        update_pirate_cove = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = pirate_cove_image2
                        
                        last_move_time = current_time
        if power_out == True:
            sec_power += 1
        if sec_power == 420:
            music_box.play()
            power_out_fred_active = True
        if sec_power == 1320:
            power_out_fred_active = False
        if sec_power == 1500:
            jumpscare_sound.play() 
            jumpscare_end_fred = True
            stop_left = True
            stop_right = True
            show_camera = False
        sec_call += 1
        sec_fred_move += 1
        sec_fox_move += 1
        current_time3 = pygame.time.get_ticks()
        # Check if it's time to flicker
        if current_time3 - last_flicker_time >= flicker_interval and power_out_fred_active == True:
            show_power_out_fred = not show_power_out_fred  # Toggle visibility
            last_flicker_time = current_time3

        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama2_active == True:
            show_green_cama2_flicker = not show_green_cama2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb2_active == True:
            show_green_camb2_flicker = not show_green_camb2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama4_active == True:
            show_green_cama4_flicker = not show_green_cama4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb4_active == True:
            show_green_camb4_flicker = not show_green_camb4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama3_active == True:
            show_green_cama3_flicker = not show_green_cama3_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama5_active == True:
            show_green_cama5_flicker = not show_green_cama5_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama6_active == True:
            show_green_cama6_flicker = not show_green_cama6_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama7_active == True:
            show_green_cama7_flicker = not show_green_cama7_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama1_active == True:
            show_green_cama1_flicker = not show_green_cama1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb1_active == True:
            show_green_camb1_flicker = not show_green_camb1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camc1_active == True:
            show_green_camc1_flicker = not show_green_camc1_flicker  # Toggle visibility
            last_flicker_time = current_time3

        current_time2 = time.time()
        if current_time2 - last_event_time >= event_interval and power_out == False:
            sec_number3 += 1   
            rng = random.randint(1, 20)
            print(rng)
            #freddy fazbear
            if show_camera == False:
                sec_fred_move = 0
                if fred_ai_number >= rng and sec_fred_move >= 1000 - 100 * fred_ai_number:
                    fred_stage_number += 1
                    print("Fred Stage INCREASED!!!!!!!")
                    if fred_stage_number == 1 and chica_stage_number == 1 and bonnie_stage_number == 1:
                        show_stage_image2 = show_stage_image
                    if fred_stage_number == 2:
                        show_stage_image2 = show_stage_stage4_image
                    if fred_stage_number >= 6:
                        e_hall_corner_image2 = e_hall_corner_stage3_image
            if camera_area.image != e_hall_corner_image2 and show_right_door == False and fred_stage_number >= 6:
                jumpscare_end_fred = True
                jumpscare_sound.play()
                stop_left = True
                stop_right = True
                show_camera = False
            if camera_area.image != e_hall_corner_image2 and show_right_door == True and fred_stage_number >= 6:
                e_hall_corner_image2 = e_hall_corner_image
                fred_stage_number = 5
                    
            #foxy
            if show_camera == False and sec_fox_move >= random.randint(50, 1000):
                sec_fox_move = 0
                if fox_ai_number >= rng:
                    pirate_cove_stage_number += 1
                    print("fox stage increased!")
                    if pirate_cove_stage_number == 1:
                        pirate_cove_image2 = pirate_cove_image
                        
                    if pirate_cove_image2 == pirate_cove_image and pirate_cove_stage_number == 2:
                        pirate_cove_image2 = pirate_cove_stage2_image    

                    if pirate_cove_image2 == pirate_cove_stage2_image and pirate_cove_stage_number == 3:
                        pirate_cove_image2 = pirate_cove_stage3_image
                        
                    if pirate_cove_image2 == pirate_cove_stage3_image and pirate_cove_stage_number == 4:
                        sec_number3 = 0
                        pirate_cove_image2 = pirate_cove_stage4_image
                    
            
            
            if fox_ai_number >= rng:   
                if sec_number3 == 5 and show_left_door == True or camera_area.image == w_hall_image2 and show_left_door == True:
                    play_next_sound()
                    power_number -= 1
                    pirate_cove_image2 = pirate_cove_image
                    sec_number3 = 0
                    pirate_cove_stage_number = 1
                if sec_number3 == 5 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image or camera_area.image == w_hall_image2 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image:
                    jumpscare_end_fox = True
                    jumpscare_sound.play()
                    stop_left = True
                    stop_right = True
                    show_camera = False
                
            #bonnie
            if bon_ai_number >= rng:
                bonnie_stage_number += 1
                print("bonnie stage increased!")
                if bonnie_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if bonnie_stage_number == 2:
                    show_stage_image2 = show_stage_stage2_image
                    dining_area_image2 = dining_area_stage2_image
                if bonnie_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    backstage_image2 = backstage_stage2_image
                if bonnie_stage_number == 4:
                    backstage_image2 = backstage_image
                    w_hall_image2 = w_hall_stage2_image
                if bonnie_stage_number == 5:
                    w_hall_image2 = w_hall_image
                    supply_closet_image2 = supply_closet_stage2_image
                if bonnie_stage_number == 6:
                    loud_footsteps_sound.play()
                    supply_closet_image2 = supply_closet_image
                    w_hall_corner_image2 = w_hall_corner_stage2_image
                if bonnie_stage_number >= 7:
                    w_hall_corner_image2 = w_hall_corner_image
                    show_bon = True

            if bon_ai_number >= rng and show_left_door == True and show_bon == True:
                show_bon = False
                quiet_footsteps_sound.play()
                bonnie_stage_number = 2
                sec_number2 = 0
            if bon_ai_number < rng:
                print("bonnie failed to move")
            if show_bon == True and show_left_light == True and show_camera == False:
                jump_sound.play()
            if show_bon == True and show_left_door == False:
                sec_number2 += 1
            if sec_number2 >= 2 and show_left_door == False and bon_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end = True
                show_bon = True
                show_left_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                bon.image = pygame.transform.scale(bon.image, (5000, 1000))
                
            
            #chica
            if chic_ai_number >= rng:
                chica_stage_number += 1
                print("Chica Stage Increased!!!")
                if chica_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if chica_stage_number == 2:
                    show_stage_image2 = show_stage_stage3_image
                    dining_area_image2 = dining_area_stage3_image
                if chica_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    restrooms_image2 = restrooms_stage2_image
                if chica_stage_number == 4:
                    restrooms_image2 = restrooms_image
                if chica_stage_number == 5:
                    e_hall_image2 = e_hall_stage2_image
                if chica_stage_number == 6:
                    loud_footsteps_sound.play()
                    e_hall_image2 = e_hall_image
                    e_hall_corner_image2 = e_hall_corner_stage2_image
                if chica_stage_number == 7:
                    e_hall_corner_image2 = e_hall_corner_image
                    show_chic = True

            if chic_ai_number >= rng and show_right_door == True and show_chic == True:
                show_chic = False
                quiet_footsteps_sound.play()
                chica_stage_number = 2
                sec_number4 = 0
            if chic_ai_number < rng:
                print("chica failed to move")
            if show_chic == True and show_right_light == True and show_camera == False:
                jump_sound.play()
            if show_chic == True and show_right_door == False:
                sec_number4 += 1
            if sec_number4 >= 2 and show_right_door == False and chic_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end_chic = True
                show_chic = True
                show_right_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                chic.image = pygame.transform.scale(chic.image, (2500, 1000))
                chic.x = bon.x

            last_event_time = current_time2

        if jumpscare_end == True:
            sec += 1
            phoneguy_night1.stop()
            show_bon = True
            show_left_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec >= 70:
            mainmenu()
        
        if jumpscare_end_chic == True:
            sec_chic += 1
            phoneguy_night1.stop()
            show_chic = True
            show_right_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_chic >= 70:
            mainmenu()
        
        if jumpscare_end_fox == True:
            sec_fox += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fox >= 140:
            mainmenu()

        if jumpscare_end_fred == True:
            sec_fred += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fred >= 70:
            mainmenu()
        
        if mute_call == True:
            phoneguy_night4.set_volume(0.00)

        if sec_call >= 1380:
            mute_call_button.x = -100000

        if show_camera == True and update_pirate_cove == True:
            camera_area.image = pirate_cove_image2

        if show_camera == True and update_backstage == True:
            camera_area.image = backstage_image2

        if show_camera == True and update_dining_area == True:
            camera_area.image = dining_area_image2

        if show_camera == True and update_e_hall == True:
            camera_area.image = e_hall_image2

        if show_camera == True and update_e_hall_corner == True:
            camera_area.image = e_hall_corner_image2

        if show_camera == True and update_restrooms == True:
            camera_area.image = restrooms_image2

        if show_camera == True and update_show_stage == True:
            camera_area.image = show_stage_image2

        if show_camera == True and update_supply_closet == True:
            camera_area.image = supply_closet_image2
        
        if show_camera == True and update_w_hall == True:
            camera_area.image = w_hall_image2
        
        if show_camera == True and update_w_hall_corner == True:
            camera_area.image = w_hall_corner_image2
            

        if stop_left == False and camerax < -100:
            camerax += 10
            
        if stop_right == False and camerax > -500:
            camerax -= 10

        if stop_left == False and officex < -5:
            officex += 10
            boop_button.x += 10
            left_light.x += 10
            right_light.x += 10
            left_door.x += 10
            right_door.x += 10
            bon.x += 10
            chic.x += 10
            light_button.x += 10
            light_button2.x += 10
            light_button_on.x += 10
            light_button_on2.x += 10
            door_button.x += 10
            door_button2.x += 10
            door_button_on.x += 10
            door_button_on2.x += 10
        if stop_right == False and officex > -970:
            officex -= 10
            boop_button.x -= 10
            left_light.x -= 10
            right_light.x -= 10
            left_door.x -= 10
            right_door.x -= 10
            bon.x -= 10
            chic.x -= 10
            light_button.x -= 10
            light_button2.x -= 10
            light_button_on.x -= 10
            light_button_on2.x -= 10
            door_button.x -= 10
            door_button2.x -= 10
            door_button_on.x -= 10
            door_button_on2.x -= 10

        sec_number5 += 1
        if sec_number5 >= 240:
            power_number -= 1
            sec_number5 = 0

        sec_number+=1
        if sec_number == 5400:
            am_number = 1
        if sec_number == 10800:
            bon_ai_number += 1
            am_number = 2
        if sec_number == 16200:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 3
        if sec_number == 21600:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 4
        if sec_number == 27000:
            am_number = 5
        if sec_number == 32400:
            power_out = False
            data_night['night_number'] = 5
            with open(os.path.join('data', 'night.json'),'w') as night:
                json.dump(data_night, night)
            win6am()

        if power_number <= 0:
            power_out = True

        if power_out == False:
            Usage_text = Small_Font.render("Usage:", 1, WHITE)
            Power_left_text = Small_Font.render("Power left:", 1, WHITE)
            Night_text = Small_Font.render("Night " + str(int(night_number)), 1, WHITE)
            AM_text = Big_Font.render(str(int(am_number)) + " AM", 1, WHITE)
            Power_number_text = Big_Font.render(str(int(power_number)) + "%", 1, WHITE)
        Light_text = Small_Font.render("LIGHT", 1, WHITE)
        Door_text = Small_Font.render("DOOR", 1, WHITE)
        if power_out == False:
            camera_area_text = Big_Font.render(camera_area_text1, 1, WHITE)
        window.fill((0, 0, 0))
        if power_out == False:
            if show_right_light == True and show_chic == True and show_camera == False:
                window.blit(chic.image, (chic.x, chic.y))
        window.blit(office_bg_image, (officex, 0))
        window.blit(boop_button.image, (boop_button.x, boop_button.y))
        window.blit(mute_call_button.image, (mute_call_button.x, mute_call_button.y))
        if power_out == False:
            window.blit(camera_button.image, (camera_button.x, camera_button.y))
        if power_out == False:
            if jumpscare_end_chic == True:
                window.blit(chic.image, (chic.x, chic.y))
            if jumpscare_end_fox == True:
                window.blit(fox_image, (bon.x + 100, chic.y))
            if show_camera == True:
                power_number -= 0.0008
                window.blit(camera_area.image, (camerax, camera_area.y))
                window.blit(camera_area_text, (735, 130))
                window.blit(green_bar_image, (125, 670))
                window.blit(map_image, (750, 200))
                if show_green_cama1_flicker == False:
                    a1_button.x = 900
                    a1_on_button.x = 11900
                if show_green_cama2_flicker == False:
                    a2_button.x = 870
                    a2_on_button.x = 11870
                if show_green_camb2_flicker == False:
                    b2_button.x = 870
                    b2_on_button.x = 11870
                if show_green_camc1_flicker == False:
                    c1_button.x = 850
                    c1_on_button.x = 11850
                if show_green_camb1_flicker == False:
                    b1_button.x = 890
                    b1_on_button.x = 11890
                if show_green_cama7_flicker == False:
                    a7_button.x = 1140
                    a7_on_button.x = 111140
                if show_green_cama6_flicker == False:
                    a6_button.x = 1130
                    a6_on_button.x = 111130
                if show_green_cama5_flicker == False:
                    a5_button.x = 730
                    a5_on_button.x = 11730
                if show_green_cama3_flicker == False:
                    a3_button.x = 740
                    a3_on_button.x = 11740
                if show_green_camb4_flicker == False:
                    b4_button.x = 1030
                    b4_on_button.x = 111030
                if show_green_cama4_flicker == False:
                    a4_button.x = 1030
                    a4_on_button.x = 111030
                if show_green_cama2_flicker == True:
                    a2_button.x = 11870
                    a2_on_button.x = 870
                if cama2_active == False:
                    a2_button.x = 870
                if show_green_camb2_flicker == True:
                    b2_button.x = 11870
                    b2_on_button.x = 870
                if camb2_active == False:
                    b2_button.x = 870
                if show_green_camc1_flicker == True:
                    c1_button.x = 11850
                    c1_on_button.x = 850
                if camc1_active == False:
                    c1_button.x = 850
                if show_green_camb1_flicker == True:
                    b1_button.x = 11890
                    b1_on_button.x = 890
                if camb1_active == False:
                    b1_button.x = 890
                if show_green_cama1_flicker == True:
                    a1_button.x = 11900
                    a1_on_button.x = 900
                if cama1_active == False:
                    a1_button.x = 900
                if show_green_cama7_flicker == True:
                    a7_button.x = 111140
                    a7_on_button.x = 1140
                if cama7_active == False:
                    a7_button.x = 1140
                if show_green_cama6_flicker == True:
                    a6_button.x = 111130
                    a6_on_button.x = 1130
                if cama6_active == False:
                    a6_button.x = 1130
                if show_green_cama5_flicker == True:
                    a5_button.x = 11730
                    a5_on_button.x = 730
                if cama5_active == False:
                    a5_button.x = 730
                if show_green_cama3_flicker == True:
                    a3_button.x = 11740
                    a3_on_button.x = 740
                if cama3_active == False:
                    a3_button.x = 740
                if show_green_camb4_flicker == True:
                    b4_button.x = 111030
                    b4_on_button.x = 1030
                if camb4_active == False:
                    b4_button.x = 1030
                if show_green_cama4_flicker == True:
                    a4_button.x = 111030
                    a4_on_button.x = 1030
                if cama4_active == False:
                    a4_button.x = 1030
                window.blit(a2_on_button.image, (a2_on_button.x, a2_on_button.y))
                window.blit(b2_on_button.image, (b2_on_button.x, b2_on_button.y))
                window.blit(a4_on_button.image, (a4_on_button.x, a4_on_button.y))
                window.blit(b4_on_button.image, (b4_on_button.x, b4_on_button.y))
                window.blit(a3_on_button.image, (a3_on_button.x, a3_on_button.y))
                window.blit(a5_on_button.image, (a5_on_button.x, a5_on_button.y))
                window.blit(a6_on_button.image, (a6_on_button.x, a6_on_button.y))
                window.blit(a7_on_button.image, (a7_on_button.x, a7_on_button.y))
                window.blit(a1_on_button.image, (a1_on_button.x, a1_on_button.y))
                window.blit(b1_on_button.image, (b1_on_button.x, b1_on_button.y))
                window.blit(c1_on_button.image, (c1_on_button.x, c1_on_button.y))
                
                window.blit(a2_button.image, (a2_button.x, a2_button.y))           
                window.blit(b2_button.image, (b2_button.x, b2_button.y))             
                window.blit(a4_button.image, (a4_button.x, a4_button.y))              
                window.blit(b4_button.image, (b4_button.x, b4_button.y))              
                window.blit(a3_button.image, (a3_button.x, a3_button.y))  
                window.blit(a5_button.image, (a5_button.x, a5_button.y))               
                window.blit(a6_button.image, (a6_button.x, a6_button.y))    
                window.blit(a7_button.image, (a7_button.x, a7_button.y))             
                window.blit(a1_button.image, (a1_button.x, a1_button.y))             
                window.blit(b1_button.image, (b1_button.x, b1_button.y)) 
                window.blit(c1_button.image, (c1_button.x, c1_button.y))
                window.blit(camera_button2.image, (camera_button2.x, camera_button2.y))
            if show_left_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_left_light == True and show_camera == False:
                window.blit(left_light.image, (left_light.x, left_light.y))
            if show_left_light == True and show_bon == True and show_camera == False:
                window.blit(bon.image, (bon.x, bon.y))
            if show_right_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_right_light == True and show_camera == False:
                window.blit(right_light.image, (right_light.x, right_light.y))
            if show_left_door == True:
                power_number -= 0.002
                window.blit(yellow_bar_image, (150, 670))
            if show_left_door == True and show_camera == False:
                window.blit(left_door.image, (left_door.x, left_door.y))
            if show_right_door == True:
                power_number -= 0.002
                window.blit(red_bar_image, (175, 670))
            if show_right_door == True and show_camera == False:
                window.blit(right_door.image, (right_door.x, right_door.y))
            if show_right_door == False and show_left_door == False and show_right_light == False and show_left_light == False and show_camera == False:
                power_number -= 0
            window.blit(green_bar_image, (100, 670))
            power_number -= 0.0008
        if power_out == True and show_power_out_fred == True and power_out_fred_active == True:
            window.blit(fred_power_out_image, (bon.x, bon.y))

        if jumpscare_end_fred == True:
            fred_image = pygame.transform.scale(fred_image, (2500, 1000))
            window.blit(fred_image, (bon.x, chic.y))

        if show_camera == False:
            window.blit(door_button2.image, (door_button2.x, door_button2.y))
            window.blit(door_button.image, (door_button.x, door_button.y))
            window.blit(door_button_on2.image, (door_button_on2.x, door_button_on2.y))
            window.blit(door_button_on.image, (door_button_on.x, door_button_on.y))

            window.blit(light_button2.image, (light_button2.x, light_button2.y))
            window.blit(light_button.image, (light_button.x, light_button.y))
            window.blit(light_button_on2.image, (light_button_on2.x, light_button_on2.y))
            window.blit(light_button_on.image, (light_button_on.x, light_button_on.y))

            office_bg_image.blit(Light_text, (50, 500))
            office_bg_image.blit(Light_text, (2150, 500))
            office_bg_image.blit(Door_text, (50, 350))
            office_bg_image.blit(Door_text, (2150, 350))
        if power_out == False:
            window.blit(AM_text, (1150, 0))
            window.blit(Night_text, (1150, 50))
            window.blit(Usage_text, (0, 660))
            window.blit(Power_left_text, (0, 600))
            window.blit(Power_number_text, (160, 590))
        pygame.display.update()
def night5():
    
    sec = 0
    sec_power = 0
    sec_chic = 0
    sec_fox = 0
    sec_fred = 0
    camera_area_text1 = "W. Hall Corner"

    fred_image = pygame.image.load(os.path.join('Images', 'animatronics', 'fred.png'))

    pirate_cove_image2 = pirate_cove_image
    show_stage_image2 = show_stage_image
    w_hall_corner_image2 = w_hall_corner_image
    w_hall_image2 = w_hall_image
    supply_closet_image2 = supply_closet_image
    restrooms_image2 = restrooms_image
    e_hall_corner_image2 = e_hall_corner_image
    e_hall_image2 = e_hall_image
    dining_area_image2 = dining_area_image
    backstage_image2 = backstage_image

    bon_ai_number = 5
    fox_ai_number = 5
    chic_ai_number = 7
    fred_ai_number = 3

    move_delay = 250  # milliseconds
    move_delay_camera = 450  # milliseconds
    last_move_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    light_button = button(1850, 400, 100, 100, light_button_image)
    light_button2 = button(-250, 400, 100, 100, light_button_image)
    light_button_on = button(8150, 400, 100, 100, light_button_on_image)
    light_button_on2 = button(8150, 400, 100, 100, light_button_on_image)
    door_button = button(1850, 250, 100, 100, door_button_image)
    door_button2 = button(-250, 250, 100, 100, door_button_image)
    door_button_on = button(8150, 250, 100, 100, door_button_on_image)
    door_button_on2 = button(8150, 250, 100, 100, door_button_on_image)
    left_light = button(-100, 30, 200, 700, left_light_image)
    right_light = button(1600, 30, 200, 700, right_light_image)
    left_door = button(-100, 30, 200, 700, left_door_image)
    right_door = button(1600, 30, 200, 700, right_door_image)
    bon = button(-100, 30, 500, 700, bon_image)
    chic = button(1300, 10, 200, 550, chic_image)
    camera_button = button(300, 650, 500, 50, camera_button_image)
    camera_button2 = button(21500, 650, 500, 50, camera_button_image)
    a2_button = button(870, 550, 95, 65, a2_image)
    a2_on_button = button(11870, 550, 95, 65, a2_on_image)
    b2_button = button(870, 615, 95, 65, b2_image)
    b2_on_button = button(11870, 615, 95, 65, b2_on_image)
    a4_button = button(1030, 550, 95, 65, a4_image)
    a4_on_button = button(111030, 550, 95, 65, a4_on_image)
    b4_button = button(1030, 615, 95, 65, b4_image)
    b4_on_button = button(111030, 615, 95, 65, b4_on_image)
    a3_button = button(740, 500, 95, 65, a3_image)
    a3_on_button = button(11740, 500, 95, 65, a3_on_image)
    a5_button = button(730, 330, 95, 65, a5_image)
    a5_on_button = button(11730, 330, 95, 65, a5_on_image)
    a6_button = button(1130, 500, 95, 65, a6_image)
    a6_on_button = button(111130, 500, 95, 65, a6_on_image)
    a7_button = button(1140, 300, 95, 65, a7_image)
    a7_on_button = button(111140, 300, 95, 65, a7_on_image)
    a1_button = button(900, 200, 95, 65, a1_image)
    a1_on_button = button(11900, 200, 95, 65, a1_on_image)
    b1_button = button(890, 300, 95, 65, b1_image)
    b1_on_button = button(11890, 300, 95, 65, b1_on_image)
    c1_button = button(850, 400, 95, 65, c1_image)
    c1_on_button = button(11850, 400, 95, 65, c1_on_image)
    camera_area = button(-300, 0, 2250, 720, pirate_cove_image)
    boop_button = button(650, 150, 10, 10, boop_image)
    
    officex = -300
    camerax = -300
    last_event_time = time.time()
    event_interval = 5  # Time interval in seconds

    flicker_interval = 500  # milliseconds
    last_flicker_time = pygame.time.get_ticks()
    show_power_out_fred = True

    update_pirate_cove = True
    update_backstage = True
    update_dining_area = True
    update_e_hall = True
    update_e_hall_corner = True
    update_restrooms = True
    update_show_stage = True
    update_supply_closet = True
    update_w_hall = True
    update_w_hall_corner = True

    stop_left = True
    stop_right = True
    show_left_light = False
    show_right_light = False
    show_left_door = False
    show_right_door = False
    show_bon = False
    show_chic = False
    show_camera = False
    jumpscare_end = False
    jumpscare_end_chic = False
    jumpscare_end_fox = False
    jumpscare_end_fred = False
    power_out = False
    power_out_fred_active = False
    cama2_active = False
    camb2_active = True
    cama4_active = False
    camb4_active = False
    cama3_active = False
    cama5_active = False
    cama6_active = False
    cama7_active = False
    cama1_active = False
    camb1_active = False
    camc1_active = False
    show_green_cama2_flicker = False
    show_green_camb2_flicker = False
    show_green_cama4_flicker = False
    show_green_camb4_flicker = False
    show_green_cama3_flicker = False
    show_green_cama5_flicker = False
    show_green_cama6_flicker = False
    show_green_cama7_flicker = False
    show_green_cama1_flicker = False
    show_green_camb1_flicker = False
    show_green_camc1_flicker = False

    night_number = 5
    am_number = 12
    power_number = 100
    sec_number = 0
    sec_number2 = 0
    sec_number3 = 0
    sec_number4 = 0
    sec_number5 = 0
    sec_fred_move = 0
    sec_fox_move = 0

    pirate_cove_stage_number = 1
    bonnie_stage_number = 1
    chica_stage_number = 1
    fred_stage_number = 1
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'night.json'),'w') as night:
                    json.dump(data_night, night)
                run = False
                pygame.quit()
            current_time = pygame.time.get_ticks()

            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
                camera_button_rect = pygame.Rect(camera_button.x, camera_button.y, camera_button.width, camera_button.height)
                camera_button2_rect = pygame.Rect(camera_button2.x, camera_button2.y, camera_button2.width, camera_button2.height)
                if mousex < 400:
                    stop_left = False
                elif mousex > 900:
                    stop_right = False
                else:
                    stop_left = True
                    stop_right = True
                if power_out == False:
                    if camera_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 21500
                        camera_button2.x = 300
                        show_camera = True
                        last_move_time = current_time
                    if camera_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 300
                        camera_button2.x = 21500
                        show_camera = False
                        last_move_time = current_time
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                light_button_rect = pygame.Rect(light_button.x, light_button.y, light_button.width, light_button.height)
                light_button2_rect = pygame.Rect(light_button2.x, light_button2.y, light_button2.width, light_button2.height)
                light_button_on_rect = pygame.Rect(light_button_on.x, light_button_on.y, light_button_on.width, light_button_on.height)
                light_button_on2_rect = pygame.Rect(light_button_on2.x, light_button_on2.y, light_button_on2.width, light_button_on2.height)
                door_button_rect = pygame.Rect(door_button.x, door_button.y, door_button.width, door_button.height)
                door_button2_rect = pygame.Rect(door_button2.x, door_button2.y, door_button2.width, door_button2.height)
                door_button_on_rect = pygame.Rect(door_button_on.x, door_button_on.y, door_button_on.width, door_button_on.height)
                door_button_on2_rect = pygame.Rect(door_button_on2.x, door_button_on2.y, door_button_on2.width, door_button_on2.height)

                boop_button_rect = pygame.Rect(boop_button.x, boop_button.y, boop_button.width, boop_button.height)

                a2_button_rect = pygame.Rect(a2_button.x, a2_button.y, a2_button.width, a2_button.height)
                b2_button_rect = pygame.Rect(b2_button.x, b2_button.y, b2_button.width, b2_button.height)
                a4_button_rect = pygame.Rect(a4_button.x, a4_button.y, a4_button.width, a4_button.height)
                b4_button_rect = pygame.Rect(b4_button.x, b4_button.y, b4_button.width, b4_button.height)
                a3_button_rect = pygame.Rect(a3_button.x, a3_button.y, a3_button.width, a3_button.height)
                a5_button_rect = pygame.Rect(a5_button.x, a5_button.y, a5_button.width, a5_button.height)
                a6_button_rect = pygame.Rect(a6_button.x, a6_button.y, a6_button.width, a6_button.height)
                a7_button_rect = pygame.Rect(a7_button.x, a7_button.y, a7_button.width, a7_button.height)
                a1_button_rect = pygame.Rect(a1_button.x, a1_button.y, a1_button.width, a1_button.height)
                b1_button_rect = pygame.Rect(b1_button.x, b1_button.y, b1_button.width, b1_button.height)
                c1_button_rect = pygame.Rect(c1_button.x, c1_button.y, c1_button.width, c1_button.height)

                if show_camera == False and power_out == False:

                    if door_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_right_door = True
                        door_button_on.x = 1180
                        door_button.x = 8150
                        last_move_time = current_time
                    if door_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_left_door = True
                        door_button_on2.x = 50
                        door_button2.x = 8150
                        last_move_time = current_time
                    if door_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_right_door = False
                        door_button_on.x = 8150
                        door_button.x = 1180
                        last_move_time = current_time
                    if door_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_left_door = False
                        door_button_on2.x = 8150
                        door_button2.x = 50
                        last_move_time = current_time

                    if light_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_right_light = True
                        light_button_on.x = 1180
                        light_button.x = 8150
                        last_move_time = current_time
                    if light_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_left_light = True
                        light_button_on2.x = 50
                        light_button2.x = 8150
                        last_move_time = current_time
                    if light_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_right_light = False
                        light_button_on.x = 8150
                        light_button.x = 1180
                        last_move_time = current_time
                    if light_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_left_light = False
                        light_button_on2.x = 8150
                        light_button2.x = 50
                        last_move_time = current_time
                if show_camera == False:
                    if boop_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        boop_sound.play()
                        last_move_time = current_time
                if show_camera == True:
                    if a2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama2_active = True
                        camb2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "West Hall"
                        update_w_hall = True
                        update_pirate_cove = False
                        update_w_hall_corner = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_image2
                        last_move_time = current_time
                    if b2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb2_active = True
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "W. Hall Corner"
                        update_w_hall_corner = True
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_corner_image2
                        last_move_time = current_time
                    if a4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama4_active = True
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_e_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "East Hall"
                        update_e_hall = True
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_image2
                        last_move_time = current_time
                    if b4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb4_active = True
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_e_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "E. Hall Corner"
                        update_e_hall_corner = True
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_corner_image2
                        last_move_time = current_time
                    if a3_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama3_active = True
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_supply_closet == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Supply Closet"
                        update_supply_closet = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        camera_area.image = supply_closet_image2
                        last_move_time = current_time
                    if a5_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama5_active = True
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_backstage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Backstage"
                        update_backstage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = backstage_image2
                        last_move_time = current_time
                    if a6_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        if cama6_active == False:
                            change_camera_sound.play()
                        cama6_active = True
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        camera_area_text1 = "Kitchen"
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = kitchen_image
                        last_move_time = current_time
                    if a7_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama7_active = True
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_restrooms == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Restrooms"
                        update_restrooms = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = restrooms_image2
                        last_move_time = current_time
                    if a1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama1_active = True
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_show_stage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Show Stage"
                        update_show_stage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_supply_closet = False
                        camera_area.image = show_stage_image2
                        last_move_time = current_time
                    if b1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb1_active = True
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camc1_active = False
                        if update_dining_area == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Dining Area"
                        update_dining_area = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = dining_area_image2
                        last_move_time = current_time
                    if c1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camc1_active = True
                        camb1_active = False
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        if update_pirate_cove == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Pirates Cove"
                        update_pirate_cove = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = pirate_cove_image2
                        
                        last_move_time = current_time
        if power_out == True:
            sec_power += 1
        if sec_power == 420:
            music_box.play()
            power_out_fred_active = True
        if sec_power == 1320:
            power_out_fred_active = False
        if sec_power == 1500:
            jumpscare_sound.play() 
            jumpscare_end_fred = True
            stop_left = True
            stop_right = True
            show_camera = False
        sec_fred_move += 1
        sec_fox_move += 1
        current_time3 = pygame.time.get_ticks()
        # Check if it's time to flicker
        if current_time3 - last_flicker_time >= flicker_interval and power_out_fred_active == True:
            show_power_out_fred = not show_power_out_fred  # Toggle visibility
            last_flicker_time = current_time3

        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama2_active == True:
            show_green_cama2_flicker = not show_green_cama2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb2_active == True:
            show_green_camb2_flicker = not show_green_camb2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama4_active == True:
            show_green_cama4_flicker = not show_green_cama4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb4_active == True:
            show_green_camb4_flicker = not show_green_camb4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama3_active == True:
            show_green_cama3_flicker = not show_green_cama3_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama5_active == True:
            show_green_cama5_flicker = not show_green_cama5_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama6_active == True:
            show_green_cama6_flicker = not show_green_cama6_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama7_active == True:
            show_green_cama7_flicker = not show_green_cama7_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama1_active == True:
            show_green_cama1_flicker = not show_green_cama1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb1_active == True:
            show_green_camb1_flicker = not show_green_camb1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camc1_active == True:
            show_green_camc1_flicker = not show_green_camc1_flicker  # Toggle visibility
            last_flicker_time = current_time3

        current_time2 = time.time()
        if current_time2 - last_event_time >= event_interval and power_out == False:
            sec_number3 += 1   
            rng = random.randint(1, 20)
            print(rng)
            #freddy fazbear
            if show_camera == False:
                sec_fred_move = 0
                if fred_ai_number >= rng and sec_fred_move >= 1000 - 100 * fred_ai_number:
                    fred_stage_number += 1
                    print("Fred Stage INCREASED!!!!!!!")
                    if fred_stage_number == 1 and chica_stage_number == 1 and bonnie_stage_number == 1:
                        show_stage_image2 = show_stage_image
                    if fred_stage_number == 2:
                        show_stage_image2 = show_stage_stage4_image
                    if fred_stage_number >= 6:
                        e_hall_corner_image2 = e_hall_corner_stage3_image
            if camera_area.image != e_hall_corner_image2 and show_right_door == False and fred_stage_number >= 6:
                jumpscare_end_fred = True
                jumpscare_sound.play()
                stop_left = True
                stop_right = True
                show_camera = False
            if camera_area.image != e_hall_corner_image2 and show_right_door == True and fred_stage_number >= 6:
                e_hall_corner_image2 = e_hall_corner_image
                fred_stage_number = 5
                    
            #foxy
            if show_camera == False and sec_fox_move >= random.randint(50, 1000):
                sec_fox_move = 0
                if fox_ai_number >= rng:
                    pirate_cove_stage_number += 1
                    print("fox stage increased!")
                    if pirate_cove_stage_number == 1:
                        pirate_cove_image2 = pirate_cove_image
                        
                    if pirate_cove_image2 == pirate_cove_image and pirate_cove_stage_number == 2:
                        pirate_cove_image2 = pirate_cove_stage2_image    

                    if pirate_cove_image2 == pirate_cove_stage2_image and pirate_cove_stage_number == 3:
                        pirate_cove_image2 = pirate_cove_stage3_image
                        
                    if pirate_cove_image2 == pirate_cove_stage3_image and pirate_cove_stage_number == 4:
                        sec_number3 = 0
                        pirate_cove_image2 = pirate_cove_stage4_image
                    
            
            
            if fox_ai_number >= rng:   
                if sec_number3 == 5 and show_left_door == True or camera_area.image == w_hall_image2 and show_left_door == True:
                    play_next_sound()
                    power_number -= 1
                    pirate_cove_image2 = pirate_cove_image
                    sec_number3 = 0
                    pirate_cove_stage_number = 1
                if sec_number3 == 5 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image or camera_area.image == w_hall_image2 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image:
                    jumpscare_end_fox = True
                    jumpscare_sound.play()
                    stop_left = True
                    stop_right = True
                    show_camera = False
                
            #bonnie
            if bon_ai_number >= rng:
                bonnie_stage_number += 1
                print("bonnie stage increased!")
                if bonnie_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if bonnie_stage_number == 2:
                    show_stage_image2 = show_stage_stage2_image
                    dining_area_image2 = dining_area_stage2_image
                if bonnie_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    backstage_image2 = backstage_stage2_image
                if bonnie_stage_number == 4:
                    backstage_image2 = backstage_image
                    w_hall_image2 = w_hall_stage2_image
                if bonnie_stage_number == 5:
                    w_hall_image2 = w_hall_image
                    supply_closet_image2 = supply_closet_stage2_image
                if bonnie_stage_number == 6:
                    loud_footsteps_sound.play()
                    supply_closet_image2 = supply_closet_image
                    w_hall_corner_image2 = w_hall_corner_stage2_image
                if bonnie_stage_number >= 7:
                    w_hall_corner_image2 = w_hall_corner_image
                    show_bon = True

            if bon_ai_number >= rng and show_left_door == True and show_bon == True:
                show_bon = False
                quiet_footsteps_sound.play()
                bonnie_stage_number = 2
                sec_number2 = 0
            if bon_ai_number < rng:
                print("bonnie failed to move")
            if show_bon == True and show_left_light == True and show_camera == False:
                jump_sound.play()
            if show_bon == True and show_left_door == False:
                sec_number2 += 1
            if sec_number2 >= 2 and show_left_door == False and bon_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end = True
                show_bon = True
                show_left_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                bon.image = pygame.transform.scale(bon.image, (5000, 1000))
                
            
            #chica
            if chic_ai_number >= rng:
                chica_stage_number += 1
                print("Chica Stage Increased!!!")
                if chica_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if chica_stage_number == 2:
                    show_stage_image2 = show_stage_stage3_image
                    dining_area_image2 = dining_area_stage3_image
                if chica_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    restrooms_image2 = restrooms_stage2_image
                if chica_stage_number == 4:
                    restrooms_image2 = restrooms_image
                if chica_stage_number == 5:
                    e_hall_image2 = e_hall_stage2_image
                if chica_stage_number == 6:
                    loud_footsteps_sound.play()
                    e_hall_image2 = e_hall_image
                    e_hall_corner_image2 = e_hall_corner_stage2_image
                if chica_stage_number == 7:
                    e_hall_corner_image2 = e_hall_corner_image
                    show_chic = True

            if chic_ai_number >= rng and show_right_door == True and show_chic == True:
                show_chic = False
                quiet_footsteps_sound.play()
                chica_stage_number = 2
                sec_number4 = 0
            if chic_ai_number < rng:
                print("chica failed to move")
            if show_chic == True and show_right_light == True and show_camera == False:
                jump_sound.play()
            if show_chic == True and show_right_door == False:
                sec_number4 += 1
            if sec_number4 >= 2 and show_right_door == False and chic_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end_chic = True
                show_chic = True
                show_right_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                chic.image = pygame.transform.scale(chic.image, (2500, 1000))
                chic.x = bon.x

            last_event_time = current_time2

        if jumpscare_end == True:
            sec += 1
            phoneguy_night1.stop()
            show_bon = True
            show_left_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec >= 70:
            mainmenu()
        
        if jumpscare_end_chic == True:
            sec_chic += 1
            phoneguy_night1.stop()
            show_chic = True
            show_right_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_chic >= 70:
            mainmenu()
        
        if jumpscare_end_fox == True:
            sec_fox += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fox >= 140:
            mainmenu()

        if jumpscare_end_fred == True:
            sec_fred += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fred >= 70:
            mainmenu()

        if show_camera == True and update_pirate_cove == True:
            camera_area.image = pirate_cove_image2

        if show_camera == True and update_backstage == True:
            camera_area.image = backstage_image2

        if show_camera == True and update_dining_area == True:
            camera_area.image = dining_area_image2

        if show_camera == True and update_e_hall == True:
            camera_area.image = e_hall_image2

        if show_camera == True and update_e_hall_corner == True:
            camera_area.image = e_hall_corner_image2

        if show_camera == True and update_restrooms == True:
            camera_area.image = restrooms_image2

        if show_camera == True and update_show_stage == True:
            camera_area.image = show_stage_image2

        if show_camera == True and update_supply_closet == True:
            camera_area.image = supply_closet_image2
        
        if show_camera == True and update_w_hall == True:
            camera_area.image = w_hall_image2
        
        if show_camera == True and update_w_hall_corner == True:
            camera_area.image = w_hall_corner_image2
            

        if stop_left == False and camerax < -100:
            camerax += 10
            
        if stop_right == False and camerax > -500:
            camerax -= 10

        if stop_left == False and officex < -5:
            officex += 10
            boop_button.x += 10
            left_light.x += 10
            right_light.x += 10
            left_door.x += 10
            right_door.x += 10
            bon.x += 10
            chic.x += 10
            light_button.x += 10
            light_button2.x += 10
            light_button_on.x += 10
            light_button_on2.x += 10
            door_button.x += 10
            door_button2.x += 10
            door_button_on.x += 10
            door_button_on2.x += 10
        if stop_right == False and officex > -970:
            officex -= 10
            boop_button.x -= 10
            left_light.x -= 10
            right_light.x -= 10
            left_door.x -= 10
            right_door.x -= 10
            bon.x -= 10
            chic.x -= 10
            light_button.x -= 10
            light_button2.x -= 10
            light_button_on.x -= 10
            light_button_on2.x -= 10
            door_button.x -= 10
            door_button2.x -= 10
            door_button_on.x -= 10
            door_button_on2.x -= 10

        sec_number5 += 1
        if sec_number5 >= 180:
            power_number -= 1
            sec_number5 = 0

        sec_number+=1
        if sec_number == 5400:
            am_number = 1
        if sec_number == 10800:
            bon_ai_number += 1
            am_number = 2
        if sec_number == 16200:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 3
        if sec_number == 21600:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 4
        if sec_number == 27000:
            am_number = 5
        if sec_number == 32400:
            power_out = False
            data_night['night_6_unlocked'] = True
            with open(os.path.join('data', 'night.json'),'w') as night:
                json.dump(data_night, night)
            win6am()

        if power_number <= 0:
            power_out = True

        if power_out == False:
            Usage_text = Small_Font.render("Usage:", 1, WHITE)
            Power_left_text = Small_Font.render("Power left:", 1, WHITE)
            Night_text = Small_Font.render("Night " + str(int(night_number)), 1, WHITE)
            AM_text = Big_Font.render(str(int(am_number)) + " AM", 1, WHITE)
            Power_number_text = Big_Font.render(str(int(power_number)) + "%", 1, WHITE)
        Light_text = Small_Font.render("LIGHT", 1, WHITE)
        Door_text = Small_Font.render("DOOR", 1, WHITE)
        if power_out == False:
            camera_area_text = Big_Font.render(camera_area_text1, 1, WHITE)
        window.fill((0, 0, 0))
        if power_out == False:
            if show_right_light == True and show_chic == True and show_camera == False:
                window.blit(chic.image, (chic.x, chic.y))
        window.blit(office_bg_image, (officex, 0))
        window.blit(boop_button.image, (boop_button.x, boop_button.y))
        if power_out == False:
            window.blit(camera_button.image, (camera_button.x, camera_button.y))
        if power_out == False:
            if jumpscare_end_chic == True:
                window.blit(chic.image, (chic.x, chic.y))
            if jumpscare_end_fox == True:
                window.blit(fox_image, (bon.x + 100, chic.y))
            if show_camera == True:
                power_number -= 0.0008
                window.blit(camera_area.image, (camerax, camera_area.y))
                window.blit(camera_area_text, (735, 130))
                window.blit(green_bar_image, (125, 670))
                window.blit(map_image, (750, 200))
                if show_green_cama1_flicker == False:
                    a1_button.x = 900
                    a1_on_button.x = 11900
                if show_green_cama2_flicker == False:
                    a2_button.x = 870
                    a2_on_button.x = 11870
                if show_green_camb2_flicker == False:
                    b2_button.x = 870
                    b2_on_button.x = 11870
                if show_green_camc1_flicker == False:
                    c1_button.x = 850
                    c1_on_button.x = 11850
                if show_green_camb1_flicker == False:
                    b1_button.x = 890
                    b1_on_button.x = 11890
                if show_green_cama7_flicker == False:
                    a7_button.x = 1140
                    a7_on_button.x = 111140
                if show_green_cama6_flicker == False:
                    a6_button.x = 1130
                    a6_on_button.x = 111130
                if show_green_cama5_flicker == False:
                    a5_button.x = 730
                    a5_on_button.x = 11730
                if show_green_cama3_flicker == False:
                    a3_button.x = 740
                    a3_on_button.x = 11740
                if show_green_camb4_flicker == False:
                    b4_button.x = 1030
                    b4_on_button.x = 111030
                if show_green_cama4_flicker == False:
                    a4_button.x = 1030
                    a4_on_button.x = 111030
                if show_green_cama2_flicker == True:
                    a2_button.x = 11870
                    a2_on_button.x = 870
                if cama2_active == False:
                    a2_button.x = 870
                if show_green_camb2_flicker == True:
                    b2_button.x = 11870
                    b2_on_button.x = 870
                if camb2_active == False:
                    b2_button.x = 870
                if show_green_camc1_flicker == True:
                    c1_button.x = 11850
                    c1_on_button.x = 850
                if camc1_active == False:
                    c1_button.x = 850
                if show_green_camb1_flicker == True:
                    b1_button.x = 11890
                    b1_on_button.x = 890
                if camb1_active == False:
                    b1_button.x = 890
                if show_green_cama1_flicker == True:
                    a1_button.x = 11900
                    a1_on_button.x = 900
                if cama1_active == False:
                    a1_button.x = 900
                if show_green_cama7_flicker == True:
                    a7_button.x = 111140
                    a7_on_button.x = 1140
                if cama7_active == False:
                    a7_button.x = 1140
                if show_green_cama6_flicker == True:
                    a6_button.x = 111130
                    a6_on_button.x = 1130
                if cama6_active == False:
                    a6_button.x = 1130
                if show_green_cama5_flicker == True:
                    a5_button.x = 11730
                    a5_on_button.x = 730
                if cama5_active == False:
                    a5_button.x = 730
                if show_green_cama3_flicker == True:
                    a3_button.x = 11740
                    a3_on_button.x = 740
                if cama3_active == False:
                    a3_button.x = 740
                if show_green_camb4_flicker == True:
                    b4_button.x = 111030
                    b4_on_button.x = 1030
                if camb4_active == False:
                    b4_button.x = 1030
                if show_green_cama4_flicker == True:
                    a4_button.x = 111030
                    a4_on_button.x = 1030
                if cama4_active == False:
                    a4_button.x = 1030
                window.blit(a2_on_button.image, (a2_on_button.x, a2_on_button.y))
                window.blit(b2_on_button.image, (b2_on_button.x, b2_on_button.y))
                window.blit(a4_on_button.image, (a4_on_button.x, a4_on_button.y))
                window.blit(b4_on_button.image, (b4_on_button.x, b4_on_button.y))
                window.blit(a3_on_button.image, (a3_on_button.x, a3_on_button.y))
                window.blit(a5_on_button.image, (a5_on_button.x, a5_on_button.y))
                window.blit(a6_on_button.image, (a6_on_button.x, a6_on_button.y))
                window.blit(a7_on_button.image, (a7_on_button.x, a7_on_button.y))
                window.blit(a1_on_button.image, (a1_on_button.x, a1_on_button.y))
                window.blit(b1_on_button.image, (b1_on_button.x, b1_on_button.y))
                window.blit(c1_on_button.image, (c1_on_button.x, c1_on_button.y))
                
                window.blit(a2_button.image, (a2_button.x, a2_button.y))           
                window.blit(b2_button.image, (b2_button.x, b2_button.y))             
                window.blit(a4_button.image, (a4_button.x, a4_button.y))              
                window.blit(b4_button.image, (b4_button.x, b4_button.y))              
                window.blit(a3_button.image, (a3_button.x, a3_button.y))  
                window.blit(a5_button.image, (a5_button.x, a5_button.y))               
                window.blit(a6_button.image, (a6_button.x, a6_button.y))    
                window.blit(a7_button.image, (a7_button.x, a7_button.y))             
                window.blit(a1_button.image, (a1_button.x, a1_button.y))             
                window.blit(b1_button.image, (b1_button.x, b1_button.y)) 
                window.blit(c1_button.image, (c1_button.x, c1_button.y))
                window.blit(camera_button2.image, (camera_button2.x, camera_button2.y))
            if show_left_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_left_light == True and show_camera == False:
                window.blit(left_light.image, (left_light.x, left_light.y))
            if show_left_light == True and show_bon == True and show_camera == False:
                window.blit(bon.image, (bon.x, bon.y))
            if show_right_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_right_light == True and show_camera == False:
                window.blit(right_light.image, (right_light.x, right_light.y))
            if show_left_door == True:
                power_number -= 0.002
                window.blit(yellow_bar_image, (150, 670))
            if show_left_door == True and show_camera == False:
                window.blit(left_door.image, (left_door.x, left_door.y))
            if show_right_door == True:
                power_number -= 0.002
                window.blit(red_bar_image, (175, 670))
            if show_right_door == True and show_camera == False:
                window.blit(right_door.image, (right_door.x, right_door.y))
            if show_right_door == False and show_left_door == False and show_right_light == False and show_left_light == False and show_camera == False:
                power_number -= 0
            window.blit(green_bar_image, (100, 670))
            power_number -= 0.0008
        if power_out == True and show_power_out_fred == True and power_out_fred_active == True:
            window.blit(fred_power_out_image, (bon.x, bon.y))

        if jumpscare_end_fred == True:
            fred_image = pygame.transform.scale(fred_image, (2500, 1000))
            window.blit(fred_image, (bon.x, chic.y))

        if show_camera == False:
            window.blit(door_button2.image, (door_button2.x, door_button2.y))
            window.blit(door_button.image, (door_button.x, door_button.y))
            window.blit(door_button_on2.image, (door_button_on2.x, door_button_on2.y))
            window.blit(door_button_on.image, (door_button_on.x, door_button_on.y))

            window.blit(light_button2.image, (light_button2.x, light_button2.y))
            window.blit(light_button.image, (light_button.x, light_button.y))
            window.blit(light_button_on2.image, (light_button_on2.x, light_button_on2.y))
            window.blit(light_button_on.image, (light_button_on.x, light_button_on.y))

            office_bg_image.blit(Light_text, (50, 500))
            office_bg_image.blit(Light_text, (2150, 500))
            office_bg_image.blit(Door_text, (50, 350))
            office_bg_image.blit(Door_text, (2150, 350))
        if power_out == False:
            window.blit(AM_text, (1150, 0))
            window.blit(Night_text, (1150, 50))
            window.blit(Usage_text, (0, 660))
            window.blit(Power_left_text, (0, 600))
            window.blit(Power_number_text, (160, 590))
        pygame.display.update()

def night6():
    data_night['night_6_on'] = False
    
    sec = 0
    sec_power = 0
    sec_chic = 0
    sec_fox = 0
    sec_fred = 0
    camera_area_text1 = "W. Hall Corner"

    fred_image = pygame.image.load(os.path.join('Images', 'animatronics', 'fred.png'))

    pirate_cove_image2 = pirate_cove_image
    show_stage_image2 = show_stage_image
    w_hall_corner_image2 = w_hall_corner_image
    w_hall_image2 = w_hall_image
    supply_closet_image2 = supply_closet_image
    restrooms_image2 = restrooms_image
    e_hall_corner_image2 = e_hall_corner_image
    e_hall_image2 = e_hall_image
    dining_area_image2 = dining_area_image
    backstage_image2 = backstage_image

    bon_ai_number = 10
    fox_ai_number = 16
    chic_ai_number = 12
    fred_ai_number = 4

    move_delay = 250  # milliseconds
    move_delay_camera = 450  # milliseconds
    last_move_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    light_button = button(1850, 400, 100, 100, light_button_image)
    light_button2 = button(-250, 400, 100, 100, light_button_image)
    light_button_on = button(8150, 400, 100, 100, light_button_on_image)
    light_button_on2 = button(8150, 400, 100, 100, light_button_on_image)
    door_button = button(1850, 250, 100, 100, door_button_image)
    door_button2 = button(-250, 250, 100, 100, door_button_image)
    door_button_on = button(8150, 250, 100, 100, door_button_on_image)
    door_button_on2 = button(8150, 250, 100, 100, door_button_on_image)
    left_light = button(-100, 30, 200, 700, left_light_image)
    right_light = button(1600, 30, 200, 700, right_light_image)
    left_door = button(-100, 30, 200, 700, left_door_image)
    right_door = button(1600, 30, 200, 700, right_door_image)
    bon = button(-100, 30, 500, 700, bon_image)
    chic = button(1300, 10, 200, 550, chic_image)
    camera_button = button(300, 650, 500, 50, camera_button_image)
    camera_button2 = button(21500, 650, 500, 50, camera_button_image)
    a2_button = button(870, 550, 95, 65, a2_image)
    a2_on_button = button(11870, 550, 95, 65, a2_on_image)
    b2_button = button(870, 615, 95, 65, b2_image)
    b2_on_button = button(11870, 615, 95, 65, b2_on_image)
    a4_button = button(1030, 550, 95, 65, a4_image)
    a4_on_button = button(111030, 550, 95, 65, a4_on_image)
    b4_button = button(1030, 615, 95, 65, b4_image)
    b4_on_button = button(111030, 615, 95, 65, b4_on_image)
    a3_button = button(740, 500, 95, 65, a3_image)
    a3_on_button = button(11740, 500, 95, 65, a3_on_image)
    a5_button = button(730, 330, 95, 65, a5_image)
    a5_on_button = button(11730, 330, 95, 65, a5_on_image)
    a6_button = button(1130, 500, 95, 65, a6_image)
    a6_on_button = button(111130, 500, 95, 65, a6_on_image)
    a7_button = button(1140, 300, 95, 65, a7_image)
    a7_on_button = button(111140, 300, 95, 65, a7_on_image)
    a1_button = button(900, 200, 95, 65, a1_image)
    a1_on_button = button(11900, 200, 95, 65, a1_on_image)
    b1_button = button(890, 300, 95, 65, b1_image)
    b1_on_button = button(11890, 300, 95, 65, b1_on_image)
    c1_button = button(850, 400, 95, 65, c1_image)
    c1_on_button = button(11850, 400, 95, 65, c1_on_image)
    camera_area = button(-300, 0, 2250, 720, pirate_cove_image)
    boop_button = button(650, 150, 10, 10, boop_image)
    
    officex = -300
    camerax = -300
    last_event_time = time.time()
    event_interval = 5  # Time interval in seconds

    flicker_interval = 500  # milliseconds
    last_flicker_time = pygame.time.get_ticks()
    show_power_out_fred = True

    update_pirate_cove = True
    update_backstage = True
    update_dining_area = True
    update_e_hall = True
    update_e_hall_corner = True
    update_restrooms = True
    update_show_stage = True
    update_supply_closet = True
    update_w_hall = True
    update_w_hall_corner = True

    stop_left = True
    stop_right = True
    show_left_light = False
    show_right_light = False
    show_left_door = False
    show_right_door = False
    show_bon = False
    show_chic = False
    show_camera = False
    jumpscare_end = False
    jumpscare_end_chic = False
    jumpscare_end_fox = False
    jumpscare_end_fred = False
    power_out = False
    power_out_fred_active = False
    cama2_active = False
    camb2_active = True
    cama4_active = False
    camb4_active = False
    cama3_active = False
    cama5_active = False
    cama6_active = False
    cama7_active = False
    cama1_active = False
    camb1_active = False
    camc1_active = False
    show_green_cama2_flicker = False
    show_green_camb2_flicker = False
    show_green_cama4_flicker = False
    show_green_camb4_flicker = False
    show_green_cama3_flicker = False
    show_green_cama5_flicker = False
    show_green_cama6_flicker = False
    show_green_cama7_flicker = False
    show_green_cama1_flicker = False
    show_green_camb1_flicker = False
    show_green_camc1_flicker = False

    night_number = 6
    am_number = 12
    power_number = 100
    sec_number = 0
    sec_number2 = 0
    sec_number3 = 0
    sec_number4 = 0
    sec_number5 = 0
    sec_fred_move = 0
    sec_fox_move = 0

    pirate_cove_stage_number = 1
    bonnie_stage_number = 1
    chica_stage_number = 1
    fred_stage_number = 1
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'night.json'),'w') as night:
                    json.dump(data_night, night)
                run = False
                pygame.quit()
            current_time = pygame.time.get_ticks()

            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
                camera_button_rect = pygame.Rect(camera_button.x, camera_button.y, camera_button.width, camera_button.height)
                camera_button2_rect = pygame.Rect(camera_button2.x, camera_button2.y, camera_button2.width, camera_button2.height)
                if mousex < 400:
                    stop_left = False
                elif mousex > 900:
                    stop_right = False
                else:
                    stop_left = True
                    stop_right = True
                if power_out == False:
                    if camera_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 21500
                        camera_button2.x = 300
                        show_camera = True
                        last_move_time = current_time
                    if camera_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 300
                        camera_button2.x = 21500
                        show_camera = False
                        last_move_time = current_time
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                light_button_rect = pygame.Rect(light_button.x, light_button.y, light_button.width, light_button.height)
                light_button2_rect = pygame.Rect(light_button2.x, light_button2.y, light_button2.width, light_button2.height)
                light_button_on_rect = pygame.Rect(light_button_on.x, light_button_on.y, light_button_on.width, light_button_on.height)
                light_button_on2_rect = pygame.Rect(light_button_on2.x, light_button_on2.y, light_button_on2.width, light_button_on2.height)
                door_button_rect = pygame.Rect(door_button.x, door_button.y, door_button.width, door_button.height)
                door_button2_rect = pygame.Rect(door_button2.x, door_button2.y, door_button2.width, door_button2.height)
                door_button_on_rect = pygame.Rect(door_button_on.x, door_button_on.y, door_button_on.width, door_button_on.height)
                door_button_on2_rect = pygame.Rect(door_button_on2.x, door_button_on2.y, door_button_on2.width, door_button_on2.height)

                boop_button_rect = pygame.Rect(boop_button.x, boop_button.y, boop_button.width, boop_button.height)

                a2_button_rect = pygame.Rect(a2_button.x, a2_button.y, a2_button.width, a2_button.height)
                b2_button_rect = pygame.Rect(b2_button.x, b2_button.y, b2_button.width, b2_button.height)
                a4_button_rect = pygame.Rect(a4_button.x, a4_button.y, a4_button.width, a4_button.height)
                b4_button_rect = pygame.Rect(b4_button.x, b4_button.y, b4_button.width, b4_button.height)
                a3_button_rect = pygame.Rect(a3_button.x, a3_button.y, a3_button.width, a3_button.height)
                a5_button_rect = pygame.Rect(a5_button.x, a5_button.y, a5_button.width, a5_button.height)
                a6_button_rect = pygame.Rect(a6_button.x, a6_button.y, a6_button.width, a6_button.height)
                a7_button_rect = pygame.Rect(a7_button.x, a7_button.y, a7_button.width, a7_button.height)
                a1_button_rect = pygame.Rect(a1_button.x, a1_button.y, a1_button.width, a1_button.height)
                b1_button_rect = pygame.Rect(b1_button.x, b1_button.y, b1_button.width, b1_button.height)
                c1_button_rect = pygame.Rect(c1_button.x, c1_button.y, c1_button.width, c1_button.height)

                if show_camera == False and power_out == False:

                    if door_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_right_door = True
                        door_button_on.x = 1180
                        door_button.x = 8150
                        last_move_time = current_time
                    if door_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_left_door = True
                        door_button_on2.x = 50
                        door_button2.x = 8150
                        last_move_time = current_time
                    if door_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_right_door = False
                        door_button_on.x = 8150
                        door_button.x = 1180
                        last_move_time = current_time
                    if door_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_left_door = False
                        door_button_on2.x = 8150
                        door_button2.x = 50
                        last_move_time = current_time

                    if light_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_right_light = True
                        light_button_on.x = 1180
                        light_button.x = 8150
                        last_move_time = current_time
                    if light_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_left_light = True
                        light_button_on2.x = 50
                        light_button2.x = 8150
                        last_move_time = current_time
                    if light_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_right_light = False
                        light_button_on.x = 8150
                        light_button.x = 1180
                        last_move_time = current_time
                    if light_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_left_light = False
                        light_button_on2.x = 8150
                        light_button2.x = 50
                        last_move_time = current_time
                if show_camera == False:
                    if boop_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        boop_sound.play()
                        last_move_time = current_time
                if show_camera == True:
                    if a2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama2_active = True
                        camb2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "West Hall"
                        update_w_hall = True
                        update_pirate_cove = False
                        update_w_hall_corner = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_image2
                        last_move_time = current_time
                    if b2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb2_active = True
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "W. Hall Corner"
                        update_w_hall_corner = True
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_corner_image2
                        last_move_time = current_time
                    if a4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama4_active = True
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_e_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "East Hall"
                        update_e_hall = True
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_image2
                        last_move_time = current_time
                    if b4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb4_active = True
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_e_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "E. Hall Corner"
                        update_e_hall_corner = True
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_corner_image2
                        last_move_time = current_time
                    if a3_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama3_active = True
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_supply_closet == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Supply Closet"
                        update_supply_closet = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        camera_area.image = supply_closet_image2
                        last_move_time = current_time
                    if a5_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama5_active = True
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_backstage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Backstage"
                        update_backstage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = backstage_image2
                        last_move_time = current_time
                    if a6_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        if cama6_active == False:
                            change_camera_sound.play()
                        cama6_active = True
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        camera_area_text1 = "Kitchen"
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = kitchen_image
                        last_move_time = current_time
                    if a7_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama7_active = True
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_restrooms == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Restrooms"
                        update_restrooms = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = restrooms_image2
                        last_move_time = current_time
                    if a1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama1_active = True
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_show_stage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Show Stage"
                        update_show_stage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_supply_closet = False
                        camera_area.image = show_stage_image2
                        last_move_time = current_time
                    if b1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb1_active = True
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camc1_active = False
                        if update_dining_area == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Dining Area"
                        update_dining_area = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = dining_area_image2
                        last_move_time = current_time
                    if c1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camc1_active = True
                        camb1_active = False
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        if update_pirate_cove == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Pirates Cove"
                        update_pirate_cove = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = pirate_cove_image2
                        
                        last_move_time = current_time
        if power_out == True:
            sec_power += 1
        if sec_power == 420:
            music_box.play()
            power_out_fred_active = True
        if sec_power == 1320:
            power_out_fred_active = False
        if sec_power == 1500:
            jumpscare_sound.play() 
            jumpscare_end_fred = True
            stop_left = True
            stop_right = True
            show_camera = False
        sec_fred_move += 1
        sec_fox_move += 1
        current_time3 = pygame.time.get_ticks()
        # Check if it's time to flicker
        if current_time3 - last_flicker_time >= flicker_interval and power_out_fred_active == True:
            show_power_out_fred = not show_power_out_fred  # Toggle visibility
            last_flicker_time = current_time3

        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama2_active == True:
            show_green_cama2_flicker = not show_green_cama2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb2_active == True:
            show_green_camb2_flicker = not show_green_camb2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama4_active == True:
            show_green_cama4_flicker = not show_green_cama4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb4_active == True:
            show_green_camb4_flicker = not show_green_camb4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama3_active == True:
            show_green_cama3_flicker = not show_green_cama3_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama5_active == True:
            show_green_cama5_flicker = not show_green_cama5_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama6_active == True:
            show_green_cama6_flicker = not show_green_cama6_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama7_active == True:
            show_green_cama7_flicker = not show_green_cama7_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama1_active == True:
            show_green_cama1_flicker = not show_green_cama1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb1_active == True:
            show_green_camb1_flicker = not show_green_camb1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camc1_active == True:
            show_green_camc1_flicker = not show_green_camc1_flicker  # Toggle visibility
            last_flicker_time = current_time3

        current_time2 = time.time()
        if current_time2 - last_event_time >= event_interval and power_out == False:
            sec_number3 += 1   
            rng = random.randint(1, 20)
            print(rng)
            #freddy fazbear
            if show_camera == False:
                sec_fred_move = 0
                if fred_ai_number >= rng and sec_fred_move >= 1000 - 100 * fred_ai_number:
                    fred_stage_number += 1
                    print("Fred Stage INCREASED!!!!!!!")
                    if fred_stage_number == 1 and chica_stage_number == 1 and bonnie_stage_number == 1:
                        show_stage_image2 = show_stage_image
                    if fred_stage_number == 2:
                        show_stage_image2 = show_stage_stage4_image
                    if fred_stage_number >= 6:
                        e_hall_corner_image2 = e_hall_corner_stage3_image
            if camera_area.image != e_hall_corner_image2 and show_right_door == False and fred_stage_number >= 6:
                jumpscare_end_fred = True
                jumpscare_sound.play()
                stop_left = True
                stop_right = True
                show_camera = False
            if camera_area.image != e_hall_corner_image2 and show_right_door == True and fred_stage_number >= 6:
                e_hall_corner_image2 = e_hall_corner_image
                fred_stage_number = 5
                    
            #foxy
            if show_camera == False and sec_fox_move >= random.randint(50, 1000):
                sec_fox_move = 0
                if fox_ai_number >= rng:
                    pirate_cove_stage_number += 1
                    print("fox stage increased!")
                    if pirate_cove_stage_number == 1:
                        pirate_cove_image2 = pirate_cove_image
                        
                    if pirate_cove_image2 == pirate_cove_image and pirate_cove_stage_number == 2:
                        pirate_cove_image2 = pirate_cove_stage2_image    

                    if pirate_cove_image2 == pirate_cove_stage2_image and pirate_cove_stage_number == 3:
                        pirate_cove_image2 = pirate_cove_stage3_image
                        
                    if pirate_cove_image2 == pirate_cove_stage3_image and pirate_cove_stage_number == 4:
                        sec_number3 = 0
                        pirate_cove_image2 = pirate_cove_stage4_image
                    
            
            
            if fox_ai_number >= rng:   
                if sec_number3 == 5 and show_left_door == True or camera_area.image == w_hall_image2 and show_left_door == True:
                    play_next_sound()
                    power_number -= 1
                    pirate_cove_image2 = pirate_cove_image
                    sec_number3 = 0
                    pirate_cove_stage_number = 1
                if sec_number3 == 5 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image or camera_area.image == w_hall_image2 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image:
                    jumpscare_end_fox = True
                    jumpscare_sound.play()
                    stop_left = True
                    stop_right = True
                    show_camera = False
                
            #bonnie
            if bon_ai_number >= rng:
                bonnie_stage_number += 1
                print("bonnie stage increased!")
                if bonnie_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if bonnie_stage_number == 2:
                    show_stage_image2 = show_stage_stage2_image
                    dining_area_image2 = dining_area_stage2_image
                if bonnie_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    backstage_image2 = backstage_stage2_image
                if bonnie_stage_number == 4:
                    backstage_image2 = backstage_image
                    w_hall_image2 = w_hall_stage2_image
                if bonnie_stage_number == 5:
                    w_hall_image2 = w_hall_image
                    supply_closet_image2 = supply_closet_stage2_image
                if bonnie_stage_number == 6:
                    loud_footsteps_sound.play()
                    supply_closet_image2 = supply_closet_image
                    w_hall_corner_image2 = w_hall_corner_stage2_image
                if bonnie_stage_number >= 7:
                    w_hall_corner_image2 = w_hall_corner_image
                    show_bon = True

            if bon_ai_number >= rng and show_left_door == True and show_bon == True:
                show_bon = False
                quiet_footsteps_sound.play()
                bonnie_stage_number = 2
                sec_number2 = 0
            if bon_ai_number < rng:
                print("bonnie failed to move")
            if show_bon == True and show_left_light == True and show_camera == False:
                jump_sound.play()
            if show_bon == True and show_left_door == False:
                sec_number2 += 1
            if sec_number2 >= 2 and show_left_door == False and bon_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end = True
                show_bon = True
                show_left_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                bon.image = pygame.transform.scale(bon.image, (5000, 1000))
                
            
            #chica
            if chic_ai_number >= rng:
                chica_stage_number += 1
                print("Chica Stage Increased!!!")
                if chica_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if chica_stage_number == 2:
                    show_stage_image2 = show_stage_stage3_image
                    dining_area_image2 = dining_area_stage3_image
                if chica_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    restrooms_image2 = restrooms_stage2_image
                if chica_stage_number == 4:
                    restrooms_image2 = restrooms_image
                if chica_stage_number == 5:
                    e_hall_image2 = e_hall_stage2_image
                if chica_stage_number == 6:
                    loud_footsteps_sound.play()
                    e_hall_image2 = e_hall_image
                    e_hall_corner_image2 = e_hall_corner_stage2_image
                if chica_stage_number == 7:
                    e_hall_corner_image2 = e_hall_corner_image
                    show_chic = True

            if chic_ai_number >= rng and show_right_door == True and show_chic == True:
                show_chic = False
                quiet_footsteps_sound.play()
                chica_stage_number = 2
                sec_number4 = 0
            if chic_ai_number < rng:
                print("chica failed to move")
            if show_chic == True and show_right_light == True and show_camera == False:
                jump_sound.play()
            if show_chic == True and show_right_door == False:
                sec_number4 += 1
            if sec_number4 >= 2 and show_right_door == False and chic_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end_chic = True
                show_chic = True
                show_right_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                chic.image = pygame.transform.scale(chic.image, (2500, 1000))
                chic.x = bon.x

            last_event_time = current_time2

        if jumpscare_end == True:
            sec += 1
            phoneguy_night1.stop()
            show_bon = True
            show_left_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec >= 70:
            mainmenu()
        
        if jumpscare_end_chic == True:
            sec_chic += 1
            phoneguy_night1.stop()
            show_chic = True
            show_right_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_chic >= 70:
            mainmenu()
        
        if jumpscare_end_fox == True:
            sec_fox += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fox >= 140:
            mainmenu()

        if jumpscare_end_fred == True:
            sec_fred += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fred >= 70:
            mainmenu()

        if show_camera == True and update_pirate_cove == True:
            camera_area.image = pirate_cove_image2

        if show_camera == True and update_backstage == True:
            camera_area.image = backstage_image2

        if show_camera == True and update_dining_area == True:
            camera_area.image = dining_area_image2

        if show_camera == True and update_e_hall == True:
            camera_area.image = e_hall_image2

        if show_camera == True and update_e_hall_corner == True:
            camera_area.image = e_hall_corner_image2

        if show_camera == True and update_restrooms == True:
            camera_area.image = restrooms_image2

        if show_camera == True and update_show_stage == True:
            camera_area.image = show_stage_image2

        if show_camera == True and update_supply_closet == True:
            camera_area.image = supply_closet_image2
        
        if show_camera == True and update_w_hall == True:
            camera_area.image = w_hall_image2
        
        if show_camera == True and update_w_hall_corner == True:
            camera_area.image = w_hall_corner_image2
            

        if stop_left == False and camerax < -100:
            camerax += 10
            
        if stop_right == False and camerax > -500:
            camerax -= 10

        if stop_left == False and officex < -5:
            officex += 10
            boop_button.x += 10
            left_light.x += 10
            right_light.x += 10
            left_door.x += 10
            right_door.x += 10
            bon.x += 10
            chic.x += 10
            light_button.x += 10
            light_button2.x += 10
            light_button_on.x += 10
            light_button_on2.x += 10
            door_button.x += 10
            door_button2.x += 10
            door_button_on.x += 10
            door_button_on2.x += 10
        if stop_right == False and officex > -970:
            officex -= 10
            boop_button.x -= 10
            left_light.x -= 10
            right_light.x -= 10
            left_door.x -= 10
            right_door.x -= 10
            bon.x -= 10
            chic.x -= 10
            light_button.x -= 10
            light_button2.x -= 10
            light_button_on.x -= 10
            light_button_on2.x -= 10
            door_button.x -= 10
            door_button2.x -= 10
            door_button_on.x -= 10
            door_button_on2.x -= 10

        sec_number5 += 1
        if sec_number5 >= 180:
            power_number -= 1
            sec_number5 = 0

        sec_number+=1
        if sec_number == 5400:
            am_number = 1
        if sec_number == 10800:
            bon_ai_number += 1
            am_number = 2
        if sec_number == 16200:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 3
        if sec_number == 21600:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 4
        if sec_number == 27000:
            am_number = 5
        if sec_number == 32400:
            power_out = False
            data_night['custom_night_unlocked'] = True
            with open(os.path.join('data', 'night.json'),'w') as night:
                json.dump(data_night, night)
            win6am()

        if power_number <= 0:
            power_out = True

        if power_out == False:
            Usage_text = Small_Font.render("Usage:", 1, WHITE)
            Power_left_text = Small_Font.render("Power left:", 1, WHITE)
            Night_text = Small_Font.render("Night " + str(int(night_number)), 1, WHITE)
            AM_text = Big_Font.render(str(int(am_number)) + " AM", 1, WHITE)
            Power_number_text = Big_Font.render(str(int(power_number)) + "%", 1, WHITE)
        Light_text = Small_Font.render("LIGHT", 1, WHITE)
        Door_text = Small_Font.render("DOOR", 1, WHITE)
        if power_out == False:
            camera_area_text = Big_Font.render(camera_area_text1, 1, WHITE)
        window.fill((0, 0, 0))
        if power_out == False:
            if show_right_light == True and show_chic == True and show_camera == False:
                window.blit(chic.image, (chic.x, chic.y))
        window.blit(office_bg_image, (officex, 0))
        window.blit(boop_button.image, (boop_button.x, boop_button.y))
        if power_out == False:
            window.blit(camera_button.image, (camera_button.x, camera_button.y))
        if power_out == False:
            if jumpscare_end_chic == True:
                window.blit(chic.image, (chic.x, chic.y))
            if jumpscare_end_fox == True:
                window.blit(fox_image, (bon.x + 100, chic.y))
            if show_camera == True:
                power_number -= 0.0008
                window.blit(camera_area.image, (camerax, camera_area.y))
                window.blit(camera_area_text, (735, 130))
                window.blit(green_bar_image, (125, 670))
                window.blit(map_image, (750, 200))
                if show_green_cama1_flicker == False:
                    a1_button.x = 900
                    a1_on_button.x = 11900
                if show_green_cama2_flicker == False:
                    a2_button.x = 870
                    a2_on_button.x = 11870
                if show_green_camb2_flicker == False:
                    b2_button.x = 870
                    b2_on_button.x = 11870
                if show_green_camc1_flicker == False:
                    c1_button.x = 850
                    c1_on_button.x = 11850
                if show_green_camb1_flicker == False:
                    b1_button.x = 890
                    b1_on_button.x = 11890
                if show_green_cama7_flicker == False:
                    a7_button.x = 1140
                    a7_on_button.x = 111140
                if show_green_cama6_flicker == False:
                    a6_button.x = 1130
                    a6_on_button.x = 111130
                if show_green_cama5_flicker == False:
                    a5_button.x = 730
                    a5_on_button.x = 11730
                if show_green_cama3_flicker == False:
                    a3_button.x = 740
                    a3_on_button.x = 11740
                if show_green_camb4_flicker == False:
                    b4_button.x = 1030
                    b4_on_button.x = 111030
                if show_green_cama4_flicker == False:
                    a4_button.x = 1030
                    a4_on_button.x = 111030
                if show_green_cama2_flicker == True:
                    a2_button.x = 11870
                    a2_on_button.x = 870
                if cama2_active == False:
                    a2_button.x = 870
                if show_green_camb2_flicker == True:
                    b2_button.x = 11870
                    b2_on_button.x = 870
                if camb2_active == False:
                    b2_button.x = 870
                if show_green_camc1_flicker == True:
                    c1_button.x = 11850
                    c1_on_button.x = 850
                if camc1_active == False:
                    c1_button.x = 850
                if show_green_camb1_flicker == True:
                    b1_button.x = 11890
                    b1_on_button.x = 890
                if camb1_active == False:
                    b1_button.x = 890
                if show_green_cama1_flicker == True:
                    a1_button.x = 11900
                    a1_on_button.x = 900
                if cama1_active == False:
                    a1_button.x = 900
                if show_green_cama7_flicker == True:
                    a7_button.x = 111140
                    a7_on_button.x = 1140
                if cama7_active == False:
                    a7_button.x = 1140
                if show_green_cama6_flicker == True:
                    a6_button.x = 111130
                    a6_on_button.x = 1130
                if cama6_active == False:
                    a6_button.x = 1130
                if show_green_cama5_flicker == True:
                    a5_button.x = 11730
                    a5_on_button.x = 730
                if cama5_active == False:
                    a5_button.x = 730
                if show_green_cama3_flicker == True:
                    a3_button.x = 11740
                    a3_on_button.x = 740
                if cama3_active == False:
                    a3_button.x = 740
                if show_green_camb4_flicker == True:
                    b4_button.x = 111030
                    b4_on_button.x = 1030
                if camb4_active == False:
                    b4_button.x = 1030
                if show_green_cama4_flicker == True:
                    a4_button.x = 111030
                    a4_on_button.x = 1030
                if cama4_active == False:
                    a4_button.x = 1030
                window.blit(a2_on_button.image, (a2_on_button.x, a2_on_button.y))
                window.blit(b2_on_button.image, (b2_on_button.x, b2_on_button.y))
                window.blit(a4_on_button.image, (a4_on_button.x, a4_on_button.y))
                window.blit(b4_on_button.image, (b4_on_button.x, b4_on_button.y))
                window.blit(a3_on_button.image, (a3_on_button.x, a3_on_button.y))
                window.blit(a5_on_button.image, (a5_on_button.x, a5_on_button.y))
                window.blit(a6_on_button.image, (a6_on_button.x, a6_on_button.y))
                window.blit(a7_on_button.image, (a7_on_button.x, a7_on_button.y))
                window.blit(a1_on_button.image, (a1_on_button.x, a1_on_button.y))
                window.blit(b1_on_button.image, (b1_on_button.x, b1_on_button.y))
                window.blit(c1_on_button.image, (c1_on_button.x, c1_on_button.y))
                
                window.blit(a2_button.image, (a2_button.x, a2_button.y))           
                window.blit(b2_button.image, (b2_button.x, b2_button.y))             
                window.blit(a4_button.image, (a4_button.x, a4_button.y))              
                window.blit(b4_button.image, (b4_button.x, b4_button.y))              
                window.blit(a3_button.image, (a3_button.x, a3_button.y))  
                window.blit(a5_button.image, (a5_button.x, a5_button.y))               
                window.blit(a6_button.image, (a6_button.x, a6_button.y))    
                window.blit(a7_button.image, (a7_button.x, a7_button.y))             
                window.blit(a1_button.image, (a1_button.x, a1_button.y))             
                window.blit(b1_button.image, (b1_button.x, b1_button.y)) 
                window.blit(c1_button.image, (c1_button.x, c1_button.y))
                window.blit(camera_button2.image, (camera_button2.x, camera_button2.y))
            if show_left_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_left_light == True and show_camera == False:
                window.blit(left_light.image, (left_light.x, left_light.y))
            if show_left_light == True and show_bon == True and show_camera == False:
                window.blit(bon.image, (bon.x, bon.y))
            if show_right_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_right_light == True and show_camera == False:
                window.blit(right_light.image, (right_light.x, right_light.y))
            if show_left_door == True:
                power_number -= 0.002
                window.blit(yellow_bar_image, (150, 670))
            if show_left_door == True and show_camera == False:
                window.blit(left_door.image, (left_door.x, left_door.y))
            if show_right_door == True:
                power_number -= 0.002
                window.blit(red_bar_image, (175, 670))
            if show_right_door == True and show_camera == False:
                window.blit(right_door.image, (right_door.x, right_door.y))
            if show_right_door == False and show_left_door == False and show_right_light == False and show_left_light == False and show_camera == False:
                power_number -= 0
            window.blit(green_bar_image, (100, 670))
            power_number -= 0.0008
        if power_out == True and show_power_out_fred == True and power_out_fred_active == True:
            window.blit(fred_power_out_image, (bon.x, bon.y))

        if jumpscare_end_fred == True:
            fred_image = pygame.transform.scale(fred_image, (2500, 1000))
            window.blit(fred_image, (bon.x, chic.y))

        if show_camera == False:
            window.blit(door_button2.image, (door_button2.x, door_button2.y))
            window.blit(door_button.image, (door_button.x, door_button.y))
            window.blit(door_button_on2.image, (door_button_on2.x, door_button_on2.y))
            window.blit(door_button_on.image, (door_button_on.x, door_button_on.y))

            window.blit(light_button2.image, (light_button2.x, light_button2.y))
            window.blit(light_button.image, (light_button.x, light_button.y))
            window.blit(light_button_on2.image, (light_button_on2.x, light_button_on2.y))
            window.blit(light_button_on.image, (light_button_on.x, light_button_on.y))

            office_bg_image.blit(Light_text, (50, 500))
            office_bg_image.blit(Light_text, (2150, 500))
            office_bg_image.blit(Door_text, (50, 350))
            office_bg_image.blit(Door_text, (2150, 350))
        if power_out == False:
            window.blit(AM_text, (1150, 0))
            window.blit(Night_text, (1150, 50))
            window.blit(Usage_text, (0, 660))
            window.blit(Power_left_text, (0, 600))
            window.blit(Power_number_text, (160, 590))
        pygame.display.update()

def custom_night():
    with open(os.path.join('data','night.json')) as night:
        data_night = json.load(night)
    data_night['custom_night_on'] = False
    
    sec = 0
    sec_power = 0
    sec_chic = 0
    sec_fox = 0
    sec_fred = 0
    camera_area_text1 = "W. Hall Corner"

    fred_image = pygame.image.load(os.path.join('Images', 'animatronics', 'fred.png'))

    pirate_cove_image2 = pirate_cove_image
    show_stage_image2 = show_stage_image
    w_hall_corner_image2 = w_hall_corner_image
    w_hall_image2 = w_hall_image
    supply_closet_image2 = supply_closet_image
    restrooms_image2 = restrooms_image
    e_hall_corner_image2 = e_hall_corner_image
    e_hall_image2 = e_hall_image
    dining_area_image2 = dining_area_image
    backstage_image2 = backstage_image

    bon_ai_number = data_night['bon_ai']
    fox_ai_number = data_night['fox_ai']
    chic_ai_number = data_night['chic_ai']
    fred_ai_number = data_night['fred_ai']

    move_delay = 250  # milliseconds
    move_delay_camera = 450  # milliseconds
    last_move_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    run = True
    light_button = button(1850, 400, 100, 100, light_button_image)
    light_button2 = button(-250, 400, 100, 100, light_button_image)
    light_button_on = button(8150, 400, 100, 100, light_button_on_image)
    light_button_on2 = button(8150, 400, 100, 100, light_button_on_image)
    door_button = button(1850, 250, 100, 100, door_button_image)
    door_button2 = button(-250, 250, 100, 100, door_button_image)
    door_button_on = button(8150, 250, 100, 100, door_button_on_image)
    door_button_on2 = button(8150, 250, 100, 100, door_button_on_image)
    left_light = button(-100, 30, 200, 700, left_light_image)
    right_light = button(1600, 30, 200, 700, right_light_image)
    left_door = button(-100, 30, 200, 700, left_door_image)
    right_door = button(1600, 30, 200, 700, right_door_image)
    bon = button(-100, 30, 500, 700, bon_image)
    chic = button(1300, 10, 200, 550, chic_image)
    camera_button = button(300, 650, 500, 50, camera_button_image)
    camera_button2 = button(21500, 650, 500, 50, camera_button_image)
    a2_button = button(870, 550, 95, 65, a2_image)
    a2_on_button = button(11870, 550, 95, 65, a2_on_image)
    b2_button = button(870, 615, 95, 65, b2_image)
    b2_on_button = button(11870, 615, 95, 65, b2_on_image)
    a4_button = button(1030, 550, 95, 65, a4_image)
    a4_on_button = button(111030, 550, 95, 65, a4_on_image)
    b4_button = button(1030, 615, 95, 65, b4_image)
    b4_on_button = button(111030, 615, 95, 65, b4_on_image)
    a3_button = button(740, 500, 95, 65, a3_image)
    a3_on_button = button(11740, 500, 95, 65, a3_on_image)
    a5_button = button(730, 330, 95, 65, a5_image)
    a5_on_button = button(11730, 330, 95, 65, a5_on_image)
    a6_button = button(1130, 500, 95, 65, a6_image)
    a6_on_button = button(111130, 500, 95, 65, a6_on_image)
    a7_button = button(1140, 300, 95, 65, a7_image)
    a7_on_button = button(111140, 300, 95, 65, a7_on_image)
    a1_button = button(900, 200, 95, 65, a1_image)
    a1_on_button = button(11900, 200, 95, 65, a1_on_image)
    b1_button = button(890, 300, 95, 65, b1_image)
    b1_on_button = button(11890, 300, 95, 65, b1_on_image)
    c1_button = button(850, 400, 95, 65, c1_image)
    c1_on_button = button(11850, 400, 95, 65, c1_on_image)
    camera_area = button(-300, 0, 2250, 720, pirate_cove_image)
    boop_button = button(650, 150, 10, 10, boop_image)
    
    officex = -300
    camerax = -300
    last_event_time = time.time()
    event_interval = 5  # Time interval in seconds

    flicker_interval = 500  # milliseconds
    last_flicker_time = pygame.time.get_ticks()
    show_power_out_fred = True

    update_pirate_cove = True
    update_backstage = True
    update_dining_area = True
    update_e_hall = True
    update_e_hall_corner = True
    update_restrooms = True
    update_show_stage = True
    update_supply_closet = True
    update_w_hall = True
    update_w_hall_corner = True

    stop_left = True
    stop_right = True
    show_left_light = False
    show_right_light = False
    show_left_door = False
    show_right_door = False
    show_bon = False
    show_chic = False
    show_camera = False
    jumpscare_end = False
    jumpscare_end_chic = False
    jumpscare_end_fox = False
    jumpscare_end_fred = False
    power_out = False
    power_out_fred_active = False
    cama2_active = False
    camb2_active = True
    cama4_active = False
    camb4_active = False
    cama3_active = False
    cama5_active = False
    cama6_active = False
    cama7_active = False
    cama1_active = False
    camb1_active = False
    camc1_active = False
    show_green_cama2_flicker = False
    show_green_camb2_flicker = False
    show_green_cama4_flicker = False
    show_green_camb4_flicker = False
    show_green_cama3_flicker = False
    show_green_cama5_flicker = False
    show_green_cama6_flicker = False
    show_green_cama7_flicker = False
    show_green_cama1_flicker = False
    show_green_camb1_flicker = False
    show_green_camc1_flicker = False

    night_number = 7
    am_number = 12
    power_number = 100
    sec_number = 0
    sec_number2 = 0
    sec_number3 = 0
    sec_number4 = 0
    sec_number5 = 0
    sec_fred_move = 0
    sec_fox_move = 0

    pirate_cove_stage_number = 1
    bonnie_stage_number = 1
    chica_stage_number = 1
    fred_stage_number = 1
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(os.path.join('data', 'night.json'),'w') as night:
                    json.dump(data_night, night)
                run = False
                pygame.quit()
            current_time = pygame.time.get_ticks()

            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
                camera_button_rect = pygame.Rect(camera_button.x, camera_button.y, camera_button.width, camera_button.height)
                camera_button2_rect = pygame.Rect(camera_button2.x, camera_button2.y, camera_button2.width, camera_button2.height)
                if mousex < 400:
                    stop_left = False
                elif mousex > 900:
                    stop_right = False
                else:
                    stop_left = True
                    stop_right = True
                if power_out == False:
                    if camera_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 21500
                        camera_button2.x = 300
                        show_camera = True
                        last_move_time = current_time
                    if camera_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay_camera:
                        camera_sound.play()
                        camera_button.x = 300
                        camera_button2.x = 21500
                        show_camera = False
                        last_move_time = current_time
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                light_button_rect = pygame.Rect(light_button.x, light_button.y, light_button.width, light_button.height)
                light_button2_rect = pygame.Rect(light_button2.x, light_button2.y, light_button2.width, light_button2.height)
                light_button_on_rect = pygame.Rect(light_button_on.x, light_button_on.y, light_button_on.width, light_button_on.height)
                light_button_on2_rect = pygame.Rect(light_button_on2.x, light_button_on2.y, light_button_on2.width, light_button_on2.height)
                door_button_rect = pygame.Rect(door_button.x, door_button.y, door_button.width, door_button.height)
                door_button2_rect = pygame.Rect(door_button2.x, door_button2.y, door_button2.width, door_button2.height)
                door_button_on_rect = pygame.Rect(door_button_on.x, door_button_on.y, door_button_on.width, door_button_on.height)
                door_button_on2_rect = pygame.Rect(door_button_on2.x, door_button_on2.y, door_button_on2.width, door_button_on2.height)

                boop_button_rect = pygame.Rect(boop_button.x, boop_button.y, boop_button.width, boop_button.height)

                a2_button_rect = pygame.Rect(a2_button.x, a2_button.y, a2_button.width, a2_button.height)
                b2_button_rect = pygame.Rect(b2_button.x, b2_button.y, b2_button.width, b2_button.height)
                a4_button_rect = pygame.Rect(a4_button.x, a4_button.y, a4_button.width, a4_button.height)
                b4_button_rect = pygame.Rect(b4_button.x, b4_button.y, b4_button.width, b4_button.height)
                a3_button_rect = pygame.Rect(a3_button.x, a3_button.y, a3_button.width, a3_button.height)
                a5_button_rect = pygame.Rect(a5_button.x, a5_button.y, a5_button.width, a5_button.height)
                a6_button_rect = pygame.Rect(a6_button.x, a6_button.y, a6_button.width, a6_button.height)
                a7_button_rect = pygame.Rect(a7_button.x, a7_button.y, a7_button.width, a7_button.height)
                a1_button_rect = pygame.Rect(a1_button.x, a1_button.y, a1_button.width, a1_button.height)
                b1_button_rect = pygame.Rect(b1_button.x, b1_button.y, b1_button.width, b1_button.height)
                c1_button_rect = pygame.Rect(c1_button.x, c1_button.y, c1_button.width, c1_button.height)

                if show_camera == False and power_out == False:

                    if door_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_right_door = True
                        door_button_on.x = 1180
                        door_button.x = 8150
                        last_move_time = current_time
                    if door_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_close_sound.play()
                        show_left_door = True
                        door_button_on2.x = 50
                        door_button2.x = 8150
                        last_move_time = current_time
                    if door_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_right_door = False
                        door_button_on.x = 8150
                        door_button.x = 1180
                        last_move_time = current_time
                    if door_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        door_open_sound.play()
                        show_left_door = False
                        door_button_on2.x = 8150
                        door_button2.x = 50
                        last_move_time = current_time

                    if light_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_right_light = True
                        light_button_on.x = 1180
                        light_button.x = 8150
                        last_move_time = current_time
                    if light_button2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_on_sound.play()
                        show_left_light = True
                        light_button_on2.x = 50
                        light_button2.x = 8150
                        last_move_time = current_time
                    if light_button_on_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_right_light = False
                        light_button_on.x = 8150
                        light_button.x = 1180
                        last_move_time = current_time
                    if light_button_on2_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        light_off_sound.play()
                        show_left_light = False
                        light_button_on2.x = 8150
                        light_button2.x = 50
                        last_move_time = current_time
                if show_camera == False:
                    if boop_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        boop_sound.play()
                        last_move_time = current_time
                if show_camera == True:
                    if a2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama2_active = True
                        camb2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "West Hall"
                        update_w_hall = True
                        update_pirate_cove = False
                        update_w_hall_corner = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_image2
                        last_move_time = current_time
                    if b2_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb2_active = True
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama4_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_w_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "W. Hall Corner"
                        update_w_hall_corner = True
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = w_hall_corner_image2
                        last_move_time = current_time
                    if a4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama4_active = True
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camb4_active = False
                        camc1_active = False
                        if update_e_hall == False:
                            change_camera_sound.play()
                        camera_area_text1 = "East Hall"
                        update_e_hall = True
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_e_hall_corner = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_image2
                        last_move_time = current_time
                    if b4_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb4_active = True
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama3_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_e_hall_corner == False:
                            change_camera_sound.play()
                        camera_area_text1 = "E. Hall Corner"
                        update_e_hall_corner = True
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = e_hall_corner_image2
                        last_move_time = current_time
                    if a3_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama3_active = True
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama5_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_supply_closet == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Supply Closet"
                        update_supply_closet = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        camera_area.image = supply_closet_image2
                        last_move_time = current_time
                    if a5_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama5_active = True
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama6_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_backstage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Backstage"
                        update_backstage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = backstage_image2
                        last_move_time = current_time
                    if a6_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        if cama6_active == False:
                            change_camera_sound.play()
                        cama6_active = True
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        cama7_active = False
                        camb1_active = False
                        camc1_active = False
                        camera_area_text1 = "Kitchen"
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = kitchen_image
                        last_move_time = current_time
                    if a7_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama7_active = True
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        cama1_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_restrooms == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Restrooms"
                        update_restrooms = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = restrooms_image2
                        last_move_time = current_time
                    if a1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        cama1_active = True
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camb1_active = False
                        camc1_active = False
                        if update_show_stage == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Show Stage"
                        update_show_stage = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_supply_closet = False
                        camera_area.image = show_stage_image2
                        last_move_time = current_time
                    if b1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camb1_active = True
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        camc1_active = False
                        if update_dining_area == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Dining Area"
                        update_dining_area = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_pirate_cove = False
                        update_restrooms = False
                        update_backstage = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = dining_area_image2
                        last_move_time = current_time
                    if c1_button_rect.collidepoint(mousex, mousey) and current_time - last_move_time > move_delay:
                        camc1_active = True
                        camb1_active = False
                        cama1_active = False
                        cama7_active = False
                        cama6_active = False
                        cama5_active = False
                        cama3_active = False
                        camb4_active = False
                        cama4_active = False
                        camb2_active = False
                        cama2_active = False
                        if update_pirate_cove == False:
                            change_camera_sound.play()
                        camera_area_text1 = "Pirates Cove"
                        update_pirate_cove = True
                        update_e_hall_corner = False
                        update_e_hall = False
                        update_w_hall_corner = False
                        update_w_hall = False
                        update_restrooms = False
                        update_backstage = False
                        update_dining_area = False
                        update_show_stage = False
                        update_supply_closet = False
                        camera_area.image = pirate_cove_image2
                        
                        last_move_time = current_time
        if power_out == True:
            sec_power += 1
        if sec_power == 420:
            music_box.play()
            power_out_fred_active = True
        if sec_power == 1320:
            power_out_fred_active = False
        if sec_power == 1500:
            jumpscare_sound.play() 
            jumpscare_end_fred = True
            stop_left = True
            stop_right = True
            show_camera = False
        sec_fred_move += 1
        sec_fox_move += 1
        current_time3 = pygame.time.get_ticks()
        # Check if it's time to flicker
        if current_time3 - last_flicker_time >= flicker_interval and power_out_fred_active == True:
            show_power_out_fred = not show_power_out_fred  # Toggle visibility
            last_flicker_time = current_time3

        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama2_active == True:
            show_green_cama2_flicker = not show_green_cama2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb2_active == True:
            show_green_camb2_flicker = not show_green_camb2_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama4_active == True:
            show_green_cama4_flicker = not show_green_cama4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb4_active == True:
            show_green_camb4_flicker = not show_green_camb4_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama3_active == True:
            show_green_cama3_flicker = not show_green_cama3_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama5_active == True:
            show_green_cama5_flicker = not show_green_cama5_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama6_active == True:
            show_green_cama6_flicker = not show_green_cama6_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama7_active == True:
            show_green_cama7_flicker = not show_green_cama7_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and cama1_active == True:
            show_green_cama1_flicker = not show_green_cama1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camb1_active == True:
            show_green_camb1_flicker = not show_green_camb1_flicker
            last_flicker_time = current_time3
        if current_time3 - last_flicker_time >= flicker_interval and show_camera == True and camc1_active == True:
            show_green_camc1_flicker = not show_green_camc1_flicker  # Toggle visibility
            last_flicker_time = current_time3

        current_time2 = time.time()
        if current_time2 - last_event_time >= event_interval and power_out == False:
            sec_number3 += 1   
            rng = random.randint(1, 20)
            print(rng)
            #freddy fazbear
            if show_camera == False:
                sec_fred_move = 0
                if fred_ai_number >= rng and sec_fred_move >= 1000 - 100 * fred_ai_number:
                    fred_stage_number += 1
                    print("Fred Stage INCREASED!!!!!!!")
                    if fred_stage_number == 1 and chica_stage_number == 1 and bonnie_stage_number == 1:
                        show_stage_image2 = show_stage_image
                    if fred_stage_number == 2:
                        show_stage_image2 = show_stage_stage4_image
                    if fred_stage_number >= 6:
                        e_hall_corner_image2 = e_hall_corner_stage3_image
            if camera_area.image != e_hall_corner_image2 and show_right_door == False and fred_stage_number >= 6:
                jumpscare_end_fred = True
                jumpscare_sound.play()
                stop_left = True
                stop_right = True
                show_camera = False
            if camera_area.image != e_hall_corner_image2 and show_right_door == True and fred_stage_number >= 6:
                e_hall_corner_image2 = e_hall_corner_image
                fred_stage_number = 5
                    
            #foxy
            if show_camera == False and sec_fox_move >= random.randint(50, 1000):
                sec_fox_move = 0
                if fox_ai_number >= rng:
                    pirate_cove_stage_number += 1
                    print("fox stage increased!")
                    if pirate_cove_stage_number == 1:
                        pirate_cove_image2 = pirate_cove_image
                        
                    if pirate_cove_image2 == pirate_cove_image and pirate_cove_stage_number == 2:
                        pirate_cove_image2 = pirate_cove_stage2_image    

                    if pirate_cove_image2 == pirate_cove_stage2_image and pirate_cove_stage_number == 3:
                        pirate_cove_image2 = pirate_cove_stage3_image
                        
                    if pirate_cove_image2 == pirate_cove_stage3_image and pirate_cove_stage_number == 4:
                        sec_number3 = 0
                        pirate_cove_image2 = pirate_cove_stage4_image
                    
            
            
            if fox_ai_number >= rng:   
                if sec_number3 == 5 and show_left_door == True or camera_area.image == w_hall_image2 and show_left_door == True:
                    play_next_sound()
                    power_number -= 1
                    pirate_cove_image2 = pirate_cove_image
                    sec_number3 = 0
                    pirate_cove_stage_number = 1
                if sec_number3 == 5 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image or camera_area.image == w_hall_image2 and show_left_door == False and pirate_cove_image2 == pirate_cove_stage4_image:
                    jumpscare_end_fox = True
                    jumpscare_sound.play()
                    stop_left = True
                    stop_right = True
                    show_camera = False
                
            #bonnie
            if bon_ai_number >= rng:
                bonnie_stage_number += 1
                print("bonnie stage increased!")
                if bonnie_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if bonnie_stage_number == 2:
                    show_stage_image2 = show_stage_stage2_image
                    dining_area_image2 = dining_area_stage2_image
                if bonnie_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    backstage_image2 = backstage_stage2_image
                if bonnie_stage_number == 4:
                    backstage_image2 = backstage_image
                    w_hall_image2 = w_hall_stage2_image
                if bonnie_stage_number == 5:
                    w_hall_image2 = w_hall_image
                    supply_closet_image2 = supply_closet_stage2_image
                if bonnie_stage_number == 6:
                    loud_footsteps_sound.play()
                    supply_closet_image2 = supply_closet_image
                    w_hall_corner_image2 = w_hall_corner_stage2_image
                if bonnie_stage_number >= 7:
                    w_hall_corner_image2 = w_hall_corner_image
                    show_bon = True

            if bon_ai_number >= rng and show_left_door == True and show_bon == True:
                show_bon = False
                quiet_footsteps_sound.play()
                bonnie_stage_number = 2
                sec_number2 = 0
            if bon_ai_number < rng:
                print("bonnie failed to move")
            if show_bon == True and show_left_light == True and show_camera == False:
                jump_sound.play()
            if show_bon == True and show_left_door == False:
                sec_number2 += 1
            if sec_number2 >= 2 and show_left_door == False and bon_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end = True
                show_bon = True
                show_left_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                bon.image = pygame.transform.scale(bon.image, (5000, 1000))
                
            
            #chica
            if chic_ai_number >= rng:
                chica_stage_number += 1
                print("Chica Stage Increased!!!")
                if chica_stage_number == 1:
                    show_stage_image2 = show_stage_image
                if chica_stage_number == 2:
                    show_stage_image2 = show_stage_stage3_image
                    dining_area_image2 = dining_area_stage3_image
                if chica_stage_number == 3:
                    dining_area_image2 = dining_area_image
                    restrooms_image2 = restrooms_stage2_image
                if chica_stage_number == 4:
                    restrooms_image2 = restrooms_image
                if chica_stage_number == 5:
                    e_hall_image2 = e_hall_stage2_image
                if chica_stage_number == 6:
                    loud_footsteps_sound.play()
                    e_hall_image2 = e_hall_image
                    e_hall_corner_image2 = e_hall_corner_stage2_image
                if chica_stage_number == 7:
                    e_hall_corner_image2 = e_hall_corner_image
                    show_chic = True

            if chic_ai_number >= rng and show_right_door == True and show_chic == True:
                show_chic = False
                quiet_footsteps_sound.play()
                chica_stage_number = 2
                sec_number4 = 0
            if chic_ai_number < rng:
                print("chica failed to move")
            if show_chic == True and show_right_light == True and show_camera == False:
                jump_sound.play()
            if show_chic == True and show_right_door == False:
                sec_number4 += 1
            if sec_number4 >= 2 and show_right_door == False and chic_ai_number >= rng:
                jumpscare_sound.play() 
                jumpscare_end_chic = True
                show_chic = True
                show_right_light = True
                stop_left = True
                stop_right = True
                show_camera = False
                chic.image = pygame.transform.scale(chic.image, (2500, 1000))
                chic.x = bon.x

            last_event_time = current_time2

        if jumpscare_end == True:
            sec += 1
            phoneguy_night1.stop()
            show_bon = True
            show_left_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec >= 70:
            mainmenu()
        
        if jumpscare_end_chic == True:
            sec_chic += 1
            phoneguy_night1.stop()
            show_chic = True
            show_right_light = True
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_chic >= 70:
            mainmenu()
        
        if jumpscare_end_fox == True:
            sec_fox += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fox >= 140:
            mainmenu()

        if jumpscare_end_fred == True:
            sec_fred += 1
            phoneguy_night1.stop()
            stop_left = True
            stop_right = True
            show_camera = False
        if sec_fred >= 70:
            mainmenu()

        if show_camera == True and update_pirate_cove == True:
            camera_area.image = pirate_cove_image2

        if show_camera == True and update_backstage == True:
            camera_area.image = backstage_image2

        if show_camera == True and update_dining_area == True:
            camera_area.image = dining_area_image2

        if show_camera == True and update_e_hall == True:
            camera_area.image = e_hall_image2

        if show_camera == True and update_e_hall_corner == True:
            camera_area.image = e_hall_corner_image2

        if show_camera == True and update_restrooms == True:
            camera_area.image = restrooms_image2

        if show_camera == True and update_show_stage == True:
            camera_area.image = show_stage_image2

        if show_camera == True and update_supply_closet == True:
            camera_area.image = supply_closet_image2
        
        if show_camera == True and update_w_hall == True:
            camera_area.image = w_hall_image2
        
        if show_camera == True and update_w_hall_corner == True:
            camera_area.image = w_hall_corner_image2
            

        if stop_left == False and camerax < -100:
            camerax += 10
            
        if stop_right == False and camerax > -500:
            camerax -= 10

        if stop_left == False and officex < -5:
            officex += 10
            boop_button.x += 10
            left_light.x += 10
            right_light.x += 10
            left_door.x += 10
            right_door.x += 10
            bon.x += 10
            chic.x += 10
            light_button.x += 10
            light_button2.x += 10
            light_button_on.x += 10
            light_button_on2.x += 10
            door_button.x += 10
            door_button2.x += 10
            door_button_on.x += 10
            door_button_on2.x += 10
        if stop_right == False and officex > -970:
            officex -= 10
            boop_button.x -= 10
            left_light.x -= 10
            right_light.x -= 10
            left_door.x -= 10
            right_door.x -= 10
            bon.x -= 10
            chic.x -= 10
            light_button.x -= 10
            light_button2.x -= 10
            light_button_on.x -= 10
            light_button_on2.x -= 10
            door_button.x -= 10
            door_button2.x -= 10
            door_button_on.x -= 10
            door_button_on2.x -= 10

        sec_number5 += 1
        if sec_number5 >= 180:
            power_number -= 1
            sec_number5 = 0

        sec_number+=1
        if sec_number == 5400:
            am_number = 1
        if sec_number == 10800:
            bon_ai_number += 1
            am_number = 2
        if sec_number == 16200:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 3
        if sec_number == 21600:
            bon_ai_number += 1
            chic_ai_number += 1
            fox_ai_number += 1
            am_number = 4
        if sec_number == 27000:
            am_number = 5
        if sec_number == 32400:
            power_out = False
            with open(os.path.join('data', 'night.json'),'w') as night:
                json.dump(data_night, night)
            win6am()

        if power_number <= 0:
            power_out = True

        if power_out == False:
            Usage_text = Small_Font.render("Usage:", 1, WHITE)
            Power_left_text = Small_Font.render("Power left:", 1, WHITE)
            Night_text = Small_Font.render("Night " + str(int(night_number)), 1, WHITE)
            AM_text = Big_Font.render(str(int(am_number)) + " AM", 1, WHITE)
            Power_number_text = Big_Font.render(str(int(power_number)) + "%", 1, WHITE)
        Light_text = Small_Font.render("LIGHT", 1, WHITE)
        Door_text = Small_Font.render("DOOR", 1, WHITE)
        if power_out == False:
            camera_area_text = Big_Font.render(camera_area_text1, 1, WHITE)
        window.fill((0, 0, 0))
        if power_out == False:
            if show_right_light == True and show_chic == True and show_camera == False:
                window.blit(chic.image, (chic.x, chic.y))
        window.blit(office_bg_image, (officex, 0))
        window.blit(boop_button.image, (boop_button.x, boop_button.y))
        if power_out == False:
            window.blit(camera_button.image, (camera_button.x, camera_button.y))
        if power_out == False:
            if jumpscare_end_chic == True:
                window.blit(chic.image, (chic.x, chic.y))
            if jumpscare_end_fox == True:
                window.blit(fox_image, (bon.x + 100, chic.y))
            if show_camera == True:
                power_number -= 0.0008
                window.blit(camera_area.image, (camerax, camera_area.y))
                window.blit(camera_area_text, (735, 130))
                window.blit(green_bar_image, (125, 670))
                window.blit(map_image, (750, 200))
                if show_green_cama1_flicker == False:
                    a1_button.x = 900
                    a1_on_button.x = 11900
                if show_green_cama2_flicker == False:
                    a2_button.x = 870
                    a2_on_button.x = 11870
                if show_green_camb2_flicker == False:
                    b2_button.x = 870
                    b2_on_button.x = 11870
                if show_green_camc1_flicker == False:
                    c1_button.x = 850
                    c1_on_button.x = 11850
                if show_green_camb1_flicker == False:
                    b1_button.x = 890
                    b1_on_button.x = 11890
                if show_green_cama7_flicker == False:
                    a7_button.x = 1140
                    a7_on_button.x = 111140
                if show_green_cama6_flicker == False:
                    a6_button.x = 1130
                    a6_on_button.x = 111130
                if show_green_cama5_flicker == False:
                    a5_button.x = 730
                    a5_on_button.x = 11730
                if show_green_cama3_flicker == False:
                    a3_button.x = 740
                    a3_on_button.x = 11740
                if show_green_camb4_flicker == False:
                    b4_button.x = 1030
                    b4_on_button.x = 111030
                if show_green_cama4_flicker == False:
                    a4_button.x = 1030
                    a4_on_button.x = 111030
                if show_green_cama2_flicker == True:
                    a2_button.x = 11870
                    a2_on_button.x = 870
                if cama2_active == False:
                    a2_button.x = 870
                if show_green_camb2_flicker == True:
                    b2_button.x = 11870
                    b2_on_button.x = 870
                if camb2_active == False:
                    b2_button.x = 870
                if show_green_camc1_flicker == True:
                    c1_button.x = 11850
                    c1_on_button.x = 850
                if camc1_active == False:
                    c1_button.x = 850
                if show_green_camb1_flicker == True:
                    b1_button.x = 11890
                    b1_on_button.x = 890
                if camb1_active == False:
                    b1_button.x = 890
                if show_green_cama1_flicker == True:
                    a1_button.x = 11900
                    a1_on_button.x = 900
                if cama1_active == False:
                    a1_button.x = 900
                if show_green_cama7_flicker == True:
                    a7_button.x = 111140
                    a7_on_button.x = 1140
                if cama7_active == False:
                    a7_button.x = 1140
                if show_green_cama6_flicker == True:
                    a6_button.x = 111130
                    a6_on_button.x = 1130
                if cama6_active == False:
                    a6_button.x = 1130
                if show_green_cama5_flicker == True:
                    a5_button.x = 11730
                    a5_on_button.x = 730
                if cama5_active == False:
                    a5_button.x = 730
                if show_green_cama3_flicker == True:
                    a3_button.x = 11740
                    a3_on_button.x = 740
                if cama3_active == False:
                    a3_button.x = 740
                if show_green_camb4_flicker == True:
                    b4_button.x = 111030
                    b4_on_button.x = 1030
                if camb4_active == False:
                    b4_button.x = 1030
                if show_green_cama4_flicker == True:
                    a4_button.x = 111030
                    a4_on_button.x = 1030
                if cama4_active == False:
                    a4_button.x = 1030
                window.blit(a2_on_button.image, (a2_on_button.x, a2_on_button.y))
                window.blit(b2_on_button.image, (b2_on_button.x, b2_on_button.y))
                window.blit(a4_on_button.image, (a4_on_button.x, a4_on_button.y))
                window.blit(b4_on_button.image, (b4_on_button.x, b4_on_button.y))
                window.blit(a3_on_button.image, (a3_on_button.x, a3_on_button.y))
                window.blit(a5_on_button.image, (a5_on_button.x, a5_on_button.y))
                window.blit(a6_on_button.image, (a6_on_button.x, a6_on_button.y))
                window.blit(a7_on_button.image, (a7_on_button.x, a7_on_button.y))
                window.blit(a1_on_button.image, (a1_on_button.x, a1_on_button.y))
                window.blit(b1_on_button.image, (b1_on_button.x, b1_on_button.y))
                window.blit(c1_on_button.image, (c1_on_button.x, c1_on_button.y))
                
                window.blit(a2_button.image, (a2_button.x, a2_button.y))           
                window.blit(b2_button.image, (b2_button.x, b2_button.y))             
                window.blit(a4_button.image, (a4_button.x, a4_button.y))              
                window.blit(b4_button.image, (b4_button.x, b4_button.y))              
                window.blit(a3_button.image, (a3_button.x, a3_button.y))  
                window.blit(a5_button.image, (a5_button.x, a5_button.y))               
                window.blit(a6_button.image, (a6_button.x, a6_button.y))    
                window.blit(a7_button.image, (a7_button.x, a7_button.y))             
                window.blit(a1_button.image, (a1_button.x, a1_button.y))             
                window.blit(b1_button.image, (b1_button.x, b1_button.y)) 
                window.blit(c1_button.image, (c1_button.x, c1_button.y))
                window.blit(camera_button2.image, (camera_button2.x, camera_button2.y))
            if show_left_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_left_light == True and show_camera == False:
                window.blit(left_light.image, (left_light.x, left_light.y))
            if show_left_light == True and show_bon == True and show_camera == False:
                window.blit(bon.image, (bon.x, bon.y))
            if show_right_light == True:
                power_number -= 0.0008
                window.blit(green_bar_image, (125, 670))
            if show_right_light == True and show_camera == False:
                window.blit(right_light.image, (right_light.x, right_light.y))
            if show_left_door == True:
                power_number -= 0.002
                window.blit(yellow_bar_image, (150, 670))
            if show_left_door == True and show_camera == False:
                window.blit(left_door.image, (left_door.x, left_door.y))
            if show_right_door == True:
                power_number -= 0.002
                window.blit(red_bar_image, (175, 670))
            if show_right_door == True and show_camera == False:
                window.blit(right_door.image, (right_door.x, right_door.y))
            if show_right_door == False and show_left_door == False and show_right_light == False and show_left_light == False and show_camera == False:
                power_number -= 0
            window.blit(green_bar_image, (100, 670))
            power_number -= 0.0008
        if power_out == True and show_power_out_fred == True and power_out_fred_active == True:
            window.blit(fred_power_out_image, (bon.x, bon.y))

        if jumpscare_end_fred == True:
            fred_image = pygame.transform.scale(fred_image, (2500, 1000))
            window.blit(fred_image, (bon.x, chic.y))

        if show_camera == False:
            window.blit(door_button2.image, (door_button2.x, door_button2.y))
            window.blit(door_button.image, (door_button.x, door_button.y))
            window.blit(door_button_on2.image, (door_button_on2.x, door_button_on2.y))
            window.blit(door_button_on.image, (door_button_on.x, door_button_on.y))

            window.blit(light_button2.image, (light_button2.x, light_button2.y))
            window.blit(light_button.image, (light_button.x, light_button.y))
            window.blit(light_button_on2.image, (light_button_on2.x, light_button_on2.y))
            window.blit(light_button_on.image, (light_button_on.x, light_button_on.y))

            office_bg_image.blit(Light_text, (50, 500))
            office_bg_image.blit(Light_text, (2150, 500))
            office_bg_image.blit(Door_text, (50, 350))
            office_bg_image.blit(Door_text, (2150, 350))
        if power_out == False:
            window.blit(AM_text, (1150, 0))
            window.blit(Night_text, (1150, 50))
            window.blit(Usage_text, (0, 660))
            window.blit(Power_left_text, (0, 600))
            window.blit(Power_number_text, (160, 590))
        pygame.display.update()
if __name__ == "__main__":
    mainmenu()