import random
import time

# Player Stats

player_hp = 10
player_attack = 5
player_defence = 5
current_player_hp = 10 # resets to 10 after each combat victory

# Enemy Stats

current_enemy_hp = 5 # resets to 5 after each combat victory
current_enemy_attack = 2
current_enemy_defence = 2

# Boss Stats

boss_hp = 10
boss_defence = 3
current_boss_hp = 10

# Choices & error management

choice_a = ("a", "A")
choice_b = ("b", "B")
combat_choice_A = ("a", "A")
combat_choice_B = ("b", "B")
yes = ("y", "Y", "Yes", "yes", "YES")
no = ("n","N", "No", "no", "NO")
error = ("Please only use A or B")

current_game_level = 0 # Added to exit combat to correct level upon victory script

banner = ("""





______ __ __   ___      ____   ___ ____  ______ __ __  ___  __ __  _____  ___ 
|      |  |  | /  _]    |    \ /  _|    \|      |  |  |/   \|  |  |/ ___/ /  _]
|      |  |  |/  [_     |  o  /  [_|  _  |      |  |  |     |  |  (   \_ /  [_ 
|_|  |_|  _  |    _]    |   _|    _|  |  |_|  |_|  _  |  O  |  |  |\__  |    _]
  |  | |  |  |   [_     |  | |   [_|  |  | |  | |  |  |     |  :  |/  \ |   [_ 
  |  | |  |  |     |    |  | |     |  |  | |  | |  |  |     |     |\    |     |
  |__| |__|__|_____|    |__| |_____|__|__| |__| |__|__|\___/ \__,_| \___|_____|
                                                                               
  by The Syntax Errorz: Simon He, Edward Solanke, Mark Fitzmaurice  c.MMXXI                                                                                                                               
                                                                                                                                
                                                                                                                                

""")


# Enemy Combat System


def combat_choice():
    print(" Select a combat action ..."
    "\n A - Attack!"
    "\n B - Special Attack!")
    time.sleep(1)
    combat_input = input("---> ")
    if combat_input in combat_choice_A: # attack
        player_attacking()
    elif combat_input in combat_choice_B: # special attack
        special_attack_roll()
    else:
        print(error)
        combat_choice()



def player_attacking():
    global current_enemy_hp, current_enemy_defence, player_attack 
    damage = (player_attack - current_enemy_defence)
    if damage > current_enemy_hp:
        print(f"Damage dealt ({damage}) exceeds current enemy HP!")
        time.sleep(1)
        print("you kicked his ass!")
        time.sleep(1)
        victory_script()
    else:
        print(f"Enemy\'s Current HP is {current_enemy_hp}!")
        current_enemy_hp = (current_enemy_hp - damage)
        time.sleep(1)
        print(f"You hit the enemy for {damage}!")
        time.sleep(1)
        print(f"Enemy\'s Current HP is {current_enemy_hp}!")
        time.sleep(1)
        print("**  ENEMY\'S ATTACK PHASE **")
        enemy_attacking()
        
            


def enemy_attacking():
    global current_player_hp, current_enemy_attack, player_defence 
    damage = (player_defence - current_enemy_attack)
    if current_player_hp >0:
        print(f"Your Current HP is {current_player_hp}!")
        time.sleep(1)
        current_player_hp = (current_player_hp - damage)
        print(f"Enemy hits you for {damage}!")
        time.sleep(1)
        print(f"Your Current HP is {current_player_hp}!")
        time.sleep(1)
        print("**  PLAYER\'S ATTACK PHASE **")
        combat_choice()        
    else:
        print(f"Damage taken ({damage}) exceeds current player HP!")
        time.sleep(1)
        print("YOU DIED! GAME OVER, LOSER")
        time.sleep(1)
        game_over_script()
        


