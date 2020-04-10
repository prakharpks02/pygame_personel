import pygame, sys, random
import pygame.gfxdraw

# Colors-----------

white = (255,255,255)
black = (0,0,0)
green = (0,206,177)

# Initializing Pygame
pygame.init()

# Screen window size defined
screen = pygame.display.set_mode((600,800))

# Naming the Screen (Name of the Game)
pygame.display.set_caption('Chaos Snake')

# Fills window with black color
screen.fill(black)

clock = pygame.time.Clock()
# clock.tick(FPS) tells the refresh rate, or the running speed of the loop


# -------------------- Structure of code -------------------------
# Part 0 - Quit game
# Part 1 - Create snake
# Part 2 - Generate food
# Part 3 - Move snake
# Part 4 - Eat Food check
# Part 5 - Reach screen side
# Part 6 - Game over
# Part 7 - Game Pause



def quit_game():
    pygame.quit()
    sys.exit(0)


def create_snake(position):
    for location in position:
        x_location = location[0]
        y_location = location[1]
        pygame.draw.rect(screen,white,(x_location,y_location,20,20),1)


def generate_food():
    x_food = random.randint(30,570)
    y_food = random.randint(30,770)
    pygame.gfxdraw.filled_circle(screen, x_food, y_food, 10, green)
    
    return x_food,y_food


def move_snake(direction):
    if direction=='left':
        x_change=-20
        y_change=0
    if direction=='right':
        x_change=20
        y_change=0
    if direction=='top':
        x_change=0
        y_change=-20
    if direction=='bottom':
        x_change=0
        y_change=+20

    return x_change,y_change


def eat_food_check(position, x_food, y_food):
    check = False            #-------------------------------- False means food not eaten, thus const x_food amd y_food
    for location in position:
        if location[0]<=(x_food+10) and location[0]>=(x_food-10) and location[1]<=(y_food+10) and location[1]>=(y_food-10):
            check = True
        if (location[0]+20)<=(x_food+10) and (location[0]+20)>=(x_food-10) and (location[1]+20)<=(y_food+10) and (location[1]+20)>=(y_food-10):
            check = True

    return check


def screen_end(position):
    check = False            #-------------------------------- False means screen not end. In true, its Gameover
    if position[-1][0]>=(600) or position[-1][1]>=(800) or position[-1][0]<=(0) or position[-1][1]<=(0):
            check = True
    if (position[-1][0]+20)>=(600) or (position[-1][1]+20)>=(800) or (position[-1][0]+20)<=(0) or (position[-1][1]+20)<=(0):
            check = True

    return check



def game_over():
    pass


def game_pause():
    pass


def game_loop():
    #start with single block snake at centre
    position = [(300,400)]
    snake_length=1
    
    # Initializing change variables of snake position to be zero till correct buttons are pressed
    x_change = 0
    y_change = 0

    create_snake(position) #snake created

    x_food,y_food = generate_food() #food generated

    pygame.display.update()

    while True:

        if screen_end(position):
            print('screen ends')
            quit_game()

        screen.fill(black)
        
        pygame.gfxdraw.filled_circle(screen, x_food, y_food, 10, green)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_pause()
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    x_change,y_change=move_snake('top')
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    x_change,y_change=move_snake('bottom')
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x_change,y_change=move_snake('left')
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x_change,y_change=move_snake('right')

        x_new = position[-1][0] + x_change
        y_new = position[-1][1] + y_change

        #print(position)

        position.append((x_new,y_new))
        
        check_food = eat_food_check(position, x_food, y_food)

        if check_food==True:
            x_food, y_food = generate_food()
            snake_length = snake_length + 1
            print('Hurray - Your score is ',snake_length)

        if check_food==False:
            #print('one down')
            del position[0]

        create_snake(position)

        pygame.display.update()

        clock.tick(3)


game_loop()