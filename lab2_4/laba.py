import pickle
import shelve
import os
class game():
    def __init__(self):
        #self.player_list = set()
        self.players = []# stores objects(name,weapon list as object,age)
    def load(self):
        # if os.path.exists("player_data"):
        #     # open a file, where you stored the pickled data
        #     file = open('player_data', 'rb')
        #     # dump information to that file
        #     #self.player_list = pickle.load(file)
        #     # close the file
        #     file.close()
        mydb = shelve.open('db')
        for key in mydb.keys():
            self.players.append(mydb[key])
            #print(key)
        mydb.close()

    def save(self):
        # open a file, where you ant to store the data
        #file = open('player_data', 'wb')
        # dump information to that file
        #pickle.dump(self.player_list, file)
        # close the file
        #file.close()
        mydb = shelve.open('db')
        for gamer in self.players:
            mydb[gamer.name] = gamer
        mydb.close()

    def new_player(self,nickname,age):
        gamer = player(nickname,age)
        self.players.append(gamer)
        #self.player_list.add(nickname)
    def rename_player(self,nickname, newname):
        for obj in self.players:
            if obj.name == nickname:
                obj.name = newname
    def show_players(self):
        #for name in self.player_list:
         for gamer in self.players:
            gamer.whoami()
class weapon():
    def __init__(self, name):
        self.name = name
        self.effect = 0
    # def whoami(self):
    #     print("class=" + self.__class__.__name__, end="\t")
    #     # print all class variables
    #     temp = vars(self)
    #     for item in temp:
    #         print(item, ':', temp[item], end="\t")
    #     print("")
class axe(weapon):
    def __init__(self, name):
        super().__init__(name)
        self.effect = 20
class gun(weapon):
    def __init__(self, name):
        super().__init__(name)
        self.effect = 70

class player():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.weapon = []
    def add_weapon(self,any_obj):
        self.weapon.append(any_obj)

    # def load(self):
    #     # open a file, where you stored the pickled data
    #     file = open('player_data', 'rb')
    #     # dump information to that file
    #     self.weapon = pickle.load(file)
    #     # close the file
    #     file.close()
    # def save(self):
    #     # open a file, where you ant to store the data
    #     file = open('player_data', 'wb')
    #     # dump information to that file
    #     pickle.dump(self.weapon, file)
    #     # close the file
    #     file.close()

    def whoami(self):
        print("class=" + self.__class__.__name__, end="\t")
        # print all class variables
        temp = vars(self)
        for item in temp:
            if isinstance(temp[item], (float, int, str)):
                print(item, ':', temp[item], end="\t")
        print("WEAPOONLIST:")
        for wp in self.weapon:
            print('name:'+wp.name+'\teffect:'+str(wp.effect)+'\t')
            # wp.whoami()


game1 = game()
game1.load()
# game1.new_player("milo",12)
# game1.new_player("sam",10)
# game1.new_player("ric",17)
# game1.players[1].add_weapon(axe('axe1'))
# game1.players[2].add_weapon(gun('newgun'))
# game1.new_player("morty",18)
# game1.players[3].add_weapon(gun('gun1'))


#game1.rename_player('sam','petya')

game1.show_players()
game1.save()

'''
player1 = player("nic", 12)
#ax1 = axe('axe1')
# gun1 = gun('gun1')
# player1.add_weapon(axe('axe1'))
# player1.add_weapon(gun1)

#player1.weapon.append('axe')
#player1.save()

player1.load()
player1.whoami()


######## init and save to shelve
# ar1 = [1,2,3,4]
# ar2 = ['sg','fg','wg']
# mydb = shelve.open('db')
# mydb['key_ar1'] = ar1
# mydb['key_ar2'] = ar2
# mydb.close()
ar1 =[]
###### load from shelve
mydb = shelve.open('db')
ar1 = mydb['key_ar1']
ar2 = mydb['key_ar2']
mydb.close()
print(ar1)
print(ar2)
'''
#
# var1 = ['afadf','wefdwf']
# x = player('xxxx',111)
# # open a file, where you ant to store the data
# file = open('myfile.dat', 'wb')
# # dump information to that file
# #pickle.dump(var1, file)
# pickle.dump(x, file)
# # close the file
# file.close()
# del(var1)
# # open a file, where you stored the pickled data
# file = open('myfile.dat', 'rb')
# # dump information to that file
# var2 = pickle.load(file)
# # close the file
# file.close()