def special_attack_roll():
    global r, current_enemy_hp, player_attack
    r = random.randint(1, 10)
    if r == 1:
        print(f"You rolled {r}, ACTIVATE SPECIAL ATTACK!!!") # Full attack start dealt as damage to enemy
        # special attack active script
        damage = player_attack
        if damage >= current_enemy_hp: # win
            print(f"Damage dealt ({damage}) exceeds current enemy HP!")
            time.sleep(1)
            print("YOU WIN THE FIGHT!") # Combat Victory Script
            victory_script()
        else:
            current_enemy_hp = (current_enemy_hp - damage)
            print(f"You hit the enemy for {damage}!")
            time.sleep(1)
            print(f"Enemy\'s Current HP is {current_enemy_hp}!")
            time.sleep(1)
            print("**  ENEMY\'S ATTACK PHASE **")
            enemy_attacking()
    elif r == 10:
        print(f"You rolled {r} ACTIVATE MEGA ATTACK!!!") # Instakill enemy
        # insta kill enemy script
        print(".....wait.....")
        time.sleep(1)
        print("JESUS CHRIST!!!!, WHERE DID YOU GET A BAZOOKA FROM?!")
        time.sleep(1)
        # victory script
        print("BOOOOOOOM")
        time.sleep(1)
        print("You KILLED them all!")
        time.sleep(1)
        victory_script()
    elif r == 5:
        print(f"You rolled {r}, SPECIAL ATTACK FAILED!!!") # enemy ONE HIT KILLS YOU
        # enemy 1 shots you script
        time.sleep(1)
        print("You live by the sword, you die by the sword!")
        # game over script
        print("GAME OVER! LOSER!!!!!!!!!!!!!!")
        game_over_script() 
    else:
        print("SPECIAL ATTACK FAILED!!!")
        time.sleep(1)
        print("**  ENEMY\'S ATTACK PHASE **")
        time.sleep(1)
        enemy_attacking()
       
# Boss Combat System

def boss_combat_choice():
    print(" Select a combat action ..."
    "\n A - Attack!"
    "\n B - Special Attack!")
    time.sleep(1)
    combat_input = input("---> ")
    if combat_input in combat_choice_A: # attack
        player_attacking_boss()
    elif combat_input in combat_choice_B: # special attack
        special_attack_roll_against_boss()
    else:
        print(error)
        boss_combat_choice()



def player_attacking_boss():
    global current_boss_hp, boss_defence, player_attack 
    damage = (random.randint(2,5)) # EXCLUSIVE TO BOSS COMBAT
    if damage > current_boss_hp :
        print(f"Damage dealt ({damage}) exceeds current boss HP!")
        time.sleep(1)
        victory_script()
    elif current_boss_hp <1:
        print(f"Damage dealt ({damage}) exceeds current boss HP!")
        time.sleep(1)
        victory_script()
    elif current_boss_hp == 0:
        print(f"Damage dealt ({damage}) exceeds current boss HP!")
        time.sleep(1)
        victory_script()
    else:
        print(f"BOSS\' Current HP is {current_boss_hp}!")
        current_boss_hp = (current_boss_hp - damage)
        time.sleep(1)
        print(f"You hit the boss for {damage}!")
        time.sleep(1)
        print(f"BOSS\' Current HP is {current_boss_hp}!")
        time.sleep(1)
        print("**  BOSS\' ATTACK PHASE **")
        time.sleep(1)
        boss_attacking()
        
            


def boss_attacking():
    global current_player_hp
    damage = (random.randint(1,5))
    if damage > current_player_hp:
        print(f"Damage taken ({damage}) exceeds current player HP!")
        time.sleep(1)
        print("He riddled you with bullets, you died!!!!!!!")
        time.sleep(1)
        game_over_script()
    elif current_player_hp <1:
        print(f"Damage taken ({damage}) exceeds current player HP!")
        time.sleep(1)
        print("He riddled you with bullets, you died!!!!!!!")
        time.sleep(1)
        game_over_script()
    elif current_player_hp == 0:
        print(f"Damage taken ({damage}) exceeds current player HP!")
        time.sleep(1)
        print("He riddled you with bullets, you died!!!!!!!")
        time.sleep(1)
        game_over_script()
    else:
        print(f"Your Current HP is {current_player_hp}!")
        current_player_hp = (current_player_hp - damage)
        time.sleep(1)
        print(f"Boss hits you for {damage}!")
        time.sleep(1)
        print(f"Your Current HP is {current_player_hp}!")
        time.sleep(1)
        print("**  PLAYER\'S ATTACK PHASE **")
        time.sleep(1)
        boss_combat_choice()

