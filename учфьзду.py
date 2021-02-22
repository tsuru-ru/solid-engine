import os
import sys
import time
import pygame
import random

n = 0
clock = pygame.time.Clock()
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
p = ['e.jpg', 'e.jpg', 'w.jpg', 'w.jpg', 'q.jpg', 'q.jpg']
random.shuffle(p)
b = []
r = 0
p_n = [p[:3],p[3:]]
picture = {}
picture_1 = {}

def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def proverka_cc(x, y): # координаты
    x0 = (x - 100) // 100
    y0 = (y - 100) // 100
    if x0 > -1 and y0 > -1 and  x0 < 2 and y0 < 3:
        return y0, x0
    else:
        print(None)

def finish(one, two):
    picture_1[one] = 1
    picture_1[two] = 1
    print(picture_1)
    if len(picture_1) == 6:
        print("FINISH")
        return True


def look(z): # показать
    image = load_image(p_n[z[1]][z[0]])
    image1 = pygame.transform.scale(image, (100, 100))  # размер картинки
    screen.blit(image1, (100 + 100 * z[1], 100 + 100 * z[0]))  # нахождение картинки

ap = []
print(picture)
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('получаю картинку')
    running = True
    lo_f, lo_s = False, False
    for i in range(2): # расположение карточек
        for j in range(3):
            picture[i, j] = 1
            image = load_image("short.png")
            image1 = pygame.transform.scale(image, (100, 100))  # размер картинки
            screen.blit(image1, (100 + 100 * i, 100 + 100 * j))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                z1 = proverka_cc(x, y)
                st = pygame.time.get_ticks()
                if z1:
                    look(z1)
                    if z1 not in ap:
                        ap.append(z1)
                '''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                    z2 = proverka_cc(x, y)
                    st = pygame.time.get_ticks()
                    look(z2)
                    if z2 not in ap:
                        ap.append(z2)
                '''
                if len(ap) == 3:
                    print(ap)
                    if p_n[ap[0][1]][ ap[0][0]] == p_n[ap[1][1]][ap[1][0]]:
                        print('Right')
                        if finish(ap[0], ap[1]):
                            break
                        ap = [ap[-1]]
                    else:
                        print('NOO')
                        st = pygame.time.get_ticks()
                        while st + 1000 > pygame.time.get_ticks():
                            image = load_image("short.png")
                            image1 = pygame.transform.scale(image, (100, 100))  # размер картинки
                            screen.blit(image1, (100 + 100 * ap[0][1], 100 + 100 * ap[0][0]))
                            screen.blit(image1, (100 + 100 * ap[1][1], 100 + 100 * ap[1][0]))
                        ap = [ap[-1]]
                elif len(ap) > 3:
                    ap = []
                elif len(ap) == 2:
                    if finish(ap[0], ap[1]):
                        break


        pygame.display.flip()
        pygame.time.wait(10)
    pygame.quit()
