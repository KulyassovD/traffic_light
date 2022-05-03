import datetime
from tkinter import *
from tkinter import Tk, Label
from dataclasses import dataclass
from typing import Dict, Type


class CountdownTimer(Tk):
    def __init__(self):
        super().__init__()
        self.label_secs = Label(self, text="0",  bg="white")
        self.label_secs.grid(row=1, column=3)
        self.rem_seconds = (data_dict['red_a']-1000)/1000
        self.after(1000, self.start_countdown)

    def start_countdown(self):
        if self.rem_seconds == -1:
            self.rem_seconds = (data_dict['red_s']-1000)/1000
            self.start_countdown1()
        else:
            self.label_secs.configure(text="%d" % self.rem_seconds)
            self.rem_seconds -= 1
            self.after(1000, self.start_countdown)

    def start_countdown1(self):
        if self.rem_seconds == -1:
            self.rem_seconds = (data_dict['red_a']-1000)/1000
            self.start_countdown()
        else:
            self.label_secs.configure(text="%d" % self.rem_seconds)
            self.rem_seconds -= 1
            self.after(1000, self.start_countdown1)


class Frame(Tk):
    def __init__(self):
        self.state = 0
        super().__init__()
        self.title(data_dict['name'])
        self.canvas = c = Canvas(self, width=140, height=380, bg="black")
        self.r = c.create_oval(20, 20, 120, 120, fill="#ff0000")
        self.y = c.create_oval(20, 140, 120, 240, fill="#808000")
        self.g = c.create_oval(20, 260, 120, 360, fill="#008000")
        c.pack()
        self.state1 = 0
        self.title('Шаляпина-Алтынсарина')
        self.canvas1 = c1 = Canvas(self, width=140, height=380, bg="black")
        self.red = c1.create_oval(20, 20, 120, 120, fill='#800000')
        self.yellow = c1.create_oval(20, 140, 120, 240, fill="#808000")
        self.green = c1.create_oval(20, 260, 120, 360, fill='#00ff00')
        c1.pack()
        self.update()
        self.after(1000, self.upd1)
        self.after(1000, self.upd)

    def upd(self):
        """Время зеленого Шаляпина"""
        if self.state == 0:
            self.state = 1
            self.canvas.itemconfigure(self.r, fill='#800000')
            self.canvas.itemconfigure(self.g, fill='#00ff00')
            self.after(data_dict['green_s'], self.upd)
        elif self.state == 1:
            """Код для моргания зеленого Шаляпина"""
            self.state = 2
            self.canvas.itemconfigure(self.g, fill='#008000')
            self.after(500, self.upd)
        elif self.state == 2:
            """Код для моргания зеленого Шаляпина"""
            self.state = 3
            self.canvas.itemconfigure(self.g, fill='#00ff00')
            self.after(500, self.upd)
        elif self.state == 3:
            """Код для моргания зеленого Шаляпина"""
            self.state = 4
            self.canvas.itemconfigure(self.g, fill='#008000')
            self.after(500, self.upd)
        elif self.state == 4:
            """Код для моргания зеленого Шаляпина"""
            self.state = 5
            self.canvas.itemconfigure(self.g, fill='#00ff00')
            self.after(500, self.upd)
        elif self.state == 5:
            """Код для моргания зеленого Шаляпина"""
            self.state = 6
            self.canvas.itemconfigure(self.g, fill='#008000')
            self.after(500, self.upd)
        elif self.state == 6:
            """Код для моргания зеленого Шаляпина"""
            self.state = 7
            self.canvas.itemconfigure(self.g, fill='#00ff00')
            self.after(500, self.upd)
        elif self.state == 7:
            """Время желтого Шаляпина"""
            self.state = 8
            self.canvas.itemconfigure(self.g, fill='#008000')
            self.canvas.itemconfigure(self.y, fill='#ffff00')
            self.after(data_dict['yellow_s'], self.upd)
        else:
            """Время красного в конце цикла Шаляпина"""
            self.state = 0
            self.canvas.itemconfigure(self.r, fill='#ff0000')
            self.canvas.itemconfigure(self.y, fill='#808000')
            self.after(data_dict['red_s'], self.upd)

    def upd1(self):
        """Время красного Алтынсарина"""
        if self.state1 == 0:
            self.state1 = 1
            self.canvas1.itemconfigure(self.red, fill="#ff0000")
            self.canvas1.itemconfigure(self.yellow, fill='#808000')
            self.canvas1.itemconfigure(self.green, fill="#008000")
            self.after(data_dict['red_a'], self.upd1)
            """Время зеленого Алтынсарина"""
        elif self.state1 == 1:
            self.state1 = 2
            self.canvas1.itemconfigure(self.red, fill='#800000')
            self.canvas1.itemconfigure(self.green, fill='#00ff00')
            self.after(data_dict['green_a'], self.upd1)
        elif self.state1 == 2:
            """Код для моргания зеленого Алтынсарина"""
            self.state1 = 3
            self.canvas1.itemconfigure(self.red, fill='#800000')
            self.canvas1.itemconfigure(self.green, fill="#008000")
            self.after(500, self.upd1)
        elif self.state1 == 3:
            """Код для моргания зеленого Алтынсарина"""
            self.state1 = 4
            self.canvas1.itemconfigure(self.red, fill='#800000')
            self.canvas1.itemconfigure(self.green, fill='#00ff00')
            self.after(500, self.upd1)
        elif self.state1 == 4:
            """Код для моргания зеленого Алтынсарина"""
            self.state1 = 5
            self.canvas1.itemconfigure(self.red, fill='#800000')
            self.canvas1.itemconfigure(self.green, fill="#008000")
            self.after(500, self.upd1)
        elif self.state1 == 5:
            """Код для моргания зеленого Алтынсарина"""
            self.state1 = 6
            self.canvas1.itemconfigure(self.red, fill='#800000')
            self.canvas1.itemconfigure(self.green, fill='#00ff00')
            self.after(500, self.upd1)
        elif self.state1 == 6:
            """Код для моргания зеленого Алтынсарина"""
            self.state1 = 7
            self.canvas1.itemconfigure(self.red, fill='#800000')
            self.canvas1.itemconfigure(self.green, fill="#008000")
            self.after(500, self.upd1)
        elif self.state1 == 7:
            """Код для моргания зеленого Алтынсарина"""
            self.state1 = 8
            self.canvas1.itemconfigure(self.red, fill='#800000')
            self.canvas1.itemconfigure(self.green, fill='#00ff00')
            self.after(500, self.upd1)
        elif self.state1 == 8:
            """Код желтого Алтынсарина"""
            self.state1 = 0
            self.canvas1.itemconfigure(self.red, fill='#800000')
            self.canvas1.itemconfigure(self.yellow, fill='#ffff00')
            self.canvas1.itemconfigure(self.green, fill='#008000')
            self.after(data_dict['yellow_a'], self.upd1)


