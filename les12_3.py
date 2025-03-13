from mcpi.minecraft import Minecraft



mc = Minecraft.create()

while True:
    command = input('Куб, башня или выход: ').lower()
    if command == "выход":
        print("до свидание!")
        break
    x, y,z = mc.player.getTilePos()
    if command == "куб":
        block_type =int(input('Введите id блока: '))
        mc.setBlocks(x, y, z, x+4, y+4, z+4, block_type)
    elif command == "башня":
        h = int(input("Ввидите высоту башни:  "))
        for i in range(h):
            mc.setBlock(x, y, z, 57)
            y += 1
    else:
        print("такой команды нет вот тебе камень!!!")
        mc.setBlock(x, y, z, 1)
    print("-"*40)
