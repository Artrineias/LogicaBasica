import pygame

pygame.init()
pygame.mixer.music.load('/home/artrineias/Documentos/exercicios_de python/4°exercicios/musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
