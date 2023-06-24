# player  = {'name' : 'Robin', 'attack' : 20, 'heal' : 40, 'health' : 100}
# monster = {'name' : 'Max', 'attack' : 15, 'health' : 100}
from random import randint
from ast import Str
from re import A, M
from tkinter import E

game_running = True
final_game_results = []


def calculate_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)

def game_ends(winner):
    print(f" {winner}, won the game")


while game_running == True:
    round_counter = 0
    new_round = True
    player  = {'name' : 'Robin', 'attack' : 20, 'heal' : 40, 'health' : 100}
    monster = {'name' : 'Max', 'attack_min' : 15, 'attack_max' : 25, 'health' : 100}

    print('*********||||||G||A||M||E|||||||**************')
    print('Enter a player name to start the Game!')
    player['name'] = input()

    print(player['name'] + ' has ' + str(player['health']) + ' health ')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health ')
 
    while new_round == True:
        round_counter = round_counter + 1
        
        player_won = False
        monster_won = False

        print('*****|||||GAME||||******||||STARTS|||******')
        print('Please select action:')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('4) Game Results')

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
            if player['health'] <= 0:
                monster_won = True
        
        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
        if player['health'] <= 0:
                monster_won = True

        elif player_choice == '3':
            new_round = False
            game_running = False

        elif player_choice == '4':
            for result_grid in final_game_results:
                print(result_grid)

        else:
            print('Sorry!, you entered invalid input.')

        if player_won == False and monster_won == False:

            print(player['name'] + ', The Player has ' + str(player['health']) + ' left ' )
            print(monster['name'] + ', The Monster has ' + str(monster['health']) + ' left ')

        elif player_won:
            game_ends(player['name'])
            final_round_result = {'Player_name' : player['name'], 'Ending_lifespan' : player['health'], 'Game_Rounds' : round_counter}
            final_game_results.append(final_round_result)
            new_round == False

        elif monster_won:
            game_ends(monster['name'])
            final_round_result = {'Monster_name' : monster['name'], 'Ending_lifespan' : monster['health'], 'Game_Rounds' : round_counter}
            final_game_results.append(final_round_result)
            print(final_game_results)
            new_round == False
            print('GameOver')

        if player_won == True or monster_won == True:
            new_round = False
            print()
            print('----******---GAME-ENDS---*****----')
            print()
           



