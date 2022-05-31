from enum import Enum
import pygame

class value(Enum):
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Seven = 7
    Eight = 8
    Ten = 10
    Eleven = 11
    Twelve = 12
    Sorry = 'Sorry!'


pi = 3.14
y = 250

class Card:
    def __init__(self, v):
        self.value = v

    def set_value(self, setter):
        self.value = setter

    def get_value(self):
        return self.value

    def draw(self, screen):
        black = (0, 0, 0)
        white = (250, 250, 250)
        cyan = (0, 250, 250)
        x = 250
        pygame.draw.rect(screen, white, pygame.Rect(x, y, 70, 150))
        pygame.draw.rect(screen, white, pygame.Rect(x-15, y+15, 100, 120))
        pygame.draw.circle(screen, white, (x, y + 15), 15)
        pygame.draw.circle(screen, white, (x + 70, y + 15), 15)
        pygame.draw.circle(screen, white, (x, y + 135), 15)
        pygame.draw.circle(screen, white, (x + 70, y + 135), 15)

        pygame.draw.arc(screen, black, (x - 15, y, 30, 30), pi/2, pi)
        pygame.draw.line(screen, black, (x - 15, y + 15), (x - 15, y + 135))
        pygame.draw.arc(screen, black, (x - 15, y + 120, 30, 30), pi, 3 * pi/2)
        pygame.draw.line(screen, black, (x, y + 150), (x + 70, y + 150))
        pygame.draw.arc(screen, black, (x + 55, y + 120, 30, 30), 3 * pi / 2, 2 * pi)
        pygame.draw.line(screen, black, (x + 85, y + 135), (x + 85, y + 15))
        pygame.draw.arc(screen, black, (x + 55, y, 30, 30), 2 * pi, pi / 2)
        pygame.draw.line(screen, black, (x, y), (x + 70, y))

        if self.value.value == 1:
            pygame.draw.lines(screen, black, False, [(x + 25, y + 45), (x + 40, y + 30), (x + 40, y + 100),
                                                 (x + 20, y + 100), (x + 55, y + 100)])
        if self.value.value == 2:
            pygame.draw.arc(screen, black, (x + 15, y + 35, 40, 40), 0, pi)
            pygame.draw.lines(screen, black, False, [(x + 55, y + 55), (x + 15, y + 100), (x + 55, y + 100)])

        if self.value.value == 3:
            pygame.draw.arc(screen, black, (x + 15, y + 35, 40, 40), 3 * pi / 2, 3 * pi)
            pygame.draw.arc(screen, black, (x + 15, y + 75, 40, 40), pi, 5 * pi / 2)

        if self.value.value == 4:
            pygame.draw.lines(screen, black, False, [(x + 55, y + 75),
                                                     (x + 5, y + 75), (x + 40, y + 30), (x + 40, y + 100)])
        if self.value.value == 5:
            pygame.draw.lines(screen, black, False, [(x + 55, y + 30), (x + 25, y + 30), (x + 25, y + 60)])
            pygame.draw.arc(screen, black, (x, y + 60, 50, 50), -pi/2, -3 * pi/2)

        if self.value.value == 7:
            pygame.draw.lines(screen, black, False, [(x + 15, y + 30), (x + 55, y + 30), (x + 15, y + 110)])

        if self.value.value == 8:
            pygame.draw.circle(screen, black, (x + 35, y + 45), 30, 1)
            pygame.draw.circle(screen, black, (x + 35, y + 103), 30, 1)

        if self.value.value == 10:
            pygame.draw.lines(screen, black, False, [(x + 5, y + 45), (x + 20, y + 30), (x + 20, y + 100),
                                                     (x, y + 100), (x + 35, y + 100)])
            pygame.draw.arc(screen, black, (x + 45, y + 32, 30, 70), 0, 3 * pi)

        if self.value.value == 11:
            pygame.draw.lines(screen, black, False, [(x + 5, y + 45), (x + 20, y + 30), (x + 20, y + 100),
                                                     (x, y + 100), (x + 35, y + 100)])
            pygame.draw.lines(screen, black, False, [(x + 45, y + 45), (x + 60, y + 30), (x + 60, y + 100),
                                                     (x + 40, y + 100), (x + 75, y + 100)])

        if self.value.value == 12:
            pygame.draw.lines(screen, black, False, [(x + 5, y + 45), (x + 20, y + 30), (x + 20, y + 100),
                                                     (x, y + 100), (x + 35, y + 100)])
            pygame.draw.arc(screen, black, (x + 35, y + 35, 40, 40), 0, pi)
            pygame.draw.lines(screen, black, False, [(x + 75, y + 55), (x + 45, y + 100), (x + 80, y + 100)])

        if self.value.value == "Sorry!":
            pygame.draw.rect(screen, black, pygame.Rect(x - 13, y + 45, 95, 55), 1)

            pygame.draw.arc(screen, black, (x - 10, y + 50, 20, 20), 2 * pi, 7*pi/2)
            pygame.draw.arc(screen, black, (x - 10, y + 70, 20, 20), pi, 5 * pi / 2)
            pygame.draw.arc(screen, black, (x + 11, y + 50, 15, 40), 0, 3 * pi)
            pygame.draw.line(screen, black, (x + 26, y + 50), (x + 26, y + 90))
            pygame.draw.arc(screen, black, (x + 16, y + 50, 20, 20), -pi/2, -3 * pi/2)
            pygame.draw.line(screen, black, (x + 30, y + 70), (x + 40, y + 90))
            pygame.draw.line(screen, black, (x + 40, y + 50), (x + 40, y + 90))
            pygame.draw.arc(screen, black, (x + 30, y + 50, 20, 20), -pi / 2, -3 * pi / 2)
            pygame.draw.line(screen, black, (x + 40, y + 70), (x + 50, y + 90))
            pygame.draw.lines(screen, black, False, [(x + 50, y + 50), (x + 55, y + 70),
                                                     (x + 60, y + 50), (x + 55, y + 70), (x + 55, y + 90)])
            pygame.draw.rect(screen, black, pygame.Rect(x + 65, y + 50, 10, 30))
            pygame.draw.circle(screen, black, (x + 70, y + 90), 5)

        pygame.display.flip()

    def draw_back(self, screen):
        teal = (0, 125, 250)
        black = (0, 0, 0)
        white = (250, 250, 250)

        x = 360
        pygame.draw.rect(screen, teal, pygame.Rect(x, y, 70, 150))
        pygame.draw.rect(screen, teal, pygame.Rect(x - 15, y + 15, 100, 120))
        pygame.draw.circle(screen, teal, (x, y + 15), 15)
        pygame.draw.circle(screen, teal, (x + 70, y + 15), 15)
        pygame.draw.circle(screen, teal, (x, y + 135), 15)
        pygame.draw.circle(screen, teal, (x + 70, y + 135), 15)

        pygame.draw.arc(screen, black, (x - 15, y, 30, 30), pi / 2, pi)
        pygame.draw.line(screen, black, (x - 15, y + 15), (x - 15, y + 135))
        pygame.draw.arc(screen, black, (x - 15, y + 120, 30, 30), pi, 3 * pi / 2)
        pygame.draw.line(screen, black, (x, y + 150), (x + 70, y + 150))
        pygame.draw.arc(screen, black, (x + 55, y + 120, 30, 30), 3 * pi / 2, 2 * pi)
        pygame.draw.line(screen, black, (x + 85, y + 135), (x + 85, y + 15))
        pygame.draw.arc(screen, black, (x + 55, y, 30, 30), 2 * pi, pi / 2)
        pygame.draw.line(screen, black, (x, y), (x + 70, y))
        pygame.draw.lines(screen, black, True, [(x - 15, y + 75), (x + 35, y + 15),
                                                    (x + 85, y + 75), (x + 35, y + 135)])

        pygame.draw.rect(screen, white, pygame.Rect(x + 10, y + 25, 50, 100))
        pygame.draw.rect(screen, black, pygame.Rect(x + 10, y + 25, 50, 100), 1)
        pygame.draw.arc(screen, black, (x + 15, y + 100, 20, 20), pi, 2 * pi, 2)
        pygame.draw.arc(screen, black, (x + 35, y + 103, 20, 20), 2 * pi, 3 * pi, 2)
        pygame.draw.arc(screen, black, (x + 15, y + 90, 40, 15), 0, 3 * pi, 2)
        pygame.draw.line(screen, black, (x + 15, y + 85), (x + 55, y + 85), 2)
        pygame.draw.arc(screen, black, (x + 15, y + 75, 20, 20), 2 * pi, 3 * pi, 2)
        pygame.draw.line(screen, black, (x + 35, y + 85), (x + 50, y + 75), 2)
        pygame.draw.line(screen, black, (x + 15, y + 70), (x + 55, y + 70), 2)
        pygame.draw.arc(screen, black, (x + 15, y + 60, 20, 20), 2 * pi, 3 * pi, 2)
        pygame.draw.line(screen, black, (x + 35, y + 70), (x + 50, y + 60), 2)
        pygame.draw.lines(screen, black, False, [(x + 15, y + 55), (x + 35, y + 50),
                                                            (x + 15, y + 45), (x + 35, y + 50), (x + 55, y + 50)], 2)
        pygame.draw.rect(screen, black, pygame.Rect(x + 15, y + 35, 30, 5))
        pygame.draw.circle(screen, black, (x + 53, y + 37), 3)