import pygame
pygame.init()

#colores
black = (0, 0, 0)
white = (255, 255, 255)
verde = (50, 255, 100)
screen_size = (800, 600)
player_whidth = 15
player_height = 90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0

# coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_whidth
player2_y_coor = 300 - 45
player2_y_speed = 0

#coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3

# imagen de fondo
background = pygame.image.load("cancha12.png").convert()



game_over = False

sound = pygame.mixer.Sound("golpe1.mp3")
sound2 = pygame.mixer.Sound("golpe2.mp3")


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game:over = True
        if event.type == pygame.KEYDOWN:
            #jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3
            #jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3

        if event.type == pygame.KEYUP:
            #jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
                sound.play()
            #jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0
                sound2.play()

    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1

    # revisa si la pelota sale del lado derecho
    if pelota_x > 800:
        pelota_x = 400
        pelota_y = 300
        #si sale de la pantalla invierte direccion
        pelota_speed_x *= -1
        pelota_speed_y *= -1

    # revisa si la pelota sale del lado izquierdo
    if pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        #si sale de la pantalla invierte direccion
        pelota_speed_x *= -1
        pelota_speed_y *= -1

    # modifica las coordenadas para dar movimiento a los jugadores/ pelota
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed
    #movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y
    
    screen.blit(background, [0, 0])

    #zona de dibujo
    jugador1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_whidth, player_height))
    jugador2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_whidth, player_height))
    pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)

    # colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1

    pygame.display.flip()
    clock.tick(100)
pygame.quit()