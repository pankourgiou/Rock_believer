import pygame
import sys

# Initialize pygame
pygame.init()

# Load the map image
map_image = pygame.image.load("rock_believer.jpg")

# Set screen dimensions based on image size
SCREEN_WIDTH, SCREEN_HEIGHT = map_image.get_size()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fantasy Map Adventure")

# Define locations with clickable areas (x, y, width, height)
locations = {
    "Rock Believer": (200, 200, 100, 100),
    "Rock Believer 2": (300, 400, 100, 100),
    "Rock Believer 3": (600, 100, 100, 150),
    "Rock Believer 4": (500, 300, 100, 100),
    "Rock Believer 5": (700, 600, 90, 90),
    "Rock Believer 6": (400, 50, 110, 110),
    "Rock Believer 7": (400, 700, 100, 100)
}

# Define event messages for locations
events = {
    "Rock Believer": "I'm a rock believer You start to crawl until you walk You make a scream and learn to talk You discover life on every day From the first day you were born You walked a lifeline of your own And if you always keep the faith",
    "Rock Believer 2": "No one can take your dreams away In the ruins of their souls You saw the beauty of it all Simply a generation change How our fathers came to steal But we came back to make you feel Our love in every song we play Scream for me, screamer I'm a rock believer like you Just like you Come on, scream for me, screamer I'm a rock believer like you Just like you",
    "Rock Believer 3": "We go from here to everywhere So many moments that we share All boarded up, we give and take Love came to me so many ways No matter what some haters say No one can take our dreams away Scream for me, screamer I'm a rock believer like you Just like you Come on, scream for me, screamer I'm a rock believer like you Just like you",
    "Rock Believer 4": "Scream, scream, scream (I'm a rock believer)Scream, scream, scream (I'm a rock believer) No one can take our dreams away No one can take our dreams away Scream for me, screamer I m a rock believer like you Just like you Come on, scream for me, screamer I m a rock believer like you Just like you",
    "Rock Believer 5": "I'm a rock believer like you Just like you",
    "Rock Believer 6": "I'm a rock believer like you Just like you",
    "Rock Believer 7": "I'm a rock believer like you Just like you"
}

# Function to check if a point is inside a rectangle
def is_inside(x, y, rect):
    rx, ry, rw, rh = rect
    return rx <= x <= rx + rw and ry <= y <= ry + rh

# Game loop
running = True
while running:
    screen.blit(map_image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for location, rect in locations.items():
                if is_inside(mx, my, rect):
                    print(events[location])  # Display event message in console

    pygame.display.flip()

pygame.quit()
sys.exit()
