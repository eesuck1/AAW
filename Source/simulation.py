import sys
from typing import Any, List, Tuple

import numpy.random
import pygame

from Source.constants import SIZE, FPS, BACKGROUND_COLOR, PLANE_SIZE, BACKGROUND_IMAGE
from Source.gun import Gun
from Source.model import Model
from Source.plane import Plane


class AAW:
    def __init__(self):
        self._screen_ = pygame.display.set_mode(SIZE)
        self._clock_ = pygame.time.Clock()

        self._gun_ = Gun()
        self._bullets_ = []
        self._planes_ = []

        self._model_ = Model()

        self._delay_counter_ = 0
        self._prediction_ = None

        self.spawn_planes()
        self._target_ = numpy.random.choice(self._planes_)
        self._target_.set_color((140, 0, 0))

        self._positions_ = {
            "mouse": (0, 0),
            "plane": self.get_planes_coordinates(),
        }

        pygame.display.set_caption("AAW")

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()

                    self._bullets_.append(self._gun_.shoot(mouse_position))

                    self._positions_["mouse"] = mouse_position
                    self._positions_["plane"] = self.get_planes_coordinates()

            self.update_game()

    def update_game(self) -> None:
        self._screen_.blit(BACKGROUND_IMAGE, (0, 0))
        self.draw_gun()

        self.spawn_planes()
        self._delay_counter_ += 1

        if self._target_ not in self._planes_:
            self._target_ = numpy.random.choice(self._planes_)
            self._target_.set_color((140, 0, 0))

        if self._delay_counter_ % 10 == 0:
            self.update_target_prediction()

        if self._delay_counter_ % 1000 == 0:
            self._model_.train()

        self.update_planes()
        self.update_bullets()

        self._clock_.tick(FPS)
        pygame.display.update()

    def draw_gun(self) -> None:
        self._screen_.blit(self._gun_.get_image(), self._gun_.get_coordinates())

    def update_target_prediction(self) -> None:
        self._prediction_ = self._model_.predict(
            numpy.array((*self._target_.get_coordinates(), self._target_.get_direction())).reshape(-1, 3)
        )
        self._positions_["mouse"] = self._prediction_
        self._positions_["plane"] = self.get_planes_coordinates()
        self._bullets_.append(self._gun_.shoot(self._prediction_))

    def update_planes(self) -> None:
        for plane in self._planes_:
            plane.move()
            self.draw_plane(plane)

            if self.check_borders(plane):
                self._planes_.remove(plane)

    def draw_plane(self, plane: Plane) -> None:
        self._screen_.blit(plane.get_image(), plane.get_coordinates())

    def update_bullets(self) -> None:
        for bullet in self._bullets_:
            bullet.move()
            self.draw_bullet(bullet)

            collision = bullet.get_rect().collidelist([plane.get_rect() for plane in self._planes_])
            if collision != -1:
                self.handle_collision(collision)

            if self.check_borders(bullet):
                self._bullets_.remove(bullet)

    def draw_bullet(self, bullet: Any) -> None:
        pygame.draw.rect(self._screen_, (250, 250, 250), bullet.get_rect())

    def handle_collision(self, collision: int) -> None:
        plane = self._planes_[collision]
        if plane.get_color() == (140, 0, 0):  # and not (400 < plane.get_coordinates()[0] < 800):
            # mouse_x, mouse_y = self._positions_.get("mouse")
            # plane_x, plane_y = self._positions_.get("plane")[collision]
            # with open("labels.txt", "a") as file:
            #     file.write(f'{mouse_x}, {mouse_y}, {plane_x}, {plane_y}, {plane.get_direction()}\n')

            self._planes_.pop(collision)
            self._bullets_.clear()

    def spawn_planes(self) -> None:
        if len(self._planes_) < 1:
            self._planes_.append(Plane())

    def get_planes_coordinates(self) -> List[Tuple[int, int]]:
        if self._planes_:
            return [plane.get_coordinates() for plane in self._planes_]

    @staticmethod
    def check_borders(sprite: Any) -> bool:
        x, y = sprite.get_coordinates()

        if not (-sprite.get_rect().width < x < SIZE[0]) or not (0 < y < SIZE[1]):
            return True
