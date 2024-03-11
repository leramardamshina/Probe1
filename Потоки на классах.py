#Инструкции:
#Напишите программу с использованием механизмов многопоточности, которая создает два потока-рыцаря.

#Каждый рыцарь должен иметь имя (name) и умение(skill). Умение рыцаря определяет, сколько времени потребуется рыцарю,
#чтобы выполнить свою защитную миссию для королевства.
#Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить вражеское войско на skill-человек.
#Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
#Чем выше умение, тем быстрее рыцарь защитит королевство.

import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        print(f'{self.name} на нас напали!', flush=True)
        enemies = 100
        days = 0
        while enemies > 0:
            days += 1
            enemies = enemies - self.skill
            if enemies < 0:
                enemies = 0
            print(f' {self.name} сражается {days} день(дня)... , осталось {enemies} воинов', flush=True)
            time.sleep(5)
        print(f'{self.name} одержал побежу спустя {days} дней',flush=True)

knight1 = Knight("Sir Lancelot", 10) # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20) # Высокий уровень умения

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Все битвы закончились!")