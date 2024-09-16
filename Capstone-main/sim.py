import pyglet
from algo import algo
from app import views

# Set up the thresholds and weights
box_data = {
    "room_temperature": 22,  # Assuming the temperature in the room is 22C
    "humidity": 45  # Assuming the humidity in the room is 45%
    # Add more data from the weather box as needed
}

# Define thresholds for each variable (min, max)
room_thresholds = {
    "room_temperature": (21, 24),  # Threshold for temperature (21C to 24C)
    "humidity": (40, 60)  # Threshold for humidity (40% to 60%)
    # Add more thresholds as needed
}

# Define weights for each variable
weights = {
    "room_temperature": 1.0,  # Weight for temperature comparison
    "humidity": 0.8  # Weight for humidity comparison
    # Add more weights as needed
}

algo_threshold = 1.0

# Set up the window
window = pyglet.window.Window(width=750, height=500)

# Load background image
background = pyglet.image.load("imgs/room_background.png")

# Load window sprite
window_sprite = pyglet.sprite.Sprite(pyglet.image.load("imgs/window_closed.jpg"))

# Calculate the coordinates to center the window on the background
window_sprite.x = (background.width - window_sprite.width) // 2
window_sprite.y = ((background.height - window_sprite.height) // 2) + 65

# Function to update window state based on algorithm output
def update_window(dt):
    # Call your algorithm function to determine whether the window should be open or closed
    window_open = algo.check_threshold(box_data, room_thresholds, algo_threshold, weights)

    # Update window sprite based on algorithm output
    if window_open == 1:
        # Set window sprite to open position
        window_sprite.image = pyglet.image.load("imgs/window_open.png")
    else:
        # Set window sprite to closed position
        window_sprite.image = pyglet.image.load("imgs/window_closed.jpg")

    # Redraw the window to reflect the updated sprite
    window.clear()
    background.blit(0, 0)  # Draw background
    window_sprite.draw()    # Draw window

# Register update function
pyglet.clock.schedule_interval(update_window, 1.0 / 30)  # Update every 1/30th of a second


def main():
    # Run the application
    pyglet.app.run()

if __name__ == '__main__':
    main()
