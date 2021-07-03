# Imports
import qrcode 
# Func

def img(l,s):
    po = qrcode.make(l)
    po.save(s)

# GitHub
img1 = qrcode.make("https://github.com/MarcoPaoletta") # link 
img1.save("GitHub.png") # save img

# Python
img2 = qrcode.make("https://www.python.org")
img2.save("Python.png")

# Godot Engine
img3 = qrcode.make("https://godotengine.org")
img3.save("Godot.png")

# JavaScript
img("https://www.javascript.com", "JavaScript.png")

# Unity
img("https://unity.com/es", "Unity.png")

# Game Maker Studio
img("https://www.yoyogames.com/es/gamemaker", "GameMaker.png")

"""
We can use a func (line 7) or we can use separated variables
They work the same but I think it is better if you use a function
"""
# The user will create the qrcode


print("Hello and welcome to my qrcode generator!")
l = input("Write down a link: ") 
n = input("Give the archive a name a name and a valid extension (.png): ")

img(l,n)

print("Perfect! Check the project folder")

print("Final results:")
print("LInk: " + l)
print("Archive name: " + n)