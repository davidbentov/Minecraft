from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def get_wool_state(color):
    if color == 'белый':
        return 0
    elif color == 'оранжевый':
        return 1
    elif color == "сиреневый":
        return 2
    elif color == "светло-синий":
        return 3
    elif color == "желтый":
        return 4
    elif color == "лаймовый":
        return 5
    elif color == "розовый":
        return 6
    elif color == "серый":
        return 7
    elif color == "светло-серый":
        return 8
    elif color == "бирюзовый":
        return 9
    elif color == "фиолетовый":
        return 10
    elif color == "синий":
        return 11
    elif color == "коричневый":
        return 12
    elif color == "зеленый":
        return 13
    elif color == "красный":
        return 14
    elif color == "черный":
        return 15
    else:
        print('Я не знаю такого цвета :( Вот тебе белая шерсть')
        return 0

color = input('Введите цвет шерсти: ')
state = get_wool_state(color)

x, y, z = mc.player.getTilePos()
mc.setBlocks(x, y, z, x+3, y+3, z+3, 35, state)

def get_wool_state():