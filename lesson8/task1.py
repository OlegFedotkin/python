month = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
         '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}


class Date:

    @classmethod
    def date_conversion(cls, date):
        new_date = date.split('-')
        int_date = [int(j) for j in new_date]
        return int_date

    @staticmethod
    def check_int(date):
        n_date = Date.date_conversion(date)
        if 1 < n_date[1] > 12:
            return f'Неверно указан номер месяца!'
        elif n_date[2] < 0:
            return f'Неверно указан год!'
        elif 1 < n_date[0] > month.get(str(n_date[1])):
            return f'Неверно указано число!'
        else:
            return f'Дата указана верно!'


print(Date.date_conversion('11-02-2021'))
print(Date.check_int('11-02-2021'))