@dataclass
class InfoMessage:
    W: int
    E: int
    N: int
    S: int
    now_time: datetime.time()
    morning = datetime.time(8)
    day = datetime.time(10)
    evening = datetime.time(17)
    night = datetime.time(20)

    def comparison(self):
        """Функция сравнения"""
        if self.now_time == self.morning and (self.E or self.W) > 20:
            global data_dict
            data_dict = {'red_s':6000,
                         'yellow_s':1000,
                         'green_s':14000,
                         'red_a':18000,
                         'yellow_a': 1000,
                         'green_a': 2000,
                         'name': 'Утро Шаляпина- Алтынсарина'}
            app = CountdownTimer()
            root = Frame()
            app.mainloop()
            root.mainloop()
            return data_dict
        elif self.now_time == self.day:
            data_dict = {'red_s':8000,
                         'yellow_s':1000,
                         'green_s':11000,
                         'red_a':15000,
                         'yellow_a': 1000,
                         'green_a': 4000,
                         'name': 'День Шаляпина- Алтынсарина'}
            app = CountdownTimer()
            root = Frame()
            app.mainloop()
            root.mainloop()
            return data_dict
        elif self.now_time == self.evening and (self.E or self.W)  > 20:
            data_dict = {'red_s':6000,
                         'yellow_s':1000,
                         'green_s':14000,
                         'red_a':18000,
                         'yellow_a': 1000,
                         'green_a': 2000,
                         'name': 'Вечер Шаляпина- Алтынсарина'}
            app = CountdownTimer()
            root = Frame()
            app.mainloop()
            root.mainloop()
            return data_dict
        elif self.now_time == self.night:
            data_dict = {'red_s':7000,
                         'yellow_s':1000,
                         'green_s':11000,
                         'red_a':14000,
                         'yellow_a': 1000,
                         'green_a': 3000,
                         'name': 'Ночь Шаляпина- Алтынсарина'}
            app = CountdownTimer()
            root = Frame()
            app.mainloop()
            root.mainloop()
            return data_dict


def read_package(workout_type: str, data: int) -> InfoMessage:
    """Прочитать данные полученные от датчиков."""
    dict: Dict[str, Type[InfoMessage]] = {'PAC': InfoMessage,
                                          'PAC_2': InfoMessage,
                                          'PAC_3': InfoMessage}
    return dict[workout_type](*data)


def main(traffic: InfoMessage) -> None:
    """Главная функция."""
    traffic.comparison()


if __name__ == '__main__':
    """водимые данные"""
    packages = [
        ('PAC', [15, 21, 10, 8, datetime.time(8)]),
        ('PAC_2', [42, 10, 75, 8, datetime.time(10)]),
        ('PAC_3', [12, 45, 30, 12, datetime.time(17)]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
