import pygame

class Sprite(pygame.sprite.Sprite):
    ''' Создание родительского класса Sprite '''
    def __init__(self, x, y, width, height, filename):
        ''' Инициализация базовых параметров '''
        pygame.sprite.Sprite.__init__(self)
        # Передача атрибуту image файла с картинкой и изменение размеров
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        # Перемещение картинки в центр экрана
        self.rect = self.image.get_rect(center=(x, y))

class Button(pygame.sprite.Sprite):
    ''' Отвечает за отрисовку кнопки, расположение в ней текста и её подсветку '''
    def __init__(self, x, y, text, font):
        ''' Инициализация базовых параметров '''
        pygame.sprite.Sprite.__init__(self)
        self.text_surf, self.text_rect = font.render(text, (0, 0, 0))
        self.image = pygame.Surface((self.text_rect.width*1.5, self.text_rect.height*1.5))
        self.image.fill((242, 165, 22))
        self.blit_text()

        self.rect = self.image.get_rect(center=(x, y))

    def blit_text(self):
        ''' Расположение текста внутри кнопки посередине '''
        self.image.blit(
            self.text_surf,
            (
                (self.image.get_rect().w - self.text_rect.w) / 2,
                (self.image.get_rect().h - self.text_rect.h) / 2,
            ),
        )

    def be_inside(self, x, y):
        ''' Условия нахождения курсора мыши в кнопке и вне ее '''
        if self.rect.x < x < self.rect.right and self.rect.y < y < self.rect.bottom:
            return True
        else:
            return False

    def update(self, mouse_x, mouse_y):
        ''' Проверка нахождения курсора мыши в кнопке и изменение цвета кнопки '''
        if self.be_inside(mouse_x, mouse_y):
            self.image.fill((139, 0, 139))
            self.blit_text()
        else:
            self.image.fill((218, 112, 214))
            self.blit_text()

    def updatel(self, mouse_x, mouse_y):
        ''' Проверка нахождения курсора мыши в кнопке и изменение цвета кнопки '''
        if self.be_inside(mouse_x, mouse_y):
            self.image.fill((255, 165, 0))
            self.blit_text()
        else:
            self.image.fill((248, 213, 104))
            self.blit_text()
