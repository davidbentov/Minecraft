from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block = 57

x, y, z = mc.player.getTilePos()


mc.setBlocks(x, y, z, x+5, y+5, z+5, 57)
(mc.setBlocks(x+1, y+1, z+1, x+4, y+4, z+3, 0))

print(random.randint(1, 6))

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x_rand = random.randint(0, 50)
y_rand = random.randint(0, 25)
z_rand = random.randint(0, 50)

x, y, z = mc.player.getTilePos()
mc.player.setTilePos(x + x_rand, y + y_rand, z + z_rand)