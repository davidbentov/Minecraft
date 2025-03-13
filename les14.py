import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


def put_melon():
    melon=103
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y - 1, z, melon)
    print('Арбуз')

def put_tree():
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x, y, z, x, y+3, z, 17)
    mc.setBlocks(x-2, y+4, z-2, x+2, y+4, z+2, 17)
    mc.setBlocks(x - 1, y + 5, z - 1, x + 1, y + 5, z + 1, 18)
    mc.setBlock(x, y + 6, z, 18)


while True:
    put_tree()
    time.sleep(3)
