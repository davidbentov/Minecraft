import time
from time import sleep

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z =  mc.player.getTilePos()

for i in range(5):
    for  j in range(3):
        mc.setBlock(x, y, z, 19)
        y+= 1
    time.sleep(3)
