#GitHub Repo: https://github.com/haydensuhadolc/A8-Sprite
import math
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)
        # Add any other instance variables needed to track information as the program
        # runs here
        self.current_frame = 0

        self.fps = 10

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)
        # Make the GUI in the setupUI method
        self.setupUI()

        self.update_image()
        self.update_timer_interval()

    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()
        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        layout = QVBoxLayout()

        self.sprite_label = QLabel()
        self.sprite_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sprite_label.setPixmap(self.frames[self.current_frame])
        layout.addWidget(self.sprite_label)

        self.fps_text_label = QLabel("Frames Per Second")
        self.fps_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.fps_text_label)

        self.fps_value_label = QLabel(str(self.fps))
        self.fps_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.fps_value_label)

        self.fps_slider = QSlider(Qt.Orientation.Horizontal)
        self.fps_slider.setRange(1, 100)
        self.fps_slider.setValue(self.fps)

        self.fps_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.fps_slider.setTickInterval(5)
        self.fps_slider.valueChanged.connect(self.change_fps)

        layout.addWidget(self.fps_slider)

        frame.setLayout(layout)
        # Create needed connections between the UI components and slot methods
        # you define in this class.

        self.setCentralWidget(frame)

    def update_image(self):
        self.sprite_label.setPixmap(self.frames[self.current_frame])

    def next_frame(self):
        self.current_frame = (self.current_frame+1) % self.num_frames
        self.update_image()

    def change_fps(self):
        self.fps = self.fps_slider.value()
        self.fps_value_label.setText(str(self.fps))
        self.update_image_interval()

    def update_timer_interval(self):
        interval = int(1000/self.fps)
        self.timer.setInterval(interval)

    def start_animation(self):
        self.timer.start()

    def stop_animation(self):
        self.timer.stop()


    # You will need methods in the class to act as slots to connect to signals


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
