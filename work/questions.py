

from kivy.uix.button import Button


class Questions:
  
    def __init__(self, app, label, layout):
        self.app = app
        self.label = label
        self.layout = layout
        self.score = app.score
        self.current_question = app.current_question  # Здесь мы правильно сохраняем атрибут

    def next_question(self):
        # print(f"Текущий вопрос: {self.current_question}") Включать, если нужна отладка
        # print(f"Текущий балл: {self.app.score}")
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

        
        self.buttons_thorax = [
        Button(text='0: Грудь и живот равномерно участвуют в акте дыхания',
            #    size_hint=(0.8, 0.8),  
               font_size = '20sp',
            #    size=(100, 10),  
               background_color=(1, 0, 1, 1),  
               color=(1, 1, 1, 1)),  # Белый текст
        Button(text='1: Аритмичное, неравномерное дыхание',
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1)),  # Белый текст
        Button(text='2: Западение верхней части грудной клетки',
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1)),  # Белый текст
    ]
        for button in self.buttons_thorax:
            button.bind(on_press=self.evaluate_thorax)
            self.layout.add_widget(button)

    def ask_riber_question(self):
        self.label.text = 'II. Оценка втяжения межреберных:\nВыберите вариант:'
        self.label.font_size = '30sp'  # Размер шрифта
        self.label.color = (1, 1, 1, 1)  # Белый текст
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)

        self.buttons_riber = [
            Button(text='0: Отсутствуют',
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1)),
            Button(text='1: Легкое втяжение',            
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1)),
            Button(text='2: Заметное втяжение',           
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1))
        ]

        for button in self.buttons_riber:
            button.bind(on_press=self.evaluate_riber)
            self.layout.add_widget(button)

    def ask_xiphoid_question(self):
        self.label.text = 'III. Оценка втяжения мечевидного отростка:\nВыберите вариант:'
        self.label.font_size = '30sp'  # Размер шрифта
        self.label.color = (1, 1, 1, 1)  # Белый текст
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)

        self.buttons_xiphoid = [
            Button(text='0: Отсутствуют',             
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1)),
            Button(text='1: Небольшое втяжение',           
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1)),
            Button(text='2: Заметное втяжение',             
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1))
        ]

        for button in self.buttons_xiphoid:
            button.bind(on_press=self.evaluate_xiphoid)
            self.layout.add_widget(button)

    def ask_mandibula_question(self):
        self.label.text = 'IV. Положение нижней челюсти:\nВыберите вариант:'
        self.label.font_size = '30sp'  # Размер шрифта
        self.label.color = (1, 1, 1, 1)  # Белый текст
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)

        self.buttons_mandibula = [
            Button(text='0: Рот закрыт, нижняя челюсть не западает',
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1)),
            Button(text='1: Рот закрыт, опускание подбородка на вдохе',
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1)),
            Button(text='2: Рот открыт, опускание подбородка на вдохе',
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1))
        ]

        for button in self.buttons_mandibula:
            button.bind(on_press=self.evaluate_mandibula)
            self.layout.add_widget(button)

    def ask_breath_question(self):
        self.label.text = 'V. Звучность дыхания:\nВыберите вариант:'
        self.label.font_size = '30sp'  # Размер шрифта
        self.label.color = (1, 1, 1, 1)  # Белый текст
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)

        self.buttons_breath = [
            Button(text='0: Дыхание спокойное, ровное', 
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1)),
            Button(text='1: Экспираторные шумы слышны при аускультации',
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1)),
            Button(text='2: Экспираторные шумы слышны на расстоянии',
            #    size_hint=(None, None),
            #    size=(600, 50),
               font_size = '20sp',
               background_color=(1, 0, 1, 1), 
               color=(1, 1, 1, 1))
        ]

        for button in self.buttons_breath:
            button.bind(on_press=self.evaluate_breath)
            self.layout.add_widget(button)

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