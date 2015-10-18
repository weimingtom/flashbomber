## Domain Model ##

There should be UML picture too.



#### Game ####

This object is the main program that listens to network, keyboard, etc.

#### Player ####

Self-describing.

#### Match ####

Match is associated to an Arena.
Match has many Players.

#### Arena ####

Arena is the map, or screen that consists of Tiles.

Arena hasMany Tile

#### Tile ####

Tile is the basic building block of the Arena.

Tile has 0-1 Item

#### Bomb ####

Bomb is the exploding bomb item that players leave around the Arena.

#### BonusItem ####

BonusItems add to length of flames, amount of concurrent bombs, etc.

#### Skull ####

Skulls bring random play effects to game.