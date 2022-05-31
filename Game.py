import pygame
from board import *
from Deck import *
from player import *
#from computer import *

FPS = 60
pygame.init()
WINDOW = pygame.display.set_mode((1000, 640))
pygame.display.set_caption('Sorry!')

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Setting up sounds
background_music = pygame.mixer.music.load('sounds/background.mp3')
win_sound = pygame.mixer.Sound('sounds/win.mp3')

# maintain a terminal window that holds the five most recent messages
terminal = ["", "", "", "", ""]

def Game(player, comp1, comp2, comp3, board, deck):
    turn = 0
    winner = False

    while winner == False:
        if turn % 4 == 0:
            pygame.display.update()
            board.draw_board(WINDOW)
            msg = 'Its your turn!'
            add_to_terminal(msg)
            print(msg)
            card = draw_card(deck)
            card.draw_back(WINDOW)
            card.draw(WINDOW)
            msg = 'You drew a ' + str(card.value.value) + ' card!'
            add_to_terminal(msg)
            print(msg)

            draw_side_panel(player)
            pygame.display.update()

            player.make_turn(card)
            turn += 1

            pygame.display.update()
            board.draw_board(WINDOW)
            draw_side_panel(comp1)

        elif turn % 4 == 1:
            msg = comp1.color + "'s Turn!"
            pygame.time.wait(200)
            add_to_terminal(msg)
            print(msg)

            card = draw_card(deck)
            card.draw_back(WINDOW)
            card.draw(WINDOW)

            msg = comp1.color + ' drew a ' + str(card.value.value) + ' card!'
            add_to_terminal(msg)
            print(msg)

            comp1.make_turn_computer(card)
            turn += 1
            pygame.display.update()
            board.draw_board(WINDOW)
            draw_side_panel(comp2)
            pygame.time.wait(600)

        elif turn % 4 == 2:

            msg = comp2.color + "'s Turn!"
            pygame.time.wait(200)
            add_to_terminal(msg)
            print(msg)

            card = draw_card(deck)
            card.draw_back(WINDOW)
            card.draw(WINDOW)

            msg = comp2.color + ' drew a ' + str(card.value.value) + ' card!'
            add_to_terminal(msg)
            print(msg)

            comp2.make_turn_computer(card)
            turn += 1
            pygame.display.update()
            board.draw_board(WINDOW)
            draw_side_panel(comp3)
            pygame.time.wait(600)

        elif turn % 4 == 3:

            msg = comp3.color + "'s Turn!"
            pygame.time.wait(200)
            add_to_terminal(msg)
            print(msg)

            card = draw_card(deck)
            card.draw_back(WINDOW)
            card.draw(WINDOW)

            msg = comp3.color + ' drew a ' + str(card.value.value) + ' card!'
            add_to_terminal(msg)
            print(msg)

            comp3.make_turn_computer(card)
            turn += 1
            pygame.display.update()
            board.draw_board(WINDOW)
            draw_side_panel(player)
            pygame.time.wait(600)

        play_flag = False
        # Check for winner
        if player.won():
            msg = player.color + ' Won'
            add_to_terminal(msg)
            print(msg)
            winner = True
            play_flag = draw_win(player)
        elif comp1.won():
            msg = comp1.color + ' Won'
            add_to_terminal(msg)
            print(msg)
            winner = True
            play_flag = draw_win(comp1)
        elif comp2.won():
            msg = comp2.color + ' Won'
            add_to_terminal(msg)
            print(msg)
            winner = True
            play_flag = draw_win(comp2)
        elif comp3.won():
            msg = comp3.color + ' Won'
            add_to_terminal(msg)
            print(msg)
            winner = True
            play_flag = draw_win(comp3)

    # Will have to call function looping for the Play again or quit buttons

    return play_flag


def draw_card(deck) -> Card:
    return deck.draw_card()


