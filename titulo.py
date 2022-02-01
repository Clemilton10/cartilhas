import keyboard
from time import sleep

# Esperar teclar CTRL
keyboard.wait('ctrl')

# espera 1 segundo
sleep(1)

# ir para o inicio
# pressiona e solta a tecla home
keyboard.press_and_release('home')

# digitar
keyboard.write('# <font color=#ffdd00>', delay=0.02)

# ir para o final
# pressiona e solta a tecla end
keyboard.press_and_release('end')

# digitando o resto
keyboard.write('</font>', delay=0.02)