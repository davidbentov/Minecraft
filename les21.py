from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class Building:
    def __init__(self, p, t, b,):
        self.pos = p
        self.type = t
        self.block = b

    def build(self):
        if self.type == "коробка":
            print("коробка")
            self.box()
        elif self.type == "дерево":
            print("дерево")
            self.tree()
        else:
            print("такой постройки у нас нет :(")

    def box(self):
        x, y, z = self.pos
        mc.setBlocks(x, y, z, x+4, y+4, z+4, self.block)
        mc.setBlocks(x+1, y+1, z+1, x+3, y+3, z+3,0)

    def tree(self):
        x, y, z = self.pos
        mc.setBlocks(x, y, z, x, y + 4, z, 17)
        mc.setBlocks(x - 2, y + 5, z - 2, x + 2, y + 5, z + 2,self.block )
        mc.setBlocks(x - 1, y + 6, z - 1, x + 1, y + 6, z + 1,self.block )
        mc.setBlock(x, y + 7, z, 18)

x, y, z= mc.player.getTilePos()
box = Building((x, y, z), "коробка", 41)
box.build()

tree1 = Building((x+7, y, z), "дерево", 41)
tree1.build()