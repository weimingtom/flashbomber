## Data format ##

The data format for client-server communication uses colon separated character data.

` p2:x12:y20:status-x:`

## Design decision: XML vs. CSV ##

It has been decided that data transfer between client and server will be done with a custom character data. The reason for the decision was the data density and easier handling in Erlang.


## Types of data ##

There is game related data, such as "start game" signal, "player joins" signal, etc.

There is also player related data, such as player movement, player planting a bomb, player chat messages.

Not sure if this kind of separation is necessary.

## Architecture ##

Players send their events/data to server which then echoes it to all other clients.

Some events also originate from server (such as TrappedEvent, PlayerDiesEvent, ...).

## Player-originated data ##

  * startGame
  * chatMessage
  * joinMatch
  * movement
    * up
    * down
    * left
    * right
  * plantBomb

Example XML:
```
<playerData id="somePlayer">
	<position x="10" y="20" />
	<actions>
		<bombDrop x="11" y="20" />
		<bombDrop x="12" y="20" />
		<pickItem id="2331" />
		<pickItem id="2332" />
		<pickSkull id="6664" />
	</actions>
</playerData>
```

## Server-originated data ##

  * gameStarts
  * playerTrapped
  * playerDies

Example XML:
```
<gameData>
	<joinPlayer id="somePlayer" />
	<leavePlayer id="someOtherPlayer" />
	<startGame id="34224" />
	<endGame id="34224" />
</gameData>
```