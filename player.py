from board import *
import pygame
import random

#class move_error(Exception): pass

class Player:

    def __init__(self, color, board):
        self.color = color
        self.board = board

        # slides has the start and end index for a slide
        if color == "Green":
            self.safety_start = 3
            self.home = 8
            self.start = 11
            self.slides = [[23, 32], [38, 42], [45, 54], [60, 64], [67, 76], [82, 86]]
        elif color == "Red":
            self.safety_start = 25
            self.home = 30
            self.start = 33
            self.slides = [[1,10], [16,20], [45, 54], [60, 64], [67, 76], [82, 86]]
        elif color == "Blue":
            self.safety_start = 47
            self.home = 52
            self.start = 55
            self.slides = [[1,10], [16,20], [23, 32], [38, 42], [67, 76], [82, 86]]
        else:
            # yellow
            self.safety_start = 69
            self.home = 74
            self.start = 77
            self.slides = [[1,10], [16,20], [23, 32], [38, 42], [45, 54], [60, 64]]



    # Start with getters and setters

    def get_color(self):
        return self.color

    def get_board(self):
        return self.board

    def set_color(self, color):
        self.color = color

    def set_board(self, board):
        self.board = board

    # Class functional methods
    def select_piece(self):
        valid_piece = False
        position_board = -1
        while not valid_piece:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    position_board = self.board.select_position(pos)
                    if position_board in self.board.get_position(self.color) and position_board != self.home:
                        valid_piece = True
                    else:
                        if position_board == self.home:
                            print('Cant move peices out of home')
                        else:
                            print('Not a piece')
        return position_board


    def select_move(self, moves):
        '''
        Selects the move from click
        :param moves: the possible moves for the selected piece
        :return: the chosen move
        '''
        # Find the mapping for each move
        end_positions = []
        for item in moves:
            if not item[2] in end_positions:
                end_positions.append(item[2])

        mapping_list = []
        for space in end_positions:
            mapping_list.append(self.board.mapping[space])

        # Loop through and look for click of space
        valid_space = False
        position_board = -1
        while not valid_space:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    position_board = self.board.select_position(pos)
                    if position_board in end_positions:
                        valid_space = True
                    else:
                        print('Not a valid move')

        # Find the move of that piece
        for item in moves:
            if item[2] == position_board:
                return item

    def make_turn(self, card):
        card = card.value.value
        moves = list()

        # for sevens
        count = 0
        if card == "Sorry!":
            card = 13

        if card == 1:
            potential_moves = self.get_all_moves_forwards(1)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 2:
            potential_moves = self.get_all_moves_forwards(2)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 3:
            potential_moves = self.get_all_moves_forwards(3)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 4:
            potential_moves = self.get_all_moves_backwards(4)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 5:
            potential_moves = self.get_all_moves_forwards(5)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 7:

            # saved board
            # check that permutations can both work
            # also check if just 7 works

            # logic here is that is the roll is a seven, then you can either move forwards one
            # piece seven spaces, or split up the seven between two pieces, BUT you need to be able
            # to use both of the split numbers
            # so, only when there are moves using the first number from the split, and there will
            # still be moves available using the second number, is it a valid split


            moves = []
            # Check if there is more than 1 piece available
            count = 0
            not_in_start = []
            positions = self.board.get_position(self.color)
            for i in positions:
                if i != self.start and i != self.home:
                    not_in_start.append(i)
                    count += 1

            if count > 1:
                permutations = [[6, 1], [5, 2], [4, 3], [3, 4], [2, 5], [1, 6]]
                move = len(moves)

                for i in range(len(not_in_start)):
                    # do for all pieces not in start
                    for j in range(len(permutations)):
                        split = permutations[j]
                        moves.extend(self.get_valid_moves(split[0], split[1]))
                        #print(moves)

                """           
                while move < 1:
                    perm = random.randint(0, (len(permutations) - 1))
                    split = permutations[perm]
                    moves.extend(self.get_valid_moves(split[0], split[1]))
                    move = len(moves)
                """

            elif count == 1:
                moves.extend(self.get_all_moves_forwards(7))
            else:
                # No pieces to move
                moves.extend([None])

        elif card == 8:
            potential_moves = self.get_all_moves_forwards(8)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 10:
            potential_moves = self.get_all_moves_forwards(10)
            if potential_moves is not None:
                moves.extend(potential_moves)

            potential_moves = self.get_all_moves_backwards(1)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 11:
            potential_moves = self.get_all_moves_forwards(11)
            if potential_moves is not None:
                moves.extend(potential_moves)

            potential_moves = self.get_all_moves_swap(11)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 12:
            potential_moves = self.get_all_moves_forwards(12)
            if potential_moves is not None:
                moves.extend(potential_moves)
        else:
            potential_moves = self.get_all_moves_sorry(13)
            if potential_moves is not None:
                moves.extend(potential_moves)
            potential_moves = self.get_all_moves_forwards(4)
            if potential_moves is not None:
                moves.extend(potential_moves)

        # if moves is empty, no valid moves for user
        # is moves is nonempty, get input that must match a move from the list

        if card != 7 or count == 1:
            print("Your available moves are listed below in the format [card, start_position, end_position].")
            #print("Card: " + str(card))
            print(moves)

            # Narrows down the pieces for the card
            moves_piece = []
            if len(moves) != 0:
                if card != 7 and  moves != [None]:
                    piece_position = self.select_piece()
                    if [self.home, self.home, self.home, self.home] == self.board.get_position(self.color):
                        invalid_piece = True
                    else:
                        invalid_piece = False
                    while not invalid_piece:
                        moves_piece.clear()
                        for item in moves:
                            if piece_position == item[1]:
                                moves_piece.append(item)
                        if len(moves_piece) < 1:
                            print("No moves for this piece, please select another")
                            piece_position = self.select_piece()
                        else:
                            invalid_piece = True
                    # Highlight the end spaces on board.
                    self.board.highlight_spaces(moves_piece)

                    # Have user select square and parse the move
                    move_picked = self.select_move(moves_piece)
                    print('You picked: ' + str(move_picked))
                    self.parse_move(move_picked)
                    return move_picked

                elif card == 7:
                    moves_piece = []
                    num_pieces_board = 0
                    for position in self.board.get_position(self.color):
                        if position != self.start and position != self.home:
                            num_pieces_board += 1

                    # Only moves one piece
                    if num_pieces_board == 1:
                        piece_position = self.select_piece()
                        invalid_piece = False
                        while not invalid_piece:
                            moves_piece.clear()
                            for item in moves:
                                if piece_position == item[1]:
                                    moves_piece.append(item)
                            if len(moves_piece) < 1:
                                print("No moves for this piece, please select another")
                                piece_position = self.select_piece()
                            else:
                                invalid_piece = True

                        # Highlight the end spaces on board.
                        self.board.highlight_spaces(moves_piece)

                        # Single piece moves seven spaces.
                        move_picked = self.select_move(moves_piece)
                        print('You picked: ' + str(move_picked))
                        self.parse_move(move_picked)
                        return move_picked

        elif card == 7 and len(moves) != 0 and moves != [None]:
            # Handle split 7
            valid_moves = False
            moves_making = []
            while not valid_moves:
                moves_making.clear()
                # Select one piece
                piece_position = self.select_piece()

                moves_piece = []
                this_moves = []
                # Get all available moves for moving (1-7)
                this_moves = self.get_all_moves_forwards(1)
                this_moves.extend(self.get_all_moves_forwards(2))
                this_moves.extend(self.get_all_moves_forwards(3))
                this_moves.extend(self.get_all_moves_forwards(4))
                this_moves.extend(self.get_all_moves_forwards(5))
                this_moves.extend(self.get_all_moves_forwards(6))
                this_moves.extend(self.get_all_moves_forwards(7))

                # Narrow down the possibilities for the piece
                for move in this_moves:
                    if move[1] == piece_position:
                        moves_piece.append(move)

                # Have them choose a move
                self.board.highlight_spaces(moves_piece)

                move_picked1 = self.select_move(moves_piece)
                print('You picked: ' + str(move_picked1))

                num_spaces = move_picked1[0]
                if num_spaces == 7:
                    valid_moves = True
                    moves_making.append(move_picked1)

                # If not full 7, make sure that at least one other piece
                # can be moved the remainder.
                this_moves.clear()
                this_moves = self.get_all_moves_forwards(7 - num_spaces)

                if len(this_moves) != 0 and this_moves != [None]:
                    # Select a second piece
                    piece_position = self.select_piece()
                    invalid_piece = False

                    # Clear from the first selection
                    moves_piece.clear()
                    while not invalid_piece:
                        moves_piece.clear()
                        for item in this_moves:
                            if piece_position == item[1]:
                                moves_piece.append(item)
                        if len(moves_piece) < 1:
                            print("No moves for this piece, please select another")
                            piece_position = self.select_piece()
                        else:
                            invalid_piece = True

                    # Have them choose a move
                    self.board.highlight_spaces(moves_piece)

                    move_picked2 = self.select_move(moves_piece)
                    print('You picked: ' + str(move_picked2))

                    # If both are valid moves, then parse them.
                    valid_moves = True
                    moves_making.append(move_picked1)
                    moves_making.append(move_picked2)


            for item in moves_making:
                self.parse_move(item)

            return moves_making
        else:
            print('No moves available')



    def make_turn_computer(self, c):
        '''
        Draws card for computer, calculates all possible moves for the card drawn.
        Picks a move at random and acts on it.
        :return: board? nothing? (will fix)
        '''

        # Show user the card
        card = c.value.value
        moves = list()
        print("The Computer drew a " + str(card) + ' card.')
        if card == 1:
            potential_moves = self.get_all_moves_forwards(1)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 2:
            potential_moves = self.get_all_moves_forwards(2)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 3:
            potential_moves = self.get_all_moves_forwards(3)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 4:
            potential_moves = self.get_all_moves_backwards(4)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 5:
            potential_moves = self.get_all_moves_forwards(5)
            if potential_moves is not None:
                moves.extend(potential_moves)

        elif card == 7:
            # Check if there is more than 1 piece available
            count = 0
            not_in_start = []
            positions = self.board.get_position(self.color)
            for i in positions:
                if i != self.start and i != self.home:
                    not_in_start.append(i)
                    count += 1

            if count > 1:
                permutations = [[6, 1], [5, 2], [4, 3], [3, 4], [2, 5], [1, 6]]
                perm = random.randint(0, (len(permutations) - 1))
                split = permutations[perm]
                moves.extend(self.get_valid_moves(split[0], split[1]))
            elif count == 1:
                moves.extend(self.get_all_moves_forwards(7))
        elif card == 8:
            potential_moves = self.get_all_moves_forwards(8)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 10:
            potential_moves = self.get_all_moves_forwards(10)
            if potential_moves is not None:
                moves.extend(potential_moves)
            potential_moves = self.get_all_moves_backwards(1)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 11:
            potential_moves = self.get_all_moves_forwards(11)
            if potential_moves is not None:
                moves.extend(potential_moves)
            potential_moves = self.get_all_moves_swap(11)
            if potential_moves is not None:
                moves.extend(potential_moves)
        elif card == 12:
            potential_moves = self.get_all_moves_forwards(12)
            if potential_moves is not None:
                moves.extend(potential_moves)
        else:
            potential_moves = self.get_all_moves_sorry(13)
            if potential_moves is not None:
                moves.extend(potential_moves)
            potential_moves = self.get_all_moves_forwards(4)
            if potential_moves is not None:
                moves.extend(potential_moves)

        # Computer picks a random move
        if len(moves) > 0:
            choice = random.randint(0, (len(moves) - 1))
            print("Computer picked: " + str(moves[choice]))

            if len(moves) == 0:
                # No moves
                print("Computer has no valid moves")
            elif card == 7:
                l_moves = moves[choice]
                if len(l_moves) == 2:
                    self.parse_move(l_moves[0])
                    self.parse_move(l_moves[1])
                elif len(l_moves) == 3:
                    self.parse_move(l_moves)
            else:
                self.parse_move(moves[choice])
        else:
            # No valid moves
            print("Computer has no valid moves")


    def get_all_moves_forwards(self, card):
        '''
        Calculates all possible moves for the card
        :param card: The number on the card
        :return: List[all possible moves]
        '''
        positions = self.board.get_position(self.color)
        moveable = []
        for i in range(len(positions)):
            if positions[i] != self.home and positions[i] != self.start:
                if positions[i] not in moveable:
                    moveable.append(positions[i])

        all_moves = []
        # If card is a 1 or a 2, if theres no piece of theirs on the space after, they can move from start.
        if card == 1 or card == 2:
            occupied_by_color = False
            in_start = False
            for i in range(len(positions)):
                if positions[i] == self.start - 1:
                    occupied_by_color = True
                elif positions[i] == self.start:
                    in_start = True

            if not occupied_by_color:
                # card, start pos, end pos
                if in_start:
                    all_moves.append([card, self.start, (self.start - 1)])

        for i in range(len(moveable)):
            j = card
            pos = moveable[i]
            while j > 0:
                next = (pos + 1) % len(self.board.get_board())

                if self.board.get_board()[next].get_type() == reserved_type.NONE:
                    # If its a normal piece, move forwards normally
                    pos = next
                    j -= 1

                elif self.board.get_board()[next].get_type() == reserved_type.START:
                    # If its a start piece, skip it
                    pos = next

                elif self.board.get_board()[next].get_type() == reserved_type.RED_SAFETY:
                    # if its a safety piece not of your own color, skip it
                    # if its a safety piece matching your color, move forwards normally
                    if self.color == "Red":
                        pos = next
                        j -= 1
                    else:
                        pos = next

                elif self.board.get_board()[next].get_type() == reserved_type.YELLOW_SAFETY:
                    if self.color == "Yellow":
                        pos = next
                        j -= 1
                    else:
                        pos = next

                elif self.board.get_board()[next].get_type() == reserved_type.GREEN_SAFETY:
                    if self.color == "Green":
                        pos = next
                        j -= 1
                    else:
                        pos = next

                elif self.board.get_board()[next].get_type() == reserved_type.BLUE_SAFETY:
                    if self.color == "Blue":
                        pos = next
                        j -= 1
                    else:
                        pos = next

                elif self.board.get_board()[next].get_type() == reserved_type.HOME:
                    # if its a home piece, make sure your turn ends on this move, and it makes your own home
                    if next != self.home:
                        pos = next
                    elif j > 1:
                        # Place holder for move being bad (moving past home piece)
                        pos = -1
                        j = 0
                    else:
                        # When we land exactly on home :)
                        pos = next
                        j -= 1
                else:
                    # SLIDES
                    # Check that landed on the start of slide
                    start = False
                    end_pos = -1
                    for item in self.slides:
                        if item[0] == next:
                            start = True
                            end_pos = item[1]

                    if j == 1 and start:
                        if end_pos > 0:
                            pos = end_pos
                            j -= 1
                    else:
                        pos = next
                        j -= 1

            if pos != -1:
                # Check the spot isn't occupied by a piece of your own color
                if self.board.get_board()[pos].get_occupied() != occupied_type.NONE:
                    if self.board.get_board()[pos].get_occupied().value != self.color:
                        # card, start pos, end pos
                        all_moves.append([card, moveable[i], pos])

                else:
                    all_moves.append([card, moveable[i], pos])

        return all_moves


    def get_all_moves_backwards(self, card):
        positions = self.board.get_position(self.color)
        moveable = []
        pos_types = []
        for i in range(len(positions)):
            if positions[i] != self.home and positions[i] != self.start:
                if positions[i] not in moveable:
                    moveable.append(positions[i])
                    pos_types.append(self.board.get_board()[positions[i]].get_type())

        #print(moveable)

        all_moves = []

        if self.color == 'Green':
            our_res = reserved_type.GREEN_SAFETY
        elif self.color == 'Red':
            our_res = reserved_type.RED_SAFETY
        elif self.color == 'Blue':
            our_res = reserved_type.BLUE_SAFETY
        else:
            our_res = reserved_type.YELLOW_SAFETY

        for i in range(len(moveable)):

            j = card
            pos = moveable[i]
            while j > 0:

                # if its a normal piece, move forwards normally
                # if its a start piece, skip it
                # if its a safety piece not of your own color, skip it
                # if its a safety piece matching your color, move forwards normally
                # if its a home piece, make sure your turn ends on this move, and it makes your own home

                next = (pos-1)%len(self.board.get_board())

                #print(next)

                #print(self.board.get_board()[next].get_type())

                if self.board.get_board()[next].get_type() == reserved_type.NONE:
                    pos = next
                    j-=1

                elif self.board.get_board()[next].get_type() == reserved_type.START:
                    pos = next

                elif self.board.get_board()[next].get_type() == reserved_type.RED_SAFETY or \
                    self.board.get_board()[next].get_type() == reserved_type.YELLOW_SAFETY or \
                    self.board.get_board()[next].get_type() == reserved_type.GREEN_SAFETY or \
                    self.board.get_board()[next].get_type() == reserved_type.BLUE_SAFETY:

                    # Can only back up in a safety zone if it was in a safety zone.
                    # To prevent it from backing from right after start into the safety zone
                    if pos_types[i] == reserved_type.RED_SAFETY or pos_types[i] == reserved_type.YELLOW_SAFETY or \
                         pos_types[i] == reserved_type.GREEN_SAFETY or pos_types[i] == reserved_type.BLUE_SAFETY:
                        if self.board.get_board()[next].get_type() == our_res:
                            # If its a safety piece matching your color, move backwards normally
                            pos = next
                            j -= 1
                        else:
                            # If its a safety piece not of your own color, skip it
                            pos = next
                    else:
                        pos = next

                elif self.board.get_board()[next].get_type() == reserved_type.HOME:
                    pos = next
                else:
                    # SLIDES
                    # Check that landed on the start of slide
                    start = False
                    end_pos = -1
                    for item in self.slides:
                        if item[0] == next:
                            start = True
                            end_pos = item[1]

                    if j == 1 and start:
                        if end_pos > 0:
                            pos = end_pos
                            j -= 1
                    else:
                        pos = next
                        j -= 1

                #print(j)

            #print(pos)
            # pos is only -1 when we attempt to move past our home (not allowed)
            if pos != -1:
                # sure the spot isn't occupied by a piece of your own color
                if self.board.get_board()[pos].get_occupied() != occupied_type.NONE:
                    if self.board.get_board()[pos].get_occupied().value != self.color:
                        # card, start pos, end pos
                        all_moves.append([card, moveable[i], pos])

                    # If start pos == end pos, add it as an option.
                    # This case is only for dealign with backing up on slides
                    elif moveable[i] == pos:
                        all_moves.append([card, moveable[i], pos])

                else:
                    all_moves.append([card, moveable[i], pos])

        return all_moves

    def get_all_moves_swap(self, card):

        positions = self.board.get_position(self.color)
        moveable = []
        for i in range(len(positions)):
            if positions[i] != self.home and positions[i] != self.start:
                moveable.append(positions[i])

        all_moves = []
        for i in range(len(self.board.get_board())):
            if (self.board.get_board()[i].get_type() != reserved_type.RED_SAFETY and self.board.get_board()[i].get_type() != reserved_type.GREEN_SAFETY
                    and self.board.get_board()[i].get_type() != reserved_type.BLUE_SAFETY and self.board.get_board()[i].get_type() != reserved_type.YELLOW_SAFETY
                    and self.board.get_board()[i].get_type() != reserved_type.START and self.board.get_board()[i].get_type() != reserved_type.HOME):

                if self.board.get_board()[i].get_occupied() != occupied_type.NONE:
                    if self.board.get_board()[i].get_occupied().value != self.color:
                        for j in range(len(moveable)):
                            # card, start pos, end pos
                            all_moves.append([card, moveable[j], i])

        print(all_moves)
        return all_moves


    def get_all_moves_sorry(self, card):
        positions = self.board.get_position(self.color)
        moveable = []
        for i in range(len(positions)):
            if positions[i] != self.home:
                if positions[i] not in moveable:
                    moveable.append(positions[i])

        all_moves = []
        for i in range(len(self.board.get_board())):
            if (self.board.get_board()[i].get_type() != reserved_type.RED_SAFETY and self.board.get_board()[i].get_type() != reserved_type.GREEN_SAFETY
                    and self.board.get_board()[i].get_type() != reserved_type.BLUE_SAFETY and self.board.get_board()[i].get_type() != reserved_type.YELLOW_SAFETY
                    and self.board.get_board()[i].get_type() != reserved_type.START and self.board.get_board()[i].get_type() != reserved_type.HOME):

                if self.board.get_board()[i].get_occupied() != occupied_type.NONE:
                    if self.board.get_board()[i].get_occupied().value != self.color:
                        for j in range(len(moveable)):
                            # card, start pos, end pos
                            all_moves.append([card, moveable[j], i])


        return all_moves

    def get_valid_moves(self, first, second):
        '''
        Card 7 case, going to get possible moves for both numbers, and pair them together
        :param first: first number of spaces
        :param second: second number of spaces
        :return: a list of pairs of movements
        '''
        move1 = self.get_all_moves_forwards(first)
        move2 = self.get_all_moves_forwards(second)

        # Remove any that are moving pieces from start
        if [1, self.start, self.start - 1] in move1 or [2, self.start, self.start - 1] in move1:
            if first == 1:
                move1.remove([1, self.start, self.start - 1])
            elif first == 2:
                move1.remove([2, self.start, self.start - 1])

        if [1, self.start, self.start - 1] in move2 or [2, self.start, self.start - 1] in move2:
            if second == 1:
                move2.remove([1, self.start, self.start - 1])
            elif second == 2:
                move2.remove([2, self.start, self.start - 1])

        # Now make all the possible pairs
        pairs = []
        for item in move1:
            for i in move2:
                # Make sure its not moving the same piece
                if item[1] != i[1]:
                    pairs.append((item, i))

        return pairs


    def won(self):
        return self.board.won(self.color)

    def parse_move(self, move):
        '''
        Performs the move. Handles if occupied and slide. Changes the space enums
        :param move: The move selected by the computer
        :return: Nothing
        '''

        def handle_slides(size_slide):
            # TODO: Slides are buggy
            # length of slide
            if size_slide == 9:
                i = 4
            else:
                i = 5

            slide_start = 0
            for ind in self.slides:
                if ind[1] == end:
                    slide_start = ind[0]
            if slide_start != 0:
                if start == end:
                    pos = slide_start
                else:
                    pos = start
            else:
                # Don't slide because its our color or not the start of the slide
                i = -1
                pos = -1

            while i > 0:
                next = (pos + 1) % len(self.board.get_board())

                # Skips over safe zones and starts
                if (self.board.get_board()[pos].get_type() != reserved_type.RED_SLIDE and
                        self.board.get_board()[
                            pos].get_type() != reserved_type.GREEN_SLIDE and
                        self.board.get_board()[pos].get_type() != reserved_type.BLUE_SLIDE and
                        self.board.get_board()[pos].get_type() != reserved_type.YELLOW_SLIDE):
                    pos = next

                else:
                    if self.board.get_board()[pos].get_occupied() != occupied_type.NONE:
                        print(self.board.get_board()[pos].get_occupied())

                        if self.board.get_board()[pos].get_occupied() == occupied_type.GREEN:
                            col = "Green"
                            start_op = 11
                        elif self.board.get_board()[pos].get_occupied() == occupied_type.RED:
                            col = "Red"
                            start_op = 33
                        elif self.board.get_board()[pos].get_occupied() == occupied_type.BLUE:
                            col = "Blue"
                            start_op = 55
                        else:
                            col = "Yellow"
                            start_op = 77

                        piece = 0
                        for id in range(len(self.board.get_position(col))):
                            if self.board.get_position(col)[id] == pos:
                                piece = id

                        if pos != start:
                            self.board.set_position(col, piece, start_op)
                            self.board.get_board()[pos].set_occupied(occupied_type.NONE)
                    pos = next
                    i -= 1

        if move is not None:
            card = move[0]
            start = move[1]
            end = move[2]

            do_nothing = False
            if start == end:
                do_nothing = True

                for i in self.slides:
                    if end == i[1]:
                        slide_size = i[1] - i[0]
                        handle_slides(slide_size)

            if not do_nothing:
                # If the spot is occupied by another color, sends them back to start.
                if self.board.get_board()[end].get_occupied() != occupied_type.NONE:
                    if self.board.get_board()[end].get_occupied() == occupied_type.GREEN:
                        col = "Green"
                        start_op = 11
                    elif self.board.get_board()[end].get_occupied() == occupied_type.RED:
                        col = "Red"
                        start_op = 33
                    elif self.board.get_board()[end].get_occupied() == occupied_type.BLUE:
                        col = "Blue"
                        start_op = 55
                    else:
                        col = "Yellow"
                        start_op = 77

                    # Move the other players piece back to start
                    piece = -1
                    for i in range(0, 4):
                        if self.board.get_position(col)[i] == end:
                            piece = i
                    self.board.set_position(col, piece, start_op)

                # if we encounter a slide, we must move our piece to the end of it and knock off any
                slide = False
                size_slide = 0
                for i in self.slides:
                    if card == 4 or card == 1:
                        if start > end:
                            if (start - card) == i[0]:
                                slide = True
                                size_slide = i[1] - i[0]
                        else:
                            if (start + card) == i[0]:
                                slide = True
                                size_slide = i[1] - i[0]
                    else:
                        if (start + card) == i[0]:
                            slide = True
                            size_slide = i[1] - i[0]

                if slide:
                    handle_slides(size_slide)

                # Everything else should default here
                piece = -1
                for i in range(0, 4):
                    if self.board.get_position(self.color)[i] == start:
                        piece = i
                self.board.set_position(self.color, piece, end)
                self.board.get_board()[start].set_occupied(occupied_type.NONE)

                if self.color == 'Green':
                    col = occupied_type.GREEN
                elif self.color == 'Red':
                    col = occupied_type.RED
                elif self.color == 'Blue':
                    col = occupied_type.BLUE
                else:
                    col = occupied_type.YELLOW

                if self.board.get_board()[end] != self.home:
                    self.board.get_board()[end].set_occupied(col)

                # If home gets occupied then it wont let others move into it.
                self.board.get_board()[self.home].set_occupied(occupied_type.NONE)