def special_attack_roll_against_boss():
    global r, current_boss_hp, player_attack, current_game_level
    r = random.randint(1, 10)
    if r == 1:
        print(f"You rolled {r}, ACTIVATE SPECIAL ATTACK!!!") # Full attack start dealt as damage to boss
        # special attack active script
        damage = player_attack
        time.sleep(1)
        if damage >= current_boss_hp: # win
            print("you broke all his limbs!") # Combat Victory Script
            time.sleep(1)
            current_game_level = 3
            victory_script()
        else:
            current_boss_hp = (current_boss_hp - damage)
            print(f"You hit the boss for {damage}!")
            time.sleep(1)
            print(f"BOSS\' Current HP is {current_boss_hp}!")
            time.sleep(1)
            print("**  BOSS\' ATTACK PHASE **")
            time.sleep(1)
            boss_attacking()
    elif r == 10:
        print(f"You rolled {r} ACTIVATE MEGA ATTACK!!!") # Instakill BOSS
        time.sleep(1)
        print("STOP! he's already dead!")
        time.sleep(1)
        print("His mum wouldn\'t even recognise him!")
        time.sleep(1)
        current_game_level = 3
        victory_script()
    elif r == 5:
        print(f"You rolled {r}, SPECIAL ATTACK FAILED!!!") # BOSS ONE HIT KILLS YOU
        time.sleep(1)
        print("!!HEADSHOT!!!")
        time.sleep(1)
        print("He riddled you with bullets, you died!")
        time.sleep(1)
        game_over_script() 
    else:
        print("SPECIAL ATTACK FAILED!!!")
        time.sleep(1)
        print("**  BOSS\' ATTACK PHASE **")
        time.sleep(1)
        boss_attacking()

  
# Game over & Victory Script functions for combat
def victory_script():
    global current_game_level, current_enemy_hp, current_player_hp
    current_enemy_hp = 5
    current_player_hp = 10
    if current_game_level == 1:
        time.sleep(1)
        print(f"Your health is recharged, your current hp is {current_player_hp}")
        time.sleep(1)
        level_2_intro()
    elif current_game_level == 2:
        time.sleep(1)
        print(f"Your health is recharged, your current hp is {current_player_hp}")
        time.sleep(1)
        level_3_intro()
    elif current_game_level == 3: # Triggers when boss complete
        time.sleep(2)
        print("you rescued her! It’s over, you’re a hero! She uses this chance to tell you she’s…pregnant")
        time.sleep(1)
        print(" Quick! What do you do??? ..."
        "\n A - Run"
        "\n B - ....."
        "\n---> ")
        time.sleep(1)
        print("Mary - 'Where did he go?...SONNOFA!!!'")
        time.sleep(1)
    else:
        print("ERROR")
        print(f"Current game level is {current_game_level}")    


def game_over_script():
    time.sleep(1)
    print("""
    
    ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░              """)
    time.sleep(2)
    print("Mary\'s death is caused by your weakness!")
    time.sleep(3)
    title_screen()

# Success Rolls for levels

def success_roll_1():
    roll = random.randint(1,10)
    if (roll % 2) == 0:
        print("...it didn\'t work, prepare to fight!")
        time.sleep(2)
        print(" ** COMBAT START **")
        combat_choice()
    else:
        print("You lucky git, onto the next floor!")
        time.sleep(1)
        level_2_intro()

def success_roll_2():
    roll = random.randint(1,10)
    if roll <10:
        print("You took too long deciding idiot! the guards caught up ")
        time.sleep(2)
        print("You get headshotted!")
        time.sleep(1)
        game_over_script()
    else:
        print("the lift is taking you up to the Penthouse floor!")
        level_3_intro()

def success_roll_3():
    roll = random.randint(1,10)
    if (roll % 2) == 0:
        print("He noticed you! Both you and Mary eat 10 bullets")
        time.sleep(1)
        game_over_script()
    else:
        print("...it didn\'t work, he's charging at you!")
        time.sleep(2)
        print(" ** BOSS COMBAT START **")
        boss_combat_choice() 