def draw_side_panel(user):

    # create the container for the side panel, and display the game's name
    panel_container = pygame.Rect(640, 0, 360, 640)
    panel_container_color = (10, 10, 10)
    pygame.draw.rect(WINDOW, panel_container_color, panel_container)

    title_font = pygame.font.SysFont('arial', 50)
    WINDOW.blit(title_font.render("Sorry!", True, (255,255,255)), (750, 25))

    # this next section covers the turn indicators
    turn_font = pygame.font.SysFont('arial', 20)
    WINDOW.blit(turn_font.render("Turn", True, (255,255,255)), (925, 100))

    turn_green = pygame.Rect(950, 130, 200, 20)
    green = (0, 255, 0)
    turn_red = pygame.Rect(950, 160, 200, 20)
    red = (255, 0, 0)
    turn_blue = pygame.Rect(950, 190, 200, 20)
    blue = (0, 0, 255)
    turn_yellow = pygame.Rect(950, 220, 200, 20)
    yellow = (255, 255, 0)

    if user.get_color() == "Green":
        turn_green = turn_green.move(-60, 0)
    elif user.get_color() == "Red":
        turn_red = turn_red.move(-60, 0)
    elif user.get_color() == "Blue":
        turn_blue = turn_blue.move(-60, 0)
    else:
        turn_yellow = turn_yellow.move(-60, 0)

    pygame.draw.rect(WINDOW, green, turn_green)
    pygame.draw.rect(WINDOW, red, turn_red)
    pygame.draw.rect(WINDOW, blue, turn_blue)
    pygame.draw.rect(WINDOW, yellow, turn_yellow)

    # terminal, which shows the five most recent messages
    terminal_container = pygame.Rect(650, 550, 340, 80)
    terminal_container_color = (150, 150, 150)
    pygame.draw.rect(WINDOW, terminal_container_color, terminal_container)

    terminal_font = pygame.font.SysFont('arial', 18)
    WINDOW.blit(terminal_font.render("Terminal:", True, (255,255,255)), (650, 530))

    msg_font = pygame.font.SysFont('arial', 12)
    WINDOW.blit(msg_font.render(terminal[4], True, (255,255,255)), (655, 555))
    WINDOW.blit(msg_font.render(terminal[3], True, (255,255,255)), (655, 570))
    WINDOW.blit(msg_font.render(terminal[2], True, (255,255,255)), (655, 585))
    WINDOW.blit(msg_font.render(terminal[1], True, (255,255,255)), (655, 600))
    WINDOW.blit(msg_font.render(terminal[0], True, (255,255,255)), (655, 615))

    # card rules displayed for the user
    card_title_font = pygame.font.SysFont('arial', 18)
    WINDOW.blit(card_title_font.render("Card Rules:", True, (255,255,255)), (650, 105))

    card_rules_font = pygame.font.SysFont('arial', 14)
    WINDOW.blit(card_rules_font.render("1: Move a piece forwards 1, or", True, (255,255,255)), (650, 130))
    WINDOW.blit(card_rules_font.render("move a piece out of start", True, (255,255,255)), (650, 150))
    WINDOW.blit(card_rules_font.render("2: Move a piece forwards 2, or", True, (255,255,255)), (650, 170))
    WINDOW.blit(card_rules_font.render("move a piece out of start", True, (255,255,255)), (650, 190))
    WINDOW.blit(card_rules_font.render("3: Move a piece forwards 3", True, (255,255,255)), (650, 210))
    WINDOW.blit(card_rules_font.render("4: Move a piece backwards 4", True, (255,255,255)), (650, 230))
    WINDOW.blit(card_rules_font.render("5: Move a piece forwards 5", True, (255,255,255)), (650, 250))
    WINDOW.blit(card_rules_font.render("7: Move a piece forwards 7, or split the 7 into", True, (255,255,255)), (650, 270))
    WINDOW.blit(card_rules_font.render("two whole numbers and move two different pieces", True, (255,255,255)), (650, 290))
    WINDOW.blit(card_rules_font.render("8: Move a piece forwards 8", True, (255,255,255)), (650, 310))
    WINDOW.blit(card_rules_font.render("10: Move a piece forwards 10, or backwards 1", True, (255,255,255)), (650, 330))
    WINDOW.blit(card_rules_font.render("11: Switch pawn positions with an opponent, or", True, (255,255,255)), (650, 350))
    WINDOW.blit(card_rules_font.render("move a piece forwards 11", True, (255,255,255)), (650, 370))
    WINDOW.blit(card_rules_font.render("12: Move a piece forwards 12", True, (255,255,255)), (650, 390))
    WINDOW.blit(card_rules_font.render("Sorry!: Move a piece from your start to take the", True, (255,255,255)), (650, 410))
    WINDOW.blit(card_rules_font.render("place of an opponents pawn, or move a piece", True, (255,255,255)), (650, 430))
    WINDOW.blit(card_rules_font.render("forwards 4", True, (255,255,255)), (650, 450))


def add_to_terminal(msg):
    # add new message
    terminal.insert(0, msg)
    # remove oldest
    terminal.pop(5)

def draw_win(winner):
    pygame.mixer.music.pause()
    pygame.mixer.Sound.play(win_sound)
    win_container = pygame.Rect(640, 0, 360, 640)
    win_container_color = (10, 10, 10)
    pygame.draw.rect(WINDOW, win_container_color, win_container)
    win_font = pygame.font.SysFont('arial', 50)
    if winner.color == 'Red':
        color = red
    elif winner.color == 'Blue':
        color = blue
    elif winner.color == 'Green':
        color = green
    else:
        color = yellow
    WINDOW.blit(win_font.render(winner.color + " has won!", True, color), (660, 25))
    new_game_button = pygame.Rect(650, 450, 340, 80)
    quit_game_button = pygame.Rect(650, 550, 340, 80)
    pygame.draw.rect(WINDOW, (150, 150, 150), new_game_button)
    pygame.draw.rect(WINDOW, (150, 150, 150), quit_game_button)
    button_font = pygame.font.SysFont('arial', 20)
    WINDOW.blit(button_font.render("New Game", True, (0, 0, 0)), (660, 460))
    WINDOW.blit(button_font.render("Exit Game", True, (0, 0, 0)), (660, 560))
    pygame.display.update()
    pygame.time.wait(3000)
    button_clicked = False
    while not button_clicked:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = event.pos
                if new_game_button.collidepoint(mouse):
                    button_clicked = True
                    pygame.mixer.music.unpause()
                    return True
                if quit_game_button.collidepoint(mouse):
                    button_clicked = True
                    return False

def main():
    run = True

    pygame.mixer.music.play(-1)
    while run:
        board = Board(WINDOW)
        deck = Deck()
        player = Player("Green", board)
        comp1 = Player("Red", board)
        comp2 = Player("Blue", board)
        comp3 = Player("Yellow", board)

        run = Game(player, comp1, comp2, comp3, board, deck)

        board.draw_board(WINDOW)
        draw_side_panel(player)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

main()
