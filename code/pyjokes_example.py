import pyjokes

joke = pyjokes.get_joke()

print(joke)

import pyfiglet
ascii_art = pyfiglet.figlet_format("Hello World!")
print(ascii_art)

import cowsay
cowsay.cow("Moo! I am Yang Zhou, a Python programmer!")

# Using different animals
cowsay.trex("Yang is amazing!")
cowsay.dragon("Yang love Python!")
cowsay.cat("Yang is a good boy!")
