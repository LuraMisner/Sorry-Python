from space import *
import pygame


# Orientation: Corner by green safety, going clockwise around board.
class Board:
    def __init__(self, win):
        pygame.init()
        self.window = win
        # Make 88 total spaces
        board_list = list()
        for i in range(88):
            new_space = Space()
            board_list.append(new_space)

        # Start Spaces, G - 11, R - 33, B - 55, Y - 77
        board_list[11].set_type(reserved_type.START)
        board_list[33].set_type(reserved_type.START)
        board_list[55].set_type(reserved_type.START)
        board_list[77].set_type(reserved_type.START)

        # Slides
        # Green Slides - (1-2,9-10), 16-20
        board_list[1].set_type(reserved_type.GREEN_SLIDE)
        board_list[2].set_type(reserved_type.GREEN_SLIDE)
        board_list[9].set_type(reserved_type.GREEN_SLIDE)
        board_list[10].set_type(reserved_type.GREEN_SLIDE)

        board_list[16].set_type(reserved_type.GREEN_SLIDE)
        board_list[17].set_type(reserved_type.GREEN_SLIDE)
        board_list[18].set_type(reserved_type.GREEN_SLIDE)
        board_list[19].set_type(reserved_type.GREEN_SLIDE)
        board_list[20].set_type(reserved_type.GREEN_SLIDE)

        # Red Slide - (23-24,31-32), 38-42
        board_list[23].set_type(reserved_type.RED_SLIDE)
        board_list[24].set_type(reserved_type.RED_SLIDE)
        board_list[31].set_type(reserved_type.RED_SLIDE)
        board_list[32].set_type(reserved_type.RED_SLIDE)

        board_list[38].set_type(reserved_type.RED_SLIDE)
        board_list[39].set_type(reserved_type.RED_SLIDE)
        board_list[40].set_type(reserved_type.RED_SLIDE)
        board_list[41].set_type(reserved_type.RED_SLIDE)
        board_list[42].set_type(reserved_type.RED_SLIDE)

        # Blue Slides - (45-46, 53-54), 60-64
        board_list[45].set_type(reserved_type.BLUE_SLIDE)
        board_list[46].set_type(reserved_type.BLUE_SLIDE)
        board_list[53].set_type(reserved_type.BLUE_SLIDE)
        board_list[54].set_type(reserved_type.BLUE_SLIDE)

        board_list[60].set_type(reserved_type.BLUE_SLIDE)
        board_list[61].set_type(reserved_type.BLUE_SLIDE)
        board_list[62].set_type(reserved_type.BLUE_SLIDE)
        board_list[63].set_type(reserved_type.BLUE_SLIDE)
        board_list[64].set_type(reserved_type.BLUE_SLIDE)

        # Yellow Slides - (67-68, 75-76), 82-86
        board_list[67].set_type(reserved_type.YELLOW_SLIDE)
        board_list[68].set_type(reserved_type.YELLOW_SLIDE)
        board_list[75].set_type(reserved_type.YELLOW_SLIDE)
        board_list[76].set_type(reserved_type.YELLOW_SLIDE)

        board_list[82].set_type(reserved_type.YELLOW_SLIDE)
        board_list[83].set_type(reserved_type.YELLOW_SLIDE)
        board_list[84].set_type(reserved_type.YELLOW_SLIDE)
        board_list[85].set_type(reserved_type.YELLOW_SLIDE)
        board_list[86].set_type(reserved_type.YELLOW_SLIDE)

        # Safety zones + Home
        # Green (3-7, 8)
        board_list[3].set_type(reserved_type.GREEN_SAFETY)
        board_list[4].set_type(reserved_type.GREEN_SAFETY)
        board_list[5].set_type(reserved_type.GREEN_SAFETY)
        board_list[6].set_type(reserved_type.GREEN_SAFETY)
        board_list[7].set_type(reserved_type.GREEN_SAFETY)
        board_list[8].set_type(reserved_type.HOME)

        # Red (25-29,30)
        board_list[25].set_type(reserved_type.RED_SAFETY)
        board_list[26].set_type(reserved_type.RED_SAFETY)
        board_list[27].set_type(reserved_type.RED_SAFETY)
        board_list[28].set_type(reserved_type.RED_SAFETY)
        board_list[29].set_type(reserved_type.RED_SAFETY)
        board_list[30].set_type(reserved_type.HOME)

        # Blue (47-51,52)
        board_list[47].set_type(reserved_type.BLUE_SAFETY)
        board_list[48].set_type(reserved_type.BLUE_SAFETY)
        board_list[49].set_type(reserved_type.BLUE_SAFETY)
        board_list[50].set_type(reserved_type.BLUE_SAFETY)
        board_list[51].set_type(reserved_type.BLUE_SAFETY)
        board_list[52].set_type(reserved_type.HOME)

        # Yellow (69-73, 74)
        board_list[69].set_type(reserved_type.YELLOW_SAFETY)
        board_list[70].set_type(reserved_type.YELLOW_SAFETY)
        board_list[71].set_type(reserved_type.YELLOW_SAFETY)
        board_list[72].set_type(reserved_type.YELLOW_SAFETY)
        board_list[73].set_type(reserved_type.YELLOW_SAFETY)
        board_list[74].set_type(reserved_type.HOME)

        self.board = board_list

        # Will get updated when drawing board.
        self.mapping = list()

        # Keep track of all the pieces
        pieces = dict()

        green_positions = list()
        green_positions.append(11)
        green_positions.append(11)
        green_positions.append(11)
        green_positions.append(11)
        pieces['Green'] = green_positions

        red_positions = list()
        red_positions.append(33)
        red_positions.append(33)
        red_positions.append(33)
        red_positions.append(33)
        pieces['Red'] = red_positions

        blue_positions = list()
        blue_positions.append(55)
        blue_positions.append(55)
        blue_positions.append(55)
        blue_positions.append(55)
        pieces['Blue'] = blue_positions

        yellow_positions = list()
        yellow_positions.append(77)
        yellow_positions.append(77)
        yellow_positions.append(77)
        yellow_positions.append(77)
        pieces['Yellow'] = yellow_positions
        self.positions = pieces

    def get_board(self):
        return self.board

    def get_positions(self):
        return self.positions

    def get_position(self, color: str):
        if color == 'Red' or color == 'Green' or color == 'Blue' or color == 'Yellow':
            return self.positions[color]
        else:
            print("Invalid color")

    def set_position(self, color: str, piece: int, new: int):
        if color == 'Red' or color == 'Green' or color == 'Blue' or color == 'Yellow':
            if piece < 4:
                if new < 88:
                    self.positions[color][piece] = new
                else:
                    print("Board position out of range")
            else:
                print("Piece index out of range")
        else:
            print("Invalid color")

    def won(self, color: str):
        winner = True
        if color == "Green":
            for i in range(len(self.positions[color])):
                if self.positions[color][i] != 8:
                    winner = False
        elif color == "Red":
            for i in range(len(self.positions[color])):
                if self.positions[color][i] != 30:
                    winner = False
        elif color == "Blue":
            for i in range(len(self.positions[color])):
                if self.positions[color][i] != 52:
                    winner = False
        else:
            # yellow
            for i in range(len(self.positions[color])):
                if self.positions[color][i] != 74:
                    winner = False

        return winner

    def print_board_spaces(self):
        index = 0
        for space in self.board:
            print('index: ' + str(index) + ', ' + Space.to_string(space))
            index += 1

    def print_board(self):
        line1 = "\n"
        line1 += " 0"
        line1 += self.board[0].board_string()
        line1 += " 1"
        line1 += self.board[1].board_string()
        line1 += " 2"
        line1 += self.board[2].board_string()
        line1 += " 9"
        line1 += self.board[9].board_string()
        line1 += " 10"
        line1 += self.board[10].board_string()
        for x in range(12, 23):
            line1 += " " + str(x)
            line1 += self.board[x].board_string()
        print(line1)
        line2 = ""
        line2 += "87"
        line2 += self.board[87].board_string() + " "
        line2 += "     3"
        line2 += self.board[3].board_string() + "      "
        line2 += "11"
        line2 += self.board[11].board_string()
        for x in range(10):
            line2 += "      "
        line2 += " 23"
        line2 += self.board[23].board_string()
        print(line2)
        line3 = ""
        line3 += "86"
        line3 += self.board[86].board_string() + " "
        line3 += "     4"
        line3 += self.board[4].board_string()
        for x in range(6):
            line3 += "     "
        line3 += "     "
        for x in range(7):
            line3 += " " + str(30 - x)
            line3 += self.board[30 - x].board_string()
        print(line3)
        line4 = ""
        line4 += "85"
        line4 += self.board[85].board_string() + "      5"
        line4 += self.board[5].board_string()
        for x in range(12):
            line4 += "      "
        line4 += "31"
        line4 += self.board[31].board_string()
        print(line4)
        line5 = "84"
        line5 += self.board[84].board_string() + "      6"
        line5 += self.board[6].board_string()
        for x in range(11):
            line5 += "     "
        line5 += "           33"
        line5 += self.board[33].board_string()
        line5 += " 32"
        line5 += self.board[32].board_string()
        print(line5)
        line6 = "83"
        line6 += self.board[83].board_string() + "      7"
        line6 += self.board[7].board_string()
        for x in range(12):
            line6 += "      "
        line6 += "34"
        line6 += self.board[34].board_string()
        print(line6)
        line7 = "82"
        line7 += self.board[82].board_string() + "      8"
        line7 += self.board[8].board_string()
        for x in range(12):
            line7 += "      "
        line7 += "35"
        line7 += self.board[35].board_string()
        print(line7)
        line8 = "81"
        line8 += self.board[81].board_string()
        for x in range(14):
            line8 += "     "
        line8 += "            36"
        line8 += self.board[36].board_string()
        print(line8)
        line9 = "80"
        line9 += self.board[80].board_string()
        for x in range(14):
            line9 += "     "
        line9 += "            37"
        line9 += self.board[37].board_string()
        print(line9)
        line10 = "79"
        line10 += self.board[79].board_string()
        for x in range(12):
            line10 += "     "
        line10 += "           52"
        line10 += self.board[52].board_string() + "      38"
        line10 += self.board[38].board_string()
        print(line10)
        line11 = "78"
        line11 += self.board[78].board_string()
        for x in range(12):
            line11 += "     "
        line11 += "           51"
        line11 += self.board[51].board_string() + "      39"
        line11 += self.board[39].board_string()
        print(line11)
        line12 = "76"
        line12 += self.board[76].board_string()
        line12 += " 77"
        line12 += self.board[77].board_string()
        for x in range(11):
            line12 += "     "
        line12 += "          50"
        line12 += self.board[50].board_string() + "      40"
        line12 += self.board[40].board_string()
        print(line12)
        line13 = "75"
        line13 += self.board[75].board_string()
        for x in range(12):
            line13 += "     "
        line13 += "           49"
        line13 += self.board[49].board_string() + "      41"
        line13 += self.board[41].board_string()
        print(line13)
        line14 = "68"
        line14 += self.board[68].board_string()
        for x in range(69, 75):
            line14 += " " + str(x)
            line14 += self.board[x].board_string()
        for x in range(6):
            line14 += "     "
        line14 += "     48"
        line14 += self.board[48].board_string() + "      42"
        line14 += self.board[42].board_string()
        print(line14)
        line15 = "67"
        line15 += self.board[67].board_string()
        for x in range(10):
            line15 += "      "
        line15 += " 55"
        line15 += self.board[55].board_string() + "     47"
        line15 += self.board[47].board_string() + "      43"
        line15 += self.board[43].board_string()
        print(line15)
        line16 = ""
        for x in range(11):
            line16 += str(66 - x)
            line16 += self.board[66 - x].board_string()
            line16 += " "
        line16 += "54"
        line16 += self.board[54].board_string()
        line16 += "53"
        line16 += self.board[53].board_string()
        line16 += "46"
        line16 += self.board[46].board_string()
        line16 += "45"
        line16 += self.board[45].board_string()
        line16 += " 44"
        line16 += self.board[44].board_string()
        line16 += "\n"
        print(line16)

    def draw_board(self, win):
        RED = (255, 0, 0)
        YELLOW = (255, 255, 51)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        BACKGROUND = (192, 192, 192)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        win.fill(BACKGROUND)

        SQUARE_SIZE = 40
        rows = list()
        rows.append([0,   1,  2,  9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        rows.append([87, -1,  3, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 23])
        rows.append([86, -1,  4, -1, -1, -1, -1, -1, -1, 30, 29, 28, 27, 26, 25, 24])
        rows.append([85, -1,  5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 31])
        rows.append([84, -1,  6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 33, 32])
        rows.append([83, -1,  7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 34])
        rows.append([82, -1,  8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 35])
        rows.append([81, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 36])
        rows.append([80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 37])
        rows.append([79, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 52, -1, 38])
        rows.append([78, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 51, -1, 39])
        rows.append([76, 77, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 50, -1, 40])
        rows.append([75, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 49, -1, 41])
        rows.append([68, 69, 70, 71, 72, 73, 74, -1, -1, -1, -1, -1, -1, 48, -1, 42])
        rows.append([67, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 55, -1, 47, -1, 43])
        rows.append([66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 54, 53, 46, 45, 44])

        # Need something for mapping
        board_mapping = list()

        col = 0
        start_seen = 0
        home_seen = 0
        red_slide_seen = 0
        yellow_slide_seen = 0
        blue_slide_seen = 0
        green_slide_seen = 0

        for row in rows:
            row_num = 0
            for i in row:
                if i != -1:
                    if self.board[i].get_type() == reserved_type.HOME or\
                            self.board[i].get_type() == reserved_type.START:

                        center_x = (SQUARE_SIZE * col) + (SQUARE_SIZE // 2)
                        center_y = (SQUARE_SIZE * row_num) + (SQUARE_SIZE // 2)
                        circ = (center_y, center_x)
                        space = pygame.Rect((row_num * SQUARE_SIZE), (col * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE)
                        board_mapping.append((i, space))

                        # Green
                        if (home_seen == 1 and self.board[i].get_type() == reserved_type.HOME) or (
                                start_seen == 0 and self.board[i].get_type() == reserved_type.START):

                            pygame.draw.rect(win, BLACK, space)
                            pygame.draw.circle(win, GREEN, circ, SQUARE_SIZE // 2)

                        # Red
                        elif (home_seen == 0 and self.board[i].get_type() == reserved_type.HOME) or (
                                start_seen == 1 and self.board[i].get_type() == reserved_type.START):

                            pygame.draw.rect(win, BLACK, space)
                            pygame.draw.circle(win, RED, circ, SQUARE_SIZE // 2)
                        # Blue
                        elif (home_seen == 2 and self.board[i].get_type() == reserved_type.HOME) or (
                                start_seen == 3 and self.board[i].get_type() == reserved_type.START):

                            pygame.draw.rect(win, BLACK, space)
                            pygame.draw.circle(win, BLUE, circ, SQUARE_SIZE // 2)
                        # Yellow
                        elif (home_seen == 3 and self.board[i].get_type() == reserved_type.HOME) or (
                                start_seen == 2 and self.board[i].get_type() == reserved_type.START):

                            pygame.draw.rect(win, BLACK, space)
                            pygame.draw.circle(win, YELLOW, circ, SQUARE_SIZE // 2)

                        if self.board[i].get_type() == reserved_type.HOME:
                            home_seen += 1
                        else:
                            start_seen += 1

                    elif self.board[i].get_type() == reserved_type.NONE:
                        rect = pygame.Rect((row_num * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        pygame.draw.rect(win, BLACK, rect)
                        board_mapping.append((i, rect))
                        pygame.draw.rect(win, WHITE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                      SQUARE_SIZE - 2, SQUARE_SIZE - 2))

                    elif self.board[i].get_type() == reserved_type.RED_SAFETY:
                        rect = pygame.Rect((row_num * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        pygame.draw.rect(win, BLACK, rect)
                        board_mapping.append((i, rect))
                        pygame.draw.rect(win, RED, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                    SQUARE_SIZE - 2, SQUARE_SIZE - 2))

                    elif self.board[i].get_type() == reserved_type.RED_SLIDE:
                        rect = pygame.Rect((row_num * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        pygame.draw.rect(win, BLACK, rect)
                        board_mapping.append((i, rect))
                        pygame.draw.rect(win, WHITE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                      SQUARE_SIZE - 2, SQUARE_SIZE - 2))

                        # Start of the slide
                        if red_slide_seen == 0 or red_slide_seen == 4:
                            pygame.draw.rect(win, RED, ((row_num * SQUARE_SIZE) + 8, (col * SQUARE_SIZE) + 1,
                                                        SQUARE_SIZE - 16, SQUARE_SIZE - 2))

                            pygame.draw.polygon(win, BLACK, [[(row_num * SQUARE_SIZE), (col * SQUARE_SIZE)],
                                                             [(row_num * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                                                             ((col + .75) * SQUARE_SIZE)],
                                                             [(row_num + 1) * SQUARE_SIZE, col * SQUARE_SIZE]])
                            pygame.draw.polygon(win, RED, [[(row_num * SQUARE_SIZE) + 4, (col * SQUARE_SIZE) + 1],
                                                           [(row_num * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                                                            ((col + .75) * SQUARE_SIZE) - 4],
                                                           [((row_num + 1) * SQUARE_SIZE) - 4,
                                                            (col * SQUARE_SIZE) + 1]])

                        # End of the slide
                        elif red_slide_seen == 3 or red_slide_seen == 8:
                            pygame.draw.rect(win, RED, ((row_num * SQUARE_SIZE) + 8, (col * SQUARE_SIZE) + 1,
                                                        SQUARE_SIZE - 16, SQUARE_SIZE // 2))

                            center_y = (SQUARE_SIZE * col) + (SQUARE_SIZE // 2)
                            center_x = (SQUARE_SIZE * row_num) + (SQUARE_SIZE // 2)
                            pygame.draw.circle(win, BLACK, (center_x, center_y), (SQUARE_SIZE // 3) + 2)
                            pygame.draw.circle(win, RED, (center_x, center_y), SQUARE_SIZE // 3)

                        else:
                            pygame.draw.rect(win, RED, ((row_num * SQUARE_SIZE) + 8, (col * SQUARE_SIZE) + 1,
                                                        SQUARE_SIZE - 16, SQUARE_SIZE - 2))
                        red_slide_seen += 1

                    elif self.board[i].get_type() == reserved_type.BLUE_SAFETY:
                        rect = pygame.Rect((row_num * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        pygame.draw.rect(win, BLACK, rect)
                        pygame.draw.rect(win, BLUE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                     SQUARE_SIZE - 2, SQUARE_SIZE - 2))
                        board_mapping.append((i, rect))

                    elif self.board[i].get_type() == reserved_type.BLUE_SLIDE:
                        rect = pygame.Rect((row_num * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        pygame.draw.rect(win, BLACK, rect)
                        board_mapping.append((i, rect))

                        # Start of the slide
                        if blue_slide_seen == 4 or blue_slide_seen == 8:
                            pygame.draw.rect(win, WHITE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                          SQUARE_SIZE - 2, SQUARE_SIZE - 2))

                            pygame.draw.rect(win, BLUE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 8,
                                                         SQUARE_SIZE - 2, SQUARE_SIZE - 16))

                            pygame.draw.polygon(win, BLACK, [[((row_num + 1) * SQUARE_SIZE), ((col + 1) * SQUARE_SIZE)],
                                                             [(row_num + .25) * SQUARE_SIZE,
                                                              ((col * SQUARE_SIZE) + (SQUARE_SIZE // 2))],
                                                             [(row_num + 1) * SQUARE_SIZE, col * SQUARE_SIZE]])

                            pygame.draw.polygon(win, BLUE, [[((row_num + 1) * SQUARE_SIZE) - 2,
                                                             ((col + 1) * SQUARE_SIZE) - 4],
                                                            [(row_num + .25) * SQUARE_SIZE + 4,
                                                             ((col * SQUARE_SIZE) + (SQUARE_SIZE // 2))],
                                                            [(row_num + 1) * SQUARE_SIZE - 2, col * SQUARE_SIZE + 4]])

                        # End of the slide
                        elif blue_slide_seen == 0 or blue_slide_seen == 5:
                            pygame.draw.rect(win, WHITE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                          SQUARE_SIZE - 2, SQUARE_SIZE - 2))
                            pygame.draw.rect(win, BLUE, ((row_num * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                                                         (col * SQUARE_SIZE) + 8, SQUARE_SIZE // 2, SQUARE_SIZE - 16))

                            center_y = (SQUARE_SIZE * col) + (SQUARE_SIZE // 2)
                            center_x = (SQUARE_SIZE * row_num) + (SQUARE_SIZE // 2)
                            pygame.draw.circle(win, BLACK, (center_x, center_y), (SQUARE_SIZE // 3) + 2)
                            pygame.draw.circle(win, BLUE, (center_x, center_y), SQUARE_SIZE // 3)

                        else:
                            pygame.draw.rect(win, WHITE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                          SQUARE_SIZE - 2, SQUARE_SIZE - 2))

                            pygame.draw.rect(win, BLUE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 8,
                                                         SQUARE_SIZE - 2, SQUARE_SIZE - 16))
                        blue_slide_seen += 1

                    elif self.board[i].get_type() == reserved_type.YELLOW_SAFETY:
                        rect = pygame.Rect((row_num * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        pygame.draw.rect(win, BLACK, rect)
                        pygame.draw.rect(win, YELLOW, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                       SQUARE_SIZE - 2, SQUARE_SIZE - 2))
                        board_mapping.append((i, rect))

                    elif self.board[i].get_type() == reserved_type.YELLOW_SLIDE:
                        rect = pygame.Rect((row_num * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        pygame.draw.rect(win, BLACK, rect)
                        board_mapping.append((i, rect))

                        # Start of the slide
                        if yellow_slide_seen == 4 or yellow_slide_seen == 8:
                            pygame.draw.rect(win, WHITE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                          SQUARE_SIZE - 2, SQUARE_SIZE - 2))

                            pygame.draw.rect(win, YELLOW, ((row_num * SQUARE_SIZE) + 8, (col * SQUARE_SIZE) + 1,
                                                           SQUARE_SIZE - 16, SQUARE_SIZE - 2))

                            pygame.draw.polygon(win, BLACK, [[(row_num * SQUARE_SIZE), ((col + 1) * SQUARE_SIZE)],
                                                             [(row_num * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                                                              ((col + .25) * SQUARE_SIZE)],
                                                             [(row_num + 1) * SQUARE_SIZE, (col + 1) * SQUARE_SIZE]])
                            pygame.draw.polygon(win, YELLOW, [[(row_num * SQUARE_SIZE) + 2,
                                                               ((col + 1) * SQUARE_SIZE) + 1],
                                                              [(row_num * SQUARE_SIZE) + (SQUARE_SIZE // 2),
                                                               ((col + .25) * SQUARE_SIZE) + 4],
                                                              [((row_num + 1) * SQUARE_SIZE) - 2,
                                                               ((col + 1) * SQUARE_SIZE) + 1]])

                        # End of the slide
                        elif yellow_slide_seen == 0 or yellow_slide_seen == 5:
                            pygame.draw.rect(win, WHITE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                          SQUARE_SIZE - 2, SQUARE_SIZE - 2))
                            pygame.draw.rect(win, YELLOW, ((row_num * SQUARE_SIZE) + 8,
                                                           (col * SQUARE_SIZE) + (SQUARE_SIZE // 2) - 1,
                                                           SQUARE_SIZE - 16, SQUARE_SIZE // 2))

                            center_y = (SQUARE_SIZE * col) + (SQUARE_SIZE // 2)
                            center_x = (SQUARE_SIZE * row_num) + (SQUARE_SIZE // 2)
                            pygame.draw.circle(win, BLACK, (center_x, center_y), (SQUARE_SIZE // 3) + 2)
                            pygame.draw.circle(win, YELLOW, (center_x, center_y), SQUARE_SIZE // 3)

                        else:
                            pygame.draw.rect(win, WHITE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                          SQUARE_SIZE - 2, SQUARE_SIZE - 2))

                            pygame.draw.rect(win, YELLOW, ((row_num * SQUARE_SIZE) + 8, (col * SQUARE_SIZE) + 1,
                                                           SQUARE_SIZE - 16, SQUARE_SIZE - 2))
                        yellow_slide_seen += 1

                    elif self.board[i].get_type() == reserved_type.GREEN_SAFETY:

                        rect = pygame.Rect((row_num * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        pygame.draw.rect(win, BLACK, rect)
                        pygame.draw.rect(win, GREEN, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                      SQUARE_SIZE - 2, SQUARE_SIZE - 2))
                        board_mapping.append((i, rect))

                    elif self.board[i].get_type() == reserved_type.GREEN_SLIDE:
                        rect = pygame.Rect((row_num * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        pygame.draw.rect(win, BLACK, rect)
                        board_mapping.append((i, rect))

                        # Start of the slide
                        if green_slide_seen == 0 or green_slide_seen == 4:
                            pygame.draw.rect(win, WHITE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                          SQUARE_SIZE - 2, SQUARE_SIZE - 2))

                            pygame.draw.rect(win, GREEN, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 8,
                                                          SQUARE_SIZE - 2, SQUARE_SIZE - 16))

                            pygame.draw.polygon(win, BLACK, [[(row_num * SQUARE_SIZE), (col * SQUARE_SIZE)],
                                                             [(row_num + .75) * SQUARE_SIZE,
                                                              (col + (SQUARE_SIZE // 2))],
                                                             [row_num * SQUARE_SIZE, (col + 1) * SQUARE_SIZE]])

                            pygame.draw.polygon(win, GREEN, [[(row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 2],
                                                             [((row_num + .75) * SQUARE_SIZE) - 5,
                                                              (col + (SQUARE_SIZE // 2))],
                                                             [(row_num * SQUARE_SIZE) + 1,
                                                              ((col + 1) * SQUARE_SIZE) - 2]])

                        # End of the slide
                        elif green_slide_seen == 3 or green_slide_seen == 8:
                            pygame.draw.rect(win, WHITE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                          SQUARE_SIZE - 2, SQUARE_SIZE - 2))
                            pygame.draw.rect(win, GREEN, ((row_num * SQUARE_SIZE) + 1,
                                                          (col * SQUARE_SIZE) + 8,
                                                          SQUARE_SIZE // 2, SQUARE_SIZE - 16))

                            center_y = (SQUARE_SIZE * col) + (SQUARE_SIZE // 2)
                            center_x = (SQUARE_SIZE * row_num) + (SQUARE_SIZE // 2)
                            pygame.draw.circle(win, BLACK, (center_x, center_y), (SQUARE_SIZE // 3) + 2)
                            pygame.draw.circle(win, GREEN, (center_x, center_y), SQUARE_SIZE // 3)

                        else:
                            pygame.draw.rect(win, WHITE, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 1,
                                                          SQUARE_SIZE - 2, SQUARE_SIZE - 2))

                            pygame.draw.rect(win, GREEN, ((row_num * SQUARE_SIZE) + 1, (col * SQUARE_SIZE) + 8,
                                                          SQUARE_SIZE - 2, SQUARE_SIZE - 16))
                        green_slide_seen += 1

                # Must be background color, shows absence of a space.
                else:
                    pygame.draw.rect(win, (192, 192, 192),
                                     (row_num * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                row_num += 1
            col += 1

        self.order_mapping(board_mapping)

        # Draw pieces on the board.
        for color in self.positions:
            positions = self.positions[color]
            for item in positions:
                self.draw_piece(win, color, self.mapping[item])

    def order_mapping(self, mapping):
        '''
        Takes the board mapping, and puts it in order of spaces.
        :param mapping: A list of (space: int, location on board: rect)
        :return: Nothing, but sets self.mapping
        '''
        ordered_list = list()
        index = 0
        while len(ordered_list) != len(self.board):
            for item in mapping:
                i, rect = item
                if i == index:
                    ordered_list.append(rect)
            index += 1

        self.mapping = ordered_list


    def highlight_spaces(self, spaces):
        '''
        Highlights the end points of possible moves for user
        :param spaces: List of possible moves
        :return: Nothing, just highlights the spaces
        '''
        # Put it on all the end positions
        if spaces != None and spaces != [None]:
            for space in spaces:
                end_pos = space[2]

                rect = self.mapping[end_pos]

                # Transparentish square for highlighting end positions
                shape_surf = pygame.Surface(rect.size, pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, (0, 0, 0, 100), shape_surf.get_rect())
                self.window.blit(shape_surf, rect)
        pygame.display.update()

    def select_position(self, pos):
        mapping = self.mapping
        x, y = pos
        index = 0
        found_position = False
        for item in mapping:
            left_x = item[0]
            left_y = item[1]
            if (x > left_x and x < left_x + 40) and (y > left_y and y < left_y + 40):
                found_position = True

            else:
                if not found_position:
                    index += 1

        return index

    def draw_piece(self, win, color, square):
        '''
        Draws the piece of a color on the board
        :param win: Window
        :param color: Color of piece
        :param square: Space that it is on
        :return: Nothing
        '''
        if color == 'Blue':
            rgb_color = (0, 102, 204)
        elif color == 'Red':
            rgb_color = (255, 102, 102)
        elif color == 'Green':
            rgb_color = (178, 255, 102)
        else:
            rgb_color = (255, 215, 0)

        x = square[0]
        y = square[1]
        x_length = square[2]
        y_length = square[3]

        center_x = x + (x_length // 2)
        center_y = y + (y_length // 2)

        # Piece labels
        # Find the item in the list so that we can get the square index
        index = 0
        found = False
        for space in self.mapping:
            if space == square:
                found = True
            else:
                if not found:
                    index += 1

        # Get all positions for the color
        positions = self.get_position(color)


        # Figure out which piece it is
        piece = 1
        found_piece = False
        for i in positions:
            if index == i:
                found_piece = True
            else:
                if not found_piece:
                    piece += 1

        pygame.draw.circle(win, (255, 255, 255), (center_x, center_y), (x_length // 2.5) + 3)
        pygame.draw.circle(win, rgb_color, (center_x, center_y), x_length // 2.5)

        # label piece
        font = pygame.font.SysFont('arial', 20)
        win.blit(font.render(str(piece), True, (0,0,0)), (center_x - 5, y + 8))
