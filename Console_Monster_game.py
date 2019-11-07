#Console Game by Shepherd Kutama
import sys
import random
class Main:

    max_width = 5
    max_height = 5
    character_alive = True
    character_won = False
    monster_awake = False
    monster_awakened = False
    monster_move_per_turn = 2



    def __init__(self):
        self.display_menu()
        self.reset_current_game()

    def reset_current_game(self):
        self.character_position = [0,0]
        self.monster_position = [1,0]
        self.trap_position = [0,1]
        self.flask_position = [1,1]

    def reset_all_settings(self):
        self.character_alive = True
        self.monster_awake = False
        self.character_won = False
        self.monster_awakened = False


    def place_character(self):
        self.character_position = [0,0]

    def place_monster(self):
        self.monster_position = [random.randint(0,self.max_width - 1), random.randint(0,self.max_height - 1)]
        if(self.coordinate_collisions('monster','player')):
            self.place_monster()
        elif(self.coordinate_collisions('monster','flask')):
            self.place_monster()
        elif(self.coordinate_collisions('monster','trap')):
            self.place_monster()
        else:
            return True
        return True

    def place_trap(self):
        self.trap_position = [random.randint(0,self.max_width - 1), random.randint(0,self.max_height - 1)]
        if (self.coordinate_collisions('trap', 'player')):
            self.place_trap()
        elif (self.coordinate_collisions('trap', 'flask')):
            self.place_trap()
        elif (self.coordinate_collisions('trap', 'monster')):
            self.place_trap()
        else:
            return True
        return True


    def place_flask(self):
        self.flask_position = [random.randint(0,self.max_width - 1), random.randint(0,self.max_height - 1)]
        if (self.coordinate_collisions('flask', 'player')):
            self.place_flask()
        elif (self.coordinate_collisions('flask', 'trap')):
            self.place_flask()
        elif (self.coordinate_collisions('flask', 'monster')):
            self.place_flask()
        else:
            return True
        return True

    def start_new_game(self):
        self.reset_all_settings()
        self.reset_current_game()
        self.setup_game()
        self.draw_grid()

    def setup_game(self):
        self.place_character()
        self.place_monster()
        self.place_trap()
        self.place_flask()

    def create_setup(self):
        self.reset_all_settings()
        print('This option lets you best the settings for Monster!')
        width_choice = input('How wide do you want the game board to be? (Default: 5): ')
        try:
            width_choice = int(width_choice)
        except ValueError:
            width_choice = 5
        self.max_width = width_choice

        height_choice = input('How high do you want the game board to be? (Default: 5): ')
        try:
            height_choice = int(height_choice)
        except ValueError:
            height_choice = 5
        self.max_height = height_choice

        height_choice = input('How high do you want the game board to be? (Default: 5): ')
        try:
            height_choice = int(height_choice)
        except ValueError:
            height_choice = 5
        self.max_width = height_choice

        monster_move_count_choice = input('How many moves should the monster get, (Default: 2): ')
        try:
            monster_move_count_choice = int(monster_move_count_choice)
        except ValueError:
            monster_move_count_choice = 2
        self.monster_move_per_turn = monster_move_count_choice
        self.setup_game()


    def display_menu(self):  # display menu method
        menu_list = ['Start New Game','[Save Game]', '[Load Game]', 'Customize Setup','Exit']
        print('Type th number of your Choice:')
        print()
        for i in range(1, len(menu_list) + 1):
            print(str(i) + ' ' + menu_list[i - 1])

        choice = input('Your Choice: ')
        self.menu_choice(choice)
        print()

    def coordinate_collisions(self,coord1,coord2):
        if(coord1 == 'monster'):
            first = self.monster_position
        elif(coord1 == 'flask'):
            first = self.flask_position
        elif(coord1 == 'trap'):
            first = self.trap_position
        elif(coord1 == 'player'):
            first = self.character_position
        else:
            return None

        if (coord2 == 'monster'):
            second = self.monster_position
        elif (coord2 == 'flask'):
            second = self.flask_position
        elif (coord2 == 'trap'):
            second = self.trap_position
        elif (coord2 == 'player'):
            second = self.character_position
        else:
            return None
        if(coord1 == coord2):
            return None

        if(first[0] == second[0] and first[1] == second[1]):
            return True
        else:
            return False

    def menu_choice(self, choice):
        try:
            choice = int(choice)

        except ValueError:
            choice = 0

        if(choice == 1):
            self.start_new_game()
        elif(choice == 2):
            pass
        elif(choice == 3):
            pass
        elif(choice == 4):
            self.create_setup()
        elif(choice == 5):
            sys.exit(0)
        else:
            print('That Wasn\'t a Valid Option, Try Again')
            self.display_menu()

    def collision_check(self):
        if(self.coordinate_collisions('player','monster')):
            self.character_alive = False
            return True
        elif(self.coordinate_collisions('player','flask')):
            self.character_won = True
            return True
        elif(self.coordinate_collisions('player','trap')):
            self.monster_awakened = True
            self.trap_position = [-1,-1]
            return True
        return True

    def check_boundary(self,new_x,new_y):
        min_width = 0
        min_height = 0
        if(new_x < min_width or new_x == self.max_width or new_y < min_height or new_y  == self.max_height):
            return False
        else:
            return True

    def player_move(self,choice):
        current_x = self.character_position[0]
        current_y = self.character_position[1]
        if(choice == 'W' or choice == 'w'):
            if(self.check_boundary(current_x, current_y - 1) == False):
                return True
            else:
                self.character_position = [current_x, current_y - 1]
                return True
        elif(choice == 'A' or choice == 'a'):
            if(self.check_boundary(current_x - 1, current_y) == False):
                return False
            else:
                self.character_position = [current_x - 1, current_y]
                return True
        elif (choice == 'S' or choice == 's'):
            if (self.check_boundary(current_x , current_y + 1) == False):
                return False
            else:
                self.character_position = [current_x, current_y + 1]
                return True
        elif (choice == 'D' or choice == 'd'):
            if (self.check_boundary(current_x + 1, current_y) == False):
                return False
            else:
                self.character_position = [current_x + 1, current_y]
                return True
        else:
            return False

    def move_monster(self):
        moves_left = self.monster_move_per_turn
        while(moves_left > 0):
            mon_x = self.monster_position[0]
            mon_y = self.monster_position[1]
            player_x = self.character_position[0]
            player_y = self.character_position[0]

            if(player_x - mon_x != 0):
                if(player_x - mon_x < 0):
                    self.monster_position = [mon_x - 1, mon_y]
                else:
                    self.monster_position = [mon_x + 1, mon_y]
            else:
                if(player_y - mon_y < 0):
                    self.monster_position = [mon_x, mon_y - 1]
                else:
                    self.monster_position = [mon_x, mon_y + 1]
            moves_left = moves_left - 1



    def draw_grid(self):
        if(self.character_won == True):
            print('You have beaten Monster! Congratulations')
            choice = input('Press any key to return the menu or press enter to exit')
            if(choice):
                self.display_menu()
        elif(self.character_alive == False):
            print('You have been eaten by an Monster')
            choice = input('Press any key to return to the menu or press enter to exit')
            if(choice):
                self.display_menu()

        else:
            height = self.max_height
            width = self.max_width

            for y in range(0,height):
                for x in range(0,width):
                    y = str(y)
                    x = str(x)
                    char_x = str(self.character_position[0])
                    char_y = str(self.character_position[1])
                    if(str(self.monster_position[0]) == x and str(self.monster_position[1]) == y and self.monster_awake == True):
                        sys.stdout.write('M')
                    #elif(str(self.trap_position[0]) == x and str(self.trap_position[1]) == y):  # If you want o see the monster
                    #    sys.stdout.write('T')
                    #elif (str(self.flask_position[0]) == x and str(self.flask_position[1]) == y):
                    #    sys.stdout.write('F')
                    elif(char_x == x and char_y == y):
                        sys.stdout.write('X')
                    else:
                        sys.stdout.write('?')
                sys.stdout.write('\r\n')
            print()
            print('Move using WASD')
            choice = input('Move: ')
            if(self.player_move(choice) == False):
                print('Not a valid move')
                self.draw_grid()
            else:
                if(self.monster_awake == True):
                    self.move_monster()
                if(self.collision_check() == True):
                    if(self.monster_awakened == True):
                        self.monster_awake = True
                        print('You Awake the monster')
                        self.monster_awakened = False
                self.draw_grid()

monster = Main()

