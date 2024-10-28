""" 
Данный блок обрабатывает сумму баллов 
и выдает заключение по полученным результатам.
 """

class Result:

    def __init__(self, app):
        self.app = app
        self.score = app.score

    def get_result(self):
        score = self.score

        if 1 <= score < 3:
            result = (
                  f' {score}\n'
                  f'Начальные признаки синдрома дыхательных растройств')
            
            return result

        elif 3 <= score <= 6:
            result = (
                  f' {score}\n'
                  f'Средняя степень тяжести синдрома дыхательных расстройств')
            
            return result

        elif 7 <= score:
            result = (
                      f' {score}\n'
                      f'Тяжелый синдром дыхательных расстройств')
            
            
            return result

        else:
            result = (
                      f' {score}\n'
                      f'Признаков дыхательных расстройств нет')
            
            return result