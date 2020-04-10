import pygame, sys, random
import pygame.gfxdraw

# Colors-----------

white = (255,255,255)
black = (0,0,0)
tmos_green = (0,206,177)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

# Initializing Pygame
pygame.init()

screen_width = 600
screen_height = 800
basic_block = 20
food_radius = 10
fps = 10

# Screen window size defined
screen = pygame.display.set_mode((screen_width,screen_height))

# Naming the Screen (Name of the Game)
pygame.display.set_caption('Snake vs Chinese')

# Fills window with black color
screen.fill(black)

clock = pygame.time.Clock()
# clock.tick(FPS) tells the refresh rate, or the running speed of the loop


# -------------------- Structure of code -------------------------
# Part 0 - Quit game
# Part 1 - Create snake
# Part 2 - Generate food
# Part 3 - Move snake
# Part 4 - Eat Food check (Only from mouth)
# Part 5 - Reach screen side
# Part 6 - Game over
# Part 7 - Game Pause
# Part 8 - Show Score
# Part 9 - Check Body touch



def quit_game():
    pygame.quit()
    sys.exit(0)


def create_snake(position):
    for i in range(len(position)-1):
        location = position[i]
        x_location = location[0]
        y_location = location[1]
        pygame.draw.rect(screen,white,(x_location,y_location,basic_block,basic_block),0)

    x_head = position[-1][0]
    y_head = position[-1][1]

    pygame.draw.rect(screen,red,(x_head,y_head,basic_block,basic_block),0)


def generate_food():
    x_food = random.randint(2*basic_block,(screen_width-2*basic_block))
    y_food = random.randint(2*basic_block,(screen_height-2*basic_block))
    pygame.gfxdraw.filled_circle(screen, x_food, y_food, food_radius, green)
    
    return x_food,y_food


def move_snake(direction):
    if direction=='left':
        x_change=-1*basic_block
        y_change=0
    if direction=='right':
        x_change=1*basic_block
        y_change=0
    if direction=='top':
        x_change=0
        y_change=-1*basic_block
    if direction=='bottom':
        x_change=0
        y_change=1*basic_block

    return x_change,y_change


def eat_food_check(position, x_food, y_food):
    check = False            #-------------------------------- False means food not eaten, thus const x_food amd y_food
    #for location in position:
    location = position[-1]

    if location[0]<=(x_food+food_radius) and location[0]>=(x_food-food_radius) and location[1]<=(y_food+food_radius) and location[1]>=(y_food-food_radius):
        check = True
    if (location[0]+basic_block)<=(x_food+food_radius) and (location[0]+basic_block)>=(x_food-food_radius) and (location[1]+basic_block)<=(y_food+food_radius) and (location[1]+basic_block)>=(y_food-food_radius):
        check = True
    if (location[0]+basic_block)<=(x_food+food_radius) and (location[0]+basic_block)>=(x_food-food_radius) and (location[1])<=(y_food+food_radius) and (location[1])>=(y_food-food_radius):
        check = True
    if (location[0])<=(x_food+food_radius) and (location[0])>=(x_food-food_radius) and (location[1]+basic_block)<=(y_food+food_radius) and (location[1]+basic_block)>=(y_food-food_radius):
        check = True

    return check


def screen_end(position):
    check = False            #-------------------------------- False means screen not end. In true, its Gameover
    if position[-1][0]>(screen_width) or position[-1][1]>(screen_height) or position[-1][0]<(0) or position[-1][1]<(0):
            check = True
    if (position[-1][0]+basic_block)>(screen_width) or (position[-1][1]+basic_block)>(screen_height) or (position[-1][0]+basic_block)<(0) or (position[-1][1]+basic_block)<(0):
            check = True

    return check



