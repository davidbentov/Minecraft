# import time
# import random
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
#
# def put_block(id_block):
#     x, y, z = mc.player.getTilePos()
#     mc.setBlock(x, y-1, z, id_block)
#     print(id_block)
#
# while True:
#     put_block(57)
#     time.sleep(3)

# def summa(num1,num2,):
#     print(num1 + num2)
# a = int(input('num_1: '))
# b = int(input('num_2: '))
# summa(a, b)
#
# summa(5,  7)



# def mul(num1, num2,):
#     print(num1, * num2)
# a = int(input()


def calc(num_1, num_2, o):
     if op == '*':
         return n1 * n2

n1 = int(input("n1: "))
n2 = int(input("n2: "))
op = input("op: ")
#print(op)
#calc(n1, n2, op)
#$calc(2, 3,  "*")
print(calc(n1, n2, op))

