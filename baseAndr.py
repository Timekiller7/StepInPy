from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button

from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

from kivy.graphics import Line, Color
from kivy.uix.label import Label



class Background(GridLayout):
    def __init__(self):
        super(Background, self).__init__()
        self.width = Window.size[0]
        self.height = Window.size[1]
        self.add_gradient()


    def add_gradient(self):
        channel = 0
        rate = 1 / self.width

        for sep in range(self.width):
            self.canvas.add(Color(rgba=(0.4, 0.7, channel, 0.5)))
            self.canvas.add(Line(points=[sep, 0, sep, self.height], width=1))
            channel += rate
        # alpha_channel_rate += increase_rate


class MusicWindow(App):

    def build(self):
        # returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1    # само окно делит
        self.window.size_hint = (1, 3)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        # self.window.add_widget(Image(source="logo.png"))

        # label widget
        self.head = Label(
            text="Songs: ",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.head)

        layout = GridLayout(cols=2)
        for i in range(4):
            if i == 1:
                btn1 = Button(text=str(i + 1), background_normal='txc.jpg')
            elif i == 2:
                btn1 = Button(text=str(i + 1), background_normal='fad.jpg')
            else:
                btn1 = Button(text=str(i+1))
            btn1.bind(on_press=self.callback1)

            layout.add_widget(btn1)
        self.window.add_widget(layout)

        self.window.add_widget(Background())
        return self.window

    def callback1(self, instance):
        self.play_music(int(instance.text))


    def play_music(self, arg):
        if arg == 1:
            arg = 'mus/vspm.mp3'
        if arg == 2:
            arg = 'mus/steele.mp3'
        if arg == 3:
            arg = 'mus/fad.mp3'
        if arg == 4:
            arg = 'mus/rose.wav'
        music = SoundLoader.load(arg)
        if music:
            music.play()


if __name__ == "__main__":
    window = MusicWindow()
    window.run()
