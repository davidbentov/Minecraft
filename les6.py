from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer=input("создать кратер? да/нет:")

if answer== "да":
    x, y, z=mc.player.getTilePos()
    mc.setBlocks(x-2, y-2, z-2, x-2, y-1, z-2, 0, )
    print('бабах')

