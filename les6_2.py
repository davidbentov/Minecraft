from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x_ocean=101
y_ocean=63
z_ocean=354
answer=input("выбири локацыю (океан): ")

if answer=="океан":
    mc.player.setTilePos(x_ocean, y_ocean, z_ocean,)
else:
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x - 2, y - 2, z - 2, x - 2, y - 1, z - 2, 0, )
print('я не знаю такой локации на диржы кратер')

