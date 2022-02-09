"""
Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

#Importação da biblioteca
import pygame

#O Mixer deve ser iniciado primeiro que o Pygame
#Iniciando o Mixer
pygame.mixer.init()

#Iniciando o Pygame
pygame.init()

#Carregando a Música
pygame.mixer.music.load('DJSmash.mp3')

#SOM NA CAIXA DJ!
pygame.mixer.music.play()

pygame.event.wait()

