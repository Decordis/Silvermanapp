from kivy.uix.button import Button


class Questions:
    def __init__(self, app, label, layout):
        self.app = app
        self.label = label
        self.layout = layout
        self.score = app.score
        # Здесь мы правильно сохраняем атрибут
        self.current_question = app.current_question

    def next_question(self):
        if self.current_question == 0:
            self.ask_thorax_question()
        elif self.current_question == 1:
            self.ask_riber_question()
        elif self.current_question == 2:
            self.ask_xiphoid_question()
        elif self.current_question == 3:
            self.ask_mandibula_question()
        elif self.current_question == 4:
            self.ask_breath_question()
        else:
            self.app.finalize()  # вызов finalize через app

    def ask_thorax_question(self):
        # Устанавливаем текст и стиль для Label
        self.label.text = ('I. Оценка движения грудной клетки.'
                           '\nВыберите вариант:')
        self.label.font_size = '30sp'  # Размер шрифта
        self.label.color = (1, 1, 1, 1)  # Белый текст
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)

        # Создаем кнопки с увеличенными размерами
        self.buttons_thorax = [
            Button(text='0: Грудь и живот равномерно участвуют в акте дыхания',
                   font_size='24sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),  # Размер кнопки
                   pos_hint={'center_x': 0.5, 'center_y': 0.5}),
            Button(text='1: Аритмичное, неравномерное дыхание',
                   font_size='24sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.4}),
            Button(text='2: Западение верхней части грудной клетки',
                   font_size='24sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.3}),
                   ]
        for button in self.buttons_thorax:
            button.bind(on_press=self.evaluate_thorax)
            self.layout.add_widget(button)
        self.add_restart_button()
        self.add_get_main_button()

    def ask_riber_question(self):
        self.label.text = 'II. Оценка втяжения межреберных:\nВыберите вариант:'
        self.label.font_size = '30sp'
        self.label.color = (1, 1, 1, 1)
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)

        self.buttons_riber = [
            Button(text='0: Отсутствуют',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.5}),
            Button(text='1: Легкое втяжение',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.4}),
            Button(text='2: Заметное втяжение',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.3})
                   ]

        for button in self.buttons_riber:
            button.bind(on_press=self.evaluate_riber)
            self.layout.add_widget(button)
        self.add_restart_button()
        self.add_get_main_button()

    def ask_xiphoid_question(self):
        self.label.text = 'III. Оценка втяжения мечевидного отростка:'
        '\n Выберите вариант:'
        self.label.font_size = '30sp'
        self.label.color = (1, 1, 1, 1)
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)

        self.buttons_xiphoid = [
            Button(text='0: Отсутствуют',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.5}),
            Button(text='1: Небольшое втяжение',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.4}),
            Button(text='2: Заметное втяжение',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.3})
        ]

        for button in self.buttons_xiphoid:
            button.bind(on_press=self.evaluate_xiphoid)
            self.layout.add_widget(button)

        self.add_restart_button()
        self.add_get_main_button()

    def ask_mandibula_question(self):
        self.label.text = 'IV. Положение нижней челюсти:\nВыберите вариант:'
        self.label.font_size = '30sp'
        self.label.color = (1, 1, 1, 1)
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)

        self.buttons_mandibula = [
            Button(text='0: Рот закрыт, нижняя челюсть не западает',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.5}),
            Button(text='1: Рот закрыт, опускание подбородка на вдохе',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.4}),
            Button(text='2: Рот открыт, опускание подбородка на вдохе',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.3})
                   ]

        for button in self.buttons_mandibula:
            button.bind(on_press=self.evaluate_mandibula)
            self.layout.add_widget(button)
        self.add_restart_button()
        self.add_get_main_button()

    def ask_breath_question(self):
        self.label.text = 'V. Звучность дыхания:\nВыберите вариант:'
        self.label.font_size = '30sp'
        self.label.color = (1, 1, 1, 1)
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)

        self.buttons_breath = [
            Button(text='0: Дыхание спокойное, ровное',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.5}),
            Button(text='1: Экспираторные шумы слышны при аускультации',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.4}),
            Button(text='2: Экспираторные шумы слышны на расстоянии',
                   font_size='20sp',
                   background_color=(1, 0, 1, 1),
                   color=(1, 1, 1, 1),
                   size_hint=(None, None),
                   size=(400, 60),
                   pos_hint={'center_x': 0.5, 'center_y': 0.3}),
        ]

        for button in self.buttons_breath:
            button.bind(on_press=self.evaluate_breath)
            self.layout.add_widget(button)

        self.add_restart_button()
        self.add_get_main_button()

    def evaluate_thorax(self, instance):
        thorax_score = int(instance.text.split(':')[0])
        self.app.score += thorax_score
        self.current_question += 1
        self.app.current_question = self.current_question
        self.next_question()

    def evaluate_riber(self, instance):
        riber_score = int(instance.text.split(':')[0])
        self.app.score += riber_score
        self.current_question += 1
        self.next_question()

    def evaluate_xiphoid(self, instance):
        xiphoid_score = int(instance.text.split(':')[0])
        self.app.score += xiphoid_score
        self.current_question += 1
        self.next_question()

    def evaluate_mandibula(self, instance):
        mandibula_score = int(instance.text.split(':')[0])
        self.app.score += mandibula_score
        self.current_question += 1
        self.next_question()

    def evaluate_breath(self, instance):
        breath_score = int(instance.text.split(':')[0])
        self.app.score += breath_score
        self.current_question += 1
        self.app.current_question = self.current_question
        self.next_question()

    def add_restart_button(self):
        restart_button = Button(
            text='Начать заново',
            font_size='20sp',
            background_color=(1, 0, 0, 1),
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(400, 60),
            pos_hint={'center_x': 0.5, 'center_y': 0.2})
        restart_button.bind(on_press=self.restart_test)
        self.layout.add_widget(restart_button)

    def add_get_main_button(self):
        restart_button = Button(
            text='Вернуться в меню',
            font_size='20sp',
            background_color=(1, 0, 0, 1),
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(400, 60),
            pos_hint={'center_x': 0.5, 'center_y': 0.1})
        restart_button.bind(on_press=self.get_main)
        self.layout.add_widget(restart_button)

    def restart_test(self, instance):
        self.app.score = 0
        self.current_question = 0
        self.ask_thorax_question()

    def get_main(self, instance):
        self.app.restart(instance)
