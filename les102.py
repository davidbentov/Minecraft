from mcpi.minecraft import Minecraft
mc = Minecraft.create()

matrix_list = [
    [57 ,57 ,57 ,57],
    [46 ,46 ,46 ,46],
    [20 ,20 ,20 ,20]
]

x, y, z = mc.player.getTilePos()
x_start = x
for row in matrix_list:
    for block in row:

        mc.setBlock(x, y, z, block )
        x += 1
    y += 1
    x = x_start