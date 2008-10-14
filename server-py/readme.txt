- Server

	- connections

	hasMany Players
	hasMany Messages
	
- Message

	- player
	- action
	- parameters
	
- Player

	- position
	- connection

	hasMany Items
	
- Arena

	hasMany Items
	hasMany Bombs
	hasMany Tiles
	
- Tile	

	- type
	- position

- Item

	- type : [EXTRA_BOMB, EXTRA_FLAME]
	- position

- Bomb

- Match

	hasMany Players
	hasOne Arena
	

