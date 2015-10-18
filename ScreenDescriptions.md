## Title Screen ##

When the game starts, the user is shown the Title Screen. This screen has a background image that is suitable to the game's theme, and the logo of the game.

User can enter login credentials or go to registration (see below).

```
[input: username]
[input: password]
[button: join server]
[button: registration]
```

## Registration ##

On this screen user can register his/her username.

```
[input: username]
[input: password]
[input: e-mail address]
```

## Lounge ##

After user has successfully logged in to the server, he goes to lounge to wait for the match to start.

At lounge players can see who's online at the server, choose the next map to play, to chat, and to start the game.

In later versions of the game, there could be multiple concurrent games going on, but in the first version there is only one.

```
[panel: list of players at the lounge]
[panel: windows for chat & status messages]
[input: textfield for user's own chat messages]
[input: number of players]
[input: number of required victories]
[input: which arena to play next]
```

## Arena ##

This is the main game screen. Here the battles take place.

```
[panel: grid of game tiles]
[panel: chat window for those players who have been blasted]
```

## Inter-match results ##

This screen shows the current match results and highlights the last round's winner.

## Match results ##

This screen shows the total match results and highlights the winner.

## Hall Of Fame ##

On this screen users can view the statistics of the past matches.

There should be some kind of top 10 list.