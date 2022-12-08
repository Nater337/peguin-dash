import arcade
MOVEMENT_SPEED = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

 #Set Background color
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Demonstrate a Window")
arcade.set_background_color(arcade.glacier.jpg)


def on_key_press(self, key, modifiers):
    """
    Called whenever a key is pressed.
    """
    if key == arcade.key.UP:
        self.player_sprite.change_y = MOVEMENT_SPEED
    elif key == arcade.key.DOWN:
        self.player_sprite.change_y = -MOVEMENT_SPEED
    elif key == arcade.key.LEFT:
        self.player_sprite.change_x = -MOVEMENT_SPEED
    elif key == arcade.key.RIGHT:
        self.player_sprite.change_x = MOVEMENT_SPEED
