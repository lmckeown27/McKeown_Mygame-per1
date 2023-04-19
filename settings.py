WIDTH = 1200
HEIGHT = 800
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
# could not figure out a legitimate kill code; made the velocity and absurd amount so that it will appear as if player is killed
PLAYER_DIE = 9999999999999999
PLAYER_GRAV = 0.8
PLAYER_VEL_RIGHT = -50
PLAYER_VEL_LEFT = 50
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GOLD = (212, 175, 55)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 100, (200, 200, 200), "normal"),
                 # (WIDTH / 2 - 50, HEIGHT * 0.85, 100,
                 # 20, (100, 255, 100), "bouncey"),
                 # (125, HEIGHT - 350, 100, 5, (200, 100, 50), "disappearing"),

                 # Each block is organized in a specific place
                 # "normal" labelled blocks cause no augmentation,
                 # "death" labelled blocks set the player's x-velocity to an absurd amount
                 # "goal" labelled block is similar to normal block with the only exception being that it is gold
                 # "bouncey" labelled block increases the players y-velocity a specific amount
                 (550, 50, 100, 20, (200, 28, 200), "normal"),
                 (250, 500, 100, 20, (200, 28, 200), "death"),
                 (0, 50, 100, 20, (212, 175, 55), "goal"),
                 (750, 500, 100, 20, (200, 28, 200), "normal"),
                 (700, 200, 100, 20, (200, 28, 200), "death"),
                 (900, 600, 100, 20, (200, 28, 200), "normal"),
                 (1000, 200, 100, 20, (200, 28, 200), "death"),
                 (550, 700, 100, 20, (200, 28, 200), "normal"),
                 (800, 300, 100, 20, (200, 28, 200), "death"),
                 (550, 500, 100, 20, (200, 28, 200), "normal"),
                 (320, 150, 100, 20, (200, 28, 200), "death"),
                 (150, 300, 100, 20, (200, 28, 200), "bouncey"),
                 (600, 350, 100, 20, (200, 28, 200), "normal"),
                 (213, 70, 100, 20, (200, 28, 200), "death"),
                 (143, 600, 100, 20, (200, 28, 200), "death"),
                 (304, 900, 100, 20, (200, 28, 200), "normal"),
                 ]
