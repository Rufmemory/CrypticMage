import random
import sys
import time

class MainMethod:
    object_name = ""
    object_desc = ""
    def check_desc(self):
        print("Upon inspecting the "+self.object_name+",you notice that this is "+ self.object_desc)
        
class Mage(MainMethod):
    def __init__(self):
        self.object_name = "mage"
        self.health_points = 100
        self.object_desc = "the playable character, \n that you may help. He is on his way back into the 'crypt' in order \n to find his lost staff, and book of spells taken away by this 'ghost'"
        self.inventory = []
    def method_status(self):
        if len(self.inventory) > 0:
            inventory_phrase = "in possession of his {}, \n as he may now use the fireball spell bound to the staff, \n which he may use by casting ('cast') at the 'ghost'".format(self.inventory[0])
        else:
            inventory_phrase = "still looking \n for the 'ghost' that stole and brought his book of spells \n in this cursed 'crypt'"
        if self.health_points == 100:
            health_phrase = "in top shape,"
        elif self.health_points >= 50:
            health_phrase = "wounded with {}%HP left,".format(self.health_points)           
        elif self.health_points >= 1:
            health_phrase = "badly Wounded with {}%HP left,".format(self.health_points)
        self.check_desc()
        print("The mage seems " + health_phrase + " and is " + inventory_phrase)

class Crypt(MainMethod):
    def __init__(self):
        self.object_name = "crypt"
        self.object_desc = "This seems to be the ancient underground crypt, \n that is haunted by a well known 'ghost'." 
        self.inventory = ['staff',]
    def method_status(self):
        if 'staff' in self.inventory:
            inspect_phrase = "he can 'pickup' following items: {}".format(self.inventory)
        else:
            inspect_phrase = "there is nothing here to 'pickup' here anymore, \n rather a grim looking 'ghost' ready to 'cast' spells back at you"
        print(self.object_desc + " \n The mage notices that " + inspect_phrase)
        
class Ghost(MainMethod):
    def __init__(self):
        self.object_name = "ghost"
        self.health_points = 100
        self.object_desc = " a dangerous ghost! \n the mage remembers that they both previously fought \n in a long and gruesome battle and he then managed \n to warp away... \n yet mr. ghost is back here, roaming the crypt. \n The mage notices the ghost still attempting to decipher his book \n Help the mage stop this ghost!"
    def method_status(self):
        if self.health_points == 100:
            health_phrase = "in top shape,"
        elif self.health_points >= 50:
            health_phrase = "wounded with {}%HP left,".format(self.health_points)           
        elif self.health_points >= 1:
            health_phrase = "badly Wounded with {}%HP left,".format(self.health_points)
        self.check_desc()
        print("The ghost seems " + health_phrase)

