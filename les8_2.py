import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

time.sleep(15)

blockHits = mc.events.pollBlockHits()   # Получаем список ударов
my_items = []   # Создаем пустой список для хранения id блоков

item_pos0 = blockHits[0].pos        # Получаем координаты 0-го удара
item0 = mc.getBlock(item_pos0)      # Получаем id блока по координатам
my_items.append(item0)              # Добавляем блок в НАШ саисок

item_pos1 = blockHits[1].pos
item1 = mc.getBlock(item_pos1)
my_items.append(item1)

item_pos2 = blockHits[2].pos
item2 = mc.getBlock(item_pos2)
my_items.append(item2)

x, y, z = mc.player.getTilePos()
mc.setBlock(x, y, z, my_items[0])
mc.setBlock(x, y+1, z, my_items[1])
mc.setBlock(x, y+2, z, my_items[2])