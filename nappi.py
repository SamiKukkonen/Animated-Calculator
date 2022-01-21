import pygame
from pygame.constants import MOUSEBUTTONDOWN
class Nappi():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		komento = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			while pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				komento = True
			if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
				self.clicked = False
		
		return komento
pkuva_0 = pygame.image.load("kuvat/0p.png")
pkuva_1 = pygame.image.load("kuvat/1p.png")
pkuva_2 = pygame.image.load("kuvat/2p.png")
pkuva_3 = pygame.image.load("kuvat/3.png")
pkuva_4 = pygame.image.load("kuvat/4p.png")
pkuva_5 = pygame.image.load("kuvat/5p.png")
pkuva_6 = pygame.image.load("kuvat/6p.png")
pkuva_7 = pygame.image.load("kuvat/7p.png")
pkuva_8 = pygame.image.load("kuvat/8p.png")
pkuva_9 = pygame.image.load("kuvat/9p.png")
laskin_kuva = pygame.image.load("kuvat/laskin1.png")
numero_kuva = pygame.image.load("kuvat/0.png")
ac_kuva = pygame.image.load("kuvat/AC.png")
nappi_1 = Nappi(18, 264, numero_kuva, 1)
nappi_2 = Nappi(100, 264, numero_kuva, 1)
nappi_3 = Nappi(180, 264, numero_kuva, 1)
nappi_4 = Nappi(18, 184, numero_kuva, 1)
nappi_5 = Nappi(100, 184, numero_kuva, 1)
nappi_6 = Nappi(180, 184, numero_kuva, 1)
nappi_7 = Nappi(18, 103, numero_kuva, 1)
nappi_8 = Nappi(100, 103, numero_kuva, 1)
nappi_9 = Nappi(180, 103, numero_kuva, 1)
nappi_0 = Nappi(18, 345, numero_kuva, 1)
poisto_nappi = Nappi(180,423, numero_kuva, 1)
tyhjays_nappi = Nappi(15,423,ac_kuva, 1)
piste_nappi = Nappi(100,345, numero_kuva, 1)
summa_nappi = Nappi(260, 345, numero_kuva, 1)
erotus_nappi = Nappi(260,264, numero_kuva, 1)
kerto_nappi = Nappi(260, 184, numero_kuva, 1)
jako_nappi = Nappi(260, 103, numero_kuva, 1)
prosentti_nappi = Nappi(260, 423, numero_kuva, 1)
yhteensa_nappi = Nappi(180, 345, numero_kuva, 1) 

