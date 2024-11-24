import pygame
import numpy as np
import random
import time

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
rozmiar_x = 50  # Liczba wierszy
rozmiar_y = 100  # Liczba kolumn
szerokosc_okna = 800
wysokosc_okna = 400
rozmiar_komorki = 10

# Kolory
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)
ZIELONY = (0, 255, 0)
CZERWONY = (255, 0, 0)

# Stworzenie okna gry
okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
pygame.display.set_caption("Gra w życie - Conway's Game of Life")


# Funkcja do tworzenia początkowej planszy
def utworz_plansze(rozmiar_x, rozmiar_y):
    plansza = np.random.randint(2, size=(rozmiar_x, rozmiar_y))
    return plansza


# Funkcja do liczenia żywych sąsiadów
def licz_sasiadow(plansza, x, y):
    sasiadow = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue
            if 0 <= i < len(plansza) and 0 <= j < len(plansza[0]):
                sasiadow += plansza[i, j]
    return sasiadow


# Funkcja do aktualizacji planszy
def aktualizuj_plansze(plansza):
    nowa_plansza = np.copy(plansza)
    for i in range(len(plansza)):
        for j in range(len(plansza[0])):
            sasiadow = licz_sasiadow(plansza, i, j)
            if plansza[i, j] == 1:
                if sasiadow < 2 or sasiadow > 3:
                    nowa_plansza[i, j] = 0
            else:
                if sasiadow == 3:
                    nowa_plansza[i, j] = 1
    return nowa_plansza


# Funkcja do rysowania planszy
def rysuj_plansze(plansza):
    for i in range(len(plansza)):
        for j in range(len(plansza[0])):
            kolor = ZIELONY if plansza[i, j] == 1 else CZARNY
            pygame.draw.rect(okno, kolor, (j * rozmiar_komorki, i * rozmiar_komorki, rozmiar_komorki, rozmiar_komorki))


# Funkcja do uruchomienia gry
def gra_w_zycie(rozmiar_x, rozmiar_y, iteracje=100):
    plansza = utworz_plansze(rozmiar_x, rozmiar_y)

    # Pętla gry
    uruchom_gry = True
    while uruchom_gry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                uruchom_gry = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    uruchom_gry = False

        # Aktualizacja i rysowanie planszy
        okno.fill(CZARNY)
        rysuj_plansze(plansza)
        pygame.display.update()

        # Aktualizacja planszy
        plansza = aktualizuj_plansze(plansza)

        # Opóźnienie, aby gra była płynniejsza
        time.sleep(0.1)


# Uruchomienie gry
gra_w_zycie(rozmiar_x, rozmiar_y)
pygame.quit()
