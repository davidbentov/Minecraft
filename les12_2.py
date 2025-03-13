import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y, z, 57)
    time.sleep(0.2)