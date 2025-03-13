from mcpi.minecraft import Minecraft
mc = Minecraft.create()

username = input("видите имя: ")

while True:
    text = input("видите текст: ")
    if text == "стоп":
        break
    else:
         mc.postToChat(username + ": " + text)

