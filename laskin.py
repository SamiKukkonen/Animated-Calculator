import pygame, math
from sys import exit
from nappi import *
from pygame.constants import K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_RETURN, RESIZABLE
pygame.init()


tulos = ""
laskin = ""

fontti = pygame.font.SysFont("Ariel", 120)
LEVEYS, KORKEUS = (laskin_kuva.get_width(), laskin_kuva.get_height())
RUUTU = pygame.display.set_mode((LEVEYS, KORKEUS), RESIZABLE)
pygame.display.set_caption("Laskin")
musta = (0,0,0)
def tuloksen_piirto(x, y):
    global fontti
    if len(tulos) == 1:
        fontti = pygame.font.SysFont("Ariel", 120)
    if len(tulos) >= 2:
        fontti = pygame.font.SysFont("Ariel", 120)
        x -= 52
        if "." in tulos:
            x += 30
    if len(tulos) >= 3:
        fontti = pygame.font.SysFont("Ariel", 120)
        x -= 52
    if len(tulos) >= 4:
        fontti = pygame.font.SysFont("Ariel", 120)
        x -= 52
    if len(tulos) >= 5:
        fontti = pygame.font.SysFont("Ariel", 120)
        x -= 52
    if len(tulos) >= 6:
        fontti = pygame.font.SysFont("Ariel", 100)
        x -= 10
    if len(tulos) >= 7:
        fontti = pygame.font.SysFont("Ariel", 90)
        x -= 20
    if len(tulos) >= 8:
        fontti = pygame.font.SysFont("Ariel", 80)
        x -= 20
    lasku = fontti.render(str(tulos), True, (musta))
    RUUTU.blit(lasku, (x,y))

pohjassa = False
while True:
    RUUTU.blit(laskin_kuva, (0,0))
    keys = pygame.key.get_pressed()
    for komento in pygame.event.get():
        if komento.type == pygame.QUIT:
            pygame.quit()
            exit
        if komento.type == pygame.KEYDOWN:
            if komento.key == pygame.K_RETURN:
                vastaus = eval(laskin)
                tulos = str(vastaus)
        if komento.type == pygame.KEYDOWN:
            pohjassa = True
        if komento.type == pygame.KEYUP:
            pohjassa = False
    if nappi_0.draw(RUUTU) or keys[K_0] and pohjassa == False:
        tulos += "0"
        laskin += "0"
    if nappi_1.draw(RUUTU) or keys[K_1] and pohjassa == False:
        tulos += "1"
        laskin += "1"
    if nappi_2.draw(RUUTU) or keys[K_2] and pohjassa == False:
        tulos += "2"
        laskin += "2"
    if nappi_3.draw(RUUTU) or keys[K_3] and pohjassa == False:
        tulos += "3"
        laskin += "3"
    if nappi_4.draw(RUUTU) or keys[K_4] and pohjassa == False:
        tulos += "4"
        laskin += "4"
    if nappi_5.draw(RUUTU) or keys[K_5] and pohjassa == False:
        tulos += "5"
        laskin += "5"
    if nappi_6.draw(RUUTU) or keys[K_6] and pohjassa == False:
        tulos += "6"
        laskin += "6"
    if nappi_7.draw(RUUTU) or keys[K_7] and pohjassa == False:
        tulos += "7"
        laskin += "7"
    if nappi_8.draw(RUUTU) or keys[K_8] and pohjassa == False:
        tulos += "8"
        laskin += "8"
    if nappi_9.draw(RUUTU) or keys[K_9] and pohjassa == False:
        tulos += "9"
        laskin += "9"
    if poisto_nappi.draw(RUUTU):
        tulos = tulos[:-1]
        laskin = laskin[:-1]
    if tyhjays_nappi.draw(RUUTU):
        tulos = ""
        laskin = ""
    if piste_nappi.draw(RUUTU):
        tulos += "."
        laskin += "."
    if summa_nappi.draw(RUUTU):
        tulos += "+"
        laskin += "+"
    if erotus_nappi.draw(RUUTU):
        tulos += "-"
        laskin += "-"
    if kerto_nappi.draw(RUUTU):
        tulos += "*"
        laskin += "*"
    if jako_nappi.draw(RUUTU):
        tulos += "/"
        laskin += "/"
    if prosentti_nappi.draw(RUUTU):
        tulos += "%"
        laskin += "%"
    if keys[K_0] and pohjassa == True:
         RUUTU.blit(pkuva_0, (18, 345))
    if keys[K_1] and pohjassa == True:
         RUUTU.blit(pkuva_1, (18, 264))
    if keys[K_2] and pohjassa == True:
         RUUTU.blit(pkuva_2, (100, 264))
    if keys[K_3] and pohjassa == True:
         RUUTU.blit(pkuva_3, (180, 264))
    if keys[K_4] and pohjassa == True:
         RUUTU.blit(pkuva_4, (18, 184))
    if keys[K_5] and pohjassa == True:
         RUUTU.blit(pkuva_5, (100, 184))
    if keys[K_6] and pohjassa == True:
         RUUTU.blit(pkuva_6, (180, 184))
    if keys[K_7] and pohjassa == True:
         RUUTU.blit(pkuva_7, (18, 103))
    if keys[K_8] and pohjassa == True:
         RUUTU.blit(pkuva_8, (100, 103))
    if keys[K_9] and pohjassa == True:
         RUUTU.blit(pkuva_9, (180, 103))
    if yhteensa_nappi.draw(RUUTU):
        vastaus = eval(laskin)
        checkfloat = isinstance(vastaus, float)
        if checkfloat:
            vastaus = str(round(vastaus, 5))
        else:
            pass
        tulos = str(vastaus)
    tuloksen_piirto(285, 10)
    pygame.display.update()