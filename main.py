from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.texture import Texture

from PIL import Image as PILImage
import os

screenshot_path = "/storage/emulated/0/py_server/forcode/screenshot.png"

class ScreenMirrorApp(App):
    def build(self):
        Window.fullscreen = True  # На весь экран
        self.img_widget = Image()
        layout = FloatLayout()
        layout.add_widget(self.img_widget)

        # обновлять изображение каждые 2 секунды
        Clock.schedule_interval(self.update_image, 2)

        return layout

    def update_image(self, dt):
        if not os.path.exists(screenshot_path):
            return

        try:
            img = PILImage.open(screenshot_path).convert('RGB')
            width, height = img.size

            # Верхняя половина
            upper_half = img.crop((0, 0, width, height // 2))
            flipped = upper_half.transpose(PILImage.FLIP_TOP_BOTTOM)
            img.paste(flipped, (0, 0))

            # Преобразуем в texture
            img = img.resize((Window.width, Window.height))
            texture = Texture.create(size=(img.width, img.height))
            texture.blit_buffer(img.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
            texture.flip_vertical()

            # Обновить виджет
            self.img_widget.texture = texture

        except Exception as e:
            print("Ошибка:", e)


if __name__ == '__main__':
    ScreenMirrorApp().run()