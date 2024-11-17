from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from progs.texts import Start, Info
from work.questions import Questions
from kivy.uix.image import Image


class Silverman(App):
    """
    Основной класс приложения Silverman,
    контролирующий логику интерфейса и навигацию между экранами.
    """
    def build(self):  # Создает основное окно с виджетами.
        self.score = 0
        self.current_question = 0
        self.layout = FloatLayout()

        # Установка фона
        with self.layout.canvas.before:
            Color(0.5, 0.5, 1, 1)  # RGB-цвет (синий)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        img_neon = Image(
            source='images/neon.png',
            size_hint=(None, None),
            size=(150, 150)  # Увеличен размер изображения
        )
        img_neon.pos_hint = {'right': 1, 'top': 1}  # В верхнем углу
        self.layout.add_widget(img_neon)

        self.label = Label(
            text=Start().greet(),
            font_size='30sp',
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': 0.5, 'top': 0.85}  # Центрирование
        )
        self.layout.add_widget(self.label)

        self.start_button = Button(
            text='Начать оценку',
            font_size='24sp',
            background_color=(1, 0, 1, 1),
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(400, 80),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.start_button.bind(on_press=self.start_evaluation)
        self.instruction_button = Button(
            text='Инструкция',
            font_size='24sp',
            background_color=(1, 0, 1, 1),
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(400, 80),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        self.instruction_button.bind(on_press=self.get_instruction)
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.instruction_button)
        return self.layout

    def _update_rect(self, *args):
        self.rect.pos = self.layout.pos
        self.rect.size = self.layout.size

    def get_instruction(self, instance):
        self.label.text = Info().instruction()
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)
        back_button = Button(
            text='Назад',
            font_size='20sp',
            background_color=(1, 0, 1, 1),
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(300, 60),
            pos_hint={'center_x': 0.5, 'center_y': 0.3}
        )
        back_button.bind(on_press=self.back_to_main)
        self.layout.add_widget(back_button)

    def back_to_main(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.instruction_button)
        self.label.text = Start().greet()

    def start_evaluation(self, instance):
        self.question_handler = Questions(self, self.label, self.layout)
        self.question_handler.next_question()  # Начинаем с первого вопроса

    def finalize(self):  # Завершает оценивание и показывает общий балл.
        from progs.result import Result
        end = Result(self).get_result()
        if 1 <= self.score < 3:
            with self.layout.canvas.before:
                Color(0, 1, 0, 1)  # Зеленый
                self.rect = Rectangle(size=self.layout.size,
                                      pos=self.layout.pos)
            self.layout.bind(size=self._update_rect,
                             pos=self._update_rect)
        elif 3 <= self.score < 6:
            with self.layout.canvas.before:
                Color(1, 1, 0, 1)  # Желтый
                self.rect = Rectangle(size=self.layout.size,
                                      pos=self.layout.pos)
            self.layout.bind(size=self._update_rect,
                             pos=self._update_rect)
        elif 7 <= self.score:
            with self.layout.canvas.before:
                Color(1, 0, 0, 1)  # Красный
                self.rect = Rectangle(size=self.layout.size,
                                      pos=self.layout.pos)
            self.layout.bind(size=self._update_rect, pos=self._update_rect)

        self.label = Label(
            text=f'Общий балл: {end}',
            font_size='30sp',
            color=(0, 0, 0, 1),
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': 0.5, 'top': 0.85}
        )

        self.layout.clear_widgets()
        self.layout.add_widget(self.label)
        restart_button = Button(
            text='Начать заново',
            font_size='24sp',
            background_color=(1, 0, 1, 1),
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(800, 80),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        restart_button.bind(on_press=self.restart)
        self.layout.add_widget(restart_button)

    def restart(self, instance):
        """
        Сбрасывает состояние приложения и
        возвращает пользователя на главный экран.

        Параметры:
        instance: Текущий экземпляр кнопки, которая вызвала это действие.
        """
        self.score = 0
        self.current_question = 0
        with self.layout.canvas.before:
            Color(0.5, 0.5, 1, 1)  # RGB-цвет (синий)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.bind(size=self._update_rect, pos=self._update_rect)
        self.back_to_main(instance)
