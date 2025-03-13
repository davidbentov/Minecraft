from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def check_block(x_block,y_block, z_block):
    block = mc.getBlock(x_block,y_block, z_block)
    value_blocks = [57, 46, 41, 20]
    if block in value_blocks:
        return "ура ценный блокнайден :)"
    else:
        return "Увы, ценного блока нет :("

x, y, z = mc.player.getTilePos()
message = check_block(x,y-1, z)
print(message)