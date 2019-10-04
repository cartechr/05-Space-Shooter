import sys, logging, os, random, math, arcade, open_color

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000
Margin = 20
SCREEN_TITLE = "Space Shooter"

Number_Of_Enemies = 5
Number_Of_Enemies2 = 2
Number_Of_Enemies3 = 2
Starting_Location = (600,300)
Bullet_Damage = 100
Enemy_Hp = 100
Enemy_Hp2 = 1000
Kill_Score = 100

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("assets/Titan.png", 0.5)
        (self.center_x, self.center_y) = Starting_Location

class Enemy(arcade.Sprite):
    def __init__(self, position):
        #starts the alien enemy
        '''
        Parameter: position: (x,y) tuple
        '''
        #normal enemies
        super().__init__("assets/alien2_2.png", 2)
        self.hp = Enemy_Hp
        (self.center_x, self.center_y) = position

class Enemy2(arcade.Sprite):
    def __init__(self, position):
        #boss
        super().__init__("assets/alienpblog.png", 0.5)
        self.hp = Enemy_Hp2
        (self.center_x, self.center_y) = position

class Missile1(arcade.Sprite):
    def __init__(self, position, velocity, damage):
        #starts the missile
        '''
        Parameters: position: (x,y) tuple
            velocity: (dx, dy) tuple
            damage: int (or float)
        '''
        super().__init__("assets/spr_missile.png", 0.5)
        (self.center_x, self.center_y) = position
        (self.dx, self.dy) = velocity
        self.damage = damage

    def update(self):
        #Moves the missile
        self.center_x += self.dx
        self.center_y += self.dy

class Window(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(True)

        self.missile_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player1 = Player()
        self.score = 0

        arcade.set_background_color(open_color.black)
        self.boss = False

        



    def setup(self):
        '''
        Set up enemies
        '''
        for i in range(Number_Of_Enemies):
            x = random.randint(MARGIN, SCREEN_WIDTH - Margin)
            y = 900
            dx = random.uniform(-In)
            enemy = Enemy((x,y))
            self.enemy_list.append(enemy)
        

    def update(self, delta_time):
        self.missile_list.update()
        for e in self.enemy_list:
            boolets = arcade.check_for_collision_with_list(e,self.missile_list)
            for b in boolets:
                e.hp = e.hp - b.damage
                b.kill()
                if e.hp <= 0:
                    e.kill()
                    self.score = self.score + Kill_Score
        if len(self.enemy_list) == 0 and not self.boss:
            x = 600
            y = 900
            enemy = Enemy2((x,y))
            self.enemy_list.append(enemy) 
            self.boss = True
            for i in range(Number_Of_Enemies2):
                x2 = 220 * (i+.5) + 50
                y2 = 900
                enemy = Enemy((x2,y2))
                self.enemy_list.append(enemy)
            for i in range(Number_Of_Enemies3):
                x2 = 220 * (i+3.5) + 50
                y2 = 900
                enemy = Enemy((x2,y2))
                self.enemy_list.append(enemy)

            
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_text(str(self.score), 20, SCREEN_HEIGHT - 40, open_color.white, 16)
        self.player1.draw()
        self.missile_list.draw()
        self.enemy_list.draw()




    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.player1.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            x = self.player1.center_x
            y = self.player1.center_y + 15
            missile = Missile1((x,y),(0,10),Bullet_Damage)
            self.missile_list.append(missile)


    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            print("Left")
        elif key == arcade.key.RIGHT:
            print("Right")
        elif key == arcade.key.UP:
            print("Up")
        elif key == arcade.key.DOWN:
            print("Down")

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        pass


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()