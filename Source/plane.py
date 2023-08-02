import random

import pygame

from Source.constants import SIZE, PLANE_SIZE, PLANE_SPEED


class Plane:
    def __init__(self):
        # random.randint(0, SIZE[0] - PLANE_SIZE[0])
        self._rect_ = pygame.Rect(random.randint(0, SIZE[0] - PLANE_SIZE[0]), random.randint(0, 300), *PLANE_SIZE)
        self._color_ = (250, 250, 250)

        self._direction_ = random.choice([-2, -1.5, -1, 1, 1.5, 2])
        self._momentum_ = (PLANE_SPEED * self._direction_, 0)

    def move(self) -> None:
        self._rect_.x += self._momentum_[0]
        self._rect_.y += self._momentum_[1]

    def get_coordinates(self) -> tuple[int, int]:
        return self._rect_.x, self._rect_.y

    def get_rect(self) -> pygame.Rect:
        return self._rect_

    def set_color(self, color: tuple[int, int, int]) -> None:
        self._color_ = color

    def get_color(self) -> tuple[int, int, int]:
        return self._color_

    def get_direction(self) -> float:
        return self._direction_
