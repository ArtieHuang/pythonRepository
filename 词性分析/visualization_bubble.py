
import arcade
import random
import csv
import math

# Set up the constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Sentiments!"

NUMBER_OF_SHAPES = 50


class Shape:
    def __init__(self, x, y, width, height, delta_x, delta_y,
                 color, word):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.delta_x = delta_x
        self.delta_y = delta_y

        self.color = color
        self.words = word

    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y

        if self.x - self.width/2 <= 0 and self.delta_x - self.width/2 <= 0:
            self.x = self.width / 2
            self.delta_x *= -1
        if self.y - self.height/2 <= 0 and self.delta_y - self.height/2 <= 0:
            self.delta_y *= -1
            self.y = self.width / 2
        if self.x + self.width/2 >= SCREEN_WIDTH and self.delta_x + self.width/2 >= 0:
            self.delta_x *= -1
            self.x =- self.width / 2 + SCREEN_WIDTH
        if self.y + self.height/2 >= SCREEN_HEIGHT and self.delta_y + self.height/2 >= 0:
            self.delta_y *= -1
            self.y = - self.width / 2 + SCREEN_HEIGHT


class Ellipse(Shape):

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.width, self.height,
                                   self.color)
        arcade.draw_text(self.words,self.x - len(self.words) * 7 ,self.y - 4,(250, 250, 250), 10,font_name='simfang')



class MyGame(arcade.Window):


    def __init__(self):
        # Call the parent __init__
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Create a shape list
        self.shape_list = []
        csv_reader = csv.reader(open("theme_result.csv", encoding='utf-8'))
        arcade.set_background_color((220, 255, 255))
        for row in csv_reader:
            sentiment = float(row[1])
            times= int(row[2])
            if (sentiment>0.2 and times>700) or (sentiment<-0.2 and times>15):

                x = random.randrange(0, SCREEN_WIDTH)
                y = random.randrange(0, SCREEN_HEIGHT)
                width = math.log(times*times,1.3)+15

                height = width

                # Random movement
                d_x = random.randrange(1, 3) * random.randrange(-1, 3, 2)
                d_y = random.randrange(1, 3) * random.randrange(-1, 3, 2)

                # Random color
                if sentiment<0:
                    red =  (-sentiment)*255
                    green = 0
                    blue = 0.5
                else:
                    red = 0
                    green = (sentiment)*255
                    blue = 0.5


                alpha = 255

                # Random line, ellipse, or rect
                shape_type = random.randrange(3)

                shape = Ellipse(x, y, width, height, d_x, d_y,
                                (red, green, blue, alpha), row[0])

                self.shape_list.append(shape)

    def on_update(self, dt):

        for shape in self.shape_list:
            shape.move()

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen
        arcade.start_render()

        # Draw the shapes
        for shape in self.shape_list:
            shape.draw()



def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()