class MethodFunctions:
    crypt = Crypt() 
    mage = Mage() 
    ghost = Ghost()
    object_name_dict = {"ghost":ghost,"mage":mage,"crypt":crypt}
    def cast(self, target_name):
        if target_name == 'ghost':
            target = MethodFunctions.ghost
            if 'staff' in MethodFunctions.mage.inventory:
                mage_attacking = random.randint(0,100)
                print("The mage throws a fireball removing {}%HP".format(mage_attacking))
                target.health_points = target.health_points - mage_attacking
                if target.health_points >= 1: 
                    ghost_attacking = random.randint(1,99)
                    print("The ghost casts a lightning back at the mage removing {}%HP".format(ghost_attacking))
                    MethodFunctions.mage.health_points = MethodFunctions.mage.health_points - ghost_attacking
                elif target.health_points <= 0:
                    magic_color = random.choice(['red charm','blue charm'])
                    print("The ghost vanishes as a dusty cloud, leaving a ")
                    print("familiar book, yet something is still odd.")
                    print("Upon examining what seems to be his lost book of spells")
                    print("The mage gasps, as he notices a strange seal,")
                    print("that is preventing him from opening it without harm.")
                    print("He now has to guess right charm colour, it will either be")
                    print("the 'red charm' or 'blue charm' that will dispell the seal.")
                    print("Make your final guess, and may it be the right one!")
                    time.sleep(3)
                    last_choice = input("Guess here")
                    if last_choice == magic_color:
                        print("The mage is now relieved from the ghost's spells, \n he has gotten his items back and can now continue on his journey")
                        print("(\_/) Well")
                        print("(^_^) done!")
                        print("(___) The End.")
                        time.sleep(3)
                        sys.exit()
                    else:
                        print("The mage is now trapped in another dimension... ")
                        print("(\_/) ")
                        print("(-_-) ")
                        print("(___) ")
                        time.sleep(3)
                        sys.exit()
                if MethodFunctions.mage.health_points <= 0:
                        print("The mage is too wounded and has to warp out of here again.")
                        print("(\_/) ")
                        print("(~.~) ")
                        print("(___) ")
                        time.sleep(3)
                        sys.exit()
            else:
                print("You cannot 'cast' your spells at {} for now, \n as the mage does not even have his own 'staff'!".format(target_name))
        else:
            print("The mage sees no point to cast anything at {}? \n Rather focusing on the ghost for now... ('cast' 'ghost')".format(target_name))
    def inspect(self, target_name):
        if target_name in MethodFunctions.object_name_dict:
            MethodFunctions.object_name_dict[target_name].method_status()
        else:
            print("There is no such {} to inspect around here.".format(target_name))
    def pickup(self, target_name):
        if target_name in MethodFunctions.crypt.inventory:
            MethodFunctions.crypt.inventory.remove(target_name)
            MethodFunctions.mage.inventory.insert(1, target_name)
            print("By picking up his {}, the mage may now fight the 'ghost' again \n (try to 'cast' spells at the 'ghost')".format(target_name))
        else:
            print("There is no {} to pickup around here.".format(target_name))
    def exit(self, target_name):
        exit_target = 'game'
        if target_name == exit_target:
            print("Goodbye dear Wizzard, take good care of yourself!")
            time.sleep(3)
            sys.exit()
        else: 
            print("you may want to try 'exit game', instead")
    def __init__(self):
            self.first_command_dict = {"cast": MethodFunctions.cast,
                                       "inspect": MethodFunctions.inspect,
                                       "pickup": MethodFunctions.pickup,
                                       "exit": MethodFunctions.exit}
            self.turns_left = 20
            print('#' * 60 + '\n')
            print("A deep voice is waking an old 'mage' from his nightmare...............")
            print("{-_-}Zzz Wake up! Brave one!, it is time to 'inspect' your surroundings")
            print("He felt unconscious under a fight with an old 'ghost' from this 'crypt'")
            print('\n' + '#' * 60)
            time.sleep(3)
            print('#' * 60 + '\n')
            print(" Try to type 'inspect''mage' and notice further keywords! ")
            print(" The 'inspect' command may show him the way forward... ")             
            print("(Time is running out and you may only type a certain amount")        
            print("  of commands counted as [actions] until the mage has to warp out)")
            print(" Possible commands: 'cast', 'inspect', 'pickup', 'exit'.")
            print('\n' + '#' * 60)
            time.sleep(2)
            print('#' * 60 + '\n')
            print("(\_/) Ruf memory")
            print("(o.0) Training")
            print("(___) Presents...")
            print('\n' + '#' * 60)
            time.sleep(1)
            print('#' * 60 + '\n')
            print("Cryptic Mage")
            print("A 'Simple' Text Based Game")
            print("Learn to program the fun way!")
            print('\n' + '#' * 60)
            while self.turns_left > 0:
                print('#' * 60)
                print("Actions left: {}".format(self.turns_left))
                print('#' * 60)
                self.typed_command = input("Enter something here: ").split()
                try:
                    self.first_command_word = self.typed_command[0]
                    if self.first_command_word in self.first_command_dict:
                        self.first_command = self.first_command_dict[self.first_command_word]
                        if len(self.typed_command) >= 2:
                            self.target_name_word = self.typed_command[1]
                            self.first_command(self, self.target_name_word)
                    else:
                        print("Unknown command")
                except (IndexError, UnboundLocalError) as errors:
                    print("Unknown words")
                self.turns_left = self.turns_left - 1
                if self.turns_left == 1:
                    print('#' * 60)
                    print("At the last second, the mage chooses to warp out of here, time is out.")
                    print('#' * 60)
                    time.sleep(3)
                    sys.exit()
MethodFunctions()

