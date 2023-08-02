from typing import Any

import pygame.rect

from Source.constants import SIZE, GUN_SIZE, GUN_IMAGE, BULLET_SPEED, BULLET_SIZE


class Gun:
    def __init__(self):
        self._rect_ = pygame.Rect(SIZE[0] // 2 - GUN_SIZE[0] // 2, SIZE[1] - GUN_SIZE[1], *GUN_SIZE)
        self._image_ = GUN_IMAGE
        self.__start_image__ = self._image_.copy()

    def get_rect(self) -> pygame.rect.Rect:
        return self._rect_

    def get_image(self) -> pygame.Surface:
        return self._image_

    def get_coordinates(self) -> tuple[int, int]:
        return self._rect_.x, self._rect_.y

    def shoot(self, mouse_coordinates: tuple[int, int]) -> Any:
        x, y = mouse_coordinates

        scale_x = -(self._rect_.x - x) / SIZE[0]
        scale_y = -(self._rect_.y - y) / SIZE[1]

        return Bullet(self, (BULLET_SPEED * scale_x, BULLET_SPEED * scale_y))


class Bullet:
    def __init__(self, gun: Gun, momentum: tuple[int, int]):
        gun_x, gun_y = gun.get_coordinates()
        self._rect_ = pygame.Rect(gun_x + gun.get_rect().width // 2, gun_y, BULLET_SIZE, BULLET_SIZE)
        self._momentum_ = momentum

    def move(self) -> None:
        self._rect_.x += self._momentum_[0]
        self._rect_.y += self._momentum_[1]

    def get_rect(self) -> pygame.Rect:
        return self._rect_

    def get_coordinates(self) -> tuple[int, int]:
        return self._rect_.x, self._rect_.y
