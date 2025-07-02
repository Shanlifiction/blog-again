########################## PART 1
class Map:
  def __init__ (self, x_max, y_max, treasure_x, treasure_y):
        self.x_max = x_max
        self.y_max = y_max
        self.treasure_x = treasure_x
        self.treasure_y = treasure_y

class Player:
    def __init__ (self, name, map):
        self.name = name #player name
        self.map = map #player position (?)
        self.x = 0 #player postion 
        self.y = 0                  #värde(n) kan skrivas i listan direkt (utan att enges i parantesen ovan)

    def move_up(self): #y eftersom y-axeln är vertikal
        if self.y < self.map.y_max: #om spelarens position är mindre än y max flytta -> kan flytta
            self.y += 1 #self.y = self.y + 1 (öka värdet med ett)

    def move_down(self):
        if self.y > 0:
            self.y -= 1
    
    def move_right(self): #x eftersom x-axeln är horisontell
        if self.x < self.map.x_max:
            self.x += 1
    
    def move_left(self):
        if self.x < 0:
            self.x -= 1

    def pick_treasure(self):
       #kontrollera om spelaren har hittat skatten
       #om spelarens x-koordinat är samma som skattens koordinat, och spelarens y-koordinater
        if self.x == self.map.treasure_x and self.y == self.map.treasure_y:
          print("Yey", self.name + "! You found the tresure.")
        else:
          print("Sorry", self.name + ", the treasure was not found.")
   
# class Star:
#    def __init__ (self, )
    
########################## PART 2 [skapa objek]
#skapa karta och ett par spelare (utanför klassdefinitionerna)
map_object = Map(5, 4, 2, 1)
p1 = Player("Alwin", map_object)
p2 = Player("William", map_object)

#flytta på spelarna och skriv ut deras positioner
#object.metod()
p1.move_up()
p2.move_up()
print(p1.name + ":", p1.x, "|", p1.y, "\t", p2.name + ":", p2.x, "|", p2.y)

p1.move_up()
p2.move_right()
print(p1.name + ":", p1.x, "|", p1.y, "\t", p2.name + ":", p2.x, "|", p2.y)

p1.move_up()
p2.move_right()
print(p1.name + ":", p1.x, "|", p1.y, "\t", p2.name + ":", p2.x, "|", p2.y)

#låt spelarna "prova" plocka skatten
p1.pick_treasure()
p2.pick_treasure()