'''import playsound
playsound.playsound('sertanejo.mp3')
'''

import pygame
pygame.mixer.init()#iniciando
pygame.mixer.music.load('sertanejo.mp3')
pygame.mixer.music.play() #dá o play
input('tocar')
pygame.event.wait() #fecha qdo acaba