def game_over(score):
    pause = True

    while pause:
        for event in pygame.event.get():
            try:
                if event.type == pygame.QUIT:
                    quit_game()
                if event.key == pygame.K_ESCAPE:
                    game_loop()
            except:
                pass

        screen.fill(tmos_green)

        mssg_1 = 'Game Over'
        screen_text_1 = pygame.font.Font(None,100).render(mssg_1, True, black)
        screen.blit(screen_text_1, [(screen_width/4), (screen_height/4)])

        mssg_2 = 'Your Score : '+str(score)
        screen_text_2 = pygame.font.Font(None,40).render(mssg_2, True, black)
        screen.blit(screen_text_2, [(screen_width/3), (screen_height/3)])

        mssg_3 = 'Press Esc to Retry'
        screen_text_2 = pygame.font.Font(None,40).render(mssg_3, True, black)
        screen.blit(screen_text_2, [(screen_width/3), (screen_height/2)])
        
        pygame.display.update()
        clock.tick(fps)


def game_pause(score):
    pause = True

    while pause:
        for event in pygame.event.get():
            try:
                if event.type == pygame.QUIT:
                    quit_game()
                if event.key == pygame.K_ESCAPE:
                    print(event.key)
                    pause = False
                    return pause
            except:
                pass

        screen.fill(tmos_green)

        mssg_1 = 'Game Paused'
        screen_text_1 = pygame.font.Font(None,100).render(mssg_1, True, black)
        screen.blit(screen_text_1, [(screen_width/4), (screen_height/4)])

        mssg_2 = 'Your Score : '+str(score)
        screen_text_2 = pygame.font.Font(None,40).render(mssg_2, True, black)
        screen.blit(screen_text_2, [(screen_width/3), (screen_height/3)])

        mssg_3 = 'Press Esc to Resume'
        screen_text_2 = pygame.font.Font(None,40).render(mssg_3, True, black)
        screen.blit(screen_text_2, [(screen_width/3), (screen_height/2)])
        
        pygame.display.update()
        clock.tick(fps)


def show_score(score):
    mssg = 'Score : '+str(score)
    screen_text = pygame.font.Font(None, 60).render(mssg, True, white)
    screen.blit(screen_text, [(screen_width/2-70), 0])

def body_check(position):
    check = False
    for i in range(len(position)-2):
        if position[-1]==position[i]:
            check=True

    return check



### ----------------------------------------- Main Loop -------------------------------


def game_loop():
    #start with single block snake at centre
    position = [((screen_width/2-basic_block/2),(screen_height/2-basic_block/2))]
    snake_length=1
    
    # Initializing change variables of snake position to be zero till correct buttons are pressed
    x_change = 0
    y_change = 0

    # The key that was placed last
    last_key = 'none'

    create_snake(position) #snake created

    x_food,y_food = generate_food() #food generated

    show_score(snake_length-1) #show score

    pygame.display.update()

    while True:

        if screen_end(position):
            print('screen ends')
            game_over(snake_length)

        if snake_length>2:
            if body_check(position):
                print('You ate yourself')
                game_over(snake_length)

        screen.fill(black)
        
        pygame.gfxdraw.filled_circle(screen, x_food, y_food, food_radius, green)
        show_score(snake_length-1)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = game_pause(snake_length)

                if (last_key!='bottom') and (event.key == pygame.K_w or event.key == pygame.K_UP):
                    x_change,y_change=move_snake('top')
                    last_key = 'top'

                if (last_key!='top') and (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                    x_change,y_change=move_snake('bottom')
                    last_key = 'bottom'

                if (last_key!='right') and (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                    x_change,y_change=move_snake('left')
                    last_key = 'left'

                if (last_key!='left') and (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                    x_change,y_change=move_snake('right')
                    last_key = 'right'


        x_new = position[-1][0] + x_change
        y_new = position[-1][1] + y_change

        #print(position)

        position.append((x_new,y_new))
        
        check_food = eat_food_check(position, x_food, y_food)

        if check_food==True:
            x_food, y_food = generate_food()
            snake_length = snake_length + 1
            #print('Hurray - Your score is ',snake_length-1)

        if check_food==False:
            #print('one down')
            del position[0]

        create_snake(position)

        pygame.display.update()

        clock.tick(fps)


game_loop()