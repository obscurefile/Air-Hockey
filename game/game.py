import pygame as pg
from puck import Puck
from player import Player

class Game:
    HEIGHT = 800
    WIDTH = 600

    player = Player(WIDTH/2, HEIGHT/2)
    opponent = Player(WIDTH/2, HEIGHT/4)

    puck = Puck()

    top_wall = pg.Rect(0, 0, WIDTH, 1)
    bottom_wall = pg.Rect(0, HEIGHT - 1, WIDTH, 1)
    left_wall = pg.Rect(0, 0, WIDTH - (WIDTH-1), HEIGHT)
    right_wall = pg.Rect(WIDTH-1, 0, 1, HEIGHT)

    last_surface = None

    def draw_rink(self, window):
        window.fill("white")

        #Goals
        pg.draw.circle(window, "blue", [(self.WIDTH/2), 0 - (self.HEIGHT/20)], 75, 3)
        pg.draw.circle(window, "blue", [(self.WIDTH/2), (self.HEIGHT + (self.HEIGHT/20))], 75, 3)

        #Lines
        pg.draw.line(window, "blue", (0, self.HEIGHT/4), (self.WIDTH, self.HEIGHT/4), 4)
        pg.draw.line(window, "blue", (0, (self.HEIGHT - (self.HEIGHT/4))), (self.WIDTH, (self.HEIGHT - (self.HEIGHT/4))), 4)

        #Top Circles
        pg.draw.circle(window, "red", [(self.WIDTH/10), (self.HEIGHT/8)], 60, 3)
        pg.draw.circle(window, "red", [(self.WIDTH/10), (self.HEIGHT/8)], 8)
        
        pg.draw.circle(window, "red", [(self.WIDTH - (self.WIDTH/10)), (self.HEIGHT/8)], 60, 3)
        pg.draw.circle(window, "red", [(self.WIDTH - (self.WIDTH/10)), (self.HEIGHT/8)], 8)

        #Bottom Circles
        pg.draw.circle(window, "red", [(self.WIDTH/10), (self.HEIGHT -(self.HEIGHT/8))], 60, 3)
        pg.draw.circle(window, "red", [(self.WIDTH/10), (self.HEIGHT -(self.HEIGHT/8))], 8)
        
        pg.draw.circle(window, "red", [(self.WIDTH - (self.WIDTH/10)), (self.HEIGHT - (self.HEIGHT/8))], 60, 3)
        pg.draw.circle(window, "red", [(self.WIDTH - (self.WIDTH/10)), (self.HEIGHT - (self.HEIGHT/8))], 8)

        #Center Line
        for x in range(12):
            start = x * (self.WIDTH/26)
            pg.draw.line(window, "red", (start, self.HEIGHT/2), ((start + 10), self.HEIGHT/2), 4)

        for x in range(12):
            start = (x * (self.WIDTH/26)) + (self.WIDTH - (self.WIDTH/2) + 59)
            pg.draw.line(window, "red", (start, self.HEIGHT/2), ((start + 10), self.HEIGHT/2), 4)

        #Center
        pg.draw.circle(window, "white", [(self.WIDTH/2), (self.HEIGHT/2)], 54)
        pg.draw.circle(window, "blue", [(self.WIDTH/2), (self.HEIGHT/2)], 54, 3)
        pg.draw.circle(window, "red", [(self.WIDTH/2), (self.HEIGHT/2)], 8)

        #Scores
        pg.draw.rect(window, "red", pg.Rect(0, self.HEIGHT/2, 50, 50))
        pg.draw.rect(window, "crimson", pg.Rect(0, self.HEIGHT/2, 50, 50), 4)

        pg.draw.rect(window, "blue", pg.Rect(0, (self.HEIGHT/2) - 50, 50, 50))
        pg.draw.rect(window, "dark blue", pg.Rect(0, (self.HEIGHT/2) - 50, 50, 50), 4)

        #Borders
        pg.draw.rect(window, "yellow", self.top_wall, 0)
        pg.draw.rect(window, "yellow", self.bottom_wall, 0)
        pg.draw.rect(window, "yellow", self.left_wall, 0)
        pg.draw.rect(window, "yellow", self.right_wall, 0)
        
    def hitbox_collision(self, rect, puck_rect):
        return pg.Rect.colliderect(rect, puck_rect)

    def surface_hit(self):
        if(self.hitbox_collision(self.player.get_hitbox(), self.puck.get_hitbox())):
            self.last_surface = self.player.get_hitbox()
        
        elif (self.hitbox_collision(self.opponent.get_hitbox(), self.puck.get_hitbox())):
            self.last_surface = self.opponent.get_hitbox()
        
        elif (self.hitbox_collision(self.top_wall, self.puck.get_hitbox())):
            self.last_surface = self.top_wall
            
        elif (self.hitbox_collision(self.bottom_wall, self.puck.get_hitbox())):
            self.last_surface = self.bottom_wall
            
        elif (self.hitbox_collision(self.left_wall, self.puck.get_hitbox())):
            self.last_surface = self.left_wall
            
        elif (self.hitbox_collision(self.right_wall, self.puck.get_hitbox())):
            self.last_surface = self.right_wall

    def puck_hit(self, puck):
        if (self.hitbox_collision(self.player.get_hitbox(), puck.get_hitbox())):
                        
            if(puck.x > self.player.x and puck.x_vel < 0):                 
                puck.x_vel *= -1

            elif(puck.x < self.player.x and puck.x_vel > 0):
                puck.x_vel *= -1

            if(puck.y > self.player.y and puck.y_vel < 0):
                self.puck.y_vel *= -1

            elif(puck.y < self.player.y and puck.y_vel > 0):
                self.puck.y_vel *= -1

        elif (self.hitbox_collision(self.opponent.get_hitbox(), self.puck.get_hitbox())):
            if(puck.x > self.opponent.x and puck.x_vel < 0):                 
                puck.x_vel *= -1

            elif(puck.x < self.opponent.x and puck.x_vel > 0):
                puck.x_vel *= -1

            if(puck.y > self.opponent.y and puck.y_vel < 0):
                self.puck.y_vel *= -1

            elif(puck.y < self.opponent.y and puck.y_vel > 0):
                self.puck.y_vel *= -1
                                    
        elif (self.hitbox_collision(self.top_wall, puck.get_hitbox())):
            puck.y_vel *= -1
        
        elif (self.hitbox_collision(self.bottom_wall, puck.get_hitbox())):
            puck.y_vel *= -1
        
        elif (self.hitbox_collision(self.left_wall, puck.get_hitbox())):
            puck.x_vel *= -1
        
        elif (self.hitbox_collision(self.right_wall, puck.get_hitbox())):
            puck.x_vel *= -1

    def move_puck(self, puck, surface):
        if(self.hitbox_collision(surface, puck.get_hitbox())):
           if (puck.vel < 7.5):
               puck.vel += 1

           if (puck.x_vel > 0):
               puck.x_vel = puck.vel
                
           else:
               puck.x_vel = puck.vel * -1

           if (puck.y_vel > 0):
               puck.y_vel = puck.vel
                
           else:
               puck.y_vel = puck.vel * -1

        if (puck.vel > 0):
            puck.x += puck.x_vel
            puck.y += puck.y_vel
        
    def goal(self, player):
        player.score = player.score + 1

    def draw_scores(self, font, player_score, opponent_score):
        player_text = font.render(str(player_score), True, (0, 0, 0))
        opponent_text = font.render(str(opponent_score), True, (0, 0, 0))
        
        self.screen.blit(player_text, (15, self.HEIGHT/2 - 40))
        self.screen.blit(opponent_text, (15, (self.HEIGHT/2 + 10)))

    def game_over(self):
        return self.player.score == 7 or self.opponent.score == 7

    def start(self):
        
        #Initializes pygame
        pg.init()

        #Creates window icon
        icon = pg.image.load('assets/hockey_icon.png')

        #Sets up window
        self.screen = pg.display.set_caption("Air Hockey")
        self.screen = pg.display.set_icon(icon)
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        
        self.clock = pg.time.Clock()

        #Score font
        font = pg.font.SysFont(None, 50)

        #Starts thread
        running = True

        pg.mouse.set_visible(False)

        #Sets the position of the puck
        self.puck.set_pos(self.WIDTH/2, (self.HEIGHT - (self.HEIGHT/7)))
        
        #Initializes opponent
        self.opponent.set_pos(self.WIDTH/2, 70)
        self.opponent.vel = 2
        
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    
            self.draw_rink(self.screen)
            
            self.draw_scores(font, self.player.score, self.opponent.score)
            
            if (self.game_over() == False):
                self.player.draw_striker(self.screen, False, "red", self.HEIGHT/2, self.HEIGHT)
                self.opponent.draw_striker(self.screen, True, "blue", 0, self.HEIGHT/2)
                
                #Puck velocity constantly decelerates
                if (self.puck.x_vel > 0):
                    self.puck.x_vel = self.puck.x_vel - (1/32)

                else:
                    self.puck.x_vel = self.puck.x_vel + (1/32)

                if (self.puck.y_vel > 0):
                    self.puck.y_vel = self.puck.y_vel - (1/32)

                else:
                    self.puck.y_vel = self.puck.y_vel + (1/32)

                if(self.puck.x_vel == (1/32)):
                    self.puck.x_vel = 0

                if(self.puck.y_vel == (1/32)):
                    self.puck.y_vel = 0
  
                #Opponent movement
                if(self.puck.y < (self.HEIGHT/2 - 10)):

                    if(self.opponent.x > self.puck.x):
                        self.opponent.x = self.opponent.x - self.opponent.vel*2

                    elif(self.opponent.x < self.puck.x):
                        self.opponent.x = self.opponent.x + self.opponent.vel*2

                    #Hit puck
                    if(self.puck.y > self.opponent.y):
                        self.opponent.y = self.opponent.y + self.opponent.vel

                else:

                    #Return to goal
                    if(self.opponent.y > 50):
                        self.opponent.y = self.opponent.y - self.opponent.vel*2
                        
                    #Center opponent
                    if(self.opponent.x > self.WIDTH/2):
                        self.opponent.x = self.opponent.x - self.opponent.vel*2
                        
                    else:
                        self.opponent.x = self.opponent.x + self.opponent.vel*2
                
                #Puck 
                if (self.puck.in_rink(self.WIDTH, self.HEIGHT)):
                    self.puck.draw_puck(self.screen)
                    
                    self.surface_hit()

                    self.puck_hit(self.puck)

                    #Puck hits surface
                    if(self.last_surface is not None):
                        self.move_puck(self.puck, self.last_surface)

                    #Player or opponent scores 
                    if (self.puck.x > 230 and self.puck.x < 360):
                        if(self.hitbox_collision(self.top_wall, self.puck.get_hitbox())):
                            self.goal(self.player)
                            self.puck.set_pos(self.WIDTH/2, (self.HEIGHT - 125))
                            self.puck.x_vel, self.puck.y_vel = 0, 0

                        elif(self.hitbox_collision(self.bottom_wall, self.puck.get_hitbox())):
                            self.goal(self.opponent)
                            self.puck.set_pos(self.WIDTH/2, 125)
                            self.puck.x_vel, self.puck.y_vel = 0, 0
                else:
                    self.puck.set_pos(self.WIDTH/2, self.HEIGHT/2)
                    self.puck.x_vel, self.puck.y_vel = 0, 0
                    
            else:
                
                #Game ends
                self.player.draw_striker(self.screen, True, "red", self.HEIGHT/2, self.HEIGHT)
                self.opponent.draw_striker(self.screen, True, "blue", 0, self.HEIGHT/2)
                    
            #Updates screen
            pg.display.flip()
            
            #Sets FPS
            self.clock.tick(60)
            
        pg.quit()
