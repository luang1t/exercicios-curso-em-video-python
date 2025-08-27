import pygame
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/luanz/OneDrive/Desktop/exercicios-curso-em-video-python/Royel Otis — Linger.mp3")
pygame.mixer.music.play()


#FIZ A PRIMEIRA VEZ E DEU ERRADO PQ ESTAVA COM BARRAS INVERTIDAS E BARRAS INVERTIDAS EM PYTHON É UM CARACTERE DE ESCAPE, ENTÃO O CERTO É SUBSTITUIR AS \ POR / TODA A VEZ. DA PRA FAZER COM CTRL + D
#pygame.mixer.init()
#pygame.mixer.music.load("C:\Users\luanz\OneDrive\Desktop\exercicios-curso-em-video-python/Royel Otis — Linger.mp3")
#pygame.mixer.music.play()

# Para manter o programa rodando enquanto toca
import time
while pygame.mixer.music.get_busy():
    time.sleep(1)