## GAME START ##
def title_screen():
    time.sleep(2)
    print(banner)
    time.sleep(1)
    start_choice = input("Begin?"
        "\n Yes or NO?"
        "\n---> ")
    if start_choice in yes:
        time.sleep(2)
        print(""
        "\n"
        "\n....I've got to get her back......")
        time.sleep(2)
        print("....I..I NEED to get her back!!.."
        "\n.....")
        time.sleep(2)
        print("....Urgh!..OK.....I can do this")
        print("...I have to do this,")
        time.sleep(2)
        print("NO!, I must")
        time.sleep(2)
        print(".....Mary....Hold on......I\'m coming!")
        time.sleep(2)
        level_1_intro()        
    elif start_choice in no:
        time.sleep(1)
        print("DON\'T BE A COWARD")
        time.sleep(1)
        title_screen()
    else:
        print(error)
        time.sleep(1)
        title_screen()

## LEVEL 1 START ##
def level_1_intro():
    global current_game_level
    current_game_level = 1
    print("You look ahead of you from the distance, and see the hotel Mary (your lady) was dragged into")
    time.sleep(2)
    print("Heavily guarded at the front entrance, you navigate your way to the side entrance,"
    "\nwithout being detected by the guards or cameras.")
    time.sleep(2)
    print("I'm in....I need to get to the lift to get to the Penthouse, Mary I'm coming")
    time.sleep(2)
    print("Making your way to the lift you encounter bodyguards who spot you. Now you are being questioned and you're faced with two options, attack them to pass them to get to lift, or run in the hopes to outrun security to get to lift"
    "\n"
    "\n")
    time.sleep(1)
    print("** LEVEL 1 START **")
    time.sleep(2)
    level_1_choices()




## LEVEL 1 CHOICES ##
def level_1_choices():
    print(" Quick! What do you do??? ..."
    "\n A - Attack the guards!"
    "\n B - Run from the guards!")
    time.sleep(1)
    level_1_input = input("---> ")
    time.sleep(1)
    if level_1_input in choice_a: #combat_system()
        print(" ** COMBAT START **")
        time.sleep(1)
        combat_choice()
    elif level_1_input in choice_b:
        success_roll_1()
    else:
        print(error)
        time.sleep(1)
        level_1_choices()


## LEVEL 2 START ##
def level_2_intro():
    global current_game_level
    current_game_level = 2
    print("** LEVEL 2 START **")
    print("You've made it to the lift, you know where you need to go, you're almost there.")
    time.sleep(1)
    print("Now, do you press the button for the penthouse floor")
    time.sleep(1)
    print("or..")
    time.sleep(1)
    print("keep going to the next floor and see if she's there?")
    time.sleep(1)
    level_2_choices()


## LEVEl 2 CHOICES ##
def level_2_choices():
    print(" Quick! What do you do??? ..."
    "\n A - Take Express lift to the Penthouse"
    "\n B - Keep going")
    time.sleep(1)
    level_2_input = input("---> ")
    time.sleep(1)
    if level_2_input in choice_a: 
        success_roll_2()
    elif level_2_input in choice_b: # script then combat_system()
        print("it takes you up, door opens more bodyguards waiting for you")
        time.sleep(1)
        print(" ** COMBAT START **")
        combat_choice()
    else:
        print(error)
        time.sleep(1)
        level_2_choices()



## LEVEL 3 START ##
def level_3_intro():# when boss combat is over print game complete script
    global current_game_level
    current_game_level = 3
    print("** LEVEL 3 START **")
    print("The elevator doors open on the Penthouse floor, you see Mary tied up, sat on a chair in the left side of the room.")
    time.sleep(1)
    print("The Gang Boss is on the right  side of the room and hasn’t noticed you yet.")
    time.sleep(1)
    print("Here’s the moment of truth….do you…. go right, risk yours and Mary’s life to get revenge for the trouble it’s caused you both,"
    "\n or")
    time.sleep(1)
    print("do you go left, sneak Mary out and into the sunset?")
    time.sleep(1)
    level_3_choices()

    
## LEVEL 3 CHOICES ##
def level_3_choices(): 
    print(" Quick! What do you do??? ..."
    "\n A - Make a run for Mary"
    "\n B - Rush the Boss!!")
    time.sleep(1)
    level_3_input = input("---> ")
    time.sleep(1)
    if level_3_input in choice_a: # loop back to choices upon success_roll_3 failure
        success_roll_3()
    elif level_3_input in choice_b: # Start Boss fight
        print(" ** BOSS COMBAT START **")
        time.sleep(1)
        boss_combat_choice()
    else:
        print(error)
        time.sleep(1)
        level_3_choices()




title_screen()