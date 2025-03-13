import random
import time

from les8 import my_items

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
my_items =[]
for i in  range(10):
    rn = random.randint(1, 45)
    my_items.append(rn)


x, y, z,= mc.player.getTilePos()

for item in my_items:
    mc.setBlock(x, y, z, item)
    y += 1  # y = y + 1
    time.sleep(1)