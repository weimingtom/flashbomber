%% Author: friluhen
%% Created: 19.9.2008
%% Description: TODO: Add description to bmbr_srv
-module(bmbr_srv).

%%
%% TCP message format
%% CREATE-command:
%%  CREATE:GAME_ID:MAX_PLAYERS
%% JOIN-command:
%%	JOIN:GAME_ID:
%% COMMAND:GAME_ID:<PLAYER_ID> | :
%%

%%
%% Include files
%%
-define(TCP_OPTIONS,[list, {packet, 0}, {active, false}, {reuseaddr, true}]).

%%
%% Exported Functions
%%
-export([listen/1]).

-record(game, {id = "", maxplayers = 4, players = [], actions = []}).

%%
%% API Functions
%%
listen(Port) ->
    Pid = spawn(fun() -> manage_clients([]) end),
    register(client_manager, Pid),
    register(game_manager, spawn(fun() -> manage_games([]) end)),
    {ok, LSocket} = gen_tcp:listen(Port, ?TCP_OPTIONS),
    do_accept(LSocket).


%%
%% Local Functions
%%
do_accept(LSocket) ->
    {ok, Socket} = gen_tcp:accept(LSocket),
    spawn(fun() -> handle_client(Socket) end),
    client_manager ! {connect, Socket},
    do_accept(LSocket).

handle_client(Socket) ->
    case gen_tcp:recv(Socket, 0) of
        {ok,Data} ->
            client_manager ! {data, Data, Socket},
            handle_client(Socket);
        {error, closed} ->
            client_manager ! {disconnect, Socket}
    end.

manage_clients(Sockets) ->
    receive
		{connect, Socket} ->
            io:fwrite("Socket connected ~w~n", [Socket]),
            NewSockets = [Socket | Sockets],
			manage_clients(NewSockets);
		{disconnect, Socket} ->
            io:fwrite("Socket disconnected ~w~n", [Socket]),
            NewSockets = lists:delete(Socket, Sockets),
			manage_clients(NewSockets);
		{data, Data, Socket} ->
            
			send_data2(Sockets, Data),   
            %%[Action | Rest] = string:tokens(Data, ":"),
            
            %%case Action of
            %%    "LIST" ->
            %%    	game_manager ! {list, Socket};
            %%    "CREATE" ->
            %%        game_manager ! {create, Socket, Rest};
            %%    "ACT" ->
           %% 		send_data2(Sockets, Data)        
			%%end,			                    
            NewSockets = Sockets,
			manage_clients(NewSockets)
	end.
	

manage_games(Games) ->
    receive 
        {list, Socket} ->
            lists:foreach(fun(Game) -> gen_tcp:send(Socket, Game#game.id) end, Games),
            NewGames = Games;
        {create, Socket, Data} ->
            [Id, MaxPlayers] = Data,
            NewGames = [#game{id = Id, maxplayers = MaxPlayers, players = [Socket], actions = []} | Games],
            gen_tcp:send(Socket, "New game created."),
        	io:fwrite("Game created ~w~n", NewGames);
        {join, Socket, Data} ->
            [Id | _] = Data,
            Game = [G || G <- Games, G#game.id =:= Id],
            
			case lists:length(Game#game.players) =:= maxplayers of
				true ->
					gen_tcp:send(Socket, "ERROR:Game full");
				false ->
					gen_tcp:send(Socket, "OK")
			end,
			
			NewGame = Game#game{players = [Socket | Game#game.players]},
			NewGames = [[G || G <- Games, G#game.id =/= Id] | NewGame];
		{act, Data} ->
			[_Action | Id] = Data,
			Game = [G || G <- Games, G#game.id =:= Id],
			NewGame = Game#game{actions = [Game#game.actions | Data]},
			NewGames = [[G || G <- Games, G#game.id =/= Id] | NewGame];
		{send} ->
			send_data(Games),
			NewGames = clear_actions(Games, [])
	end,
    manage_games(NewGames).                     
                 
send_data([]) ->
	ok;    
send_data([Game | Rest]) ->
    SendData = fun(Socket) -> 
                    lists:foreach(fun(Action) -> gen_tcp:send(Socket, Action) end, Game#game.actions)
               end,
    lists:foreach(SendData, Game#game.players),
	send_data(Rest).

send_data2(Sockets, Data) ->
	SendData = fun(Socket) ->  gen_tcp:send(Socket, Data) end,
    lists:foreach(SendData, Sockets).
	
clear_actions([], ClearedGames) ->
	ClearedGames;
clear_actions([Game | Rest], ClearedGames) ->
	NewGame = Game#game{actions = []},
	NewGames = [NewGame | ClearedGames],
	clear_actions(Rest, NewGames).