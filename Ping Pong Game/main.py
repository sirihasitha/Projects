import pygame
from paddle import Paddle
from ball import Ball
#from ending import Ending
 
pygame.init()
 
# Define some colors
GREEN = "light green"
WHITE = (255,255,255)
 
# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")
 
brickA = Paddle(WHITE, 10, 100)
brickA.rect.x = 20
brickA.rect.y = 200
 
brickB = Paddle(WHITE, 10, 100)
brickB.rect.x = 670
brickB.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195
 
#en = Ending(WHITE, 10, 10)

list_of_sprites = pygame.sprite.Group()
 

list_of_sprites.add(brickA)
list_of_sprites.add(brickB)
list_of_sprites.add(ball)
#list_of_sprites.add(en)

gameRunning = True
 
scoreA = 0
scoreB = 0

clock = pygame.time.Clock()


while gameRunning:
   
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              gameRunning = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     gameRunning=False  

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        brickA.moveUp(5)
    if keys[pygame.K_s]:
        brickA.moveDown(5)
    if keys[pygame.K_UP]:
        brickB.moveUp(5)
    if keys[pygame.K_DOWN]:
        brickB.moveDown(5) 
    
    list_of_sprites.update()

    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
        #if scoreA == 3:
         #   en.winner(screen, "Player A")
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 
 
    if pygame.sprite.collide_mask(ball, brickA) or pygame.sprite.collide_mask(ball, brickB):
      ball.bounce()


    screen.fill(GREEN)
   
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    
    list_of_sprites.draw(screen) 

    font = pygame.font.Font(None, 74)
    text = font.render("Player A : " + str(scoreA), 1, WHITE)
    screen.blit(text, (40,6))
    text = font.render("Player B : " + str(scoreB), 1, WHITE)
    screen.blit(text, (360,6))
 
    
    pygame.display.flip()
     
    
    clock.tick(100)
 

pygame.quit()
