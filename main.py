def __init__(self):
self.penguin = None


def setup(self):
    self.penguin_list = arcade.SpriteList()
    self.penguin = arcade.Sprite("./penguin.png", .75)
    self.penguin_list.append(self.penguin)

def on_draw(self):
     self.penguin_list.draw()