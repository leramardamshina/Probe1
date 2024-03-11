#Инструкции:
#Напишите программу с использованием механизмов многопоточности, которая создает два потока-рыцаря.

#Каждый рыцарь должен иметь имя (name) и умение(skill). Умение рыцаря определяет, сколько времени потребуется рыцарю,
#чтобы выполнить свою защитную миссию для королевства.
#Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить вражеское войско на skill-человек.
#Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
#Чем выше умение, тем быстрее рыцарь защитит королевство.
#enemy_count - кол-во врагов
#defend_per_day - каждый день убывает столько-то количество врагов
#remaining_enemies - оставшиеся враги

import random
import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)  #супер используется вместо родительского класса
        self.name = name
        self.skill = skill

    def run(self):
        enemy_count = random.randint(1, 100) #кол-во врагов
        print(f'Враги нападают в количестве {enemy_count} человек', flush=True)
        if self.skill >= 20:
            defend_per_day = self.skill
            remaining_enemies = enemy_count - defend_per_day
            print(f'Рыцарь {self.name} ослабил вражевское войско на {remaining_enemies} человек')
            if remaining_enemies >= 0:
                print(f'Рыцарь {self.name} победил')
            else:
                print(f'Продолжаем сражаться, врагов осталось {remaining_enemies}', flush=True)
                time.sleep(5)
        else:
            print(f'Продолжаем сражаться')



knight1 = Knight("Sir Lancelot", 10) # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20) # Высокий уровень умения

knight1.start()
knight2.start()

knight1.join()
knight2.join()